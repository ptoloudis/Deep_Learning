# Neural Collaborative Filtering (NeuMF) in PyTorch

Reproduction of **NeuMF** from [*Neural Collaborative Filtering*](https://doi.org/10.48550/arXiv.1708.05031) (He et al., 2017) on the **MovieLens-100K** dataset, for the Data Mining / Deep Learning course at the University of Thessaly. The implementation is adapted from the reference PyTorch code [guoyang9/NCF](https://github.com/guoyang9/NCF).

## Goal

Reproduce the NeuMF experiments of the paper (Figures 5 and 7) on a different dataset:

1. **HR@K** vs. K (Top-K recommendation, K = 1…10)
2. **NDCG@K** vs. K (K = 1…10)
3. **HR@10** vs. number of negative samples per positive (1…10)
4. **NDCG@10** vs. number of negative samples per positive (1…10)

## Results

Each configuration was trained for 20 epochs; the table reports the **best epoch**, as in the reference implementation.

**Top-K (default number of negatives)**

| K | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|----|
| HR@K | 0.026 | 0.036 | 0.049 | 0.060 | 0.069 | 0.081 | 0.096 | 0.103 | 0.125 | **0.137** |
| NDCG@K | 0.026 | 0.032 | 0.037 | 0.040 | 0.046 | 0.042 | 0.050 | 0.050 | 0.061 | **0.064** |

**Number of negative samples (K = 10)**

| Negatives | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|----|
| HR@10 | 0.140 | 0.129 | 0.137 | 0.127 | 0.140 | 0.140 | 0.142 | 0.129 | 0.139 | 0.127 |
| NDCG@10 | 0.060 | 0.060 | 0.067 | 0.061 | **0.069** | 0.068 | 0.063 | 0.058 | 0.064 | 0.060 |

**Observations**

- HR@K and NDCG@K increase with K, as expected.
- Varying the number of negatives gives no clear trend: HR@10 stays in the 0.13–0.14 range, and NDCG@10 peaks at 5 negatives (0.069).
- Absolute values are not directly comparable to the paper, which uses MovieLens-1M and its own evaluation protocol.

## Repository structure

| Path | Description |
|---|---|
| `final.ipynb` | Model, data loading, training and evaluation (HR / NDCG) |
| `genarate.ipynb` | Generation of the negative-sample files |
| `graphs.ipynb` | Plots of the results from `our data/Top_k.csv` and `our data/Num_ng.csv` |
| `our data/` | MovieLens-100K (`u.data`), negative samples and result CSVs |
| `original data/` | MovieLens-1M files from the reference implementation |
| `NCF-master/` | Reference implementation (`model.py`, `evaluate.py`, `data_utils.py`, `main.py`) |
| `Deep_Learning_Report.docx` | Written report (in Greek) |

## How to run

The notebooks were developed on Google Colab with a GPU. To reproduce:

1. Upload the repository to Google Drive and open `final.ipynb` in Colab.
2. Adjust the data path in the `config` cell (`%cd '.../our data'`).
3. Set `dataset = 'u.data'` and `model = 'NeuMF-end'`, then run all cells.
4. Run `graphs.ipynb` to regenerate the figures.

**Stack:** Python, PyTorch, NumPy, pandas, SciPy, scikit-learn.
