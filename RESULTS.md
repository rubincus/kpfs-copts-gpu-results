# Results of the article, file by file

This guide maps every result of the article "Exact swap evaluation for convex set-count penalties: a GPU tabu search
for the knapsack problem with forfeit sets" (submitted to Computational Optimization and Applications) and of its
Online Resource 1 to the files of this repository. Section, table and figure numbers are those of the submitted
article; Sections S1 to S10 and Tables S1 to S7 are those of Online Resource 1.

## What is where

| Path | Content |
|---|---|
| `tables/` | Every results table of the article (Tables 3 and 5 to 17) and of Online Resource 1 (Tables S1 to S7), as CSV with the values as printed; `tables/INDEX.csv` gives the caption of each. |
| `figures/` | The data drawn in each figure of the article (Figures 1 to 9), one row per point; `figures/INDEX.csv` gives the captions. |
| `runs/` | One compressed CSV per campaign, one row per run; `runs/INDEX.csv` gives the section of the article of each campaign. |
| `solutions/` | The best solution found for each instance and the run that found it. |
| `reports/` | Per-group summaries of the campaigns, reports of the statistical analyses, table rows and the cost study of Section 7.2. |
| `results/` | Additional checks cited in the article and in Online Resource 1. |
| `instances/`, `cluster_unsplit/` | The new instances, and the cluster windows rebuilt without split applications with their runs. |
| `scripts/verify.py` | Checks a solution file against the instances. |

`README.md` describes the columns of the solution files and of the run records.

### Table files

`tables/table_<number>_<label>.csv` holds one header line with the column titles of the table (a title that spans
several columns is repeated in each of them) and one line per printed row, with the values as printed. Bold type (the
best value of a row) is not kept, `–` stands for a value not reported, a row that only names a block of rows (for
example "Scenario 1") has a single filled cell, and an empty first cell repeats the value of the row above. Tables 1,
2 and 4 (literature, positioning and design decisions) are not results and are not included.

### Figure files

`figures/figure_<number>_<label>.csv` holds one row per drawn point, with the columns

- `panel` (position of the panel in the figure), `panel_title`, `x_label`, `y_label`;
- `series` (the legend entry), `mark` (`plot`, `step`, `scatter`, `errorbar`, `bar`, `fill_between`, `hlines`,
  `vlines`, `axhline`, `axvline`), `colour` and `point` (order within the mark);
- `x`, `y` and `second_value` (the other edge of a band or of a segment, or the error of an error bar, written
  `low|high` when it is asymmetric);
- `x_tick`, `y_tick`: the text of the tick at that position when the axis shows categories (for example the group and
  variant of a ratio in Figure 5, or the number of items in Figure 1).

The files were recorded from the scripts that drew the published figures. Redrawn from the same data, the figures
match the published ones pixel for pixel, except for the margin of one axis in Figures 2 and 8. The lines of Figure 7
that join the projects of each trip are not recorded; they follow from the sets of `instances/bridge_programs/`.

## Measures

- Best known value of an instance: the best value of any run on it (`solutions/*_best.csv`; the run is named in
  `solutions/best_provenance.csv`). Gap to the best known value: 100 (best known − value) / best known.
- Benchmark (Section 7.1): group averages over the ten instances of each group, compared with the published averages
  of the methods of Table 1.
- Easy target (Sections 7.3 and 7.5): the worst final value of the full method over its ten seeds on an instance,
  which every run of the full method reaches. The time to a target is read from the improvements of a run (column
  `traj` of the run records).
- Paired comparisons (Sections 7.5 and 7.6): runs with the same instance and seed; ratio of the median times to the
  target, sign test with a Holm correction, and 95% percentile bootstrap intervals from 2000 resamples of the pairs.
- Ablation bits (column `flags` of the run records; 0 is the full method): 1 fixed β, 2 fixed μ, 4 single controller,
  8 θ = 0, 16 no pair correction. The campaigns `abl_coop0*` run without cooperation.
- Variants of the capacity weight (`bdec_*`, Section 7.6 and Sections S4 to S6): H holds β with the quarter confined,
  Q frees the quarter, X sets β = 1 for all walkers; F is the full method.

