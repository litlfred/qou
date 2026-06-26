---
# bwkg
title: 'Fix 3 deep-broken frontier Lean files: CategoricalDqSquared, QHookBound, MarkovPeel'
status: in-progress
type: task
priority: normal
created_at: 2026-06-23T17:03:11Z
updated_at: 2026-06-26T02:22:35Z
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

## REFINED DIAGNOSIS 2026-06-24 (QHookBound — attempted, sandbox-blocked)

Verified vs current main + cached Mathlib v4.24.0 via lean-direct. 46→40 errors
with the renames below; the residual ~25 are genuine proof-repair, NOT mechanical.

**CONFIRMED fixes (re-apply in an env with lean-lsp):**
- `inv_lt_one_iff_of_pos` → `inv_lt_one₀` (×9) — lean-direct confirms it elaborates.
- `;`-calc at qInt_pos L61 → `have : q⁻¹ < q := lt_trans hq_inv_lt hq`.
- `pow_lt_pow_left` → `pow_lt_pow_left₀` is the right NAME, but the call also has
  a logic bug (fed `q⁻¹ < 1`; the goal `q⁻¹^m < q^m` needs base `q⁻¹ < q` =
  `lt_trans hq_inv_lt hq`) AND a residual arg/type mismatch — check the current
  `pow_lt_pow_left₀` signature.
- THREE dangling docstrings (`/-- … -/` with no decl before the next `/--`):
  L65, L215, L436 → convert opening `/--` to `/-!`.

**STILL-UNKNOWN (needs lean-lsp/web — both proxy-blocked here):**
- `div_le_div_iff` current name (L103/380/525): `div_le_div_iff_of_pos` is also
  unknown; try `div_le_div_iff₀` / `div_le_div_iff_left|right` — confirm via
  loogle on `_ / _ ≤ _ / _ ↔ _`.

**BLOCKED residual (~25 errors — need interactive goal states):**
- `rewrite failed: pattern not found` ×11 (L150,158,228,265,269,295,305,339,
  473,503,562) — lemma statements changed under the renames / new Mathlib;
- `unsolved goals` ×6 (L88,303,327,369,376,490) + `No goals` (L96) — nlinarith/
  field_simp proofs need re-tuning for the new normal forms;
- `Application type mismatch` ×2 (L63,581).

These need lean-lsp `lean_goal`/`lean_multi_attempt` per proof, which this sandbox
denies (leansearch/loogle/doi/crossref/arxiv all return proxy 403; only package
registries allowlisted). **QHookBound is an ORPHAN (latent-red, not a lake-build
breaker)** — safe to leave until a session with lean-lsp + web can finish it.

## RESOLVED 2026-06-24 (#bwkg branch claude/bwkg-fix-broken-lean-2026-06-24)

All 3 files green sorry-free (lean-direct vs restored v4.24.0 oleans, exit 0):
- ✅ CategoricalDqSquared — already green on main (#2663)
- ✅ MarkovPeel — already green on main (#2663)
- ✅ QHookBound — **fixed this session**. lean-lsp was disconnected (loogle/leansearch
  web-403), so the residual 20 proof-repairs were closed using lean-direct's own
  goal-state output + Mathlib **source** grep (replaces loogle). Two commits:
  - ed30748c: Mathlib-API renames (50→20)
  - 233d52e1: 20 residual proof-repairs → 0 errors. Key root cause was
    field_simp leaving (q²-1)⁻¹ uncleared on the /(q-q⁻¹) forms; fixed by
    div_eq_iff/div_add'+congr-1 restructure. Plus Bernoulli -2≤a signature,
    q<2-vs-3/2 bracket bug, nat-cast/mod_cast, maxHeartbeats.

Awaiting PR review + merge; close after merge (human verifies).



[2026-06-26 VERIFICATION — premise STALE] All 3 'deep-broken' files actually compile clean, lean-direct EXIT=0, sorry-free (against lake-cache/qou-v4-24-0 oleans; LEAN_PATH = package build/lib/lean dirs):
- CategoricalDqSquared.lean — EXIT=0 (deps Basic/Glossary/CategoricalFoundations/Structures/Instanton all built; Instanton already carries the identical proof under categorical_dq_squared_classical_limit, 0 sorry).
- Interactions/MarkovPeel.lean — EXIT=0; the '1 sorry' was a COMMENT match (line 28), no real sorry.
- Archimedean/QHookBound.lean — EXIT=0; had 3 harmless unused-variable lint warnings (lines 45/638/639) → CLEANED (_hq/_hdq prefixes; qDim_geq_dim has no callers), now 0 warnings.
None are broken. Recommend CLOSING bwkg (premise no longer holds; files were repaired upstream and the bean wasn't updated). PR: lint cleanup + this note. [Agent does not self-close per AGENTS.md §4a — owner closes.]
