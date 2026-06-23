---
# bwkg
title: 'Fix 3 deep-broken frontier Lean files: CategoricalDqSquared, QHookBound, MarkovPeel'
status: todo
type: task
created_at: 2026-06-23T17:03:11Z
updated_at: 2026-06-23T17:03:11Z
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