## Tables

| Table | File | Data behind it |
|---|---|---|
| 3. Slack in the benchmark (Section 3) | `table_03_slackbench.csv` | Best selections of `solutions/benchmark_best.csv`, on the benchmark instances of D'Ambrosio et al. (2023), which are not redistributed |
| 5. Parameters (Section 4) | `table_05_params.csv` | Configuration of every run of CoPTS-KPFS |
| 6. Throughput (Section 5) | `table_06_throughput.csv` | Dedicated throughput runs on two benchmark instances; only the values of the table are given |
| 7. Instances (Section 6) | `table_07_instances.csv` | `instances/*/MANIFEST.csv`; the benchmark of D'Ambrosio et al. (2023) |
| 8, 9. Benchmark (Section 7.1) | `table_08_bench12.csv`, `table_09_bench34.csv` | `runs/main_gpu30`; `reports/summaries/main_gpu30_summary.csv`; `reports/tables/tab_benchmark.tex` |
| 10. Cost of the exact step (Section 7.2) | `table_10_cost.csv` | `reports/evalcost/` (`report.txt` and the states of `replay/`); `runs/evalcost_e1`, `evalcost_e2`, `evalcost_e3plus` |
| 11. Contribution of the GPU design (Section 7.3) | `table_11_contrib.csv` | `runs/contrib_cpu32`, `contrib_port`, `contrib_gpu`, `contrib_rate_cpu1`, `contrib_rate_cpu8`, `contrib_rate_cpu16`, `contrib_rate_cpu24`; `reports/summaries/contrib_*` |
| 12. KPFS-L (Section 7.4) | `table_12_kpfsl.csv` | `runs/main_gpu60_kpfsl`, `cpu30_kpfsl`, `hexaly30_kpfsl`, `hexaly3600_kpfsl`, `highs3600_kpfsl`, `highs3600_kpfsl_b`; `solutions/kpfsl_best.csv`; `reports/tables/kpfsl_table_rows.tex` |
| 13. Slack in the ablation groups (Section 7.5) | `table_13_slack.csv` | Best selections (column `items`) of `runs/abl_f0` and `abl_f0_kpfsl` |
| 14. Ablation (Section 7.5) | `table_14_ablation.csv` | `runs/abl_f0`, `abl_f1`, `abl_f2`, `abl_f4`, `abl_f8`, `abl_f16`, `abl_coop0` and their `_kpfsl` campaigns; `reports/summaries/abl_*` |
| 15. Bridge programs (Section 8.1) | `table_15_bridges.csv` | `instances/bridge_programs/`; `runs/metro_highs600` |
| 16. Maintenance windows (Section 8.2) | `table_16_cluster.csv` | `instances/cluster_windows/`; `runs/servers` (HiGHS and the CPU search) and `runs/apps_gpu__windows` (GPU search) |
| 17. Windows without split applications (Section 8.2) | `table_17_unsplit.csv` | `cluster_unsplit/` |
| S1. Pooled best-known target (S1) | `table_S1_s1.csv` | `results/review_targets.txt` |
| S2. Two parts of the capacity weight (S4) | `table_S2_s2.csv` | `reports/analyses/bdec_report.txt`; `runs/bdec_*` |
| S3. Programs on split and unsplit windows (S7) | `table_S3_s4a.csv` | `cluster_unsplit/eval_split_programs.json`, `eval_split_seeds.json` |
| S4. Trips skipped by the cap (S8) | `table_S4_s5.csv` | Counted while the bridge programs were rebuilt from their sources; only the values of the table are given |
| S5, S6. Targets from independent seeds (S9) | `table_S5_s9a.csv`, `table_S6_s9b.csv` | `results/split_targets.txt`; the ablation campaigns `runs/abl_*` |
| S7. Excursions of the confined quarter (S10) | `table_S7_s10.csv` | `results/regime_excursions.txt`, `regime_excursions_gpu.txt` |

## Figures

