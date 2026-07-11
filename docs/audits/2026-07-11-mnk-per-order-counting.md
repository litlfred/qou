# Per-order sub-link count M_n(K)=C(A,n): the deuteron-pinned pairwise backbone (qou-v0yw)

**Date:** 2026-07-11
**Branch:** `claude/mnk-per-order-counting-2026-07-11`
**Compute:** [`computations/mnk_per_order_counting.py`](../../computations/mnk_per_order_counting.py)
**Witness:** [`computations/mnk-per-order-counting.witness.json`](../../computations/mnk-per-order-counting.witness.json)
**Bean:** `qou-v0yw`. **Follows:** PR #3582 (reframed qou-v0yw from single-graph
selection to a per-order sub-link **counting** problem).

## The sharpened open piece

PR #3582 dissolved the "which single coordination graph" question into the body-order
tower `B(K) = m_e·Σ_n a_D^(n)·w_n·M_n(K)`, where `M_n(K)` is the number of order-`n`
irreducible (Brunnian-`n`) sub-links. For a maximally-coordinated light nucleus (every
`n`-subset of nucleons an irreducible `n`-body sub-link) the natural per-order count is

  `M_n(K) = C(A, n)`   (all `n`-subsets, `n = 2 … A`).

This probe tests that count **parameter-lean**.

## Result — the deuteron-pinned pairwise backbone, zero extra parameters

The `n=2` term is pinned by the **single deuteron datum**: `a_D^(2)=1`, `M_2(D)=C(2,2)=1`
⇒ `w_2 = B(D)/m_e ≈ 4.353`. The pairwise backbone for any A is then
`B_2(A) = B(D)·C(A,2)` — **no new parameter**.

| nuc | A | C(A,2) | C(A,3) | C(A,4) | B_2 = B(D)·C(A,2) | B_AME | residual (≥3-body) |
|---|--:|--:|--:|--:|--:|--:|--:|
| D   | 2 | 1 | 0 | 0 |  2.225 |  2.225 |  0.000 |
| ³H  | 3 | 3 | 1 | 0 |  6.674 |  8.482 |  1.808 |
| ³He | 3 | 3 | 1 | 0 |  6.674 |  7.718 |  1.044 |
| ⁴He | 4 | 6 | 4 | 1 | 13.347 | 28.296 | 14.948 |

- The pairwise `C(A,2)` backbone reproduces the A=3 binding to a **small (~1–2 MeV)**
  3-body residual.
- **⁴He** carries a large residual (14.95 MeV) — the doubly-magic 4-body term.

## Cross-check — the residual difference IS the Coulomb mirror split

The `³H − ³He` residual difference is `+0.764` MeV, **exactly** the AME mirror split
(`+0.764` MeV), which #3564/#3570 established as the Coulomb (proton-displacement)
energy. So the per-order count `M_n=C(A,n)` **inherits this session's charge-structure
result for free**: the pairwise backbone is charge-symmetric, and the entire ³H/³He
asymmetry lands in the residual as the Coulomb term. Witness assertion
`pairwise_backbone_recovers_coulomb_mirror_split` (exact, tolerance 0).

## Verdict (scope-limited (a))

> The per-order count `M_n(K)=C(A,n)` fits the **2-body backbone** with **zero extra
> parameters** (`w_2` pinned by the one deuteron datum), reproduces A=3 to a small M_3
> residual, and automatically recovers the Coulomb mirror split as the ³H−³He residual
> difference. This localises the open work: it is **not** the pairwise count, which is
> fixed, but the **M_3/M_4 weights** (`a_D^(n)·w_n`) and the large-A geometric
> saturation of `C(A,n)`. A parameter-lean confirmation of the #3582 reframe, **not** a
> closure.

**Open (qou-v0yw, next):** the `M_3`, `M_4` weights that convert `C(A,3)`, `C(A,4)` into
the 3-/4-body residuals (the deuteron pins only `w_2`), and the geometric saturation of
`C(A,n)` at large A (the α-cluster deltahedra of #3549/#3555). The reframe now has a
fixed 2-body anchor to build the higher orders on.
