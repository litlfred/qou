# The μ₃ (A=3 magnitude) target is baseline-class-relative — the "1.6× gap" is smaller than the target's own convention-spread

**Date:** 2026-08-01 · **Branch:** `claude/mu3-target-frame-robustness-2026-08-01` · **PR:** #4491 ·
**Axis:** Δ_λ / A=3 magnitude gate · **Tier:** scope-(a) frame-robustness measurement (exact mpmath +
Lean-proved amplification/sign facts; **no fit**; nothing wired).

## 0. The question no sibling was asking

Every Δ_λ A=3 sibling attacks the **1.6× magnitude gap** — the derived 3-body cluster
`c₃ = 0.297 MeV = 0.63·μ₃` (`BorromeanMagnitudeLift`, #4364) reaches only `0.63×` the target
`μ₃ = +0.4708` (`AdditiveResidualSimplex`, #4320) — **assuming μ₃ is the target.** Three 0-fit routes
(s5-so3 `W_λ`, cable width, A=4 extension) all walled trying to *close* it
([2026-07-26 three-walls audit](2026-07-26-deltalambda-a3-magnitude-source-three-walls.md)).

This branch asks the orthogonal question: **is μ₃ = 0.4708 itself frame-robust, or is the "1.6× gap"
an artefact of the subtracted-baseline convention** — the way `g₂ = 1+r`'s `r` turned out
frame-flattered (`BindingResidualAmplification`, #4319 thread)?

## 1. The fragility

`μ₃ = M(3) − 3·μ₂`. With the deuteron self-reference forcing `μ₂ = M(2) = 0` (DERIVED), this collapses
to

    μ₃ = M(3) = ρ_strong(3) − ρ_grad(3) ≈ 3.8128 − 3.3420 = 0.4708.

μ₃ is a **small residual (≈0.47) that is the difference of two O(3.5) numbers** — the exact `g₂ = 1+r`
structure. A small difference of large numbers has an **amplified** sensitivity to any convention that
shifts the subtracted baseline: `relative-sensitivity(μ₃ ← ρ_grad(3)) = ρ_grad(3)/μ₃ ≈ 7.1×`. A 1%
baseline change moves μ₃ by ≈7%. (`μ₃ = M(3)` needs neither M(4) nor a 3×3 solve, and is
**independent of the simplex basis** — the basis only distributes M(4) into μ₃/μ₄; the fragility lives
entirely in the baseline.)

## 2. Result (exact, mpmath 60 dps; q₀ muon-canonical from the jet witness)

Three legitimate deuteron-normalized (`ρ_grad(2)=1`) categorical A-scaling baselines:

| baseline | ρ_grad(3) | μ₃ | gap `c₃/μ₃` | amp `ρ_grad(3)/μ₃` |
|---|---|---|---|---|
| **G** graded coinvariant dim `∏[k]_q`, `[k]=1+q+…+q^{k-1}` (**CORPUS**, #4300) | 3.3420 | **0.4708** | 0.63× | 7.10 |
| **Q** balanced quantum dim `∏[k]_q^bal`, `[k]=q^{k-1}+…+q^{-(k-1)}` | 3.0437 | 0.7691 | 0.39× | 3.96 |
| **C** classical `∏k` (q→1) | 3.0 | 0.8128 | 0.37× | 3.69 |

- **μ₃ baseline-class spread = 1.73×** (0.4708 … 0.8128).
- **The 1.6× gap factor (corpus G) = 1.585×.** ⇒ **the spread of the target EXCEEDS the gap it targets.**
- **Signs robust:** μ₃ > 0 and μ₄ < 0 for all three baselines (μ₄ = −4.591, −2.554, −2.220) — consistent
  with the damping-wall sign-robustness. Only the **magnitudes** swing.
- ρ_strong isospin-correction knob (corrected 3.8128 vs raw B(³H)/B(²H)=3.814): **0.22% of μ₃** — negligible.

## 3. Verdict — scope-(a) CAVEAT (not a refutation)

The **SIGN** structure (μ₃>0, μ₄<0) is baseline-robust; the **MAGNITUDE** target μ₃ is **baseline-CLASS-
relative** — it swings by *more than* the gap the closure attempts aim to close. Hence the "1.6× A=3
magnitude gap" is **not an absolute target**: a reviewer referencing the quantum-dimension (Q) baseline
sees a ~2.6× gap, the classical (C) baseline a ~2.7× gap.

**This does NOT refute the principled graded-dimension route.** The corpus baseline (G) is the
*more-motivated* one — it literally IS the graded coinvariant dimension (the coinvariant-algebra
Poincaré series, #4300); (Q) is a quantum dimension and (C) the classical limit, **different**
categorical objects, not interchangeable definitions of one object. So this is not the `g₂` situation of
several equivalent-looking definitions of the *same* object. What it IS: the framework does not *force*
the subtracted "smooth part" to be the graded dimension rather than the quantum/classical dimension, and
because μ₃ is a small residual, that choice moves the target by ~1.7×.

**Consequence for the closure attempts:** state the baseline. A closure claim is "closes the gap to the
**graded-dimension-referenced** μ₃," not "closes the gap" simpliciter. The near-miss `0.63×` is only as
sharp as the (G) baseline is uniquely privileged — which is a *categorical-motivation* argument (the
coinvariant Poincaré series), not a numerical one.

## 4. Lean (sorry-free, lean-direct exit 0)

[`Mu3BaselineFragility.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/Mu3BaselineFragility.lean),
registered in the QOU umbrella:

| lemma | content |
|---|---|
| `mu3_eq_M3` | with μ₂=0, `μ₃ = M3 − 3·μ₂ = M3` — the simplex adds no robustness |
| `resid_shift` | `resid S (G+d) − resid S G = −d` — the residual moves by the full baseline shift |
| `residual_amplifies` | `0 < r < G → 1 < G/r` — relative amplification exceeds unity for a small residual |
| `corpus_amplification_gt_seven` | `ρ_grad(3)/μ₃ = 3.342031/0.4708 > 7` |
| `mu3_positive_all_baselines`, `mu4_negative_all_baselines` | sign robustness across G/Q/C |
| `spread_exceeds_gap` | `0.8128 > 1.585·0.4708` — the μ₃ spread exceeds the gap |
| `a3_target_fragile_but_sign_robust` | capstone |

## 5. Anti-fit / honesty ledger

- **0 free parameters.** ρ_strong / c₃ / AME / CODATA consumed **only** as fixed targets — never inverted
  into a canonical weight; no q, no baseline solved from the data.
- `μ₂ = 0` (deuteron self-reference) preserved by **every** baseline.
- Durable claim classified **scope-(a) caveat**, explicitly **not** a refutation of the graded-dimension
  route. Nothing wired.

| statement | status |
|---|---|
| μ₃ = M(3) exactly (μ₂=0); basis-independent | **Lean-proved sorry-free** |
| μ₃ baseline-class spread 1.73× > gap 1.585× | **verified (exact) + Lean `spread_exceeds_gap`** |
| signs μ₃>0, μ₄<0 baseline-robust | **verified (exact) + Lean** |
| the "1.6× A=3 magnitude gap" is baseline-class-relative | **scope-(a) caveat** |
| the graded-dimension (G) route | **not refuted** — the more-motivated baseline; A=3 closure stays open |

Refs: probe
[`mu3_target_frame_robustness_probe.py`](../../computations/deltalambda/mu3_target_frame_robustness_probe.py);
#4320 (simplex μ₃), #4364 (c₃=0.63μ₃), #4300 (graded dim), #4319 (g₂/r frame-artifact thread), the
[2026-07-26 three-walls audit](2026-07-26-deltalambda-a3-magnitude-source-three-walls.md).
