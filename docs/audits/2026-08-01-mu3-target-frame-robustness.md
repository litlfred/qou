# The μ₃ (A=3 magnitude) target is baseline-class-relative — the "1.6× gap" is smaller than the target's own convention-spread

**Date:** 2026-08-01 · **Branch:** `claude/mu3-target-frame-robustness-2026-08-01` · **PR:** #4491 ·
**Axis:** Δ_λ / A=3 magnitude gate · **Tier:** scope-(a) frame-robustness measurement (exact mpmath +
Lean-proved amplification/sign facts; **no fit**; nothing wired).

## 0. ⚠ UNITS + SCALE (read first) — the "1.6× near-miss" is dimensionally ill-posed and scale-ambiguous

The headline "1.6× A=3 near-miss" (`c₃ = 0.63·μ₃`, #4364 / three-walls) — and the gap-factor / physical-%
numbers in §2–3c below, which followed it — **compare a MeV energy to a dimensionless ratio.**
`c₃ = 0.297` is a genuine **energy** (`E₀·(1−τ_Borr)`, `E₀ = m_e/(q₀(q₀−1)) ≈ 4.19 MeV`);
`μ₃ = 0.4708` is **dimensionless** (`ρ_strong(3) − ρ_grad(3)`). `borromean_h9_magnitude_lift_probe.py:188`
admits the pun: *"target μ₃ = 0.4708 (dimensionless, read as MeV)."*

**But repairing the pun does not give a single "honest gap"** — the categorical binding **scale is
unpinned.** The master formula `B = m_e·|Σ y_λ χ^λ sgn f^λ|` predicts the **deuteron itself** at only
`B_cat(²H) = 0.380 MeV` vs AME `2.2246` — a −82.9% undershoot, `C_knot = B_AME/B_cat = 5.85`, an
**explicitly FITTED (not derived) deficit ratio = the open Δ_λ gate**
(`binding_energy_categorical_deuteron.py`). So there are two defensible normalizations of `c₃`, differing
by exactly `C_knot`:

| normalization | `c₃` in ratio units | gap vs `μ₃` | sign |
|---|---|---|---|
| **A** ÷ AME deuteron `c₃/B_AME` | 0.1335 | **3.53×** | undershoot |
| **B** ÷ categorical deuteron `c₃/B_cat` (E₀/m_e cancels — scale-consistent) | 0.781 | **1.66×** | **overshoot** |

The gap swings from a **1.66× overshoot to a 3.53× undershoot** across the whole `C_knot = 5.85`. **The
"1.6× near-miss" is therefore not a robust proximity — it is an artifact of the unpinned scale.** The one
unambiguous object is `C_knot` itself: the 5.85× deuteron deficit, explicitly fitted = the open Δ_λ gate.
Neither normalization is rigorous (c₃ is a Borromean `E₀·deficit`; `B_cat` is the master per-λ sum —
different computations), which is itself the point: until the scale is pinned (C_knot **derived**), the
A=3 gap has no robust value.

> **Self-correction.** An earlier revision of this section (and of `a3_units_consistency_probe.py` /
> `A3UnitsConsistency.lean`) asserted "the honest gap is 3.53×" by picking normalization A alone. That
> **over-claimed** — it silently chose one of the two scales. Corrected here to the scale-ambiguity.

The **relative** findings of §2–3c (baseline spread 1.73×, amplification, order-separation *ranking*)
are **unaffected** — they are ratios within one convention. The absolute gap-factor and physical-%
figures in §2–3c inherit the pun **and** the scale-ambiguity; read them as *normalization-A* numbers, not
as robust gaps. The corpus files (#4364, three-walls, borromean probe:188) carry the pun — flagged for
coordination. Probe
[`a3_units_consistency_probe.py`](../../computations/deltalambda/a3_units_consistency_probe.py);
Lean [`A3UnitsConsistency.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/A3UnitsConsistency.lean).

## 0a. The question no sibling was asking

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

## 3a. The frame-independent statement — a 4.6% miss on the physical ratio, amplified 8× by the residual framing

The only baseline-independent object is the **physical ratio** `ρ_strong(3) = B(³H)/B(²H) = 3.8128`
(data). The corpus model's total A=3 prediction is `ρ_grad_G(3) + c₃` (graded baseline + the derived
3-body cluster; `C(3,3)=1`, so the cluster enters `M(3)` directly):

    model = ρ_grad_G(3) + c₃ = 3.3420 + 0.297 = 3.6390   vs   ρ_strong(3) = 3.8128
    absolute miss Δ = 0.1738 (ratio units).

That **one** miss Δ has two framings:

| framing | denominator | value |
|---|---|---|
| **physical** (frame-independent) | full ratio `ρ_strong(3) = 3.8128` | **4.56% miss** on `B(³H)/B(²H)` |
| **residual** (the "1.6× gap") | small residual `μ₃ = 0.4708` | 36.9% short ⇒ model reaches `0.63·μ₃` |

The residual framing **amplifies the same Δ by `ρ_strong(3)/μ₃ ≈ 8.1×`**. So the alarming "1.6× A=3
magnitude gap" is, physically, a **4.6% shortfall on `B(³H)/B(²H)`** — the multiplicative-gap number is
a presentation artifact of dividing by the small residual instead of the physical observable. This is
the honest, baseline-independent accuracy statement of the A=3 magnitude: **the categorical model gets
the tritium/deuteron binding ratio right to ~4.6%.** (Note the 4.6% is the *corpus-G* model's accuracy —
a different baseline is a different model with a different total; it is the residual *decomposition*, not
the physical accuracy, that §2–3 shows is convention-relative.)

**Information budget (why every categorical factor near-misses).** By `framing_amplification`, closing
the "1.6× gap" to relative precision `ε` on `μ₃` requires predicting the physical ratio `B(³H)/B(²H)` to
`ε · (μ₃/ρ_strong(3)) = ε · 12.35%`: a **10% closure needs `~1.2%` physical accuracy**, tighter than the
model's current ~4.6% A=3 accuracy. So a candidate factor that reproduces the physical ratio to a few
percent is *automatically* a large multiplicative miss on the small residual — which is exactly the
pattern of the three walled routes (0.63×, 33×, sign-swap). This is the **direct analog of the g₂
"36 ppm" information-starvation** (`BindingResidualAmplification`, #4319): the residual is not a
special-function puzzle separable from the binding; hitting it to a clean multiplicative factor is
equivalent to predicting the binding ratio to sub-percent, which the framework's first-order machinery
does not reach.

## 3b. How to improve A=3 precision — order-separation of the "compute higher orders" route

Localizing the 4.56% miss on `B(³H)/B(²H)`: the dominant term `ρ_grad_G(3) = [3]_q` is **exact**
(87.6% of the ratio); the derived leading (h⁴) cluster `c₃ = 0.297` is 7.8%; **all the error lives in
the subleading many-body cluster.** Can it be closed by higher cluster orders (h⁶, h⁸, …)?

Write the 3-body cluster as `c₃·(1 + a₁h² + a₂h⁴ + …)`, `h = q−q⁻¹` (`h² ≈ 0.0437` at `q₀`):

| test | value | reading |
|---|---|---|
| required h⁶ coefficient `a₁ = Δ/(c₃·h²)` | **≈ 13.4** | 13× the O(1) natural size — a fit red-flag |
| full bounded (`|aₖ| ≤ 2`) tail `c₃·2·h²/(1−h²)` | ≈ 0.027 (**0.7%** of ratio) | ≪ the 4.56% miss |

**So the routine higher-cluster-order route is order-separated out** (`bounded_tail_lt_miss`,
`required_coeff_gt_thirteen`): a bounded expansion supplies at most ~0.7%. Closing the miss needs
**either** a **new leading-order (h⁴) 3-body channel** of size `~0.585·c₃`, **or** an anomalous ~13×
coefficient — which would itself be a fit red-flag (cf. the Q_β `c₃` `1/u³` hypersensitivity,
[2026-07-12](2026-07-12-c3-hypersensitivity-is-ladder-1-over-u3.md)).

**Precision strategy (honest answer to "how do we improve precision?"):**

1. **A=3 ratio precision is Δ_λ-gated, not q₀-limited.** The overall scale cancels in `B(³H)/B(²H)`, so
   this is a categorical (Δ_λ) question — a missing *per-partition leading-order magnitude* — not a
   substrate-pin / CAL-2-floor question. It sits under **Subgoal-2** (research-grade, open-for-all since
   2026-07-11), gated only by the Δ_λ closure.
2. **Not "compute more orders."** The higher-order route is pruned (§3b); a finer cluster expansion buys
   ≤ 0.7%.
3. **Report on the frame-independent ratio.** The honest metric is **~4.6% on `B(³H)/B(²H)`**, not the
   "1.6× gap" on the residual μ₃ (which amplifies ~8× and is baseline-class-relative, §2–3a). Reporting
   the multiplicative-residual gap overstates the problem and misdirects effort toward chasing a
   convention-relative small number to high multiplicative precision.
4. **The probed 0-fit leading-channel candidates don't supply it** (weight `y_λ`/`W_λ`, cable width,
   brane level — the three walls, [2026-07-26](2026-07-26-deltalambda-a3-magnitude-source-three-walls.md)).
   The open task is a *derived* leading-order channel of size `~0.585·c₃` — squarely the Δ_λ gate.

## 3c. A=4 (⁴He) — the mirror regime, sharper (order-separation extended)

Applying the same lens to A=4 (`ρ_strong(4) = B(⁴He)/B(²H) = 13.0316`):

| | A=3 (³H) | A=4 (⁴He) |
|---|---|---|
| graded baseline vs physical ratio | **under**shoots −4.6% | **over**shoots **+20.8%** |
| add derived 3-body clusters | closes toward it | makes it **worse** (+29.9%) |
| missing leading channel | +0.17 (3-body binding) | **−3.90 (4-body α saturation)**, −24.75% of baseline |
| \|missing\|/c₃ | 0.58× | **13.1×** |
| higher-3-body-order tail vs miss | 0.027 ≪ 0.17 | 0.109 ≪ 3.90 (**order-separated**) |
| μ_k baseline-class fragility | 1.73× | **2.07×** |

**Two facts beyond three-walls Route 3** (which established the μ₄<0 sign-swap):

1. **Frame-independent magnitude localizes the accuracy loss.** The A=4 discrepancy (the missing 4-body
   channel) is −24.75% of the baseline — **~5× the A=3 discrepancy**. The framework's binding accuracy
   degrades in the **saturation regime (A≥4)**: the missing piece is the large, negative 4-body
   α-cluster term.
2. **A=3 and A=4 are opposite-sign regimes needing DISTINCT leading channels** — a small *positive*
   3-body (binding) at A=3, a large *negative* 4-body (saturation) at A=4. The order-separation rules
   out one-mechanism-plus-refinement: each isotope's leading channel is its own Δ_λ object. This is the
   `μ₃(binding)/μ₄(saturation)` split, now quantified in physical-ratio terms.

Lean [`A4PrecisionOrderSeparation.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/A4PrecisionOrderSeparation.lean)
(sorry-free): `a4_baseline_overshoots`, `a4_three_body_makes_worse`, `a4_required_channel_negative`,
`a4_higher_order_ruled_out`, `a4_four_body_dominates`, `mu4_more_fragile_than_mu3`, capstone. Probe
[`a4_precision_order_decomposition_probe.py`](../../computations/deltalambda/a4_precision_order_decomposition_probe.py).

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
| `framing_amplification` | `(Δ/μ)/(Δ/ρ) = ρ/μ` — the residual framing amplifies the physical miss by ρ/μ |
| `a3_target_fragile_but_sign_robust` | capstone (fragility) |

[`A3PrecisionOrderSeparation.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/A3PrecisionOrderSeparation.lean) (§3b, precision route-pruning):

| lemma | content |
|---|---|
| `bounded_order_term_le` | `|a| ≤ B → |a·c·h²| ≤ B·c·h²` — bounded coefficient ⇒ bounded per-order contribution |
| `bounded_tail_lt_miss` | `c₃·2·h²/(1−h²) < Δ` — full bounded tail closes ≤0.7%, ≪ the miss |
| `required_coeff_gt_thirteen` | `Δ/(c₃·h²) > 13` — a higher-order closure needs an anomalous coefficient |
| `graded_baseline_dominates` | `ρ_grad_G(3)/ρ_strong(3) > 0.87` |
| `a3_precision_needs_leading_channel` | capstone (precision Δ_λ-gated, not higher-order) |

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
