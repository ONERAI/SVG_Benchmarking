## Benchmarking methods for identification of spatially variable genes

Spatially resolved transcriptomics enables the profiling of gene expression in cells while maintaining their spatial context, thereby introducing a new dimension to the data. An essential step in analyzing such data involves identifying genes that exhibit varying expression patterns across space. A variety of computational methods have been developed with diverse strategies and assumptions to accomplish this task. However, the absence of a benchmark on the performance of these methods hinders their effective use. We here present a systematic evaluation of 13 methods on XXX simulated and XXX real-world spatial transcriptomics datasets generated by imaging-based or sequencing-based technologies.


We aim to address following question

* Are the methods robust to different spatial patterns?
* Which method have the best performance?
* When applied to real data, do they give consistent results?
* How is scalibility and usability of each method?

### Methods

| Name      | Spatial model | Language | Input       | Publication     | Year| Output| Tested by | Documentation | Availbility | Usability|
| ---       | ---                        | ---      | ---        | -----------     |-------| -----------------| -----------------------|-----------|---------------| ---------------------|
| Moran’s I | SN    | Python   | Normalized |  [Biometrika](https://academic.oup.com/biomet/article/37/1-2/17/194868) |  1950 | Correlation | Zhijian| *** | Github & Pypi| |
| SpatialDE | GP | R & Python   | Normalized |  [Nature Methods](https://www.nature.com/articles/nmeth.4636) |  2018 | P-value| Zain |***| Github ||
| Trendsceek| SN | R   | Normalized |  [Nature Methods](https://www.nature.com/articles/nmeth.4634) |  2018  | P-value | Zhijian | *** | Github ||
| SPARK     | GP | R   | Count |  [Nature Methods](https://www.nature.com/articles/s41592-019-0701-7) |  2020 | P-value |Zhijian | *** | Github | |
| BOOST-GP  | GP | R   | Count |  [Bioinformatics](https://academic.oup.com/bioinformatics/article/37/22/4129/6306406) |  2021 | P-value || | Github ||
| SOMDE     | GP | Python   | Normalized |  [Bioinformatics](https://academic.oup.com/bioinformatics/article/37/23/4392/6308937) |  2021 | P-value| Zhijian | | Github&PyPi ||
| SPARK-X   | GP | R   | Count |  [Genome Biology](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-021-02404-0) |  2021  | P-value| | | Github||
| SpaGCN    | Graph | Python   | Normalized |  [Nature Methods](https://www.nature.com/articles/s41592-021-01255-8) |  2021 | P-value| Zain | | ||
| SpatialDE2| GP | Python   | Count |  [bioRxiv](https://www.biorxiv.org/content/10.1101/2021.10.27.466045v2) |  2021  | P-value| | | ||
| sepal | Graph | Python   | Count | [Bioinformatics](https://academic.oup.com/bioinformatics/article/37/17/2644/6168120?login=false) |  2021 | | Zain | | ||
| GPcounts  | GP | Python   | Count | [Bioinformatics](https://academic.oup.com/bioinformatics/article/37/21/3788/6313161) |  2022 | P-value | Zain | | ||
| nnSVG     | GP | R | Count | [bioRxiv](https://www.biorxiv.org/content/10.1101/2022.05.16.492124v1.full) |  2022  | P-value| | | ||
| scGCO     | Graph | Python   | Count | [Nature communications](https://www.nature.com/articles/s41467-022-33182-3) |  2022 | FDR | Zhijian | | ||
| GraphST   | Graph | Python   | Count | [Nature communications](https://www.nature.com/articles/s41467-023-36796-3) |  2023 | | | | ||
| Spvnae    | SN | R   | Count | [bioRxiv](https://www.biorxiv.org/content/10.1101/2023.02.08.527623v1.abstract) |  2023 | | || ||


SN, Spatial neighborhood; GP, Gaussion process; GLSM; Generalized spatial linear models; 
GCN, Graph convolutional network; SOM, Self-organizing map; ZINB, Zero-inflated negative binomial; HMRF, Hidden Markov Random Fields; 


### Datasets

| Experimental techniques | Paper | Tissue | Num. of locations | Num. of genes | Others |
| ------------------------|-------| -------|-----------------| ---------------|-------- |

### Review paper
[Computational elucidation of spatial gene expression variation from spatially resolved transcriptomics data](https://www.sciencedirect.com/science/article/pii/S2162253121003127)

[Disparities in spatially variable gene calling highlight the need for benchmarking spatial transcriptomics methods](https://www.biorxiv.org/content/10.1101/2022.10.31.514623v1)

### Benchmarking paper
[Evaluating spatially variable gene detection methods for spatial transcriptomics data](https://www.biorxiv.org/content/10.1101/2022.11.23.517747v1)
