"""Run GPCounts"""
import warnings
warnings.filterwarnings("ignore")

import os
os.environ["OMP_NUM_THREADS"] = "10" # export OMP_NUM_THREADS=1
os.environ["OPENBLAS_NUM_THREADS"] = "10" # export OPENBLAS_NUM_THREADS=1
os.environ["MKL_NUM_THREADS"] = "10" # export MKL_NUM_THREADS=1
os.environ["VECLIB_MAXIMUM_THREADS"] = "10" # export VECLIB_MAXIMUM_THREADS=1
os.environ["NUMEXPR_NUM_THREADS"] = "10" # export NUMEXPR_NUM_THREADS=1
#os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = '3'

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scanpy as sc
import squidpy as sq
import argparse
import gpflow
import tensorflow as tf
from GPcounts.GPcounts_Module import Fit_GPcounts
import statsmodels.formula.api as smf 
import statsmodels.api as sm

def parse_args():
    parser = argparse.ArgumentParser(description="Run GPCounts with command line")
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        default=None,
        help="Input filename, must be an Anndata object",
    )
    parser.add_argument(
        "-o", "--output", type=str, default=None, help="Output filename for results"
    )

    return parser.parse_args()


def main():
    print(tf.config.list_physical_devices('GPU'))
    
    args = parse_args()

    adata = sc.read_h5ad(args.input)
    
    Y = pd.DataFrame(data=adata.X.todense().astype(int).copy(), 
                      index=adata.obs_names, 
                      columns=adata.var_names)
    
    spatial_locations = pd.DataFrame(data=adata.obsm['spatial'], 
                                     index=adata.obs_names, 
                                     columns=['x', 'y'])
    spatial_locations['total_counts'] = adata.X.sum(axis=1)

    scales = []
    for i in range(0, len(Y.columns)):
        model=smf.glm(formula = "Y.iloc[:, i]~0+spatial_locations['total_counts']", 
                      data=Y, 
                      family=sm.families.NegativeBinomial(sm.families.links.log())).fit()
        res = model.params[0]*spatial_locations['total_counts']
        scales.append(res)

    scalesdf=pd.DataFrame(scales)
    scalesdf=scalesdf.T

    Y = Y.T
    X = spatial_locations[['x', 'y']]
    
    gp_counts = Fit_GPcounts(X, Y, sparse=True, scale=scalesdf, safe_mode=False)
    log_likelihood_ratio = gp_counts.One_sample_test("Negative_binomial")
    df = gp_counts.calculate_FDR(log_likelihood_ratio)
    df.to_csv(args.output)


if __name__ == "__main__":
    main()
