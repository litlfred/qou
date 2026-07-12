# Path to 1 ppq: the calibration floor, and α_EM as the headline opportunity

**Date:** 2026-07-11 · **Axis:** precision program (L1/L2) · **Tier:** strategic analysis.
**No c_k wired; no calibration change; scope-(a) throughout.**
**Probe:** [`onepq_frontier_ratio_classification_probe.py`](../../computations/onepq_frontier_ratio_classification_probe.py).

Grounds the "what to do to get to 1 ppq" question in the live dashboards and a
structural classification of the framework's observables.

## The decomposition (avoid the ambiguity)

- **L1 (compute ≤ 1 ppQ, 10⁻¹⁵):** already **met** (`onepb-status-dashboard`, 65 dps).
- **L2 (per-observable ≤ σ_exp/100):** **2/7** (`per-observable-100x-status`,
  `beats_100x_count = 2` — m_e, m_K/m_π). This is the frontier, and it is
  *100×-of-experiment* per observable, **not** 10⁻¹⁵ absolute.

## The structural fact that gates everything

**You cannot predict an observable more accurately than the calibration input it
rides on.** So observables split by whether the calibration cancels:

| class | example | floor | 1 ppq-capable? |
|---|---|---|---|
| **calibration-scaled** (rides a CAL scale) | absolute m_p, m_n, m_⁴He | CAL-2 exp. error **~780 ppb** | **No** — floor-limited |
| **pure-q₀ dimensionless** (calibration cancels) | m_K/m_π, α_EM, m_μ/m_e | q₀ precision **~0.06 ppb** | **Yes** |

Consequences:

