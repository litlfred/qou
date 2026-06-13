# `conj-canonical-knot-id-sdp.lean` — red-file repair status + follow-up recipe

**Date:** 2026-06-13 · **Branch:** `claude/vigilant-cerf-f80u04` · **PR #2249**

## Summary

The "red conj Lean file" `content/quantum-observable-universe/mass-theory/conj-canonical-knot-id-sdp.lean`
had **never compiled** — it carries **five distinct bug classes**. It is a
content-*sibling* `.lean` (its decl `QOU.BraidKnot.helium3_uniqueness_closed`
resolves to a *different* lib module; the sibling itself is **not** in the root
Lake workspace's `lake build` targets), so CI never elaborated it and the
heuristic `proof-lean-compiles` QA checker marked it `pass` while it was in
fact deeply broken.

**Three parse-level classes are fixed this PR (the file now parses);** the
remaining two-to-three are a mechanical but large (~29-site) re-implementation,
**deferred** (owner decision 2026-06-13) to a session with a clean Mathlib
toolchain where green can be machine-confirmed.

## The five bug classes

| # | Class | Status | Mechanism (all confirmed with minimal core-Lean repros) |
|---|---|---|---|
| 1 | `structure StrictComplementarity … : Prop` holding ℝ data fields (`min_block_eig`, …) | **fixed** | a `Prop` structure can't generate data projections, and `obtain ⟨…⟩ := sc` can't eliminate a non-subsingleton `Prop` into the `Type`-valued `CanonicalKnotIdSDP` goal. Fix: drop `: Prop` → `Type` structure (matches `StrictComplementarityPair` in `MathlibExt/SDP.lean`). |
| 2 | Orphaned `/-- … -/` doc comment (line ~79) followed by `/-!` (not a decl) | **fixed** | a doc comment must attach to a declaration; `/-!` is a command. Fix: `/--` → `/-!`. |
| 3 | `(10⁻⁶ : ℝ)` superscript "literal" (line ~435) | **fixed** | `10⁻⁶` is not a valid Lean numeral (`unexpected token '⁶'`). Fix: `(1e-6 : ℝ)`. |
| 4 | Instances reference the `bindingKWord` field by **bare name** inside the `where`-block | **OPEN** | Lean structure-instance `where` fields cannot reference earlier fields by bare identifier → `unknown identifier bindingKWord`. (Note: the *class* field **types** at the `bindingKStructurallyValid : …` lines *can* depend on the prior `bindingKWord` field — dependent record — so those are only hit by bug #5, not #4.) |
| 5 | BraidWord predicates called via **dot-notation** on the `abbrev BraidWord := List Int` | **OPEN** | dot-notation unfolds the reducible abbrev to `List`, so `x.structurallyValidBinding` seeks `List.structurallyValidBinding` (not found). ~29 call sites of `.structurallyValidBinding` / `.evenPower`. |
| 6 | `by decide` over the `def`-wrapped predicate Props | **OPEN (likely)** | `decide` needs a `Decidable` instance for `structurallyValidBinding …`; instance search will not unfold a plain `def` → `failed to synthesize Decidable`. |

## Follow-up fix recipe (for a clean-Mathlib session)

1. **Bug 5 (dot-notation).** Replace every `‹expr›.structurallyValidBinding`
   with `BraidWord.structurallyValidBinding ‹expr›` and `‹expr›.evenPower`
   with `BraidWord.evenPower ‹expr›`. (`‹expr›.length` is fine — `List.length`
   resolves through the abbrev.) ~29 sites in the class field **types**, the
   3 per-nucleus instances, and the `helium3/deuterium/tritium_…` +
   `helium3_existence_with_witness_rho` theorems.
2. **Bug 4 (field-scope).** In the 3 instances, replace the bare `bindingKWord`
   in the semantic-Prop field definitions (`constituentUniqueness :=`,
   `bindingKPSDFeasible :=`, …) with the instance's literal word
   `([3, 3] : BraidWord)` (all three are `[3,3]`).
3. **Bug 6 (decide).** Mark the four predicate defs `@[reducible]`
   (`BraidWord.allNonZero`, `inInterNucleonRange`, `structurallyValidBinding`,
   `evenPower`) so `decide`'s `Decidable` search unfolds them — or replace the
   `by decide` proofs with `by unfold … <;> decide`.
4. **Verify** with direct `lean` (per `lean-environment-setup.md §322/§327`):
   build `LEAN_PATH` from the **root-tree** cache oleans
   (`$ROOT/.lake/packages/*/.lake/build/lib/lean`) + the QOU lib oleans
   (`content/quantum-observable-universe/lean/.lake/build/lib/lean`), **never**
   the lean-package lake-built Mathlib (incomplete). Build the cache-missing
   `CanonicalKnotIdSDPUniqueness.olean` once with `lean -o`. EXIT 0 = green.

## Verification caveat (this environment)

The Mathlib `lake exe cache get` is 403-blocked here; the cache orphan branch
`lake-cache/qou-v4-24-0` ships ~5920 Mathlib + the QOU oleans but **omits**
`CanonicalKnotIdSDPUniqueness.olean` (added after the cache seed). `lake build`
re-resolves deps and wipes the restored Mathlib (skill §322), so verification
must use **direct `lean` + manual `LEAN_PATH`**. The parse/scope/resolution
error *classes* (bugs 1-6) are reliably checkable this way; a residual
`failed to synthesize` class remains olean-noise (one imported QOU olean —
`HeckeAlgebra.Common` or the freshly-built `CanonicalKnotIdSDPUniqueness` —
is inconsistent with the restored Mathlib) that cannot be cleanly separated
from genuine elaboration errors without a from-source Mathlib build.

## Cross-refs

- Parse-level fixes: commits `a11107d9` (Prop), `d59d4e07` (orphan doc + `1e-6`).
- The conj's uniqueness leg (Task 3): `docs/audits/2026-06-13-strict-complementarity-sdp-uniqueness-attempt.md`.
- The L>2 binding-K enumeration (Task 2, honest negative): same PR, `binding-k-enumerator.witness.json` + `binding_k_enumerator.py --tritium-L 3 --he3-L 3`.
