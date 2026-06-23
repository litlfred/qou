# SDPRankEquality.lean — repaired (was non-building on `main`)

**Date:** 2026-06-23
**Session / PR:** `claude/idle-backlog-drain-2026-06-23` (#2637); bean `8ehe`
**Verification:** lean-direct against restored `lake-cache/qou-v4-24-0` oleans
(2951 Mathlib + QOU deps). Final state **EXIT=0, 0 errors** (2 pre-existing
unused-simp *warnings* on untouched lines remain, out of scope).

> **RESOLVED in #2637.** All six compile errors fixed and lean-direct-verified.
> The correct Mathlib lemma name (no prime) was found via GitHub code-search
> against `leanprover-community/mathlib4` (the Lean LSP / Mathlib source were
> unavailable in-sandbox).

## What was broken

[`QOU/MathlibExt/SDPRankEquality.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/SDPRankEquality.lean)
did **not compile** at `main` (31496f5c) — six errors, three distinct causes.
Its olean was correctly absent from the cache (it failed to build). The honest
placeholder counter reported only `todo:1` because it counts the one literal
`TODO` token; the file actually had six compile errors. (Consistent with the
repo's `continue-on-error` Lean CI: broken decls are tracked, not blocking.)

| Line(s) | Cause | Fix |
|---|---|---|
| 312 | `rw [← Matrix.mulVec_mulVec, …]` wrong direction — here `mulVec_mulVec : A *ᵥ B *ᵥ x = (A * B) *ᵥ x`, so `←` searched for `(M*N) *ᵥ v` (absent). | drop the `←` (forward rewrite). |
| 406 | after `dotProduct_mulVec` the goal carries `v ᵥ* M` (vecMul), so the Hermitian `Mᵀ = M` rewrite found no `Mᵀ`. | prepend `← Matrix.mulVec_transpose, ← Matrix.mulVec_transpose` to convert `v ᵥ* M → Mᵀ *ᵥ v`. |
| 467, 470, 555, 558, 563, 566 | `Matrix.rank_eq_finrank_range_toLin'` is an **unknown constant** (no such name in Mathlib). | **add the missing shim** (below). |
| 440, 499 | "unsolved goals" — downstream of the unknown constant. | cleared once the shim resolves. |

## The shim

Mathlib's `Matrix.rank` is *defined* as `finrank R (range mulVecLin)`, and ships
only the basis-general `Matrix.rank_eq_finrank_range_toLin` (no prime). The
proofs here phrase rank through `range toLin'`, so the standard-basis
specialisation the author assumed is supplied directly:

```lean
theorem Matrix.rank_eq_finrank_range_toLin' {m k : ℕ}
    (M : Matrix (Fin m) (Fin k) ℝ) :
    M.rank = Module.finrank ℝ (LinearMap.range M.toLin') := by
  have hbridge : M.toLin' = M.mulVecLin := by
    ext v i
    simp [Matrix.toLin'_apply]
  rw [hbridge]
  rfl   -- `Matrix.rank` is defeq `finrank ℝ (range mulVecLin)`
```

`toLin' = mulVecLin` (both `v ↦ M *ᵥ v`), so the two ranges coincide; the final
`rfl` discharges the `Matrix.rank` definitional unfold. Declared inside
`namespace QOU.MathlibExt.SDPRankEquality`, so the existing call sites
`Matrix.rank_eq_finrank_range_toLin' M` resolve to it unchanged.

## Net effect

Six errors → zero; `SDPRankEquality` drops out of the QOU `proof-objects.json`
error set. No statement signatures changed — only tactic bodies + one added
helper — so nothing new is axiomatised; the module's two named categorical
axioms (`strict_complementarity_kernel_disjoint`, `affine_slater_rigidity`)
are unchanged.

## Caveat

Verified against the restored `lake-cache/qou-v4-24-0` oleans. The load-bearing
error was an **unknown constant** (version-independent: an absent name is absent
regardless of Mathlib pin), and the shim uses only stable matrix API
(`toLin'_apply`, `mulVecLin`, `rank` def), so a `lake build QOU` against `main`'s
exact Mathlib pin is expected to agree. A CI Lean build will confirm.
