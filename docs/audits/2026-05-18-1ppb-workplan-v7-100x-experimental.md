# 1ppb workplan v7 — 100× experimental precision per observable

**Date:** 2026-05-18
**Branch:** `claude/track-a-b-per-isotope-and-rho-xi`
**Author:** Claude (reassessment after user direction "1 ppb compute AND 100× more precise than experimental error")
**Supersedes:** v6 (`2026-05-18-1ppb-workplan-v6-refreshed.md`)

## 1. Goal restatement (TRUE GOAL)

Per user direction this session:

> we need to work on 1ppb compute at least (depending on _precision,
> but 1ppb is default) AND 100 factors more precise than expiremental
> error (mass, Q scale, beta, etc.)

This is **two** distinct precision targets composed:

| Target | Definition | Current state |
|--------|-----------|----------------|
| **Compute precision** | internal cross-method agreement on `|tr_M|`, χ^λ, y_λ at substrate q_0 | **trivially met** — `_precision.py` default is 50 dps compute / 40 dps output (10⁻⁴⁰ relative); Layer 2 dashboard at 0.0 max_rel_delta |
| **Per-observable precision** | for each predicted observable O with experimental uncertainty σ_O, achieve `σ_pred(O) ≤ σ_O / 100` | **partial — 1 of 6 observables beat target** (only m_e by anchor definition); all others miss including Q_β (research-grade; CAL-3 σ ~0.78 ppm, not the 640 ppm AME draft figure) |

## 2. 100× experimental targets (CODATA 2022)

| Observable | value | σ_exp (MeV) | σ_rel | 100× target | Reachable from current anchors? |
|---|---:|---:|---:|---:|---|
| **Q_β (β-decay endpoint)** | 0.78233341 MeV | 6.1×10⁻⁷ | 0.78 ppm (= 779.7 ppb) | **7.8 ppb** | No — below CAL-2 floor (CAL-3 σ is sharper than expected) |
| m_e | 0.51100 MeV | 1.5×10⁻¹⁰ | 0.29 ppb | 2.9 ppt | No — *is* CAL-1 anchor |
| q_0 (substrate) | 1.10974 | 8×10⁻¹¹ | 0.07 ppb | 0.7 ppt | No — *is* CAL-2 anchor |
| m_p | 938.272 MeV | 2.9×10⁻⁷ | 0.31 ppb | 3.1 ppt | No — below 780 ppb CAL-2 floor |
| m_n | 939.566 MeV | 5.4×10⁻⁷ | 0.57 ppb | 5.7 ppt | No — below CAL-2 floor |
| m_D | 1875.6 MeV | 5.7×10⁻⁷ | 0.30 ppb | 3.0 ppt | No — below CAL-2 floor |
| m_T | 2808.9 MeV | 8.5×10⁻⁷ | 0.30 ppb | 3.0 ppt | No — below CAL-2 floor |
| m_³He | 2808.4 MeV | 8.5×10⁻⁷ | 0.30 ppb | 3.0 ppt | No — below CAL-2 floor |
| m_⁴He | 3727.4 MeV | 1.1×10⁻⁶ | 0.30 ppb | 3.0 ppt | No — below CAL-2 floor |

