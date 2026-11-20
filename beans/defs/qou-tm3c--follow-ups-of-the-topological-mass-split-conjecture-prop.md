---
# qou-tm3c
title: 'Follow-ups of the topological-mass split: provable blocks now depending on conj:topological-mass, stale labels in Lean/compute/generated files'
status: todo
type: task
priority: high
created_at: 2026-11-20T09:10:00Z
updated_at: 2026-11-20T09:10:00Z
parent: qou-ncxf
---

Follow-ups to the split of `thm:topological-mass` into `conj:topological-mass` and `prop:topological-mass-upper-bound` (owner "Y", 2026-11-20; bean qou-27ys; PR on branch `claude/topological-mass-split-2026-11-20`).

## 1. Conjecture-propagation (AGENTS.md §3b): owner decision, not done
Three provable blocks now visibly depend on the open equality. It was always conjectural; the `theorem` label hid that.
- `prop:hecke-mass-trace` (`mass-theory/hecke-mass-trace.md:19`, "the topological decomposition descends to H_n(R,q)").
- `prop:topological-mass-formula` (`mass-theory/topological-mass-formula.md:29`, "derivation proceeds from the categorical decomposition").
- `cor:quantum-dilogarithm` (`lifting-and-descent/quantum-dilogarithm.md:1`, "the transient trace contribution ... evaluates to Φ_q(z_i)"). This one may only need the transient term's definition, not the equality, so it may be retargetable rather than demoted.
For each block the options are: demote to conjecture; restate as conditional per §3b-cond, which needs a non-degenerate hypothesis class; or retarget to the upper bound when only the bound is used. Not done without owner/W1 sign-off.

## 2. Stale `thm:topological-mass` mentions left on purpose
These are outside the content-block edit. W11 promised to edit no existing `.lean` file, and the compute belongs to W2.
- Lean docstrings and comments: `quantum-universes/topological-mass-formula.lean:10`, `mass-theory/mass-endomorphism-tower.lean:45`, `lean/QOU/MassDerivation.lean:57`, `lean/QOU/ArchimedeanMassFormula.lean:13`, `lean/QOU/Torsion/TopologicalMass.lean:62,135`, `mass-endomorphism/topological-mass-conjecture.lean:24,43`.
- Compute: `computations/mass-from-q-symbolic.py:425` (`w.set_content_block("thm:topological-mass")`) and its witness field `contentBlock`. Fixing it needs a producer re-run.
- Audit witnesses in `computations/audits/*.witness.json` record the old label; they are historical.
- `lean/QOU/Torsion/mass_decomposition_categorical.lean`: the self-assuming projection no longer has a content-block consumer. Delete or de-vacuify it (W8 scope).

## 3. Generated artifacts
- The `.jsonld` files of the 11 touched blocks were regenerated with `gen-block-jsonld` at the pinned platform 82b3899. Unrelated drift was reverted: a full run rewrote 3602 files, and the platform's namespace change from `folio-assistant-core:` to `folio-assistant-sci:` now shows on these 11 files only.
- `build-foreshadows` crashes at the pin (build-foreshadows.ts:163). `foreshadows.json` was hand-patched: 5 label strings changed from thm: to conj:. Re-run it once the platform tool works.
