# Mathlib upstream package: semisimplicity of matrix rings and endomorphism rings

Date: 2026-07-19.  Sources on `main`:

- [`QOU/MathlibExt/MatrixSemisimple.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/MatrixSemisimple.lean)
  — `IsSemisimpleRing (Matrix n n K)` for `K` a `DivisionRing`, **all** index types (empty case included), sorry-free.
- [`QOU/MathlibExt/EndSemisimple.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/EndSemisimple.lean)
  — `IsSemisimpleRing (Module.End K V)` for `K` a `Field`, `V` finite-dimensional, sorry-free
  (transfer of the matrix result along `algEquivMatrix` on a chosen basis).

These fill, **in special cases**, two `proof_wanted` declarations in the *pinned* Mathlib
(commit `f897ebcf72cd`, 2025-10-14, toolchain v4.24.0), `Mathlib/RingTheory/SimpleModule/Basic.lean:454-460`:

```lean
proof_wanted IsSemisimpleRing.module_end [IsSemisimpleModule R M] [Module.Finite R M] :
    IsSemisimpleRing (Module.End R M)

proof_wanted IsSemisimpleRing.matrix [Fintype ι] [DecidableEq ι] [IsSemisimpleRing R] :
    IsSemisimpleRing (Matrix ι ι R)
```

## ⛔ STATUS: SUPERSEDED ON MATHLIB MASTER — DO NOT SUBMIT AS-IS

Checked against `leanprover-community/mathlib4` **master** on 2026-07-19 (WebFetch of the raw
files + GitHub code search). All four `proof_wanted`s in that block (`mulOpposite`,
`module_end`, `matrix`, `isSemisimpleRing_iff_pi_matrix_divisionRing`) have been **removed from
`Basic.lean` and proved in full generality** in
`Mathlib/RingTheory/SimpleModule/Basic.lean` → `Mathlib/RingTheory/SimpleModule/WedderburnArtin.lean`
(Authors: Junyan Xu):

```lean
instance (n) [Fintype n] [DecidableEq n] : IsSemisimpleRing (Matrix n n R)   -- R semisimple
theorem _root_.IsSemisimpleRing.moduleEnd : IsSemisimpleRing (Module.End R M) -- M finite semisimple
instance : IsSemisimpleRing Rᵐᵒᵖ
theorem isSemisimpleRing_mulOpposite_iff : IsSemisimpleRing Rᵐᵒᵖ ↔ IsSemisimpleRing R
theorem isSemisimpleRing_iff_pi_matrix_divisionRing : …  -- Artin–Wedderburn existence, both directions
```

Master's proofs go through the Artin–Wedderburn machinery
(`exists_ringEquiv_pi_matrix_divisionRing`, `Matrix.piRingEquiv`, `RingEquiv.mapMatrix`,
`Matrix.compRingEquiv`) and cover the **general** cases our files honestly declined
(arbitrary semisimple `R`; finite semisimple `M` over any ring — exactly the isotypic
decomposition / Morita-theoretic content our scope notes flagged as missing). Note master
renamed `module_end` → `moduleEnd` and made the matrix case an anonymous `instance`.

**Consequences for this repo (recommended follow-ups, not part of this package):**

1. **No Mathlib PR should be opened for these two results.** The upstream gap is closed,
   more generally than our versions.
2. **Residual upstream angle (weak, likely rejected):** our matrix proof is *elementary and
   import-light* — column decomposition of the regular module, no Artin–Wedderburn — and could
   in principle live in `Basic.lean` (needing only `Mathlib.Data.Matrix.Action`), far below
   `WedderburnArtin.lean` in the import graph. Mathlib would take this only if some file below
   `WedderburnArtin` actually needs the instance; absent a concrete consumer, a duplicate
   (Prop-class, so no diamond, but still redundant) instance will be declined. Ask on Zulip
   before drafting anything.
3. **On the next Mathlib bump past the landing commit**, `QOU/MathlibExt/MatrixSemisimple.lean`
   and `EndSemisimple.lean` become redundant with upstream instances: deprecate the QOU
   declarations in favour of the upstream ones (the anonymous matrix instance and
   `IsSemisimpleRing.moduleEnd`) and keep only whatever helper lemmas
   (`Matrix.exists_smul_eq`-style transitivity, `columnsEquiv`) are still consumed.

The remainder of this document is the package **as it would have been** against the pinned
Mathlib — kept as the record for the bump/deprecation work and for the (unlikely)
import-lightening pitch.

