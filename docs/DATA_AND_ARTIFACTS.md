# Data and artifact guide

## Current files

| Path | Contents |
|---|---|
| `configs/benchmark-v4.1.json` | Canonical ranking contract, task weights, source order and sensitivities |
| `configs/model-registry.json` | Model revisions, architecture, precision and tokenizer-template metadata |
| `configs/reference-panel-summary.json` | Task-bank panel version and comparison scope; documentation export, not executable registration |
| `configs/bank-description.json` | Data provenance, split/group counts, cohort hashes and source pins |
| `results/benchmark-v4.1.json` | 40 canonical profiles and 160 directed matrix rows, including sensitivities and missing values |
| `results/recorded-cells.json` | Operating metrics and old/corrected ranking fields, with active profile cell IDs |
| `results/ranking-audit.json` | Numerical/link audit and secondary AUROC/AP changes |
| `results/version-comparison.json` | OLMo legacy, numerical correction, V4.0 sensitivity and V4.1 views |
| `results/native-profiles.csv` | Primary native task profiles and conditional intervals |
| `results/transfer-matrix.csv` | Directed pairs, self-map flags, recipes and anchor budgets |
| `results/provenance.json` | Source hashes and recorded internal execution checks |

Exports copy original recorded values. Only selected fields are retained: no private Drive access references, local account paths, review bodies, model weights or activation caches. Case hashes and profile IDs connect aggregate values to recorded numerical cells. Historical controlled-bank exports are in dated subfolders and are not V4.1 defaults.

## Data origin and use

Subject routing and entity endings are controlled, assistant-authored references with construction labels. Natural sentiment uses original ratings from [Amazon Reviews 2023](https://amazon-reviews-2023.github.io/) and [the original IMDb sentiment dataset](https://ai.stanford.edu/~amaas/data/sentiment/). Ratings are proxy labels, and a new human annotation study was not conducted.

Any later distribution or commercial use needs its own terms review.

The natural bank has 2,752 reviews, including 1,536 test cases. Product/author/film grouping, exposure exclusions and a fixed 6.25% mixed-marker quota define this sample. Unknown pretraining overlap and rating/text mismatch remain possible. [Detailed counts](../configs/bank-description.json).

All banks are opened development material. The original metadata registry still carries V4.0 because the tasks, heads and cohorts did not change in V4.1. The canonical ranking version is defined by the separate V4.1 configuration; the export records both identities rather than relabeling the historical file.
