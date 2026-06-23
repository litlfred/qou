---
# bwkg
title: 'Fix 3 deep-broken frontier Lean files: CategoricalDqSquared, QHookBound, MarkovPeel'
status: todo
type: task
priority: normal
created_at: 2026-06-23T17:03:11Z
updated_at: 2026-06-23T23:55:01Z
---


Surfaced 2026-06-23 by the build-frontier hunt (claude/lean-broken-file-fixes-2,
PR #2652). These 3 frontier files are multi-error / structural — NOT bounded
single-fix red→green (unlike SDPRankEquality #2637, WenzlSchurElement +
HeckeLogDecomposition #2647, DimStandardRepS3 #2652). lean-lsp now available for
deliberate debugging. Details:

- QOU.CategoricalDqSquared: (a) docstring `/-- -/` placed before
  `noncomputable section` (a section can't take a docstring) — move section
  first; (b) missing imports Mathlib.CategoryTheory.Preadditive.Basic +
  .Linear.Basic (theorem uses [Preadditive C] [Linear R_q C]); (c) the
  `noncomputable section` is missing its closing bare `end` before `end QOU`;
  (d) AFTER (a)-(c): residual `CategoricalQExtDeriv` structure-field type errors
  (L66 "Function expected" on cqd.d_classical ≫ ...; L69 unsolved goals). (a)-(c)
  fixed+verified locally; (d) needs the structure def debugged.

- QOU.Archimedean.QHookBound: 35 errors. First is a malformed one-line calc at
  qInt_pos: `have : q⁻¹ < q := by calc q⁻¹ < 1 := hq_inv_lt; _ < q := hq` (the
  `;`-separated one-line calc is wrong). Cascade follows.

- QOU.Interactions.MarkovPeel: L112 structure field
  `hecke_quadratic : ∀ n, top n * top n = h * top n + 1` fails to synthesize the
  SMul/HMul instance for `h * top n` (h a scalar, top n an algebra element) —
  the structure likely needs an [Algebra]/[Module] hypothesis or h:H not scalar.

REFINED TRIAGE 2026-06-23 (claude/fix-deep-broken-frontier, lean-direct vs current main):
- QHookBound: ALREADY GREEN on current main (0 errors) — fixed by a sibling Archimedean
  commit since this bean was filed. Drop from scope.
- MarkovPeel (1 err, L112): class `MarkovTrace` declares only [Mul H][One H] + [CommRing R],
  but field `hecke_quadratic : top n*top n = h*top n + 1` needs [Add H] (the `+1`) AND an
  R-action h:R • top n:H ([SMul R H] / [Algebra R H]). Structural + CASCADES: strengthen
  the class binders, change `h * top n`→`h • top n`, propagate binders to the 3 in-file
  reference identities (L137/185/233) + MarkovPeelH3.lean + any proof that rw[hecke_quadratic].
- CategoricalDqSquared (4 err on main): (a) docstring before `noncomputable section` L43 —
  move section first; (b) L45-46 q_param/q_inv_param IR-noncomputable are DOWNSTREAM of (a);
  (c) missing bare `end` for the section L71; (d) missing imports Preadditive.Basic +
  Linear.Basic. AFTER (a)-(d): theorem L61-70 uses cqd.d_classical/dq/dq_classical on
  `CategoricalQExtDeriv` (defined in QOU/QuantumObservableUniverse/Instanton.lean, NOT
  imported here; Instanton exposes dq/dq_classical/proj_H). Needs: import Instanton + re-sync
  the theorem to the current structure API (the "Function expected at L66" residual).
Both remaining = genuine deep structural work; best as a focused lean-lsp pass.

## Progress 2026-06-23 (#2663)

- ✅ **CategoricalDqSquared** — fixed red→green, sorry-free (library-critical:
  QOU.lean imports it). Section ordering + imports (Instanton/Preadditive/Linear)
  + closing `end` + `[Linear R_q C]`→`[Linear ℝ C]`.
- ✅ **MarkovPeel** — fixed red→green, sorry-free (imported by MarkovPeelH3 +
  markov-axiom-recursive-ascent). Added `[Add H] [SMul R H]` to the MarkovTrace
  class + the 3 theorems; `h * top n`→`h • top n`.
- ⏳ **QHookBound** — DEFERRED (orphan = latent-red, not a lake-build breaker).
  Deeper than the calc fix the bean cites: after replacing the `;`-calc at L61
  with `lt_trans hq_inv_lt hq`, **46 errors remain**, of three kinds:
  1. Mathlib-API rot (current names needed): `inv_lt_one_iff_of_pos` (×6: L56,
     137, 225, 261, 289, 333), `pow_lt_pow_left` (L59), `div_le_div_iff`
     (L103, 380).
  2. Dangling docstrings (two `/--` with no decl between): L65-80 before
     `qInt_ratio_bound_m2`, and L204-215.
  3. A genuine proof bug at `qInt_pos`: `pow_lt_pow_left hq_inv_lt …` uses
     `q⁻¹ < 1` where the goal `q⁻¹^m < q^m` needs `q⁻¹ < q`
     (`lt_trans hq_inv_lt hq`); plus several `nlinarith`/`rw` proofs need
     re-tuning for the renamed lemmas.
  Needs lean-lsp (leansearch/loogle) for the current lemma names + deliberate
  per-proof debugging — a focused follow-up, not a mechanical sweep.
  **NOTE (reconcile vs sibling REFINED TRIAGE above):** my 46-error count was
  vs a stale olean cache (+31 behind main); the sibling reports QHookBound
  ALREADY GREEN on current main. Re-verifying against current main before
  acting — see #2663 follow-up.
