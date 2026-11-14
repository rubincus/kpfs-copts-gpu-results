# CoPTS-KPFS results for the knapsack problem with forfeit sets

Results of CoPTS-KPFS, a structure-guided cooperative tabu search with exact neighborhood evaluation on GPUs, for
the knapsack problem with forfeit sets (KPFS): the best solution found for every instance, the record of every
run of the experiments, the reports of the analyses and a verifier.

## Contents

| Path | Content |
|---|---|
| `solutions/benchmark_best.csv` | Best solution found for each of the 600 instances of the benchmark of D'Ambrosio et al. (2023). |
| `solutions/kpfsl_best.csv` | Best solution found for each of the 60 KPFS-L instances (n = 2000). |
| `solutions/best_provenance.csv` | The run behind each best value. |
| `runs/` | One compressed CSV per campaign with one row per run; `runs/INDEX.csv` lists the campaigns with their number of runs, instances and seeds, median run time, ablation flags, kernel version and the section of the article they belong to. |
| `reports/summaries/` | Per-group summaries of the campaigns (best and mean values, time of the best, published references). |
| `reports/analyses/` | Reports of the statistical analyses (ablation, targeted tests, fixed weights, decomposition of the capacity weight, rate diagnostic). |
| `reports/tables/` | Table rows generated for the article. |
| `scripts/verify.py` | Checks a solution file against the instances, with no dependency beyond Python 3. |

## Solution files

One row per instance with the columns `uid`, `file` (instance path), `scenario`, `type`, `n`, `k`, `value`
(profit minus forfeit costs), `optimal`, `found_by` and `items` (selected items, numbered from 0 and separated by
spaces). `optimal` is `yes` in the 13 benchmark groups in which CPLEX proved all ten optima and the mean of the
values equals the published CPLEX average; since the values are integers and none exceeds its optimum, each of
these 130 values is optimal. The global bound k of the benchmark follows D'Ambrosio et al. (2023, Section 4.1).

```
python scripts/verify.py solutions/benchmark_best.csv --root DIR
python scripts/verify.py solutions/kpfsl_best.csv --root DIR
```

`DIR` holds the instances under the paths of the column `file`: `KPFS_instances/` for the benchmark, as
distributed by its authors, and `kpfsl/` for KPFS-L, archived with the other new instances on Zenodo. All 660
solutions respect the capacity and the global bound and reach the stated value.

## Run records

Each row of a campaign file is one run: `uid` and `seed` identify it, and the other columns are those written by
the solver, for example `best` (value), `t_best` (seconds to the best solution), `elapsed`, `iters` (walker steps),
`it_per_s`, `flags` (ablation bits of the kernel; 0 is the full method), `kernel` (digest of the kernel source),
`restarts`, `traj` (improvements of the best value as `time:value` pairs separated by `;`) and `items` (the best
selection of the run). The runs of HiGHS and Hexaly give `status`, `obj` or `best`, `bound`, `gap` and `time`. The
per-epoch logs of the GPU runs are not included.

The GPU runs used an NVIDIA GeForce RTX 5080 (84 streaming multiprocessors) and the CPU runs an Intel Core
i9-13900KF, under Windows 11; the GPU code is CUDA C++ compiled at run time with NVRTC 12.9 through CuPy 14.2.

## Sources and license

- C. D'Ambrosio, F. Laureana, A. Raiconi, G. Vitale (2023), The knapsack problem with forfeit sets, Computers &
  Operations Research 151, 106093, https://doi.org/10.1016/j.cor.2022.106093.
- The solutions, run records and reports are licensed under CC BY 4.0 (`LICENSE-DATA`) and the scripts under the
  MIT license (`LICENSE`).
- To cite this repository, see `CITATION.cff`; the reference of the article will be added once it is published.
