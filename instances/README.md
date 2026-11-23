# New instances of the knapsack problem with forfeit sets

This package holds the new instances of the article "Exact swap evaluation for convex set-count penalties: a
GPU tabu search for the knapsack problem with forfeit sets". Section numbers refer to the article.

## Contents

| Folder | Content |
|---|---|
| `kpfsl/` | KPFS-L: 60 instances with n = 2000 items (Section 6.1), ten of each type (NC, C, FC) in scenarios 3 and 4, with capacity b = 3100 and global bound k = 133. `MANIFEST.csv` lists, for every file, its parameters, the seed and the SHA-256 digest. |
| `bridge_programs/` | The seven bridge programs L0-L6 (Section 8.1), built from the 2025 National Bridge Inventory. Per program: the instance (`.txt`), its projects, its bridges with their NBI identifiers, and its forfeit sets (CSV). `MANIFEST.csv` gives the parameters of each program, its global bound k, the constant f0 of its mandatory projects and the SHA-256 digest of the instance. |
| `bridge_programs_lambda/` | The ten variants of L4 in which the cost of a work zone is scaled by lambda from 0.05 to 3 (Section 8.1), with the same files; `lam1` is L4 itself. |
| `cluster_windows/` | The six maintenance windows R1, R10, R25, U1, U10 and U25 (Section 8.2), built from the Alibaba cluster trace v2018. Per window: the instance (`.txt`) and its forfeit sets, the services of the cluster (CSV). `MANIFEST.csv` gives b, k, the parameters and the SHA-256 digest of each window. |

## Problem and file format

A selection of items must respect the capacity (total weight at most b) and the global bound (at most k items
beyond the allowances of the forfeit sets, counted over all sets); its value is the total profit minus the cost
d of every item beyond the allowance h of each set.

The instance files follow the format of the benchmark of D'Ambrosio et al. (2023): a line `n l b`, a line with
the n profits, a line with the n weights and, for each of the l forfeit sets, a line `h d size` (allowance,
cost of each item beyond the allowance, number of items) followed by a line with its items, numbered from 0.
The global bound k is not stored in the instance files; it is given by the manifests.

In the bridge programs, the mandatory projects are removed exactly: the value of a program is the value of the
instance plus the constant `f0` of the manifest. The items of an instance are the projects with an index in
column `j` of its projects file (the mandatory projects have it empty), and the bridges file links every bridge
to its project and to its NBI record (columns `state` and `structure`). In the cluster windows, the items are the machines and each forfeit set is a service on two or
more machines. The caps of U1 (Section 8.2) and the frontier of k on L4 (Section 8.1) use the files of `srv-U1`
and `metro-NYC-L4` with other values of k.

## Sources and terms

- C. D'Ambrosio, F. Laureana, A. Raiconi, G. Vitale (2023), The knapsack problem with forfeit sets, Computers &
  Operations Research 151, 106093, https://doi.org/10.1016/j.cor.2022.106093 (benchmark whose format and
  generation recipe KPFS-L follows).
- National Bridge Inventory 2025, Federal Highway Administration, U.S. Department of Transportation,
  https://www.fhwa.dot.gov/bridge/nbi/ascii2025.cfm.
- Alibaba cluster trace v2018, Alibaba Open Cluster Trace Program, https://github.com/alibaba/clusterdata. The
  trace may be used for research or study purposes, and the maintenance windows derived from it are provided under
  the same terms.
- KPFS-L and the bridge programs are released under the Creative Commons Attribution 4.0 International license
  (CC BY 4.0).

## Changes in version 1.1

The README gives the final title of the article and the section that describes KPFS-L, and the manifest of the cluster windows adds the SHA-256 digest of each instance. The instance files are those of version 1.0.
