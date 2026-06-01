# Closed-route follow-ups (PR #1581 continuation) — 2026-06-01

Branch: `claude/closed-route-followups-2026-06-01`

Per the merged PR #1581 audit
[`docs/audits/2026-06-01-closed-route-reexamination-roundup.md`](../audits/2026-06-01-closed-route-reexamination-roundup.md),
this branch tackles four follow-up items in priority order:

1. **Bring zero-mode derivation** of the Ocneanu EM correction
   `(α_em/π) / dim H_3` (parallel to PR #1442's m_K/m_π closure).
   Goal: promote tier=near-match → tier=proved.
2. **c_2-off-integer pivot** for meson Habiro: test
   `c_2 = 4·(1 + ε·h²)` PSLQ on ε; if positive, re-frame the
   REOPENED meson Habiro c=4 finding.
3. **Yekutieli +0.5 observable hunt**: scan whether `+0.5·h²`
   appears in m_He, m_Li, or other isotope binding-energy
   linking_weights.
4. **Proton-mass identity content block update**: document the
   `(α_em/π)/dim H_3` near-match as exposition (no new
   derivation in the content block itself).

## Status

| Task | Tier | Status |
|---|---|---|
| 1. Bring zero-mode derivation | NULL | done — Bring template does NOT transfer; baseline (α_em/π)/dim H_3 stands |
| 1-alt. Alt knot-operator geometries | NULL | done — 27 alts tested; dim H_3 = 6 is structurally robust |
| 2. c_2-off-integer pivot | NULL | done — PSLQ NULL across 24 basis elements; both framings fail |
| 3. Yekutieli +0.5 observable hunt | NULL | done — no observable normalizes to +0.5·h² |
| 4. Content block exposition update | n/a | done — proton-mass-substrate-identity.md sub-ppm section added |

## Findings summary

This branch landed **4 well-defined NULL results** which collectively
narrow the search space for sub-ppm proton-mass closure:

- The (α_em/π)/dim H_3 near-match at 54 ppb is REAL but its
  structural form (denominator 6, not 5/8/24/etc.) is now confirmed
  across 27 alt-geometries — the residual is not from picking wrong
  knot-operator geometry
- The Bring zero-mode (3q²−1)/(2q²) template from m_K/m_π does NOT
  transfer to the proton's '12·m_e' term
- Both meson Habiro c=4 reopening framings (c_3 absorbs, OR c_2-off-
  integer) fail PSLQ at the substrate basis — the route stays
  REOPENED but at lower confidence
- The Yekutieli +0.5·h² doesn't have an obvious physical-observable
  home in binding-energy / multi-nucleon residual / isospin mirror
  candidates

The proton-mass identity content block now documents the sub-ppm
near-match as exposition without claiming derivation (tier=near-match
guard rails per production-vs-exploratory-discipline).

## Exploration finding (post-task-4, while-waiting)

Per user 2026-06-01 "while waiting, keep exploring" direction. The
54 ppb baseline residual after `(α_em/π)/dim H_3` was searched for a
non-trivial `f(q)` correction (`f(q_0) ≈ 1.001674`). Two empirically
tight candidates were identified (`ocneanu_54ppb_residual_exploration.py`):

  Form A: `f = 1 + (1 - π²/80)·h⁴`            → 0.003 ppb (17,584× improvement)
  Form B: `f = 1 + (7/8)·h⁴ + (G/(8π))·h⁶`    → 0.0008 ppb (68,576× improvement)

Both pass below the 1 ppQ substrate target (10⁻¹⁵ relative ≈ 10⁻⁶
ppb). But **neither has clean structural derivation**:

- The `80` in Form A (= 2⁴·5 = 16·5) tentatively suggests 5-fold
  Bring quintic × 16 EM-halvings⁴ but no derivation
- The `7/8` in Form B might come from Bring saturating-genus
  generation knot indices (T_(2,7) is one of three: T_(2,3), T_(2,5),
  T_(2,7)) but no formal categorical link
- The `G/(8π)` in Form B reuses fine-structure prefactor structure
  but in a new context

**Status: tier=near-match (exploratory).** Recorded for future
investigation. **Do not promote to production** — the empirical
fit-quality (sub-ppb) means a numerical near-match for ANY two-
parameter form would close at this precision, so PSLQ-level
discrimination is needed to determine whether these forms are
genuinely structural or coincidental.

Next steps if pursued:
- Higher-precision search (100+ dps) for tighter or alternative forms
- Structural derivation of `80 = 16·5` or `7/8` from Bring quintic
- Test cross-anchor stability (q_muon vs q_proton)
- Lean formalization once a clean structural form is identified

## Cross-references

- merged [PR #1581](https://github.com/litlfred/qou/pull/1581) (closed-route reexamination roundup)
- merged [PR #1442](https://github.com/litlfred/qou/pull/1442) (m_K/m_π EM correction via Bring zero-mode)
- audit [`2026-06-01-closed-route-reexamination-roundup.md`](../audits/2026-06-01-closed-route-reexamination-roundup.md)
- coord ledger [`option-e.md`](./option-e.md) (PROBE 1 partially addressed by PR #1581)
