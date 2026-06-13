# `conj-canonical-knot-id-sdp.lean` — red-file repair (COMPLETED)

**Date:** 2026-06-13 · **Branch:** `claude/vigilant-cerf-f80u04` · **PR #2249**
**Status:** ✅ fully repaired — the file now elaborates **green** (direct-`lean`,
EXIT 0, no errors / sorries / warnings).

## Summary

The "red conj Lean file"
`content/quantum-observable-universe/mass-theory/conj-canonical-knot-id-sdp.lean`
had **never compiled** — it carried **eight distinct bugs across six classes**.
It is a content-*sibling* `.lean` (its `lean.ref`,
`QOU.BraidKnot.helium3_uniqueness_closed`, resolves to a *different* lib
module; the sibling itself is **not** in the root Lake workspace's `lake build`
targets), so CI never elaborated it and the heuristic `proof-lean-compiles` QA
checker marked it `pass` while it was in fact deeply broken.

All bugs are now fixed (owner-approved deep repair, 2026-06-13). Because the
sibling is not CI-gated and `lake exe cache get` is 403-blocked in this
environment, verification was done with **direct `lean` + a manual `LEAN_PATH`**
(root-tree cache Mathlib + the QOU lib oleans, per `lean-environment-setup.md
§327`) — the canonical workaround for this sandbox.

## The bugs and their fixes

| # | Class | Fix | Confirmed by |
|---|---|---|---|
| 1 | `structure StrictComplementarity … : Prop` holding ℝ data fields | drop `: Prop` → `Type` structure (matches `StrictComplementarityPair` in `MathlibExt/SDP.lean`) | a `Prop` structure can't generate data projections, and `obtain ⟨…⟩ := sc` can't eliminate a non-subsingleton `Prop` into the `Type`-valued `CanonicalKnotIdSDP` goal — minimal core repro |
| 2 | orphaned `/-- … -/` doc comment (followed by `/-!`, not a decl) | `/--` → `/-!` | parse error `unexpected '/-!'; expected 'lemma'` |
| 3 | `(10⁻⁶ : ℝ)` (superscript not a valid numeral) | `(1e-6 : ℝ)` | parse error `unexpected token '⁶'` |
| 4 | instances reference the `bindingKWord` field by **bare name** inside the `where`-block (out of scope) | use the literal `([3, 3] : BraidWord)` | `unknown identifier bindingKWord` — minimal repro (later `where` fields can't see earlier ones) |
| 5 | BraidWord predicates via **dot-notation** on `abbrev BraidWord := List Int` → unfolds to `List.*` (not found); also *inside* `structurallyValidBinding`'s body | explicit `BraidWord.f x` application (~29 sites) | `Invalid field … List.structurallyValidBinding` — minimal repro |
| 6 | `by decide` can't see through the `def`-wrapped predicates | mark the 4 predicates `@[reducible]` | `failed to synthesize Decidable` — minimal repro |
| 7 | `bindingKWord_nonempty` proved by `cases n <;> decide` over a goal with the free instance var `h` | `h.bindingKStructurallyValid.1` (the `w ≠ []` conjunct — holds for ANY instance, not just the registered three) | `Expected type must not contain free variables` |
| 8 | three `*_canonical_uniqueness_*` declared `theorem` but with conclusion `CanonicalKnotIdSDP …` (a class / `Type`, not `Prop`) | `theorem` → `def` (they construct an instance, i.e. data) | `type of theorem … is not a proposition` |

Bugs 1-3 are parse-level (commits `a11107d9`, `d59d4e07`); bugs 4-8 are the deep
semantic repair (commit `b8f91a02`). Each mechanism was confirmed with a minimal
core-Lean repro before the fix.

## Verification

```bash
ROOT=/home/user/qou; cd "$ROOT/content/quantum-observable-universe/lean"
LP="$ROOT/content/quantum-observable-universe/lean/.lake/build/lib/lean"
for d in "$ROOT"/.lake/packages/*/.lake/build/lib/lean; do LP="$LP:$d"; done   # root-tree cache Mathlib
ELAN_TOOLCHAIN=lean-v4.24.0 LEAN_PATH="$LP" lean ../mass-theory/conj-canonical-knot-id-sdp.lean
# EXIT 0 — no errors/sorries/warnings
```
`CanonicalKnotIdSDPUniqueness.olean` is rebuilt once with `lean -o` (the cache
omits it — added after the cache seed). Only the **root-tree** cache Mathlib is
on `LEAN_PATH`; the lean-package lake-built Mathlib is excluded (incomplete, and
mixing two Mathlib builds causes spurious `failed to synthesize` — skill §322).

## Note for future Lean maintenance

The pervasive bug-5 (dot-notation on `abbrev … := List Int`) is a standing
hazard: any `BraidWord.f` predicate must be called as `BraidWord.f w`, never
`w.f`. If a future change wants `w.f` to work, make `BraidWord` a one-field
structure (`structure BraidWord where word : List Int`) — but that costs `.word`
everywhere List ops are used. The current explicit-application convention is the
lower-churn choice.

## Cross-refs

- The conj's uniqueness leg (Task 3): `docs/audits/2026-06-13-strict-complementarity-sdp-uniqueness-attempt.md`.
- The L>2 binding-K enumeration (Task 2, honest negative): same PR, `binding-k-enumerator.witness.json` + `binding_k_enumerator.py --tritium-L 3 --he3-L 3`.
