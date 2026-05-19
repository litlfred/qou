# Coordination ledger — `claude/canonical-discipline-l1-l3-l4-2026-05-19` (PR #802)

Goal: introduce per-row `canonical_status` taxonomy across the per-Z
canonical-isotope-witness shards; demote heuristic L3 partial-shell;
remove AME-B fallback from L4 composite mass; surface the
substrate-derivation gaps honestly.

## Sibling scope map (per `local/coordinate` §2)

| PR | Title | Classification | Relation |
|----|-------|----------------|----------|
| #801 | log-Δ categorical derivation: identifies interface-knot Δ_I^K as resolution | **complementary + dependency** | Their Δ_I^K is the categorical resolution to the tensor-product bug noted in PR #802's Q2 follow-up. Their test plan explicitly cites this branch's `canonical_status` taxonomy as a planned consumer. |
| #799 | fix(I5): correct 8 contentBlock label prefixes (7 → 0 missing-label) | **resolves blocker** | Closes the conj:/prop: prefix issue noted in PR #781's review-comment triage. |
| #800 | fix(I13): defer tower-mode upstream-coverage gaps (6 → 0) | **orthogonal** | I13 = incomplete-coverage audit (PR #788 lineage); PR #802 introduces I14 = witness-provenance audit. Different I-numbers, different audits. |
| #761 | combined Rust kernel work (Hoefsmit / GP / chirality / v6) | **infrastructure** | Rust binary for `hecke-tr-m-wenzl-lr` lives here; Q2 wiring in PR #802 follow-up would consume it. |
| #774 | i3 audit (rationale-backed skips) | **weak-overlap** | Audit infra tightening; no shared files. |
| #738 | detangler story coherence | **no-overlap** | Content structure; no compute overlap. |
| Drafts (#646, #650, #31, #411) | — | skip | — |

## Coordination comments posted

- #801 — [coordination](https://github.com/litlfred/qou/pull/801#issuecomment-4484718490): Δ_I^K resolution aligns with PR #802's Q2 follow-up; once both land, the affected atoms (D, T, ³He, ⁴He) upgrade from `canonical-with-empirical-assignment` → `canonical-recursive`.
- #799 — [coordination](https://github.com/litlfred/qou/pull/799#issuecomment-4484719472): acknowledges that #799 clears the conj:/prop: blocker noted in PR #781's review triage.

## §3 watch checklist for origin/main

main moved 56 commits while PR #802's branch was in flight (current
HEAD `610a6aa2b`). Notable landed items:

- **#777 v7 two-leg precision goal** (`docs/precision-goals.md`) — L1
  compute precision vs L2 100×-experimental. Orthogonal axis to
  PR #802's `canonical_status` (provenance, not goal).
- **#788 I12 audit batch + Lean class stubs** — added
  `class BorromeanMassFormula` (§3b-cond) which PR #802's `canonical-
  substrate` Borromean rows now consume as the Lean side of the
  conjecture.
- **#798 + #800** — I13 audit cleanup (incomplete-coverage variant).
- **#793 / #790 / #786 I1 batches** — Lean-side stub authoring.

No file overlap; clean fast-forward rebase before PR open.

## Open follow-ups (next branch / next session)

1. **Q2 — Wire $*_q$ convolution** (user-confirmed priority): replace
   the buggy tensor-product path in `rho_k_full_via_wenzl_lr.py` with
   inter-nucleon $\Delta_I^K$ junctions (per PR #801's framing).
   Effort: 1-2 days. Coverage: extends `canonical-recursive` past
   the 6 magic atoms to all atoms whose canonical braid is known.
2. **Q1 — Co-Casimir extension past D**: generalise
   `rho_k_h3a_co_casimir.py` from D-only to all 8 L1 atoms.
   Effort: hours per atom (Hoefsmit χ^λ producer cost scales with
   `p(3A)`). Quality: likely worse than current empirical assignment
   per the +954 ppm result on D.
3. **Rust path for L1 extension past ⁶Li**: build the Rust binary
   `hecke-tr-m-wenzl-lr` + integrate into `canonical_mass_table_
   extended.py`. Effort: medium. Coverage: extends L1 to ~A=10-12.

## Session work plan (TodoWrite equivalent)

- [x] Branch `claude/canonical-discipline-l1-l3-l4-2026-05-19` created
- [x] `canonical_status` taxonomy added to `assemble_row()`
- [x] L4 composite mass canonical-only wiring
- [x] L3 demotion (partial-shell → `heuristic`)
- [x] 119 per-Z shards re-emitted with new field
- [x] Atlas badges + per-Z section refresh
- [x] Q-values recomputed against L4-canonical-only composite
- [x] PR #802 opened
- [x] Coordination comments on #801, #799 posted
- [x] Coordination ledger appended (this file)
- [ ] Wait for PR review cycle / merge
- [ ] Follow-up session: Q2 $*_q$ wiring (user-confirmed priority)
