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

## Cross-references

- merged [PR #1581](https://github.com/litlfred/qou/pull/1581) (closed-route reexamination roundup)
- merged [PR #1442](https://github.com/litlfred/qou/pull/1442) (m_K/m_π EM correction via Bring zero-mode)
- audit [`2026-06-01-closed-route-reexamination-roundup.md`](../audits/2026-06-01-closed-route-reexamination-roundup.md)
- coord ledger [`option-e.md`](./option-e.md) (PROBE 1 partially addressed by PR #1581)
