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

**α_EM is a pure-q₀ dimensionless prediction, currently ~80 ppb off, and the gap
is derivation-incompleteness — not a calibration floor.**

| quantity | value |
|---|---|
| predicted α⁻¹ (`alpha_em_4pi_fixed_point_solve`) | 137.036010… |
| CODATA α⁻¹ | 137.035999084 |
| residual | **~80 ppb** |
| experimental σ_α | 0.15 ppb |
| miss factor | **~527×** |
| calibration floor (via q₀) | ~0.06 ppb — **below** σ_α ⇒ 1 ppq-capable |

Because α_EM's floor (q₀ at ~0.06 ppb) sits *below* its experimental σ (0.15 ppb),
the 80 ppb residual is a **missing-higher-order-terms** problem (the Rogers–Turaev
/ Schwinger / Bring-measure program, `alpha_em_rt_phase2/3/4`), **closable in
principle** — unlike absolute masses, which hit a hard calibration wall. Closing
α_EM to ≤ 0.15 ppb would be a **structural derivation of the fine-structure
constant** — arguably the single highest-value 1-ppq target in the framework, and
one the mass-focused L2 dashboard does not even track.

## The two active levers, ranked

1. **Q_β / m_n / Δ_pn trio (near-term, 3-for-1).** Shared root = the Q_β c₃ bar-odd
   `S`. Closing it takes 2/7 → 5/7. Live carrier = `Φ_b` (siblings #3544/#3596).
   **This session proved the geometry-side (`4₁`) is magnitude-negative (~2350×
   short) — so `Φ_b` is the only route**, with a concrete target (O(10⁻²),
   off-real-axis, near-singular; #3573).
2. **α_EM (fundamental, 1-for-∞).** ~80 ppb → 0.15 ppb via the RT derivation
   program. A *derivation* gap, not a calibration wall. Highest scientific value.

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
- **Highest value:** α_EM to 0.15 ppb (a closable derivation gap — the real 1-ppq
  prize, currently untracked by the L2 dashboard).
- **Walled off:** absolute-mass 1 ppq (calibration floor; needs s5-so3 / owner
  reversal).

## Cross-references
- L2 dashboard: `computations/per-observable-100x-status.witness.json`.
- α_EM: `computations/alpha-em-4pi-fixed-point-solve.witness.json`, `alpha_em_rt_phase*`.
- Branch selector: [`2026-07-11-qbeta-c3-pole-cusp-phase-tractability.md`](2026-07-11-qbeta-c3-pole-cusp-phase-tractability.md) (#3573).
- AGENTS.md §Precision goals; §"q₀ anchor convention"; [`docs/precision-goals.md`](../precision-goals.md).
