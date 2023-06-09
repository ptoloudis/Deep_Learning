# Deep_Learning

This repozitory read the Neural Collaborative Filtering (NeuMF) with doi: https://doi.org/10.48550/arXiv.1708.05031.

The aim is to reproduce the results ONLY for the NeuMF methodology in figures 5 and 7 of the article for a different dataset. More specifically, you should send the performance of NeuMF in the following figures: 

1) y-axis HR@Κ and x-axis K(in the Top-K item recommendation problem), varying K from 1 to 10 with a step of 1 ( 2.5 Units)
2) y-axis NDCG@Κ and x-axis K, varying K from 1 to 10 in steps of 1 (2.5 Units)
3) y-axis HR@10 and x-axis number of negatives , varying number of negatives from 1 to 10 with a step of 1 (2.5 Units)
4)  y-axis NDCG @10 and x-axis number of negatives, varying number of negatives from 1 to 10 with a step of 1 (2.5 Units )

The work will use another MovieLens dataset than the one described in the article. The new dataset is in the u.data file.

The code is for the repozitory https://github.com/guoyang9/NCF