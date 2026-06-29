import QOU.BraidKnot.Specht
import Mathlib.LinearAlgebra.SesquilinearForm.Basic
import Mathlib.Algebra.Algebra.Bilinear

/-!
# QOU.BraidKnot.SpechtIrreducible — reduction of `specht_isSimple` to two named cores

Reduces the brick-2 irreducibility obligation `QOU.BraidKnot.Specht.specht_isSimple`
to its two genuine deep cores via the **`M^μ` bilinear form** (James's submodule
theorem).

It builds the `S_n`-invariant symmetric bilinear form `⟨f, g⟩ = Σ_d f d · g d` on
`M^μ` (tabloids orthonormal) **sorry-free**, states the two cores as honest stubs,
and derives `specht_isSimple` **sorry-free** from them.

## sorry-free ↔ stubbed map

| Declaration | Status |
|---|---|
| `bilinM` (+ `_apply`, `_single_single` orthonormality, `_eq_flip`, `_symm`, `_isSymm`) | **sorry-free** |
| `bilinM_rep_invariant` (`S_n`-invariance) | **sorry-free** |
| `spechtPerp`, `mem_spechtPerp_iff` | **sorry-free** |
| `specht_submodule_dichotomy` (James §8) | **STUB** `sorry` — `-- Ref: [james1984representation]` |
| `specht_form_nondegenerate` (char-0 Gram) | **STUB** `sorry` — `-- Ref: [sagan2001]` §2.4 |
| `specht_isSimple` (the reduction) | **sorry-free MODULO the two cores** |

`#print axioms` confirms `sorryAx` enters `specht_isSimple` *only* through the two
cores; the entire invariant-form layer is `[propext, Classical.choice, Quot.sound]`.

The form lives over a generic `[CommRing k]` (§7c clean — no `ℝ`, no ordering, no
`Real.*`); only the two cores and the final theorem add `[Field k]` (submodule
lattice) and `[CharZero k]` (non-degeneracy of the Gram form).

This module carries 2 honest `sorry` targets, so — like brick 2 itself — it is
intentionally **not** imported by the `QOU.BraidKnot` umbrella. It reproduces the
brick-2 `specht_isSimple` statement as a separate, reduction-bearing theorem (brick 2
cannot import this file — the standard one-way dependency).

## References
- [james1984representation] James & Kerber, *The Representation Theory of the Symmetric
  Group* — the submodule theorem (§8) and the Gram form.
- [sagan2001] Sagan, *The Symmetric Group*, §2.4 — irreducibility of `S^μ` and the
  bilinear form.
-/

open QOU.BraidKnot.Specht

namespace QOU.BraidKnot.SpechtIrreducible

variable {k : Type} [CommRing k]

/-! ## 1. The `M^μ` bilinear form (tabloids orthonormal) -/

/-- The **standard symmetric bilinear form** on `M^μ` for which the tabloid basis
is orthonormal: `⟨f, g⟩ = Σ_d (f d) · (g d)`.  Built `sorry`-free as
`Finsupp.lsum`, hence bilinear by construction. -/
noncomputable def bilinM (μ : YoungDiagram) :
    Mtab (k := k) μ →ₗ[k] Mtab (k := k) μ →ₗ[k] k :=
  Finsupp.lsum k
    (fun d => LinearMap.smulRight (LinearMap.id : k →ₗ[k] k)
        ((Finsupp.lapply d : Mtab (k := k) μ →ₗ[k] k)))

/-- Evaluation of the form: `⟨f, g⟩ = Σ_{d ∈ supp f} f d · g d`. -/
theorem bilinM_apply (μ : YoungDiagram) (f g : Mtab (k := k) μ) :
    bilinM (k := k) μ f g = f.sum (fun d c => c * g d) := by
  unfold bilinM
  rw [Finsupp.lsum_apply, LinearMap.finsupp_sum_apply]
  apply Finsupp.sum_congr
  intro d _
  simp only [LinearMap.smulRight_apply, LinearMap.id_coe, id_eq, LinearMap.smul_apply,
    Finsupp.lapply_apply, smul_eq_mul]