## Upstream-adapted code (historical / contingency)

Target file: `Mathlib/RingTheory/SimpleModule/Basic.lean` (pinned layout). Import delta:
add `Mathlib.Data.Matrix.Action` (provides `Module (Matrix n n R) (n → R)` via `mulVec`;
itself only needs `Data.Matrix.Mul` — already imported — plus `Algebra.Ring.Opposite`, so the
import cost is negligible). Drop QOU's `import Mathlib.Tactic` (the proofs use only
`simp`/`rw`/`funext`/`Finset.sum_eq_single`, all available here). The `.symm.isSemisimpleRing`
transfer uses `RingEquiv.isSemisimpleRing` (already in `Basic.lean:72`).

Naming (Mathlib conventions): the division-ring result **cannot** keep the name
`IsSemisimpleRing.matrix` because it does not have the `proof_wanted`'s signature
(`[DivisionRing K]` is *not* an instance of `[IsSemisimpleRing K]` syntactically, though it
implies it); options were (a) replace the `proof_wanted` and *strengthen* nothing — keep the
`proof_wanted` for general `R` and add the division-ring case as an anonymous
`instance` in the `Matrix` namespace, or (b) name it `Matrix.isSemisimpleRing` as a theorem.
Master's precedent settles it: **anonymous `instance`**. `IsSemisimpleRing` is a `Prop`
class, so instance duplication is harmless (no diamonds) and inference-cheap.

```lean
/-  (New copyright joins the existing header of Basic.lean; if split into a new file:)
Copyright (c) 2026 <Author>. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: <Author>
-/

namespace Matrix

variable {n : Type*} [Fintype n] [DecidableEq n] {K : Type*} [DivisionRing K]

/-- Over a division ring, the `Matrix.mulVec` action reaches any vector from any
nonzero vector: witnessed by the matrix `fun a b => if b = i then w a * (v i)⁻¹ else 0`
for any coordinate `i` with `v i ≠ 0`. -/
theorem exists_smul_eq {v : n → K} (hv : v ≠ 0) (w : n → K) :
    ∃ A : Matrix n n K, A • v = w := by
  obtain ⟨i, hi⟩ : ∃ i, v i ≠ 0 := Function.ne_iff.mp hv
  refine ⟨.of fun a b => if b = i then w a * (v i)⁻¹ else 0, funext fun a => ?_⟩
  simp only [smul_eq_mulVec, mulVec, dotProduct, of_apply]
  rw [Finset.sum_eq_single i (fun b _ hb => by rw [if_neg hb, zero_mul])
    (fun h => absurd (Finset.mem_univ i) h)]
  rw [if_pos rfl, mul_assoc, inv_mul_cancel₀ hi, mul_one]

/-- The column module `n → K` is a simple `Matrix n n K`-module (nonempty `n`). -/
instance [Nonempty n] : IsSimpleModule (Matrix n n K) (n → K) where
  exists_pair_ne := ⟨⊥, ⊤, fun h => one_ne_zero (K := K) <| by
    simpa using (h ▸ Submodule.mem_top (x := fun _ : n => (1 : K)) :
      (fun _ => (1 : K)) ∈ (⊥ : Submodule (Matrix n n K) (n → K)))⟩
  eq_bot_or_eq_top N := or_iff_not_imp_left.mpr fun hN => by
    obtain ⟨v, hvN, hv⟩ := (Submodule.ne_bot_iff N).mp hN
    exact Submodule.eq_top_iff'.mpr fun w =>
      have ⟨A, hA⟩ := exists_smul_eq hv w; hA ▸ N.smul_mem A hvN

/-- The matrix ring as a left module over itself is the product of its columns. -/
@[simps] def columnsEquiv : Matrix n n K ≃ₗ[Matrix n n K] (n → n → K) where
  toFun A j i := A i j
  invFun c := .of fun i j => c j i
  map_add' _ _ := rfl
  map_smul' B A := funext₂ fun j i => by
    show (B * A) i j = (B • fun i => A i j) i
    simp only [smul_eq_mulVec, mul_apply, mulVec, dotProduct]

/-- Matrix rings over a division ring are semisimple (any index type). -/
instance : IsSemisimpleRing (Matrix n n K) := by
  cases isEmpty_or_nonempty n
  · exact (sSup_simples_eq_top_iff_isSemisimpleModule).mp (Subsingleton.elim _ _)
  · exact (IsSemisimpleModule.congr columnsEquiv.symm : _)  -- Pi of simples is semisimple

end Matrix

/-- Endomorphism rings of finite-dimensional vector spaces are semisimple. -/
instance Module.End.isSemisimpleRing (K V : Type*) [Field K] [AddCommGroup V]
    [Module K V] [Module.Finite K V] : IsSemisimpleRing (Module.End K V) := by
  classical
  exact ((algEquivMatrix (Module.Free.chooseBasis K V)).toRingEquiv).symm.isSemisimpleRing
```

