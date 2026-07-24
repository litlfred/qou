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
under the `(f^λ)^β` measure. This is a **Griffiths-II / FKG / Harris-type** correlation inequality.

## Why this is progress

- **Sidesteps the dimension obstruction.** The literature stalls because `f^λ = χ^λ(e)` is not a
  polynomial function of the diagram (`∉ A`). Here `Σc²` and `Σ ln h` are **both explicit box-sums** —
  the covariance is between two honest diagram statistics, the natural input to a correlation
  inequality, not a covariance with the transcendental dimension.
- **Compact interval, not a ray.** Only `β ∈ [2,3]` matters (β=3 inside the monotone window [2,4]);
  the global-`β` non-monotonicity (the `4→5` rise) is irrelevant to the kernel.
- **Names a concrete, well-populated toolkit.** Griffiths-II second correlation inequality and FKG
  give `Cov ≥ 0` for pairs of monotone (increasing) functions under log-supermodular / ferromagnetic
  measures. The remaining work is to establish log-supermodularity (or the relevant association) of
  the `(f^λ)^β` measure on the appropriate order, and monotonicity of `Σc²`, `Σ ln h` — a definite,
  checkable program.

## Verification

40-dps, fine `β`-grid over `[2,3]` (step `1/20`), all `k ≤ 14`:

| claim | status |
|---|---|
| `E_β[C₂]` monotone non-increasing on `[2,3]` | ✓ all k |
| `Cov_β(C₂, ln f) ≤ 0` on `[2,3]` | ✓ all k |
| `Cov_β(Σc², Σ ln h) ≥ 0` on `[2,3]` (the FKG target) | ✓ all k |

## Honesty

This **sharpens** the open target; it does **not** close it. The kernel remains an honest §3b
conjecture-`sorry`. What is *not* yet proved: the correlation inequality `Cov_β(Σc², Σ ln h) ≥ 0`
itself (the log-supermodularity / association of the `(f^λ)^β` measure is not established).

## Compute

- Probe: [`computations/deltalambda/wlambda_covariance_epic_phase4_interval_fkg.py`](../../computations/deltalambda/wlambda_covariance_epic_phase4_interval_fkg.py) (exit 0)
- Witness: `computations/deltalambda/wlambda-covariance-epic-phase4-interval-fkg.witness.json`

## Cross-references

- Literature assessment: [`2026-07-24-covariance-kernel-literature-assessment.md`](2026-07-24-covariance-kernel-literature-assessment.md)
- Phase 3 (β-ensemble reframing): [`2026-07-24-covariance-kernel-proof-epic-phase3.md`](2026-07-24-covariance-kernel-proof-epic-phase3.md)
- Fulman (`math/0305423`); Griffiths-II / FKG classical correlation inequalities
