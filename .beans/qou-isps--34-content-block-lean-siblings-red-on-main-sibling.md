---
# qou-isps
title: 5 content-block .lean siblings still RED on current main (re-verified 2026-09-04 14:5xZ) — 4 outside qou-e7xv's sweep list + its survivor qou-0xrn
status: completed
type: task
priority: normal
created_at: 2026-09-04T14:04:41Z
updated_at: 2026-09-05T06:20:57Z
---

Found by compiling all 907 content-block sibling .lean files against the freshly rebuilt library oleans (bean qou-n9j7, PR #6649, main 71744b7775): 866 green, 41 red. Of the 41: 4 fixed mechanically on the branch (orphan docstrings, a `fun λ =>` binder, two missing tactic imports), 1 was a harness path gap (UGB build dir), and nuclear-interactions/hyperelliptic-z5-classification is not fixed: tactic '' unmapped. The rest are REAL — proof/API drift against current Mathlib or the current library (renamed/removed declarations, structure fields that no longer exist, failed instance synthesis) — and are NOT fixed here: a real red is repaired by whoever owns the block's mathematics, never by weakening statements. Two cannot be verified in this sandbox at all (they `import Mathlib` wholesale and the cache has no Mathlib root olean). Verbatim first error per file (full excerpts were in /tmp/qou-siblings-errors.txt of the session; repro: cd content/quantum-observable-universe/lean; LEAN_PATH=<restored dirs incl. UGB> lean ../<file>):

- `braids-and-knots/braid-action-tensor.lean` (3 err): `82:18: error(lean.unknownIdentifier): Unknown constant `CategoryTheory.MonoidalCategory.whiskerRight_comp``
- `braids-and-knots/lagrange-resolvent-transform.lean` (2 err): `108:4: error: `simp` made no progress`
- `climax-volume-mass/vertex-algebra-jet-relations.lean` (1 err): `1:0: error: unknown module prefix 'UGB'`
- `fluid-dynamics/bn-mtc-action.lean` (1 err): `29:11: error: invalid binder annotation, type is not a class instance`
- `fluid-dynamics/townsend-biot-savart-strain.lean` (4 err): `150:6: error(lean.unknownIdentifier): Unknown constant `Real.tendsto_log_mul_rpow_nhdsGT_zero``
- `information-theory/quantum-volume.lean` (3 err): `55:30: error: failed to synthesize`
- `knots-particles-confinement/confinement-level-exists.lean` (1 err): `25:2: error(lean.unknownIdentifier): Unknown constant `QOU.BraidKnot.ConfinementLevel.exists``
- `lifting-and-descent/descent-cocycle-deviation.lean` (2 err): `45:10: error: failed to synthesize`
- `lifting-and-descent/euler-char-stability.lean` (2 err): `25:18: error(lean.inferBinderTypeFailed): Failed to infer type of binder `n``
- `lifting-and-descent/localized-knot.lean` (1 err): `62:2: error: Invalid field `writhe`: The environment does not contain `QOU.KnotTheory.BraidWord.writhe``
- `mass-endomorphism/chi-v21-hoefsmit-matrix-derivation.lean` (2 err): `247:8: error(lean.unknownIdentifier): Unknown identifier `hoefsmit_v21_b_sq_rational``
- `mass-endomorphism/explicit-central-idempotent.lean` (1 err): `115:2: error: failed to synthesize`
- `mass-endomorphism/u-coordinate-discharges.lean` (2 err): `82:2: error: No goals to be solved`
- `mass-theory/borromean-h4-categorical-derivation.lean` (1 err): `45:0: error: object file '/home/user/qou/.lake/packages/mathlib/.lake/build/lib/lean/Mathlib.olean' of module Mathlib does not exist`
- `mass-theory/categorical-transfer-matrix.lean` (6 err): `26:13: error: unexpected token 'section'; expected 'lemma'`
- `mass-theory/flavor-mass-splitting-bound.lean` (4 err): `74:21: error(lean.unknownIdentifier): Unknown identifier `R``
- `mass-theory/gb-depth-period-correspondence.lean` (3 err): `81:0: error: failed to synthesize`
- `mass-theory/h3-markov-wenzl-weights.lean` (1 err): `48:0: error: object file '/home/user/qou/.lake/packages/mathlib/.lake/build/lib/lean/Mathlib.olean' of module Mathlib does not exist`
- `mass-theory/knot-factor-shell-closed.lean` (3 err): `24:65: error: Application type mismatch: The argument`
- `mass-theory/pentagon-uv-commutation.lean` (1 err): `15:4: error: Application type mismatch: The argument`
- `mass-theory/qz-bicompletion.lean` (1 err): `36:42: error(lean.unknownIdentifier): Unknown identifier `zPochhammer``
- `mass-theory/residue-at-root.lean` (4 err): `29:37: error(lean.unknownIdentifier): Unknown constant `QOU.BraidKnot.ResidueAtRoot.residue``
- `mass-theory/spin-involution-lp-dual-invariance.lean` (3 err): `51:10: error: Function expected at`
- `mass-theory/typed-b3-sub-braid-extraction.lean` (1 err): `216:2: error: No goals to be solved`
- `mass-theory/vertex-operator.lean` (6 err): `30:13: error: unexpected token 'section'; expected 'lemma'`
- `nuclear-interactions/hyperelliptic-z5-classification.lean` (2 err): `48:3: error: unknown tactic`
- `observations/n-v-bring-action.lean` (8 err): `37:31: error: unexpected token 'Σ'; expected '_' or identifier`
- `observations/n-v-tower-depth-ninety.lean` (1 err): `35:10: error: typeclass instance problem is stuck, it is often due to metavariables`
- `predicted-spectra/bloch-group-quotient-construction.lean` (5 err): `368:2: error: `pentagon_subgroup_exists` is not a field of structure `HasPentagonRelation``
- `quantum-observable-universes/categorical-q-ext-deriv-unique.lean` (3 err): `67:2: error: Tactic `rfl` failed: The left-hand side`
- `quantum-observable-universes/q-connection.lean` (2 err): `26:2: error: failed to synthesize`
- `quantum-observable-universes/q-ext-deriv.lean` (3 err): `31:2: error: failed to synthesize`
- `quantum-observable-universes/q-lie-bracket.lean` (3 err): `30:2: error: failed to synthesize`
- `quantum-observable-universes/quantum-planck-constant.lean` (3 err): `27:6: error: failed to synthesize`
- `quantum-observable-universes/substrate-parameter-exists.lean` (8 err): `95:4: error: `field_pos` is not a field of structure `SubstrateParameter``
- `stochastic-mechanics/classical-limit-functor.lean` (1 err): `38:12: error(lean.unknownIdentifier): Unknown identifier `MonoidalFunctor``

NOTE for the next agent: these siblings have .qa.json sidecars; a `lean`-direct verdict recorded there before this date was measured against cached oleans and is not evidence the file compiles today.



CORRECTION: nuclear-interactions/hyperelliptic-z5-classification (listed above) was fixed after this bean was written (interval_cases → Mathlib.Tactic.IntervalCases; green), so 35 files remain: 30 real, 2 partial (categorical-transfer-matrix, vertex-operator), 2 unverifiable here (import Mathlib root), 1 harness-only (vertex-algebra-jet-relations compiles with UGB on the path? NO — it has 4 real type mismatches against UGB; vertex-algebra-relations is the harness-only one and is not in this list).



## SUPERSEDED AND RE-MEASURED 2026-09-04 14:5xZ (main ceb526bc31)
The 35-file list above was written WITHOUT grepping .beans first — bean qou-e7xv (another session; PR #6540 and follow-ups) had already swept the same files, 38 → 1, and landed the repairs on main while my pass ran. Re-verified every one of the original 41 against current main with the library's dirty closure rebuilt (4 new modules) and the UGB build dir on LEAN_PATH: **32 green, 4 harness-only (2 UGB path, 1 module main added after my list, 1 file main deleted), 5 still RED**:
- `knots-particles-confinement/confinement-level-exists.lean` (1 err): `25:2: error(lean.unknownIdentifier): Unknown constant `QOU.BraidKnot.ConfinementLevel.exists``
- `lifting-and-descent/euler-char-stability.lean` (2 err): `25:18: error(lean.inferBinderTypeFailed): Failed to infer type of binder `n``
- `lifting-and-descent/localized-knot.lean` (1 err): `62:2: error: Invalid field `writhe`: The environment does not contain `QOU.KnotTheory.BraidWord.writhe``
- `mass-theory/qz-bicompletion.lean` (1 err): `36:42: error(lean.unknownIdentifier): Unknown identifier `zPochhammer``
- `mass-theory/spin-involution-lp-dual-invariance.lean` (3 err): `51:10: error: Function expected at`

Of these, spin-involution-lp-dual-invariance is qou-e7xv's own survivor (qou-0xrn); the other FOUR are not in qou-e7xv's 38 at all (their list and my 41 differ). Repro: cd content/quantum-observable-universe/lean; LEAN_PATH=<restored dirs + UGB> lean ../<file>. Real drift, not touched here.



CORRECTION 21:0xZ: localized-knot was a HARNESS red (stale cached QOU.KnotTheory olean with a fresh mtime; BraidWord.writhe exists at KnotTheory.lean:86) — green after rebuilding the dependency. confinement-level-exists and euler-char-stability fixed on branch claude/four-sibling-reds-2026-09-04 (qou-ekgf). Remaining real: qz-bicompletion (zPochhammer never defined) and spin-involution-lp-dual-invariance (qou-0xrn).
