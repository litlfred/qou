> **DEPRECATED on 2026-05-24.** Undated audit document classified as workplan / status snapshot / migration-handoff / one-off investigation whose findings have been integrated into main or whose plan has been executed. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T5 for the deprecation rationale.

# Audit — last-2-days content vs computation-pipeline wiring

**Scope.** Commits on the qou repo since 2026-04-25 00:00 UTC.
**Question.** For every content block (`.ts` + `.md` + optional `.lean`)
added or modified in this window, is it wired to the computation
pipeline (witness JSON / Python feeder / Rust binary), and which
pipeline artifacts have no content home?

**Status.** First-pass results below. Window covers commits since
2026-04-25 00:00 UTC. The bulk of file activity comes from PR #444
(joint-tower SDP / R1–R5min / Clarabel) and PR #445 (C5 proof splits),
both merged on 2026-04-27.

## Volume

| Bucket | Count |
|---|---|
| Content `.ts` files added (incl. merged-in branches) | 1506 |
| Content `.ts` files modified | 959 |
| New witness JSONs in `computations/` | 364 |
| New Python feeders in `computations/` | ~470 |
| New Rust files in `tools/hecke-engine/src/` | 4 (1 production binary, 3 R5.5 diagnostics) |

The very large `.ts` counts are inflated by long-running feature
branches that merged in via PR #444 / PR #445 and PR #442 — most of
those blocks pre-existed those branches but reached `main` only in
this window. The rows below focus on **genuinely new** content
blocks authored in the window (non-merge commits) and on the
content blocks the SDP / mass-derivation work introduces.

## Wired-end-to-end (genuinely new in window)

Per content/.md narrative + Lean (no unjustified `sorry`) + at least
one cited witness JSON / sibling feeder / Rust binary:

| Block label | Chapter | Kind | Compute evidence |
|---|---|---|---|
| `prop:atom-knot-mass-derivation` | braids-and-knots | proposition | `joint-tower-sdp-rust.witness.json`, `joint-tower-sdp-h6-h9.witness.json`, `gb-filtration-jet-order.witness.json`, `joint_tower_sdp_solver_v2.py`, `tools/hecke-engine/src/bin/joint_tower_sdp.rs` |
| `prf:atom-knot-mass-derivation` | braids-and-knots | proof | inherits from proposition |
| `prop:joint-tower-sdp-confinement` | braids-and-knots | proposition | same as above + `gb_filtration_jet_tracker.py` |
| `prop:recursive-atom-knot-atlas` | braids-and-knots | proposition | `methodology-deprecation.witness.json`, `mass-table-ppb.witness.json`, `recursive_atom_knot_atlas_render.py` |

## Wired-partially / math-only (genuinely new in window)

Lean + narrative present, no compute counterpart yet — these are
the candidates for the next round of feeders:

| Block label | Chapter | Kind | Notes |
|---|---|---|---|
| `prop:y-lambda-recipe-from-partition` | braids-and-knots | proposition | Lean recipe lands; feeder `y_lambda_recipe_from_partition.py` exists but no witness file by that name yet |
| `prop:wenzl-qmn-synergy` | braids-and-knots | proposition | rebased from PR #427; cross-validation feeder `wenzl_qmn_cross_validation.py` exists, witness-by-name TBC |
| `prop:qmn-recursive-memoized` | braids-and-knots | proposition | feeder `q_mn_recursive_memoized.py` lands with the block; witness coverage limited |
| `prop:y-lambda-cyclotomic-factor` | braids-and-knots | proposition | feeder + witness `y-lambda-cyclotomic-factor.witness.json` paired |

## C5 proof splits (PR #445)

The C5 work (`PR #445`) split previously monolithic categorical-mass
/ topological-mass / Brings-Q proofs into smaller proof blocks
(Tier-2 + Tier-3). Per-block summary is in PR #445; the split
preserved the original wiring (witness coverage was at the parent-
proposition level, not per-sub-lemma), so the children inherit
their parents' wiring rather than introducing new compute paths.

Touched files include `topological-mass-categorical-proof.ts`,
`terminal-resolution-proof.ts`, `topological-mass-proof.ts`,
`cosimplicial-crossed-groupoid-proof`, `jet-prolongation-proof`,
`mi-sw-abelianisation-proof`, `mobius-energy-proof`,
`descent-condition-proof`, `fiber-adjoint-involution-proof`,
`brings-is-qou-proof`, `transfer-matrix-level-independence-proof`,
`non-self-intersection-proof`, `skein-generation-proof`,
`euler-char-stability` (tightened), `su2-emergence-proof` (+2
sub-lemmas) plus 7 Tier-3 proofs and 4 additional Tier-2 splits.

