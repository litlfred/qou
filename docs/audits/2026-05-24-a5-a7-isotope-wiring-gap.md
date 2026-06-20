# A ∈ {5, 6, 7} isotope wiring gap — ⁵Li, ⁶Li, ⁷Li have no atom→knot rule

**Date:** 2026-05-24
**Branch:** `claude/great-galileo-ahGfj`
**PR:** [#1089](https://github.com/litlfred/qou/pull/1089)
**Parent audit:** [`2026-05-24-low-isotope-mass-error-anatomy.md`](2026-05-24-low-isotope-mass-error-anatomy.md)
**Status:** Gap surfaced + candidate paths identified. **Owner decision needed** before any wiring (Rule 14 escalation candidate).

## The gap

[`mass_table_ppb.py`](../../computations/mass_table_ppb.py) covers atoms via two rules:

1. **Kashaev volume law** for `A ≤ 4` (D, T, ³He, ⁴He) — atom → census-assigned hyperbolic knot/link, `B_pred = ρ_F · m_e · Vol(K)`
2. **α-cluster rule** for `A ≥ 8` (⁸Be, ¹²C, ¹⁶O, ²⁰Ne, ²⁴Mg, ⁴⁰Ca) — `B_pred = n_α · B(⁴He_derived) + n_pairs · c_αα`

The intermediate range `A ∈ {5, 6, 7}` is **not covered**:

| Atom | (Z, N, A) | B_AME (MeV) | Stability | Status |
|------|-----------|-------------|-----------|--------|
| ⁵Li  | (3, 2, 5) | 26.328      | unbound (resonance, lifetime ~10⁻²² s) | no rule |
| ⁶Li  | (3, 3, 6) | 31.99405    | stable    | no rule |
| ⁷Li  | (3, 4, 7) | 39.24453    | stable    | no rule |

This PR (#1089) makes the gap **explicit** by adding `rule: "gap"` entries to `ATOM_ASSIGN` in `mass_table_ppb.py` — the witness output now carries explicit "GAP" rows with the target Vol values, rather than silently omitting them. **This does NOT close the gap** — it only surfaces it for the audit trail.

## Kashaev volume targets

For each atom, the Kashaev law `B = ρ_F · m_e · Vol(K)` gives a target volume if we fix ρ_F:

| Atom | B_AME (MeV) | Vol target (ρ_F = m_e) | Vol target (ρ_F = 2m_e) |
|------|-------------|------------------------|-------------------------|
| ⁵Li  | 26.328      | **51.52**              | 25.76                   |
| ⁶Li  | 31.99405    | **62.61**              | 31.30                   |
| ⁷Li  | 39.24453    | **76.80**              | 38.40                   |

These are **large hyperbolic volumes** — well outside the SnapPy "small knot" census (most prime knots have `Vol < 20`). Candidates would be:

- **Multi-component links** (chain links, satellite links) — volumes scale with component count and tessellation density
- **Highly twisted prime knots** (cable knots of cable knots)
- **Hyperbolic surfaces** rather than knot complements (less natural for the QOU framework)

A census search over `SnapPy.HTLinkExteriors` or `OrientableCuspedCensus` for manifolds with hyperbolic volume in `[25, 80]` would surface candidates — **but** census search is the AME-driven path explicitly admitted as CAL-4-equivalent in [`mass_table_ppb.py:18-21`](../../computations/mass_table_ppb.py) for D / T / ³He. Repeating that pattern for ⁵Li / ⁶Li / ⁷Li would extend the existing hidden-fitting risk rather than resolve it.

## Categorical paths (canonical, no fit)

For the wiring to be canonical rather than census-fit, it would need to derive the atom→knot assignment from the framework's substrate-pure inputs:

### Path 1 — α-cluster extension below A=8

The current α-cluster rule starts at A=8 (⁸Be = 2α). Extending below:

- **⁶Li** could model as `α + d` (α-cluster + deuteron). Empirical: B(⁶Li) − B(⁴He) − B(²H) = 31.99 − 28.30 − 2.22 = **1.47 MeV** of α-d binding. The framework would need a `c_αd` coupling analogous to `c_αα = m_e · Vol(7²_1) ≈ 2.43 MeV`. Candidate: `c_αd = m_e · Vol(linked_α_d_topology)` — needs the canonical α-d link identified.
- **⁷Li** could model as `α + t` (α + tritium). `B(⁷Li) − B(⁴He) − B(³H) = 39.24 − 28.30 − 8.48 = 2.46 MeV` — coincidentally close to `c_αα = 2.43 MeV` but the link topology would differ.
- **⁵Li** = `α + p` (α + free proton). Empirical: `B(⁵Li) − B(⁴He) = 26.328 − 28.296 = −1.97 MeV` (negative — ⁵Li is unbound; this matches the resonance status).

Risk: introduces three new c-couplings (`c_αp`, `c_αd`, `c_αt`) each needing a separate canonical derivation. Multiplies the hidden-fitting candidate count rather than reducing it.

### Path 2 — extend VolDensity(K) to multi-knot configurations

The canonical [PR #1080](https://github.com/litlfred/qou/pull/1080) formula is `m(K) = m_e · VolDensity(K, q₀)` for a single knot. For nuclei with multiple α-clusters + valence nucleons, the natural extension would be `VolDensity(K_1 ⊔ K_2 ⊔ ...)` over disjoint-union or connected-sum links. PR [#1081](https://github.com/litlfred/qou/pull/1081) Task 3 (S₅ ↔ SO(3) fiber action) may provide the categorical structure needed to derive multi-knot VolDensity evaluations from substrate.

Risk: depends on PR #1081 Task 3 landing. Cannot proceed on this branch.

### Path 3 — symmetric-crystal Demazure sub-crystal for unbound states

Per AGENTS.md §7b: *"Demazure sub-crystals for resonances. Unstable intermediaries (W/Z bosons, hadronic resonances, virtual particles) are Demazure sub-crystals — incomplete topological states."*

⁵Li being a resonance (lifetime ~10⁻²² s) suggests it should be modelled as a **Demazure sub-crystal of the full ⁶He / ⁵He / ⁵Li mass-near-degenerate cluster**, not as a stable knot. This is the categorically-aligned framing but requires authoring the Demazure sub-crystal machinery for the A=5 sector first.

Risk: substantial new machinery; out of scope for PR #1089.

## Recommended next steps (owner-direction needed)

1. **Decide whether to repeat the census-assignment pattern** for ⁶Li, ⁷Li (extending the CAL-4-equivalent admitted in `mass_table_ppb.py`) or **wait for canonical paths** (PR #1081 Task 3, or α-cluster extension).
2. **If canonical**: pick one of Paths 1 / 2 / 3 and escalate to Rule 14 (the 13-driver menu) — none currently identify an off-the-shelf source for the multi-cluster coupling.
3. **If pragmatic interim**: do a SnapPy census search for `Vol ∈ {62.6 ± 1, 76.8 ± 1}` and surface candidates as **EXPLORATORY shape-probes** (per AGENTS.md production-vs-exploratory rule), not as production assignments.

This audit explicitly does NOT recommend any one path — that's owner judgement.

## What PR #1089 actually delivers on this gap

- Adds explicit `rule: "gap"` rows for ⁵Li, ⁶Li, ⁷Li in `mass_table_ppb.py:ATOM_ASSIGN`
- Adds `predict()` handling for `"gap"` rule that returns a structured no-prediction record (with the target Vol values + audit-doc pointer)
- Witness output `mass-table-ppb.witness.json` will now include explicit `B_pred: null, formula: "GAP — no atom→knot rule"` rows for these atoms
- The `canonical-mass-table-extended.witness.json` downstream consumer (via [`canonical_mass_table_extended.py:262 lookup_b_pred_existing`](../../computations/canonical_mass_table_extended.py)) will pick up `null` and surface it as the existing null `prediction_MeV_50dps` field, but now with the audit-doc pointer in the upstream witness chain

The numerical content of the framework is **unchanged**. The deliverable is **audit-trail visibility** for the missing rule.

## Cross-references

- Parent audit: [`2026-05-24-low-isotope-mass-error-anatomy.md`](2026-05-24-low-isotope-mass-error-anatomy.md)
- Coordination ledger: [`docs/coordination/2026-05-24-low-isotope-mass-anatomy-ledger.md`](../coordination/2026-05-24-low-isotope-mass-anatomy-ledger.md)
- PR [#1081](https://github.com/litlfred/qou/pull/1081) — supplier for Path 2 (S₅ ↔ SO(3) fiber action)
- [`mass_table_ppb.py`](../../computations/mass_table_ppb.py) — where the gap is now surfaced explicitly
- [`isotope_record_schema.py`](../../computations/isotope_record_schema.py) — where the closure topology dict `CANONICAL_CLOSURES` would need ⁵Li / ⁶Li / ⁷Li entries once a path is chosen