1. **Absolute masses cannot reach 1 ppq** inside the 3-calibration framework —
   they are capped at the ~780 ppb CAL-2 floor. Going below needs a
   substrate-derivation of q₀ (Subgoal-2), owner-declined 2026-05-08 except the
   narrow **s5-so3 keystone** geometric `W_λ` build (PR #2503/#2524).
2. **Only dimensionless pure-q₀ observables can reach 1 ppq** — their floor is
   q₀'s own precision (~0.06 ppb), below the ~0.15 ppb-class experimental targets.
   m_K/m_π already does (the 2nd met). The lever for *more* 1-ppq observables is
   **more calibration-cancelling dimensionless predictions**, not absolute masses.

## The headline opportunity: α_EM (a derivation gap, not a wall)

**α_EM is a pure-q₀ dimensionless prediction. At the correct (proton) anchor, with
the derived Schwinger `(1−h²α)` term, it lands at `+0.313 ppb = ~2× σ_α` — the
*closest any not-yet-met observable sits to its 1-ppq target* — and the remaining
gap is derivation-incompleteness, not a calibration floor.**

> **Corrected (2026-07-12, #3625).** An earlier version of this table reported the
> residual as `~80 ppb (527× σ)`. That was the **muon anchor + quadratic form** —
> an understatement. The honest best number, at the proton anchor (which α_EM
> independently prefers to 0.245 ppb) with the RT-phase-3-*derived* Schwinger term,
> is **+0.313 ppb ≈ 2× σ_α**. See `alpha_em_schwinger_ladder_probe.py` +
> `alpha_em_anchor_preference_probe.py` (#3625).

| quantity | value |
|---|---|
| CODATA α⁻¹ | 137.035999084 |
| best α⁻¹ (proton pin + derived Schwinger) | 137.035999127 |
| **residual** | **+0.313 ppb** |
| experimental σ_α | 0.15 ppb |
| **miss factor** | **~2.1×** |
| (muon anchor + quadratic form, for reference) | +80 ppb (537×) |
| calibration floor (via q₀) | ~0.06 ppb — **below** σ_α ⇒ 1 ppq-capable |
| remaining 2-loop c₂ = resid/α² | ≈ 8.1e-4 (uncomputed; ≠ Ohtsuki κ₁) |

Because α_EM's floor (q₀ at ~0.06 ppb) sits *below* its experimental σ (0.15 ppb),
the residual is a **missing-higher-order-terms** problem (the Rogers–Turaev /
Schwinger / Bring-measure program, `alpha_em_rt_phase2/3/4`) — **a derivation gap,
not a calibration wall**, unlike absolute masses. Closing α_EM to ≤ 0.15 ppb would
be a **structural derivation of the fine-structure constant** — the single
highest-*value* 1-ppq target, one the mass-focused L2 dashboard does not track,
already at **2× σ** with the derived terms.

### Follow-up caveats (form-ladder probe — corrects the optimism above)

A standalone reconstruction of the form
([`alpha_em_form_ladder_probe.py`](../../computations/alpha_em_form_ladder_probe.py);
the committed `alpha_em_4pi_fixed_point_solve.py` has a stale `_precision` import
post-miga) shows the "closable" framing must be qualified by **three honest
caveats**:

- **The integers are NOT free fits** (fair to the framework): `g=4` is Bring's
  genus; `[9]`, `[10]` are the crossing numbers of the two genus-4 torus knots
  `T_{2,9}`, `T_{3,5}` (`prop:force-carrier-bring-uniqueness`); the zero-mode
  `2g/(4π(g−1)) = dim H¹/Area = 2/(3π)`. So `q·[9]_q·[10]_q + 2/(3π)` is
  structurally motivated, not tuned.
- **(A) It is CONJECTURAL.** The form is conditional on *three* unproved Lean
  classes (`ArchimedeanLimit`, `BlochSuslinUniqueness`, `BringZeroModeBlochClass`).
  Conditional-class ≠ established (anti-laundering rule) — it is not a proved
  derivation.
- **(B) It is ANCHOR-DEPENDENT — and α_EM picks the proton anchor.** The residual
  differs by the μ–p tension: at the proton pin `+0.313 ppb` (with Schwinger), at
  the muon pin `+80 ppb`. This is not a free choice — inverting the pure-q₀ form for
  the CODATA-exact q₀ gives `q_α` **0.245 ppb from the proton pin vs 11.78 ppb from
  the muon pin** (`alpha_em_anchor_preference_probe.py`, #3625). So α_EM *itself*
  selects the proton anchor (a third EM-sector cross-check, with m_p).
- **(C) At the correct anchor it is close, not far.** Ladder at the proton pin:
  tree `−4259 ppb` → `+zero-mode` `−21 ppb` → `+O(α)` `−21 ppb` → quadratic
  fixed-point `+1.7 ppb` → **`+`derived Schwinger `(1−h²α)` → `+0.313 ppb ≈ 2× σ_α`**
  (`alpha_em_schwinger_ladder_probe.py`, #3625). The remaining `c₂ ≈ 8.1e-4` is a
  small **uncomputed** 2-loop coefficient (RT phase-2), *not* Ohtsuki `κ₁ ≈ 0.554`.

**Revised status:** α_EM is the highest-*value* 1-ppq target, *is* a derivation gap
(not a calibration wall), and — at the correct anchor with the derived terms — is
already at **~2× σ_α**, the closest not-yet-met observable to 1 ppq. The *value*
(zero-mode, proved genus-determined, #3625) and *anchor* (proton) are settled; what
remains is the small uncomputed 2-loop `c₂` plus the still-conjectural physical
coupling claim + upstream classes. The earlier "~80 ppb / long-horizon" framing
conflated the muon anchor + quadratic form with the true best; corrected here.

## The two active levers, ranked

1. **Q_β / m_n / Δ_pn trio (near-term, 3-for-1).** Shared root = the Q_β c₃ bar-odd
   `S`. Closing it takes 2/7 → 5/7. Live carrier = `Φ_b` (siblings #3544/#3596).
   **This session proved the geometry-side (`4₁`) is magnitude-negative (~2350×
   short) — so `Φ_b` is the only route**, with a concrete target (O(10⁻²),
   off-real-axis, near-singular; #3573).
2. **α_EM (fundamental, 1-for-∞).** Already at **+0.313 ppb ≈ 2× σ_α** (proton pin
   + derived Schwinger) → 0.15 ppb. A *derivation* gap, not a calibration wall, with
   structurally-derived integers, a proved genus-determined zero-mode value, and a
   settled (proton) anchor. What remains is a **small uncomputed 2-loop `c₂`** plus
   the still-conjectural coupling claim + upstream classes. Highest scientific value;
   the closest not-yet-met observable to 1 ppq.

Absolute m_p / m_n / m_μ are **not** near-term 1-ppq targets: m_p/m_n are
CAL-2-floor-limited (Subgoal-2, needs s5-so3); m_μ is the μ–p calibration
convention (owner-gated, bean `tnjb`), exact-by-construction at the muon anchor.

## Φ_b redirect (why the canonical scan failed — ties to #3573)

The existing `Φ_b` argument scan
([`qbeta_c3_phib_argument_scan`](../../computations/qbeta/qbeta_c3_phib_argument_scan.py))
found **no zero-parameter candidate under 1e-4 among 60 substrate-canonical
readouts** (best err 1.0), noting "complex-argument space mostly unexplored."
**#3573's branch-selector result explains why:** substrate-*canonical* readouts sit
on/near the real axis, i.e. the **golden (`z²−z−1`, real, no-CS) branch**; the CS =
bar-odd `S` lives only on the **off-real-axis complex arguments** (the cusp
`z²−z+1` branch). So the scan's "unexplored complex-argument space" is *exactly*
where the phase-selected cusp branch lives — the productive next scan is the
off-real-axis `c_b`-lattice, not more canonical readouts.

## Bottom line

- **Reachable now:** 5/7 via `Φ_b` (the c₃ trio).
- **Highest value & closest:** α_EM — the real 1-ppq prize (untracked by the L2
  dashboard) and **already at ~2× σ_α** (proton pin + derived Schwinger, #3625);
  value proved genus-determined, anchor settled. What remains is a small uncomputed
  2-loop `c₂` + the conjectural coupling claim + upstream classes.
- **Walled off:** absolute-mass 1 ppq (calibration floor; needs s5-so3 / owner
  reversal).

## Cross-references
- L2 dashboard: `computations/per-observable-100x-status.witness.json`.
- α_EM: `computations/alpha-em-4pi-fixed-point-solve.witness.json`, `alpha_em_rt_phase*`.
- Branch selector: [`2026-07-11-qbeta-c3-pole-cusp-phase-tractability.md`](2026-07-11-qbeta-c3-pole-cusp-phase-tractability.md) (#3573).
- AGENTS.md §Precision goals; §"q₀ anchor convention"; [`docs/precision-goals.md`](../precision-goals.md).