## Pipeline artifacts without a content home

**Rust binaries (R5.5 SDP solver diagnostics — internal tooling, not
exposed as content):**
- `tools/hecke-engine/src/bin/r5_5_diagnose_h5.rs` — H₅ anomaly diagnostic (resolved by svec-encoding fix in commit 807a3af)
- `tools/hecke-engine/src/bin/r5_5_minimal_h5.rs` — minimal H₅ reproducer
- `tools/hecke-engine/src/bin/r5_5_scale_test.rs` — H₃→H₈+ solver scaling test

**Documentation under `tools/hecke-engine/`:**
- `R5_5_BUG_REPORT.md` — Clarabel-rs svec-encoding post-mortem
- `R5_FULL_PLAN.md` — R5 SDP roadmap (R5.6 Wedderburn decomposition pending; R5.7 ⁶Li / ⁷Li at H₁₈ pending)

These are internal tooling and are appropriate where they live;
they need no paper-block counterpart.

## Next steps for the calculation

The mass-table residuals on this branch (⁶Li −2080 ppm, ⁷Li −1851
ppm, partial-shell A=10–11 isotopes ~750–1160 ppm) are exactly the
gaps R5.6 (per-block Wedderburn decomposition) and R5.7 (⁶Li / ⁷Li
at H₁₈ with AME anchor) are designed to close. The wiring story is:

1. The pre-Archimedean pipeline (GB-NF → joint-tower SDP →
   Wedderburn-block PSD → Markov trace) is wired end-to-end at H₃,
   H₄ and now H₅–H₈ after the svec fix.
2. H₁₈+ requires R5.6 (memory-bounded decomposition); not a
   correctness blocker — a scale-out task.
3. Partial-shell isotopes (Z = 3–5, A = 6–11) are still using the
   `partial-shell:f=…` interpolation strategy (visible in
   `low-isotope-mass-table.witness.json`); they will be
   superseded once R5.7 lands and the SDP-solver path produces
   their canonical T_w directly.

## Plan

1. Enumerate added/modified blocks under
   `content/quantum-observable-universe/<chapter>/`.
2. For each, record: chapter, label, kind (definition / proposition /
   …), Added vs Modified, presence of meaningful Lean (sorry-count
   with `Ref:` annotations), computational evidence (cited witness
   JSON, sibling Python feeder, named Rust binary).
3. **DAG wiring check.** For each block, verify the `uses[]` array
   is complete and current:
   - Cross-reference labels mentioned in the `.md` body
     (`[text](#label)` links and `\hyperref[label]{}` refs in math)
     against entries in `uses[]`. Missing entries are dependency-graph
     leaks.
   - Flag entries in `uses[]` that point to labels which no longer
     exist (renamed or deleted blocks).
   - Confirm `uses[]` lists immediate neighbors only (transitive
     entries should be pruned per
     `content/pipeline/prune-transitive-deps.ts`).
   - For provable kinds (`theorem`/`proposition`/`lemma`/`corollary`),
     verify §3b conjectural-propagation: any `conj:` ancestor (direct
     or transitive) demands the block itself be `conjecture` or carry
     a documented exception.
4. Bucket each block:
   - **wired-end-to-end** — narrative + Lean (no unjustified `sorry`)
     + compute evidence + complete `uses[]`
   - **wired-partially** — Lean OR compute evidence, not both, OR
     `uses[]` is incomplete
   - **stub/skeleton** — `.ts` exists, but `.md` missing/short and no
     Lean, no compute
   - **math-only** — full narrative + Lean, no compute counterpart
5. Separately list new Python feeders / Rust bins / witness JSONs in
   the window that no content block references.

## Why this audit

PR #444 (joint-tower SDP + Clarabel + Rust GB-NF reducer + R5-minimal
α* verifier) introduced 357 file changes; PR #445 (C5 proof splits)
overlapped the same window. Several content blocks land alongside
new compute artifacts; a few may be orphaned in either direction.
Identifying those gaps unblocks the next iteration on the
**mass-derivation calculation** (sub-ppm convergence for partial-shell
isotopes ⁶Li / ⁷Li / ⁹Be / ¹⁰Be / ¹⁰B / ¹¹B), which is the active
work-stream on this branch.