/-- **Basis orthonormality.** `⟨⟦d⟧, ⟦e⟧⟩ = δ_{d,e}`: the tabloid basis is
orthonormal for the form. -/
@[simp] theorem bilinM_single_single (μ : YoungDiagram) (d e : Tabloid μ) (a b : k) :
    bilinM (k := k) μ (Finsupp.single d a) (Finsupp.single e b)
      = if d = e then a * b else 0 := by
  rw [bilinM_apply, Finsupp.sum_single_index (by simp)]
  rw [Finsupp.single_apply]
  by_cases h : d = e
  · simp [h]
  · rw [if_neg h, if_neg (Ne.symm h), mul_zero]

/-- The form equals its flip — the bilinear-map form of symmetry.  Proved by
reducing to basis pairs via `Finsupp.lhom_ext` and `mul_comm`. -/
theorem bilinM_eq_flip (μ : YoungDiagram) :
    bilinM (k := k) μ = (bilinM (k := k) μ).flip := by
  refine Finsupp.lhom_ext (fun d a => ?_)
  refine Finsupp.lhom_ext (fun e b => ?_)
  rw [LinearMap.flip_apply, bilinM_single_single, bilinM_single_single]
  by_cases h : d = e
  · simp [h, mul_comm]
  · rw [if_neg h, if_neg (Ne.symm h)]

/-- The form is **symmetric**: `⟨f, g⟩ = ⟨g, f⟩`. -/
theorem bilinM_symm (μ : YoungDiagram) (f g : Mtab (k := k) μ) :
    bilinM (k := k) μ f g = bilinM (k := k) μ g f := by
  conv_lhs => rw [bilinM_eq_flip]
  rw [LinearMap.flip_apply]

/-- `IsSymm` packaging of `bilinM_symm` (so the orthogonal complement is
reflexive — needed to commute orthogonality). -/
theorem bilinM_isSymm (μ : YoungDiagram) : (bilinM (k := k) μ).IsSymm :=
  (LinearMap.isSymm_iff_eq_flip).mpr (bilinM_eq_flip (k := k) μ)

/-! ## 2. `S_n`-invariance of the form -/

/-- **`S_n`-invariance.** The representation `Mtab.rep` preserves the form:
`⟨rep σ f, rep σ g⟩ = ⟨f, g⟩`.  (The action permutes the orthonormal tabloid
basis.) -/
@[simp] theorem bilinM_rep_invariant (μ : YoungDiagram) (σ : Equiv.Perm (Fin (nOf μ)))
    (f g : Mtab (k := k) μ) :
    bilinM (k := k) μ (Mtab.rep μ σ f) (Mtab.rep μ σ g) = bilinM (k := k) μ f g := by
  -- Reduce to basis pairs via a bilinear ext.  Define the two bilinear maps
  --   L := (f g) ↦ ⟨rep σ f, rep σ g⟩  and  R := bilinM, and show L = R on `single`s.
  have key :
      (bilinM (k := k) μ).compl₁₂ (Mtab.rep μ σ) (Mtab.rep μ σ) = bilinM (k := k) μ := by
    refine Finsupp.lhom_ext (fun d a => ?_)
    refine Finsupp.lhom_ext (fun e b => ?_)
    rw [LinearMap.compl₁₂_apply, Mtab.rep_single, Mtab.rep_single,
      bilinM_single_single, bilinM_single_single]
    -- σ • d = σ • e ↔ d = e (the action is by a bijection)
    have : (σ • d = σ • e) ↔ (d = e) := by
      constructor
      · intro h; exact (MulAction.injective σ) h
      · intro h; rw [h]
    by_cases h : d = e
    · simp [h]
    · rw [if_neg h, if_neg (by rwa [this])]
  have := LinearMap.congr_fun (LinearMap.congr_fun key f) g
  rwa [LinearMap.compl₁₂_apply] at this

/-! ## 3. The Specht orthogonal complement -/

/-- The form-orthogonal complement `(S^μ)ᗮ` of the Specht module inside `M^μ`. -/
noncomputable def spechtPerp (μ : YoungDiagram) : Submodule k (Mtab (k := k) μ) :=
  Submodule.orthogonalBilin (SpechtSubmodule (k := k) μ) (bilinM (k := k) μ)

