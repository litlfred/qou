# Deuteron-wall resummation — the "closed negatively" verdict is a wrong-transform artifact

**Date:** 2026-08-21 · **Branch:** `claude/alien-calculus-resurgence-nvvezn` · **Bean:** `qou-hok7` ·
**Discipline:** scope-(a) *mis-scope, not exclusion*; no fit; nothing wired; no `c_k`; L2 unchanged.

## Claim

The corpus currently records the deuteron-wall **resummation hypothesis as closed negatively**
(`deuteron_wall_full_transseries_probe.py`: the full level-1/2 Borel–Laplace median resummation
undershoots `B_D = 2.225 MeV` by ~40× at every substrate coupling). That verdict is answered on the
**wrong object with the wrong transform** and does **not** close the substrate deuteron resummation.

## The two mismatches

The full-transseries probe resummed:

1. **Object** — `a_D^(n) = I(n)/n`, the **q = 1** classical involution/telephone period; and
2. **Transform** — `b_n = a_D^(n) / Γ(n/2+1)`, the **classical** level-1/2 Borel divisor.

But `lever1_transfer_operator_spectral_qgevrey.py` (PR-landed) measured the **substrate** object
`Z_n(q₀)` (the q-deformed binding statistic) to be **q-Gevrey**: its per-level log-multiplier grows
linearly in `n`, so `log Z_n(q₀)` is `Θ(n²)` (lever1 records the order as `~ q₀^{n²/2}`). The same
quadratic signature `deg_q(c_n) = n²` appears in the C1 ∞-formal solution
([`2026-08-01-c1-inf-formal-solution-qgevrey`](2026-08-01-c1-inf-formal-solution-qgevrey.md)).

A Borel transform must divide the coefficients by the growth it is built to tame. The classical divisor
`Γ(n/2+1) = exp(Θ(n log n))` is exponentially too weak for `exp(Θ(n²))` growth:

| `n` | `q₀^{n²/2} / Γ(n/2+1)` (classical Borel coefficient) |
|----:|----:|
| 4 | 1.15 |
| 16 | 15.7 |
| 24 | 2.35 × 10⁴ |
| 32 | 7.59 × 10⁹ |
| 40 | 7.34 × 10¹⁷ |

The classical Borel-transformed coefficient of a q-Gevrey series **diverges** — the classical
Borel–Laplace is simply not a resummation of `Z_n(q₀)`. It is a resummation of the `q = 1` shadow
`a_D^(n)`, whose classical Borel series has a *finite* radius (`|b_n|^{1/n} → ≈1.40`), consistent with
the full-transseries probe having resummed that shadow correctly.

## Consequence

The `~40×` undershoot is a **wrong-transform artifact**, not a statement about the substrate deuteron
binding. The deuteron-wall resummation hypothesis is therefore **reopened**: the correct test is the
**q-Borel–Laplace resummation of `Z_n(q₀)`** (divisor of order `q₀^{n²/2}`, the q-Gaussian scale), which
has not been done. The q-Borel machinery exists in the corpus
([`2026-08-01-qborel-ecalle-resum-barodd`](2026-08-01-qborel-ecalle-resum-barodd.md),
`qbeta_habiro_tail_util.py`) but has not been pointed at the deuteron binding statistic.

## Honesty / scope

This does **not** claim the q-Borel sum reaches `B_D` — a faster-divergent series *can* carry a larger
non-perturbative content, which is the physical reason to test it, but that is exactly the open
computation. The finding is only that the existing negative closure is mis-scoped (a scope-(a) route
mis-classification, corrected) and must be redone with q-Borel. The separate working deuteron channel
(the q-rotational `μ₀·ℏ_q·J_q²` route, `B_D` to −9%, 0 params) is unaffected.

## Compute

- Probe: [`computations/deltalambda/deuteron_wall_wrong_transform_diagnostic.py`](../../computations/deltalambda/deuteron_wall_wrong_transform_diagnostic.py) (exit 0)
- Witness: `computations/deltalambda/deuteron-wall-resummation-wrong-transform.witness.json`

## Cross-references

- The mis-scoped negative: `computations/deltalambda/deuteron_wall_full_transseries_probe.py`
- q-Gevrey class of the substrate object: `computations/lever1_transfer_operator_spectral_qgevrey.py`
- q-Gevrey C1 signature: [`2026-08-01-c1-inf-formal-solution-qgevrey.md`](2026-08-01-c1-inf-formal-solution-qgevrey.md)
- q-Borel machinery: [`2026-08-01-qborel-ecalle-resum-barodd.md`](2026-08-01-qborel-ecalle-resum-barodd.md)
- Next step (open): q-Borel–Laplace resummation of `Z_n(q₀)` — bean `qou-hok7`.
