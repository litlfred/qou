---
# qou-24i9
title: qou-hu1f braid-word change left 168 witnesses from direct callers unregenerated, and hardcoded prose contradicting its own data
status: todo
type: task
created_at: 2026-09-06T04:01:26Z
updated_at: 2026-09-06T04:01:26Z
---

`7db032fb48` (*fix(qou-hu1f): atom_braid_word_3A emits beta_Bor*, owner-ruled
2026-09-05) changed the default atom word from the grouped assembly to the
interleaved Borromean one — **"82 % away at q0"** by its own measurement. It is
a correct fix. This bean is its regeneration fallout, which that commit did not
close out.

## Measured, by resolving call sites (not `grep -rl`)

- **321 live files** contain a direct call to `atom_braid_word_3A`,
  `atom_canonical_crossings`, or `nucleon_word_letters` (AST `Call` nodes;
  `_deprecated/` excluded, 25 more there).
- Of the witnesses those producers emit, **168 were computed BEFORE the fix**,
  17 after, 2 undated.

**168 is an UPPER BOUND on what actually moved, not a count of wrong witnesses.**
A direct call does not imply the recorded numbers changed — `7db032fb48`'s own
measurement found `the_character_ratio_derivation_path_is_the_bond_model_probe`
**bit-identical**, because the character ratio cannot see the intra ordering.
The 168 is the set that has to be *checked*; each needs a run to know.

(The static reverse-import closure over `canonical_braid_crossings` reaches
**1101 modules** — essentially the whole corpus, since everything imports a hub
that imports it. That number is useless for scoping and should not be quoted.)

## Confirmed instances (regenerated this session, merge 5f5ad14195)

`rho-binding-constancy` moved hard — ratios rose 3.8×–7.9×, non-uniformly:

| atom | before | after |
|---|---|---|
| D | 3.8677 | 14.6384 |
| T | 36.9884 | 291.0302 |
| ³He | 19.1151 | 131.7156 |

## The second defect: prose that quotes numbers it does not derive

Witness `description` fields hardcode findings. When the data moves the prose
does not, and **nothing detects it** — descriptions are prose, so no gate reads
them. Checking every regenerated witness's prose numbers against its own data
(nearest-value, to separate staleness from rounding):

| witness | stale prose numbers | worst rel. error |
|---|---|---|
| `rho-binding-constancy` | 5.73, 5.728, 5.729, 81.5, 37.4 | **49 %** |
| `delta-lambda-qdim-route-probe` | 0.41, 5.62, 82.9 | **33 %** |
| `delta-lambda-cancellation-ascaling-probe` | 0.28, 1.27, 1.31 | **8 %** |

(`delta-lambda-l1-ceiling-sign-prune`'s 0.59 vs 0.566 is 4 % — a rounding, not
staleness. Checked, not assumed.)

### A withdrawn claim, not just a stale number

`rho-binding-constancy`'s description asserted *"The D ratio 5.728 reproduces
the published α_M 5.729 (cross-validates the pipeline)"*. Under the corrected
word D is **14.64**, so that cross-validation **no longer holds** and must not
be quoted as a pipeline check until α_M is re-derived against the Borromean
word. The probe's actual REFUTATION (α_M is not a forced constant) is
unaffected — it rests on the spread, still ~190 %.

## Done here

- `rho_binding_constancy_probe.py` — description now **interpolates** its
  numbers from the computed `ratios`/`spread`, so it cannot go stale again, and
  states the withdrawal explicitly. Regenerated; prose and data now agree.

## Not done — UNCLAIMED

- The other **165** pre-hu1f witnesses from direct callers. Needs a run each.
- `delta_lambda_qdim_route_probe.py` and
  `delta_lambda_cancellation_ascaling_probe.py` — their descriptions are stale
  (33 % / 8 %). Deliberately NOT rewritten here: their prose states findings
  about convention-dependence I have not studied, and editing a conclusion I
  have not verified would be worse than leaving it visibly stale.
- The hardcode-vs-derive pattern is corpus-wide; only one producer is fixed.
