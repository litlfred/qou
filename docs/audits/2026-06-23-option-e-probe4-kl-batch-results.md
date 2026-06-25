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

## Correction (2026-06-25) — the Betti sum is cell-dependent; the table above is one cell choice

The "Betti Sum" column above is computed for a **single** left cell per shape
(`canonical_Q`, the superstandard recording tableau). That value is **not
canonical**: distinct left cells of the *same* shape $\lambda$ have *different*
KL Betti sums $B_\lambda = \sum_{w\in\Gamma_\lambda} P_{e,w}(1)$. Direct
enumeration of **all** left cells over $S_6$
([`kl_betti_cell_dependence_probe.py`](../../computations/kl_betti_cell_dependence_probe.py),
literature-validated pure-Python KL — `kazhdan_lusztig._self_test` confirms
$P_{e,3412}=1+q$, $P_{e,w_0}=1$, etc.):

| shape $\lambda$ | $f^\lambda$ | #cells | Betti range (min..max) | `canonical_Q` (table above) |
|---|---|---|---|---|
| (6,) | 1 | 1 | 1 (invariant) | 1 |
| (5, 1) | 5 | 5 | 5 (invariant) | 5 |
| (4, 1, 1) | 10 | 10 | **10..26** | 10 |
| (4, 2) | 9 | 9 | **9..20** | 20 |
| (3, 1, 1, 1) | 10 | 10 | **10..23** | 10 |
| (3, 2, 1) | 16 | 16 | **22..54** | 41 |
| (2, 1, 1, 1, 1) | 5 | 5 | **5..9** | 5 |
| (3, 3) | 5 | 5 | **6..23** | 23 |
| (2, 2, 1, 1) | 9 | 9 | **12..32** | 21 |
| (2, 2, 2) | 5 | 5 | **6..21** | 21 |
| (1, 1, 1, 1, 1, 1) | 1 | 1 | 1 (invariant) | 1 |

Two corrections to the observations above:

1. **The "hooks match $f^\lambda$" observation is a `canonical_Q` artifact.**
   Hooks are **not** cell-invariant — e.g. $(4,1,1)$ ranges $10..26$ across its
   ten cells. `canonical_Q` happens to land on the low ($=f^\lambda$) cell for
   hooks but a high cell for non-hooks, which is what produced the "hook
   projector" appearance. Only the three trivial shapes $(6,)$, $(5,1)$, $(1^6)$
   are genuinely cell-invariant.

2. **$B_\lambda$ is therefore not a function of $\lambda$** and cannot supply the
   per-partition magnitude $|\Delta_\lambda|$ without an extra, unmotivated
   cell-selection rule. This is the *magnitude* leg of the PROBE-4 prune,
   complementing the already Lean-proved *sign* leg
   (`PartitionOf5.deltaSign_mixed`).

**Deuteron consequence.** Swapping $f^\lambda \to B_\lambda$ in the binding sum
makes the prediction swing with the (arbitrary) cell choice —
$B_{\mathrm{pred}} \in 0.457..0.817$ MeV (magnification $\times1.20..\times2.15$)
— and **no** choice reaches $B_{\mathrm{AME}} = 2.2245$ MeV (closing needs
$\times5.85$). The earlier disagreement between `kl_betti_extrapolation.py`
(first-cell) and this batch (`canonical_Q`) was exactly this cell-ambiguity.
This is an **(a)-scope** negative (this construction *alone* cannot supply
$|\Delta_\lambda|$); it is **not** a structural exclusion of KL data from every
closure. Witness:
[`kl-betti-cell-dependence.witness.json`](../../computations/kl-betti-cell-dependence.witness.json).
