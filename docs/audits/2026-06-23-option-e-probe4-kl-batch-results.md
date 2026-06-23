# Audit: Option E (Probe 4) KL Multiplicity Batch Results
**Date:** 2026-06-23

## Background
The Kashiwara crystal / KL-weight sub-path (PROBE 4) was previously pruned because KL-positivity means it cannot supply the negative sign required by $\Delta_\lambda$ for certain partitions. However, as noted, this does not preclude it from supplying the **magnitude** $|\Delta_\lambda| = f^\lambda$. To verify this, we ran a batch script over $S_6$ implementing the proposed definitions of $n^w_\lambda$.

## Results

### 1. KL Betti Number Sums ($P_{e,w}(1)$)
We partitioned $S_6$ into canonical left cells using the Robinson-Schensted-Knuth (RSK) correspondence and summed the intersection cohomology Betti numbers $P_{e,w}(1)$ for $w \in \Gamma_\lambda$. 

| Partition $\lambda$ | $f^\lambda = \dim(V_\lambda)$ | Betti Sum $\sum_{w \in \Gamma_\lambda} P_{e,w}(1)$ | Crystal Depth Sum |
|---------------------|-------------------------------|----------------------------------------------------|-------------------|
| (6,)                | 1                             | 1                                                  | 0                 |
| (5, 1)              | 5                             | 5                                                  | 5                 |
| (4, 2)              | 9                             | 20                                                 | 18                |
| (4, 1, 1)           | 10                            | 10                                                 | 30                |
| (3, 3)              | 5                             | 23                                                 | 15                |
| (3, 2, 1)           | 16                            | 41                                                 | 64                |
| (3, 1, 1, 1)        | 10                            | 10                                                 | 60                |
| (2, 2, 2)           | 5                             | 21                                                 | 30                |
| (2, 2, 1, 1)        | 9                             | 21                                                 | 63                |
| (2, 1, 1, 1, 1)     | 5                             | 5                                                  | 50                |
| (1, 1, 1, 1, 1, 1)  | 1                             | 1                                                  | 15                |

### Observations
* **Hook Partitions:** For all hook partitions $\lambda = (k, 1, \dots, 1)$, the KL Betti sum **perfectly matches** the required magnitude $f^\lambda$. 
* **Bulk Partitions:** For "bulk" (non-hook) partitions, the Betti sum bulges significantly above $f^\lambda$. For instance, at $\lambda = (3,2,1)$, the Betti sum is 41 while $f^\lambda = 16$.
* **Crystal Depths:** The Kashiwara crystal depths do not align with $f^\lambda$ and scale quadratically.

### Next Steps
The KL left-cell size itself is exactly $f^\lambda$ by construction. If we assign a uniform multiplicity $n^w_\lambda = 1$ to each element of the left cell, we trivially recover $f^\lambda$. However, the Betti sums specifically highlight a fascinating structural divergence: they act as a "hook projector" that matches $f^\lambda$ exclusively for hook shapes.

Since the deuteron binding formula incorporates all shapes (including non-hooks), the Betti sum requires an additional canonical truncation or character weighting to close the bulk partitions. I will push these scaffolding results to the branch `claude/option-e-probe4-kl-batch-2026-06-23` and open a PR.