> **CAL-3 σ correction (2026-05-18 Copilot review on #777).** The Q_β
> uncertainty is the PDG 2024 / CAL-3 witness value 6.1×10⁻⁷ MeV
> (≈0.78 ppm, 779.7 ppb relative), NOT the earlier draft figure of
> 5×10⁻⁴ MeV (640 ppm). Source: `cal-3-q-beta.witness.json`. This
> moves Q_β from "trivially achievable Subgoal-1 target" to
> "research-grade Subgoal-2 target" — its 100× target (7.8 ppb) is
> **below** the CAL-2 floor.

### Binding-energy observables (typically less anchor-amplified)

For binding energies `B(Z,N) = Z·m_p + N·m_n + Z·m_e - M(Z,N)`, the
experimental σ_B is dominated by the *mass-table* uncertainty
(~10⁻⁶ for light nuclei), giving σ_rel(B) of order 1–100 ppm.
**100× targets here are in the 10–1000 ppb range — within reach
post-Borromean-tower.**

| Atom | B_AME (MeV) | σ_B (MeV) | σ_rel(B) | 100× target |
|---|---:|---:|---:|---:|
| D | 2.224 | ~10⁻⁶ | 0.45 ppm | 4.5 ppb |
| T | 8.482 | ~10⁻⁶ | 0.12 ppm | 1.2 ppb |
| ³He | 7.718 | ~10⁻⁶ | 0.13 ppm | 1.3 ppb |
| ⁴He | 28.296 | ~10⁻⁶ | 0.035 ppm | 0.35 ppb |

## 3. Two subgoals

### Subgoal-1: **Achievable** (target ≥ CAL-2 floor)

Predictions where 100× experimental is *above* the ~780 ppb CAL-2 floor:

- **Mass differences** (Δm_pn = m_n − m_p) — σ_exp_rel ≈ 474 ppb
  (combined from m_p, m_n CODATA uncertainties), so 100× target =
  4.74 ppb. Current Borromean prediction at 254 ppb misses by 54× —
  closure path is λ_scale substrate-derivation, landed on main via
  PR #751 (commit `894c3db97`, 2026-05-18):
  [`probe_workplan_0b_route_b_operator.py`](../../computations/probe_workplan_0b_route_b_operator.py),
  [`probe_c2_inflection_structure.py`](../../computations/probe_c2_inflection_structure.py),
  [`2026-05-18-workplan-0b-routes-b-c-findings.md`](2026-05-18-workplan-0b-routes-b-c-findings.md).
- **Binding energies for light atoms** (target 0.35–4.5 ppb) — gated by
  per-isotope Borromean-tower extension (Track A) and operator-valued
  branching at A≥3 (Track B). All currently `delta_lambda_unavailable`.

### Subgoal-2: **Research-grade** (target < CAL-2 floor)

Predictions where 100× experimental is *below* the 780 ppb floor:

- **Q_β (CAL-3 anchor)** — σ_exp ≈ 0.78 ppm (PDG 2024), so 100× target
  ≈ 7.8 ppb. The original v7 draft used the coarser AME quote
  (640 ppm) which would have made Q_β a trivially-achievable
  Subgoal-1 target; the PDG-grade σ shifts it into Subgoal-2.
  Current single-wrap symbolic prediction error 1.68 ppm → misses by
  ~215 000×. Closure path requires either the brane-tower full-sum
  (Workplan 2 Phase 2 m_e_Hecke lift) OR substrate-q_0 derivation.
- **Absolute m_p, m_n, m_D, m_T, m_³He, m_⁴He** — need σ_pred ~3 ppt.
  **Requires substrate-derivation of q_0** (currently declined per
  ledger 2026-05-08 explicit decision).
- Alternative: identify a *calibration-independent* formula path
  whose q_0 dependence cancels — speculative.

Subgoal-2 is **explicitly out of scope** for this branch.

## 4. What the Layer-1/2/3 dashboard actually measures

The `onepb-status-dashboard.witness.json` reports:

```
Layer 1 (LP-dual / GB NF):       6/6 compounds, gap=0
Layer 2 (Markov-trace):          8 atoms, max_rel_delta = 0.0
Layer 3 (Structural):            92.79 ppb max non-anchor Δ
```

These measure **compute consistency** — different methods agreeing on
the same quantity at substrate q_0. Layer 2's 0.0 is the cross-method
identity (Hoefsmit ≡ markov_peel ≡ chi-cache ≡ canonical-Rust ≡ Wenzl-bridge).

The 92.79 ppb in Layer 3 is the *AME publication rounding floor* —
the experimental data is rounded to fewer digits than the prediction can deliver.

**The mass-table sweep error (6.80% mean) is NOT measured by these layers** because
it's an **absolute-prediction** error, not a cross-method identity. It depends on:

1. Per-isotope mass-formula extension to A>1 (Borromean tower — Track A)
2. χ^λ at H_n ≥ 15 for ⁶Li, ⁷Li, ⁹Be (Track B + Geck-Pfeiffer #710)
3. Layer 3 hybrid α-cluster + valence (Track C — out of scope this branch)

## 5. Track A + Track B (this branch's scope)

> **Track A is gated on Δ_λ closure** — see
> [`2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md)
> for full context. The non-tautological binding formula
> `B(K) = m_e · Σ_λ y_λ χ^λ Δ_λ` requires per-block Δ_λ(K) values, and
> six closure ansätze (Frobenius co-Casimir, Demazure-fibre,
> LP-Plancherel, LP-Frobenius, crystal-graph, augmented Markov) have all
> failed on the deuteron. Until Δ_λ has a categorical derivation, Track A
> can only document the gap; it cannot close per-isotope binding-energy
> predictions to 100× experimental.
>
> **Track B is independent of Δ_λ** — operator-valued Wenzl branching is
> pure χ^λ machinery. **Track B is the in-scope work for this branch.**

### Track A — per-isotope mass-formula extension to A ∈ {2, 3, 4}

Borromean tower formula (commit `dc3a85500`) closes m_p scale gap to
0.25 ppm at the anchor. Now extend the formula systematically to
{D, T, ³He, ⁴He} using:

- Canonical |tr_M(β_atom, q_0)| from chi-cache witness (already
  computed at 50 dps for these 6 atoms):
  - p:    1.0653062286
  - n:    0.9232332972
  - D:    0.3882864715
  - T:    0.1040521187
  - ³He:  0.2065408586
  - ⁴He:  0.0538560306
- ρ_K^full consumer (PR #678 merged)
- Borromean tower per-A correction `B_3(Z,N)` derived from braid
  closure topology

**Deliverable**: per-atom binding-energy prediction witness with
σ_pred ≤ 100× experimental σ for each A ∈ {2,3,4} target binding
(B_D, B_T, B_³He, B_⁴He).

### Track B — recursive ρ_ξ in operator-valued Wenzl branching combiner

Currently A=2 verified at 7×10⁻¹⁵; A≥3 needs recursive ρ_ξ(β_inner)
at H_{3(A−1)} via inner branching (~100 lines + tests).

**Deliverable**: combiner produces |tr_M| at A=3 matching markov_peel
reference at 1e-15; A=4 sub-second (vs 22 min markov_peel).

### Synergy

Track B's A=4 sub-second combiner directly feeds Track A's ⁴He binding-
energy prediction, removing the 22-minute compute bottleneck.

## 6. Concrete next-action queue

1. **Δm_pn 100× closure (Subgoal-1)** — λ_scale substrate-derivation
   landed on main via PR #751 (Workplan-0b/M_N Routes A/B/C). Next
   step is to wire the C2-inflection / Route-B / Route-C probes into
   the m_p / m_n Borromean prediction so the 254 ppb residual moves
   toward the 4.74 ppb target. Tracked separately from this branch;
   highest-leverage Subgoal-1 task post-#777.
2. **Δ_λ closure (Track A unblock)** — independent of every other
   item; see [Δ_λ gating context](2026-05-18-delta-lambda-gating-context.md).
   Without Δ_λ, light-atom binding-energy predictions (D / T / ³He / ⁴He
   targets 0.35–4.5 ppb) remain undefined.
3. **Track B recursive ρ_ξ infrastructure** — gated on H_9+ extract
   regeneration; see [ρ_ξ blocker audit](2026-05-18-recursive-rho-xi-blocked-by-underdetermined-extracts.md).
   Track B is NOT on the immediate 1ppb critical path until the
   H_9 extracts get the test-word coverage needed to make them
   universal.
4. **Update onepb-status-dashboard** to report per-observable
   100×-experimental status alongside cross-method identity (in
   progress via `per_observable_100x_status.py`).

## 7. Updates from v6

- v6 framed 1 ppb as the headline target. v7 reframes:
  **1 ppb compute is trivially met** (50 dps default); the **binding
  constraint is per-observable 100×-experimental**, which is *variable*
  per observable.
- v6 did not separate compute consistency from absolute-prediction
  error. v7 makes this explicit.
- v6's "CAL-2 hard floor unfixable" stands — confirmed as the binding
  constraint for absolute mass predictions; logged as Subgoal-2
  (research-grade, out of scope).
- Q_β prediction target was originally drafted as 6391 ppb based on
  the AME coarse Q-value (640 ppm). Per Copilot review on #777, the
  canonical CAL-3 σ is 0.78 ppm (PDG 2024) → 100× target = 7.8 ppb,
  placing Q_β in Subgoal-2 (research-grade), not Subgoal-1.
- The mass-table sweep at 6.80% absolute is **not** a precision failure;
  it is a **structural completeness** failure of the per-isotope formula.
  Tracks A+B address this directly.

## 8. Branch deliverable summary

By end of this branch:

- [ ] Track A: per-isotope binding-energy predictions for D, T, ³He, ⁴He
      with 100× experimental verification
- [ ] Track B: recursive ρ_ξ in branching combiner; A=3,4 sub-second
- [ ] Updated `onepb-status-dashboard.witness.json` to report per-observable
      status against 100× target table
- [ ] v7 workplan document (this file) + ledger entry

## 9. Open questions

- Should Q_β be predicted (rather than calibrated) to demonstrate the
  Subgoal-1 achievement? If yes, that's a structural extension (the
  ledger has it declined; reverting requires user authorization).
- For atoms below the CAL-2 floor (m_p, m_⁴He absolute), document
  the floor explicitly per-observable in the dashboard rather than as
  a global ~780 ppb summary.
