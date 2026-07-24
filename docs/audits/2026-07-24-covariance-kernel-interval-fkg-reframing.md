# Covariance-kernel epic (qou-x631) — interval / FKG reframing (by analogy with Fulman)

**Date:** 2026-07-24 · **Branch:** `claude/deltalambda-covariance-epic-phase3-2026-07-24` ·
**Tier:** reframing (40-dps verified) · **Discipline:** scope-(a); no fit; nothing wired; no `c_k`;
L2 unchanged (2/7). **Epic:** `qou-x631`. **Follows:** the literature assessment (same branch).

## The analogy question

Can the machinery of the uploaded papers (Fulman's Stein / eigenfunction-drift, the
correlation-inequality toolkit) be used *by analogy* rather than by direct citation? **Yes — and it
sharpens the open target substantially.**

Fulman's Stein proof works because his statistic (the transposition character ratio) is an
**eigenfunction of the down-up Markov chain on Young diagrams whose drift has a controllable sign**.
Applying that lens to our kernel does not remove the dimension obstruction directly, but it re-expresses
the kernel as a **compact-interval correlation inequality** between two explicit box-sum statistics —
exactly the setting where Griffiths-II / FKG / Harris correlation inequalities apply.

## The sharpening

The kernel `cov(k) = Σ_{λ⊢k}(f^λ)³ ω₃(λ) ≤ 0` (with `ω₃ = Σ_□c(□)² − C(k,2)`) is, at the measure
level, `H(3) ≤ 0` for `H(β) := E_β[C₂] − C(k,2)`, `E_β[X] = Σ_λ(f^λ)^β X / Σ_λ(f^λ)^β`.

**We do not need the full `β ≥ 2` family** (whose global monotonicity fails — Phase 1 found `H` rises
`4→5`). `β = 3` sits **inside the monotone-decreasing window**: `E_β[C₂]` decreases `2→3→4`. So the
kernel follows from the **compact-interval** statement

> `d/dβ E_β[C₂] = Cov_β(C₂, ln f) ≤ 0`  for all `β ∈ [2,3]`,

integrated from `H(2) = 0`. And since `ln f^λ = ln(k!) − Σ_□ ln h(□)` (hook lengths), this is

> **`Cov_β( Σ_□ c(□)²,  Σ_□ ln h(□) ) ≥ 0`  for `β ∈ [2,3]`**

— a **positive correlation between two explicit box-sum statistics** (content-spread and log-hook-sum)
under the `(f^λ)^β` measure.

## Why this is progress (and its precise limits)

- **Compact interval, not a ray.** Only `β ∈ [2,3]` matters (β=3 inside the monotone window [2,4]);
  the global-`β` non-monotonicity (the `4→5` rise) is irrelevant to the kernel. *(Valid.)*
- **Lowers the dimension POWER** (not an escape). The reduction goes from the `(f^λ)³`-weighted sum to
  a `ln f`-covariance. Since `ln f` has a convergent Kerov expansion in the `Σ_μ` while `f` does not,
  this is a genuine simplification. **But it does NOT sidestep the dimension**: `Σ ln h = ln k! − ln f`
  still *is* the log-dimension, which is **not** a polynomial function of the diagram (`∉` the
  Ivanov–Olshanski algebra `A`). An earlier version of this note claimed the reduction escaped the
  dimension — that was wrong; corrected here (Phase 4b).

## Off-the-shelf closers — both ELIMINATED (Phase 4b)

The natural attempt is a Griffiths/FKG or Chebyshev correlation inequality. Both **fail**:

- **FKG on the dominance lattice — ELIMINATED.** FKG needs `(f^λ)^β` log-supermodular
  (`f^{λ∨μ}·f^{λ∧μ} ≥ f^λ·f^μ`). This holds for `k ≤ 7` but **fails at `k = 8`** (counterexample
  `λ=(4,2,1,1), μ=(3,3,2)`: `f_λ f_μ = 3780 > f_∨ f_∧ = 3136`). Moreover the two functions are **not**
  dominance-monotone: `C₂` and `Σ ln h` are conjugation-invariant and **U-shaped** (large at row and
  column extremes, small in the balanced middle), so a monotone-function FKG hypothesis cannot hold.
  *(An earlier version claimed `C₂`, `Σ ln h` monotone — wrong; corrected.)*
- **Chebyshev / comonotonicity — ELIMINATED.** If `C₂` and `Σ ln h` were comonotone, `Cov ≥ 0` under
  *every* measure (which would even contradict the Phase-1 `4→5` rise). They are only **~77–80 %
  pairwise concordant**; the systematic discordant family is the near-hook pair `(m,2)` vs `(m,1,1)`
  (`ΔC₂ = −4` while `ΔΣln h > 0`).

## Verification

40-dps, fine `β`-grid over `[2,3]` (step `1/20`), all `k ≤ 14`:

| claim | status |
|---|---|
| `E_β[C₂]` monotone non-increasing on `[2,3]` | ✓ all k |
| `Cov_β(C₂, ln f) ≤ 0` on `[2,3]` | ✓ all k |
| `Cov_β(Σc², Σ ln h) ≥ 0` on `[2,3]` | ✓ all k |
| `(f^λ)^β` log-supermodular on dominance | ✗ fails at k=8 |
| `C₂`, `Σ ln h` comonotone | ✗ ~77% concordant |

## Honesty

This **sharpens** the open target (interval reduction + lower dimension power); it does **not** close
it, and the two obvious closers (FKG, Chebyshev) are eliminated. The kernel remains an honest §3b
conjecture-`sorry`. The reduced inequality `Cov_β(C₂, ln f) ≤ 0 on [2,3]` is still genuinely open, and
still involves the log-dimension `ln f ∉ A`.

## Compute

- Probe: [`computations/deltalambda/wlambda_covariance_epic_phase4_interval_fkg.py`](../../computations/deltalambda/wlambda_covariance_epic_phase4_interval_fkg.py) (exit 0)
- Witness: `computations/deltalambda/wlambda-covariance-epic-phase4-interval-fkg.witness.json`

## Cross-references

- Literature assessment: [`2026-07-24-covariance-kernel-literature-assessment.md`](2026-07-24-covariance-kernel-literature-assessment.md)
- Phase 3 (β-ensemble reframing): [`2026-07-24-covariance-kernel-proof-epic-phase3.md`](2026-07-24-covariance-kernel-proof-epic-phase3.md)
- Fulman (`math/0305423`); Griffiths-II / FKG classical correlation inequalities