Placement notes: the `End` instance needs `algEquivMatrix`
(`Mathlib.LinearAlgebra.Matrix.ToLin`), which `Basic.lean` does not import — it would have to
go in a downstream file (e.g. `LinearAlgebra/Matrix/ToLin.lean` or a new
`RingTheory/SimpleModule/End.lean`). The nonempty-index assembly abbreviates QOU's explicit
`sSup_simples_eq_top` Pi argument; the fully spelled version is in the QOU source. The two
`proof_wanted` lines would have been **kept** (general `R` still open at the pin), with the
division-ring instances added beside them — replacing/weakening the `proof_wanted` statements
themselves would misrepresent what was proved.

## Draft PR (historical — do not submit; superseded by Junyan Xu's WedderburnArtin work)

**Title:** `feat(RingTheory/SimpleModule): matrix rings over a division ring and End of a f.d. vector space are semisimple`

**Body:**

> Adds two instances toward the `proof_wanted`s `IsSemisimpleRing.matrix` and
> `IsSemisimpleRing.module_end`:
>
> * `Matrix`: for `K` a `DivisionRing` and any `Fintype` index, `IsSemisimpleRing (Matrix n n K)`.
>   Proof: the column module `n → K` (module structure from `Mathlib.Data.Matrix.Action`) is
>   simple by explicit transitivity of `mulVec`; the regular module decomposes
>   `Matrix`-linearly into columns, so it is a finite product of simples.
>   Elementary — no Artin–Wedderburn input.
> * `Module.End`: for `K` a `Field` and `V` finite-dimensional, `IsSemisimpleRing (Module.End K V)`,
>   by transporting the matrix instance along `algEquivMatrix` on a chosen basis.
>
> The general statements (arbitrary semisimple `R`; finite semisimple `M` over any ring)
> need the isotypic decomposition / Morita theory and remain `proof_wanted`.

## Submission checklist (retained as template; item 0 already fired)

- [x] **0. Verify the `proof_wanted` still exists on current master.** ❌ It does not —
  closed in full generality in `RingTheory/SimpleModule/WedderburnArtin.lean` (Junyan Xu).
  **Package halted here.** Everything below is template for a future package.
- [ ] Naming lint: `#lint` clean; instance names auto-generated or `Namespace.isFoo` per
  convention; no `QOU`/project namespaces; theorem names snake_case, defs lowerCamel.
- [ ] Docstrings: full sentences, `/-- … -/` on every public decl, no status/process language
  ("sorry-free", bean IDs, "Route:") — strip all QOU tracking prose.
- [ ] No `#align` (post-port Mathlib is `#align`-free); no `set_option` leftovers;
  `import Mathlib.Tactic` replaced by the minimal specific imports.
- [ ] Deprecations: none needed (purely additive) — confirm nothing existing is shadowed
  (`Matrix.exists_smul_eq` name-check against master before claiming it).
- [ ] Remove/keep the `proof_wanted` lines coherently and check the file (and
  `Mathlib.lean` roots) still compiles: `lake build Mathlib.RingTheory.SimpleModule.Basic`
  plus downstream users (`WedderburnArtin`, `Maschke`, `FiniteLength`).
- [ ] Instance vs theorem: `IsSemisimpleRing` is Prop-valued — instance is appropriate and
  master's precedent for the matrix case confirms it; note master made `moduleEnd` a
  *theorem* (its `[IsSemisimpleModule R M] [Module.Finite R M]` hypotheses make instance
  search expensive/loopy) — mirror that choice for any End-variant.
- [ ] Universes: single-universe statements, no universe-carrying structure fields — no
  pinning needed (`Matrix n n K` and `n → K` live in `max` of the binders automatically).
- [ ] Zulip: post in `#mathlib4 > RingTheory` (or `#maths`) *before* opening the PR,
  linking the `proof_wanted` and asking about placement + whether work is in flight —
  precisely the step that would have caught the supersession months earlier.