theorem mem_spechtPerp_iff (μ : YoungDiagram) (x : Mtab (k := k) μ) :
    x ∈ spechtPerp (k := k) μ ↔
      ∀ y ∈ SpechtSubmodule (k := k) μ, bilinM (k := k) μ y x = 0 := by
  unfold spechtPerp
  rw [Submodule.mem_orthogonalBilin_iff]
  rfl

/-! ## 4. The two deep cores (stated, `sorry` + `-- Ref:`) -/

/-- **Core 1 — James's submodule theorem (the dichotomy).** For any `S_n`-stable
`k`-submodule `U ≤ M^μ`, either `S^μ ≤ U` or `U ≤ (S^μ)ᗮ`.  This is the heart of
the classical irreducibility proof (James, *Representation Theory of the
Symmetric Groups*, §8): if `U` is not contained in the orthogonal complement of
`S^μ`, then some polytabloid is "seen" by `U`, and the column-antisymmetrizer
forces all of `S^μ` into `U`. -/
theorem specht_submodule_dichotomy {k : Type} [Field k] (μ : YoungDiagram)
    (U : Submodule k (Mtab (k := k) μ))
    (hU : ∀ σ : Equiv.Perm (Fin (nOf μ)), ∀ x ∈ U, Mtab.rep μ σ x ∈ U) :
    SpechtSubmodule (k := k) μ ≤ U ∨ U ≤ spechtPerp (k := k) μ := by
  -- Ref: [james1984representation] §8 (the submodule theorem: for any U ≤ M^μ,
  -- either S^μ ≤ U or U ≤ (S^μ)ᗮ).  Column-antisymmetrizer / Garnir argument.
  sorry

/-- **Core 2 — non-degeneracy of the form on `S^μ` (char 0).** Over a field of
characteristic zero the Gram matrix of the form restricted to `S^μ` is nonzero
(its determinant is the James–Specht Gram determinant, a product of hook lengths
which is invertible in char 0), so `S^μ ⊓ (S^μ)ᗮ = ⊥`. -/
theorem specht_form_nondegenerate {k : Type} [Field k] [CharZero k] (μ : YoungDiagram)
    (hμ : μ.card ≠ 0) :
    SpechtSubmodule (k := k) μ ⊓ spechtPerp (k := k) μ = ⊥ := by
  -- Ref: [sagan2001] §2.4 / [james1984representation] (the Gram determinant of the
  -- bilinear form on S^μ is nonzero in characteristic 0 — a product of hook
  -- lengths; equivalently S^μ ⊄ (S^μ)ᗮ, i.e. the form is non-degenerate on S^μ).
  sorry

/-! ## 5. The reduction: `specht_isSimple` from the two cores -/

/-- **Irreducibility of `S^μ` (char 0)** — reduced `sorry`-free to the two cores
above.  Reproduces the brick-2 statement
`QOU.BraidKnot.Specht.specht_isSimple` verbatim. -/
theorem specht_isSimple {k : Type} [Field k] [CharZero k] (μ : YoungDiagram)
    (hμ : μ.card ≠ 0) :
    ∀ N : Submodule k (Mtab (k := k) μ),
      N ≤ SpechtSubmodule (k := k) μ →
      (∀ σ : Equiv.Perm (Fin (nOf μ)), ∀ x ∈ N, Mtab.rep μ σ x ∈ N) →
      N = ⊥ ∨ N = SpechtSubmodule (k := k) μ := by
  intro N hN_le hN_stable
  rcases specht_submodule_dichotomy (k := k) μ N hN_stable with hsub | hperp
  · -- S^μ ≤ N and N ≤ S^μ  ⇒  N = S^μ
    exact Or.inr (le_antisymm hN_le hsub)
  · -- N ≤ S^μ and N ≤ (S^μ)ᗮ  ⇒  N ≤ S^μ ⊓ (S^μ)ᗮ = ⊥  ⇒  N = ⊥
    left
    rw [eq_bot_iff, ← specht_form_nondegenerate (k := k) μ hμ]
    exact le_inf hN_le hperp

end QOU.BraidKnot.SpechtIrreducible
