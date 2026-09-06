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

---

## Update 2026-09-06 — main closed the DATA half; the PROSE half is still open

Merging origin/main (94 commits) brought `ecfe945b5c`
*regen(qou-hu1f): 9 of 53 producers were genuinely stale under the ordering
ruling* (owner-approved). It does the systematic data sweep this bean asked
for, and does it better than the sketch here:

- 53 producers whose witnesses reference `atom_braid_word_3A`, re-run once
  each against the committed witness as baseline.
- Raw verdict CHANGED 20 / SAME 13 / ERROR 16 / TIMEOUT 4 — then **20 is not
  20**: a binary changed/unchanged test conflates a 1.8x ordering shift with
  library last-digit churn. Two guards (relative magnitude > 1e-9, AND on a
  non-negligible value) cut 20 → 11 → **9**. Separation between the noise
  ceiling and the material floor is 47 orders of magnitude, so the threshold
  is not load-bearing.
- Only the 9 were committed; the 11 non-material regenerations were reverted
  rather than trade a meaningless digit for a degraded environment record.

**This bean's 168 was an upper bound and is now superseded as a work item.**
It counted witnesses from *direct callers*; main scoped to witnesses that
*reference* the function, ran them, and measured. Measurement beats the bound.
Cross-check that the two agree: main's regenerated borromean nucleon traces
(proton 0.62932842249, neutron 0.47513351767) match this branch's independent
`hadron_knot_table` run (0.629328, 0.475134).

### What main found that this bean did not

**The ruling breaks producers, not just numbers.** Six of the 16 errors are
invariants the alternating word violates — broken assumptions, not stale
values. `classical_floor_derivation_probe` is the clearest: it ASSERTS the
word is monotone in the generator index, which the grouped order satisfied and
the alternating order cannot. That assertion encodes the superseded
convention. It has to be **decided, not edited away**. This class is entirely
absent from the analysis above, which only ever asked "did the number move".

(One of the six, `he4_magnus_omega2_sign_sparse_probe`, was run by that pass
WITHOUT the resume fix in `3ff3d899c8` — its checkpoint read had been wrapped
as a write by the qou-sidu transform, so it could not resume. Its GATE FAIL is
about a sign disagreeing with the triton, not about resume, so the finding
stands; but a re-run on this branch now actually resumes.)

### STILL OPEN — the prose half, unclaimed

Main's sweep regenerates DATA. It does not read `description` fields, and no
gate does. Re-checked after the merge, both are still stale against their own
freshly regenerated data:

| witness | stale prose | worst rel. error |
|---|---|---|
| `delta-lambda-qdim-route-probe` | 0.41, 5.62, 82.9 | **33 %** |
| `delta-lambda-cancellation-ascaling-probe` | 0.28, 1.27, 1.31 | **8 %** |

Both were last regenerated by `8428c293c3` on this branch — which is the point:
**regenerating a witness does not fix prose that hardcodes its findings.** Only
`rho_binding_constancy_probe` has been converted to interpolate its numbers.

Remaining scope, unclaimed: the two descriptions above (deliberately not
rewritten — their prose states convention-dependence findings nobody here has
studied), the six broken-invariant producers main surfaced, and the
hardcode-vs-derive pattern generally.
