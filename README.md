# Data for “Exact swap evaluation for convex set-count penalties: a GPU tabu search for the knapsack problem with forfeit sets”

Data of the article "Exact swap evaluation for convex set-count penalties: a GPU tabu search for the knapsack
problem with forfeit sets", submitted to Computational Optimization and Applications: the new instances, the cluster windows with and without split
applications, the best solution found for each instance, the records of every run of CoPTS-KPFS and of the
reference solvers, the reports of the analyses and a solution verifier.

Authors: José García (ORCID 0000-0003-3126-8352) and Luis Rojas-Valdivia (ORCID 0009-0005-8935-7595), Escuela de Ingeniería de Construcción y Transporte, Pontificia
Universidad Católica de Valparaíso, Avenida Brasil 2147, Valparaíso, Chile. Corresponding author: José García,
jose.garcia@pucv.cl.

Online Resource 1 of the article is the PDF with its supplementary analyses (Sections S1 to S10 and Tables S1 to
S7). Section numbers below refer to the article.

| Path | Content |
|---|---|
| `solutions/benchmark_best.csv` | Best solution found for each of the 600 instances of the benchmark of D'Ambrosio et al. (2023). |
| `solutions/kpfsl_best.csv` | Best solution found for each of the 60 KPFS-L instances (n = 2000). |
| `solutions/best_provenance.csv` | The run behind each best value. |
| `runs/` | One compressed CSV per campaign with one row per run; `runs/INDEX.csv` lists the campaigns with their section of the article, number of runs, instances and seeds, median run time, ablation flags and kernel digest. |
| `reports/summaries/` | Per-group summaries of the campaigns (best and mean values, time of the best, published references). |
| `reports/analyses/` | Reports of the statistical analyses (ablation, targeted tests, fixed weights, decomposition of the capacity weight, rate diagnostic). |
| `reports/tables/` | Table rows generated for the article. |
| `reports/evalcost/` | Cost of the exact step (Section 7.2): timings of the evaluators on every recorded state. |
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
distributed by its authors, and `kpfsl/` for KPFS-L, as in `instances/kpfsl/` of this package. All 660 solutions
respect the capacity and the global bound and reach the stated value.

## Run records

Each row of a campaign file is one run: `uid` and `seed` identify it, and the other columns are those written by
the solver, for example `best` (value), `t_best` (seconds to the best solution), `elapsed`, `iters` (walker steps),
`it_per_s`, `flags` (ablation bits of the kernel; 0 is the full method), `kernel` (digest of the kernel source),
`restarts`, `traj` (improvements of the best value as `time:value` pairs separated by `;`) and `items` (the best
selection of the run). The runs of HiGHS and Hexaly give `status`, `obj` or `best`, `bound`, `gap` and `time`. The
per-epoch logs of the GPU runs are not included.

The GPU runs used an NVIDIA GeForce RTX 5080 (84 streaming multiprocessors) and the CPU runs an Intel Core
i9-13900KF, under Windows 11; the GPU code is CUDA C++ compiled at run time with NVRTC 12.9 through CuPy 14.2.

## Cost of the exact step (Section 7.2)

`reports/evalcost/replay/` holds, for each of the 23 instances of Table 10, one row per recorded state (`.csv`):
the size of the selection, the number of classes and of triplets, the share of the pairs that share a tight set, the
operation counts and the median time in microseconds of E1, E2, E3 and E3+ (`t_E1`, `t_E2`, `t_E3n`, `t_E3p`), and
whether E2, E3 and E3+ selected the same best and best non-tabu moves as E1 (`match_*`); the `.json` file of each
instance counts the discrepancies (none) and the states also checked by applying every move. `reports/evalcost/
report.txt` gives the medians per instance. The full runs of the same section are the campaigns `evalcost_e3plus`
(E3+ for 10 s with seed 1), `evalcost_e1` and `evalcost_e2` (the same number of steps with the same seed) in
`runs/`; the three follow the same trajectory in all 20 instances.

## Source

C. D'Ambrosio, F. Laureana, A. Raiconi, G. Vitale (2023), The knapsack problem with forfeit sets, Computers &
Operations Research 151, 106093, https://doi.org/10.1016/j.cor.2022.106093. The benchmark instances are not
redistributed here.

## Instances

`instances/` holds the new instances of the article: KPFS-L (`kpfsl/`, 60 instances with n = 2000), the bridge
programs (`bridge_programs/` and, for the frontier of the cost of a work zone, `bridge_programs_lambda/`) and the
maintenance windows of the cluster (`cluster_windows/`), each with a manifest; `instances/README.md` describes them.

## Cluster windows without split applications

`cluster_unsplit/` holds the windows rebuilt without splitting the five applications on 256 machines or more
(`srv-*/`, with manifests), the evaluation of the programs found on the split windows (`eval_split_programs.json`
for the best program of each search and `eval_split_seeds.json` for every seed), and the runs on the unsplit
windows (Section 8.2 and Section S7 of Online Resource 1): HiGHS for one hour (`srv-R1_highs3600.json`, started from
the best program of the GPU search, which is feasible there; `srv-R1_highs3600_cold.json` and
`srv-U1_highs3600.json`, started from no solution) and five seeds of one minute of the CPU search
(`srv-*_ts60_s*.json`). The GPU search was not run on these windows.

## Additional checks

`results/` holds the pooled best-known target analysis (`review_targets.txt`, Table S1 of Online Resource 1), the
ranges of the packed accumulators of the GPU kernel on every instance of the study (`accumulator_bounds.csv`) and
the move test with large penalty weights (`argmax_penalty.log`), the ablation with targets from independent seeds
and its ratios per instance (`split_targets.txt`, Section S9 of Online Resource 1), the excursions of the confined
quarter in the CPU and GPU implementations (`regime_excursions.txt`, `regime_excursions_gpu.txt` and, per tabu tenure,
`regime_excursions_gpu_tenure.txt`, Section S10), the moves selected by the GPU kernel with the tie-breaking noise
on, compared with an exact enumeration with the same noise (`moves_noise.txt`, Section 5.3 and Proposition 11 of the
article), and the enumeration check of the class reduction, of its sorted variant for count functions of any
curvature and of the selection of the same move under a total order (`check_generalization_sorted.txt`, Theorem 7
and Remark 1 of the article). The source code of the solvers and of the analyses is not included.

## License

The data (instances, solutions, run records and reports) are licensed under the Creative Commons Attribution 4.0
International license (CC BY 4.0). `scripts/verify.py` is licensed under the MIT license (`LICENSE`). See `LICENSE-DATA`.

## Citation

García, J., & Rojas-Valdivia, L. (2026). Data for "Exact swap evaluation for convex set-count penalties: a GPU tabu search for the knapsack problem with forfeit sets" [Data set]. GitHub.
https://github.com/rubincus/kpfs-copts-gpu-results

`CITATION.cff` gives the same reference; the reference of the article will be added once it is published.