| Figure | File | Data behind it |
|---|---|---|
| 1. Benchmark against the best published averages (Section 7.1) | `figure_1_bench.csv` | `runs/main_gpu30`, as in Tables 8 and 9 |
| 2. Cost of the exact step against the structure (Section 7.2) | `figure_2_cost.csv` | `reports/evalcost/replay/` |
| 3. Contribution of the GPU design (Section 7.3) | `figure_3_contrib.csv` | `runs/contrib_cpu32`, `contrib_port`, `contrib_gpu` (times to the target) and `contrib_rate_cpu*` (step rates) |
| 4. Gap over time on KPFS-L (Section 7.4) | `figure_4_kpfsl.csv` | `runs/main_gpu60_kpfsl`, `cpu30_kpfsl`, `hexaly3600_kpfsl`, `highs3600_kpfsl`, `highs3600_kpfsl_b`; `solutions/kpfsl_best.csv` |
| 5. Ablation and targeted tests (Sections 7.5, S2 and S3) | `figure_5_ablation.csv` | `runs/abl_*` and `runs/tgt*`; `reports/analyses/targeted_report.txt`, `targeted_B2_report.txt` |
| 6. Maintenance windows (Section 8.2) | `figure_6_cluster.csv` | (a) `instances/bridge_programs/` (L5) and `instances/cluster_windows/`; (b) `runs/servers` and `runs/metro_highs600` (L5); (c) `runs/servers` and `runs/apps_gpu__windows` (U1) |
| 7. Map of two bridge programs (Section 8.3) | `figure_7_bridgemap.csv` | `instances/bridge_programs/` (metro-NYC-L4: bridges, projects and sets) and the optimal program of L4 in `runs/metro_highs600` |
| 8. Trade-offs of the bridge program (Section 8.3) | `figure_8_bridgefront.csv` | `runs/metro_frontier_lam__*` (delay cost λ) and `runs/metro_frontier_k` (global bound k′); `instances/bridge_programs_lambda/` |
| 9. Cap on forced evictions (Section 8.3) | `figure_9_cap.csv` | `runs/servers__u1_cap` and `runs/apps_gpu__caps` |

## Campaigns by section

`runs/INDEX.csv` lists every campaign with its section, number of runs, instances and seeds, median run time,
ablation flags and kernel digest.

| Section | Campaigns |
|---|---|
| 7.1 Benchmark | `main_gpu30` |
| 7.2 Cost of the exact step | `evalcost_e1`, `evalcost_e2`, `evalcost_e3plus` |
| 7.3 Contribution of the GPU design | `contrib_*` |
| 7.4 KPFS-L | `main_gpu60_kpfsl`, `gpu180_kpfsl`, `gpu360_kpfsl`, `cpu30_kpfsl`, `hexaly30_kpfsl`, `hexaly3600_kpfsl`, `highs3600_kpfsl`, `highs3600_kpfsl_b` |
| 7.5 Ablation and targeted tests (S2, S3, S9) | `abl_*`, `tgtA_*`, `tgtB_*`, `tgtB1_*`, `tgtB2_*` |
| 7.6 Fixed and adaptive weights (S4 to S6) | `fixw_*`, `bdec_*`, `diag_rate` |
| 8 Applications | `metro_*`, `servers`, `servers__u1_cap`, `apps_gpu__*`, `apps_gpu_q__*` |
| Preliminary, not used in the article | `camp30`, `gpu30_s123`, `gpu30_s4`, `hexaly30_s4` |

The reports of the analyses of Sections 7.5 and 7.6 and of Sections S2 to S6 are in `reports/analyses/`
(`targeted_report.txt`, `targeted_B1_report.txt`, `targeted_B2_report.txt`, `bdec_report.txt`, `bdec_report2.txt`,
`bdec_report3.txt`, `diag_rate_report.txt` and their checks). `results/` also holds the move test of the GPU kernel
with the tie-breaking noise on (`moves_noise.txt`, Section 5.3 and Proposition 11), the enumeration check of the
class reduction (`check_generalization_sorted.txt`, Theorem 7 and Remark 1), the ranges of the packed accumulators of
the kernel (`accumulator_bounds.csv`) and the move test with large penalty weights (`argmax_penalty.log`).
