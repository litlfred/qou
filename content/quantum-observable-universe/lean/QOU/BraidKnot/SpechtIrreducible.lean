import QOU.BraidKnot.Specht
import QOU.BraidKnot.SpechtStandardBasis
import QOU.BraidKnot.SpechtDominanceCore
import QOU.BraidKnot.SpechtTriangularCore
import QOU.BraidKnot.SpechtBaseChange
import QOU.MathlibExt.GramNondegenerate
import QOU.MathlibExt.RankMinor
import Mathlib.LinearAlgebra.SesquilinearForm.Basic
import Mathlib.LinearAlgebra.BilinearForm.Orthogonal
import Mathlib.Algebra.Algebra.Bilinear
import Mathlib.Tactic.Group

/-!
# QOU.BraidKnot.SpechtIrreducible — reduction of `specht_isSimple` to two named cores

Reduces the brick-2 irreducibility obligation `QOU.BraidKnot.Specht.specht_isSimple`
to its two genuine deep cores via the **`M^μ` bilinear form** (James's submodule
theorem).

It builds the `S_n`-invariant symmetric bilinear form `⟨f, g⟩ = Σ_d f d · g d` on
`M^μ` (tabloids orthonormal) **sorry-free**, builds the **column antisymmetrizer
`κ_t`** and its structural theory **sorry-free** (§3.5), and thereby *proves*
James's submodule theorem (`specht_submodule_dichotomy`, §4.5) **fully sorry-free**:
the former pure-combinatorial residual `noclash_match_exists` (the Gale–Ryser /
conjugate-partition matching) is now discharged (§4.x) from four elementary
`YoungDiagram` counting helpers.

**The module is now `sorry`-free end to end.**  `specht_form_nondegenerate` —
long the single remaining core — is proved for every characteristic-zero field
(§4.4), so `specht_isSimple` is proved outright.  `#print axioms` reports
`[propext, Classical.choice, Quot.sound]` for both.

The route is *not* the standard-basis theorem.  §4.4 thins the polytabloids over
`ℚ` to an independent sub-family that still spans, observes that their
coordinate matrix `Mz` is an **integer** matrix, and pushes `det (Mz Mzᵀ) ≠ 0`
into `k` by Cauchy–Binet: the Gram determinant is a sum of squares of minors, so
positivity is an assertion about `ℤ` and never about `k`.  The sub-family comes
from generic linear algebra (`exists_linearIndepOn_extension`), so **no Garnir
straightening, no dominance core, and no standard tableau appears anywhere in
the proof** — the argument does not know what a standard tableau is.

(Those cores are in fact themselves proved — `standardBasis`,
`standardPolytabloid_span` and `specht_finrank_eq_numSYT` in
`SpechtStandardBasis` all report `[propext, Classical.choice, Quot.sound]`, and
the "STUB" rows in that module's docstring table are stale as of 2026-08-08.
Independence from them is a robustness property of this proof, not a way around
an open problem.)

§4.3-bis remains as the ordered-field Stage 1 (positive definiteness over `ℚ`,
`ℝ`) feeding `specht_isSimple_ordered`; it is now a lighter special case rather
than the only complete story.

The column-clash lemma `kap_of_mem_line` (`κ_t {s} ∈ span {e_t}`) is now **fully
sorry-free**: its two legs — the clash cancellation (`kap_of_mem_line_clash`, a
sign-reversing involution ⇒ `κ_t{s} = 0`) and the no-clash reindexing
(`kap_of_mem_line_match`, `{π₀•s} = {t}` for `π₀ ∈ C_t` ⇒ `κ_t{s} = sgn(π₀)·e_t`)
— are both sorry-free, and the matching existence `noclash_match_exists` they
consume is now proved (§4.x), so the lemma carries no residual `sorry`.

## sorry-free ↔ stubbed map

| Declaration | Status |
|---|---|
| `bilinM` (+ `_apply`, `_single_single` orthonormality, `_eq_flip`, `_symm`, `_isSymm`) | **sorry-free** |
| `bilinM_rep_invariant` (`S_n`-invariance) | **sorry-free** |
| `spechtPerp`, `mem_spechtPerp_iff` | **sorry-free** |
| `kapL` (+ `_apply`, `_of`, `_of_self`, `_mem_U`, `_selfadjoint`) — the `κ_t` operator | **sorry-free** |
| `bilinM_zsmul_left/right`, `bilinM_rep_swap`, `rep_mul_apply` | **sorry-free** |
| `conjEquiv`, `sign_conj`, `polytabloid_rep_equivariant`, `tableau_transitive` | **sorry-free** |
| `mtab_of_congr`, `kap_of_mem_line_clash` (clash ⇒ `κ_t{s}=0`), `kap_of_mem_line_match` (no-clash ⇒ `±e_t`) | **sorry-free** |
| `filterCard_reindex`, `colCells_card`, `Col_card`, `row_lt_colLen` (§4.x counting helpers) | **sorry-free** — public, consumed by `SpechtCrossDominance` |
| `noclash_match_exists` (Gale–Ryser / conjugate-partition matching) | **sorry-free** (was: full stub) |
| `kap_of_mem_line` (column-clash lemma) | **sorry-free** (was: full stub) |
| `kapL_mem_line` (from the core) | **sorry-free** |
| `specht_submodule_dichotomy` (James §8) | **sorry-free** (was: full stub) |
| `bilinM_self_eq_zero_iff` (positive definiteness, ordered field) | **sorry-free** |
| `specht_form_nondegenerate_ordered` (Stage 1: `ℚ`, `ℝ`) | **sorry-free** |
| `specht_form_nondegenerate` (char-0 Gram, every `CharZero` field) | **sorry-free** (was: the module's last stub) |
| `specht_isSimple` (the reduction, general `CharZero`) | **sorry-free — no residual core** |
| `specht_isSimple_ordered` (the reduction, ordered field) | **sorry-free — no residual core** |
| ~~`specht_gram_orthogonal`~~ | **REFUTED — false, do not restate.** `μ=(2,1)` Gram is `[[2,1],[1,2]]` |
| ~~`specht_gram_diag`~~, ~~`kap_of_clash_eq_zero`~~, ~~`sagan_row_col_clash`~~ | **removed** — true statements, but orphaned by the refutation and left non-typechecking; recover from git history |

`#print axioms` reports `[propext, Classical.choice, Quot.sound]` — no `sorryAx`
— for **every** declaration in this module, `specht_form_nondegenerate` and
`specht_isSimple` included.  Verified, not asserted.

The form and `κ_t` live over a generic `[CommRing k]` (§7c clean — no `ℝ`, no
ordering, no `Real.*`); only `specht_submodule_dichotomy` and the final theorems
add `[Field k]` (submodule lattice / `c⁻¹`) and `[CharZero k]` (non-degeneracy of
the Gram form).

**§7c note on the ordered-field additions.**  `bilinM_self_eq_zero_iff` and its
two consumers carry `[LinearOrder k] [IsStrictOrderedRing k]`.  That ordering is
*load-bearing, not gratuitous*: positive definiteness is exactly an archimedean
statement (`Σ (x d)^2 = 0 ⇒ x = 0` is false over `ℂ`), so these three
declarations sit deliberately on the archimedean side of the wall.  They are
additive — no existing generic-`R` or `CommRing` declaration was specialised,
and the substrate-side layer above is untouched.  `ℝ` itself is still never
mentioned: the statements stay over an abstract ordered field.

This module carries **no** `sorry`.  It reproduces the brick-2
`specht_isSimple` statement as a separate, reduction-bearing theorem, because
brick 2 (`QOU.BraidKnot.Specht`) cannot import this file — the standard one-way
dependency.  The brick-2 declaration of the same name is therefore still a stub;
it has no consumers, and the proved statement to cite is this one.

Note it is **not** reached by `QOU.lean`, so `lake build` does not compile it;
build it by name (`lake build QOU.BraidKnot.SpechtIrreducible`) or see bean
qou-rc7b on the build-closure gap.

## New dependencies (§4.4)

| Module | What it supplies |
|---|---|
| `QOU.BraidKnot.SpechtBaseChange` | polytabloid integrality; `ℚ`-relations survive base change |
| `QOU.MathlibExt.RankMinor` | independent rows ⇒ some maximal minor is nonzero |
| `QOU.MathlibExt.CauchyBinet` | that minor ⇒ `det (N Nᵀ) ≠ 0` over any `CharZero` field |
| `QOU.MathlibExt.GramNondegenerate` | invertible Gram ⇒ `W ⊓ Wᗮ = ⊥` |

The last three are Mathlib gaps, stated and proved generically; none mentions
Specht modules.

## References
- [james1984representation] James & Kerber, *The Representation Theory of the Symmetric
  Group* — the submodule theorem (§8) and the Gram form.
- [sagan2001] Sagan, *The Symmetric Group*, §2.4 — irreducibility of `S^μ` and the
  bilinear form.
-/

open QOU.BraidKnot.Specht
open scoped BigOperators

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

/-! ## 3.5. The column antisymmetrizer `κ_t` (sorry-free)

The classical James submodule theorem is driven by the **column antisymmetrizer**
`κ_t = Σ_{π ∈ C_t} sgn(π) · rep(π)` acting on `M^μ`.  This section builds `κ_t`
and its structural properties **sorry-free**:

* `kapL` (a genuine `M^μ →ₗ M^μ`), `kapL_apply`, `kapL_of`, `kapL_of_self`
  (`κ_t {t} = e_t`);
* `kapL_mem_U` — `κ_t` preserves any `S_n`-stable submodule (it is an integer
  combination of the group action);
* `kapL_selfadjoint` — `⟨κ_t x, y⟩ = ⟨x, κ_t y⟩` for the form (`sgn` is inversion-
  invariant and the form is `S_n`-invariant);
* `polytabloid_rep_equivariant` — `rep σ e_s = e_{σ•s}` (via the conjugation
  bijection `conjEquiv : C_s ≃ C_{σ•s}`), and `tableau_transitive` — the `S_n`-
  action on tableaux is transitive.

These reduce `specht_submodule_dichotomy` (§4.5) to a **single** combinatorial
core, `kap_of_mem_line` (§4), exactly as `SpechtDominanceCore` reduced brick 4. -/

/-- The **column antisymmetrizer** `κ_t : M^μ →ₗ M^μ`,
`κ_t = Σ_{π ∈ C_t} sgn(π) · rep(π)`. -/
noncomputable def kapL (μ : YoungDiagram) (t : Tableau μ) :
    Mtab (k := k) μ →ₗ[k] Mtab (k := k) μ :=
  ∑ π : colStab t,
    (Equiv.Perm.sign (π : Equiv.Perm (Fin (nOf μ))) : ℤ) • (Mtab.rep μ (π : Equiv.Perm (Fin (nOf μ))))

/-- Pointwise value of `κ_t`. -/
theorem kapL_apply (μ : YoungDiagram) (t : Tableau μ) (x : Mtab (k := k) μ) :
    kapL (k := k) μ t x
      = ∑ π : colStab t, (Equiv.Perm.sign (π : Equiv.Perm (Fin (nOf μ))) : ℤ) •
            Mtab.rep μ (π : Equiv.Perm (Fin (nOf μ))) x := by
  unfold kapL
  rw [LinearMap.sum_apply]; exact Finset.sum_congr rfl (fun π _ => by rw [LinearMap.smul_apply])

/-- `κ_t` on a basis tableau vector is the signed column sum. -/
theorem kapL_of (μ : YoungDiagram) (t s : Tableau μ) :
    kapL (k := k) μ t (Mtab.of s)
      = ∑ π : colStab t, (Equiv.Perm.sign (π : Equiv.Perm (Fin (nOf μ))) : ℤ) •
          Mtab.of (k := k) ((π : Equiv.Perm (Fin (nOf μ))) • s) := by
  rw [kapL_apply]; exact Finset.sum_congr rfl (fun π _ => by rw [Mtab.rep_of])

/-- `κ_t {t} = e_t`: the polytabloid is `κ_t` of its own basis vector. -/
theorem kapL_of_self (μ : YoungDiagram) (t : Tableau μ) :
    kapL (k := k) μ t (Mtab.of t) = polytabloid (k := k) t := by rw [kapL_of]; rfl

/-- `κ_t` preserves any `S_n`-stable submodule (it is a `ℤ`-combination of the
group action). -/
theorem kapL_mem_U {μ : YoungDiagram} (t : Tableau μ) (U : Submodule k (Mtab (k := k) μ))
    (x : Mtab (k := k) μ)
    (hU : ∀ σ : Equiv.Perm (Fin (nOf μ)), ∀ x ∈ U, Mtab.rep μ σ x ∈ U) (hx : x ∈ U) :
    kapL (k := k) μ t x ∈ U := by
  rw [kapL_apply]; exact Submodule.sum_mem _ (fun π _ => zsmul_mem (hU _ x hx) _)

/-- Multiplicativity of the representation on application. -/
theorem rep_mul_apply (μ : YoungDiagram) (σ τ : Equiv.Perm (Fin (nOf μ))) (y : Mtab (k := k) μ) :
    Mtab.rep μ σ (Mtab.rep μ τ y) = Mtab.rep μ (σ * τ) y := by rw [map_mul]; rfl

/-- `⟨c • a, b⟩ = c • ⟨a, b⟩` (integer scalar). -/
theorem bilinM_zsmul_left (μ : YoungDiagram) (c : ℤ) (a b : Mtab (k := k) μ) :
    bilinM (k := k) μ (c • a) b = c • bilinM (k := k) μ a b := by
  rw [← LinearMap.flip_apply (bilinM (k := k) μ) (c • a) b, map_zsmul, LinearMap.flip_apply]

/-- `⟨a, c • b⟩ = c • ⟨a, b⟩` (integer scalar). -/
theorem bilinM_zsmul_right (μ : YoungDiagram) (c : ℤ) (a b : Mtab (k := k) μ) :
    bilinM (k := k) μ a (c • b) = c • bilinM (k := k) μ a b := by rw [map_zsmul]

/-- `⟨rep σ x, y⟩ = ⟨x, rep σ⁻¹ y⟩`, from `S_n`-invariance of the form. -/
theorem bilinM_rep_swap (μ : YoungDiagram) (σ : Equiv.Perm (Fin (nOf μ))) (x y : Mtab (k := k) μ) :
    bilinM (k := k) μ (Mtab.rep μ σ x) y = bilinM (k := k) μ x (Mtab.rep μ σ⁻¹ y) := by
  have hinv := bilinM_rep_invariant (k := k) μ σ x (Mtab.rep μ σ⁻¹ y)
  rw [rep_mul_apply, mul_inv_cancel, map_one] at hinv; simpa using hinv

/-- **`κ_t` is self-adjoint** for the form: `⟨κ_t x, y⟩ = ⟨x, κ_t y⟩`.
`sgn` is inversion-invariant and the form is `S_n`-invariant, so reindexing the
column sum by `π ↦ π⁻¹` swaps the operator across the pairing. -/
theorem kapL_selfadjoint (μ : YoungDiagram) (t : Tableau μ) (x y : Mtab (k := k) μ) :
    bilinM (k := k) μ (kapL (k := k) μ t x) y = bilinM (k := k) μ x (kapL (k := k) μ t y) := by
  rw [kapL_apply, kapL_apply, map_sum, LinearMap.sum_apply, map_sum]
  refine Fintype.sum_bijective (fun π : colStab t => π⁻¹) (Equiv.inv _).bijective _ _ ?_
  intro π
  rw [bilinM_zsmul_left, bilinM_zsmul_right, bilinM_rep_swap,
      show ((π⁻¹ : colStab t) : Equiv.Perm (Fin (nOf μ))) = (π : Equiv.Perm (Fin (nOf μ)))⁻¹ from rfl,
      Equiv.Perm.sign_inv]

/-- The **conjugation bijection** `C_s ≃ C_{σ•s}`, `π ↦ σ π σ⁻¹`.  Column
stabilizers of `S_n`-translates are conjugate. -/
def conjEquiv {μ : YoungDiagram} (σ : Equiv.Perm (Fin (nOf μ))) (s : Tableau μ) :
    colStab s ≃ colStab (σ • s) where
  toFun π := ⟨σ * (π : Equiv.Perm (Fin (nOf μ))) * σ⁻¹, by
    rw [mem_colStab, colPattern_smul, smul_smul,
        (by group : (σ * (π : Equiv.Perm (Fin (nOf μ))) * σ⁻¹) * σ = σ * (π : Equiv.Perm (Fin (nOf μ)))),
        mul_smul, (show (π : Equiv.Perm (Fin (nOf μ))) • colPattern s = colPattern s from π.2)]⟩
  invFun ρ := ⟨σ⁻¹ * (ρ : Equiv.Perm (Fin (nOf μ))) * σ, by
    have hρ : (ρ : Equiv.Perm (Fin (nOf μ))) • colPattern (σ • s) = colPattern (σ • s) := ρ.2
    rw [colPattern_smul] at hρ
    rw [mem_colStab, mul_assoc, mul_smul, mul_smul, hρ, ← mul_smul, inv_mul_cancel, one_smul]⟩
  left_inv π := by
    apply Subtype.ext
    show σ⁻¹ * (σ * (π : Equiv.Perm (Fin (nOf μ))) * σ⁻¹) * σ = _; group
  right_inv ρ := by
    apply Subtype.ext
    show σ * (σ⁻¹ * (ρ : Equiv.Perm (Fin (nOf μ))) * σ) * σ⁻¹ = _; group

/-- Conjugation preserves the sign of a permutation (in the commutative unit
group `ℤˣ`). -/
theorem sign_conj {μ : YoungDiagram} (σ g : Equiv.Perm (Fin (nOf μ))) :
    Equiv.Perm.sign (σ * g * σ⁻¹) = Equiv.Perm.sign g := by
  rw [Equiv.Perm.sign_mul, Equiv.Perm.sign_mul, Equiv.Perm.sign_inv, mul_right_comm,
      Int.units_mul_self, one_mul]

/-- **`S_n`-equivariance of polytabloids**: `rep σ e_s = e_{σ•s}`.  Reindex the
`C_s` sum by `conjEquiv`; signs match by `sign_conj`, tabloids by the
`C_{σ•s}`-cell identity. -/
theorem polytabloid_rep_equivariant {μ : YoungDiagram} (σ : Equiv.Perm (Fin (nOf μ)))
    (s : Tableau μ) :
    Mtab.rep μ σ (polytabloid (k := k) s) = polytabloid (k := k) (σ • s) := by
  rw [polytabloid, polytabloid, map_sum]
  rw [← Fintype.sum_equiv (conjEquiv σ s)
      (fun π : colStab s => Mtab.rep μ σ ((Equiv.Perm.sign (π : Equiv.Perm (Fin (nOf μ))) : ℤ) •
        Mtab.of (k := k) ((π : Equiv.Perm (Fin (nOf μ))) • s)))
      (fun ρ : colStab (σ • s) => (Equiv.Perm.sign (ρ : Equiv.Perm (Fin (nOf μ))) : ℤ) •
        Mtab.of (k := k) ((ρ : Equiv.Perm (Fin (nOf μ))) • (σ • s)))]
  intro π
  rw [map_zsmul, Mtab.rep_of]
  have hsign : (Equiv.Perm.sign ((conjEquiv σ s π : colStab (σ • s)) : Equiv.Perm (Fin (nOf μ))) : ℤ)
      = (Equiv.Perm.sign (π : Equiv.Perm (Fin (nOf μ))) : ℤ) := by
    show (Equiv.Perm.sign (σ * (π : Equiv.Perm (Fin (nOf μ))) * σ⁻¹) : ℤ) = _; rw [sign_conj]
  have hcell : ((conjEquiv σ s π : colStab (σ • s)) : Equiv.Perm (Fin (nOf μ))) • (σ • s)
      = σ • ((π : Equiv.Perm (Fin (nOf μ))) • s) := by
    show (σ * (π : Equiv.Perm (Fin (nOf μ))) * σ⁻¹) • (σ • s) = _
    rw [smul_smul, (by group : (σ * (π : Equiv.Perm (Fin (nOf μ))) * σ⁻¹) * σ = σ * (π : Equiv.Perm (Fin (nOf μ)))), mul_smul]
  rw [hsign, hcell]

/-- The `S_n`-action on tableaux is **transitive** (both are bijections
`Fin n ≃ μ.cells`). -/
theorem tableau_transitive {μ : YoungDiagram} (s t' : Tableau μ) :
    ∃ σ : Equiv.Perm (Fin (nOf μ)), σ • s = t' := by
  refine ⟨(t'.trans s.symm).symm, ?_⟩
  apply Equiv.ext
  intro l
  simp [Tableau.smul_apply]

/-! ## 4. The remaining deep core (stated, `sorry` + `-- Ref:`)

Thanks to §3.5, the two legs of the column-clash lemma below (`_clash`, `_match`,
both sorry-free) **and** the §4.x discharge of the Gale–Ryser matching
`noclash_match_exists`, James's submodule theorem is now proved (§4.5) **fully
sorry-free**.  Only non-degeneracy of the form on `S^μ`
(`specht_form_nondegenerate`) remains a genuinely separate char-0 obstruction (the
James–Specht Gram determinant), unchanged by this pass. -/

/-- `Mtab.of` depends only on the tabloid class: row-equivalent tableaux give the
same basis vector. -/
theorem mtab_of_congr {μ : YoungDiagram} {s₁ s₂ : Tableau μ}
    (h : Tabloid.mk s₁ = Tabloid.mk s₂) :
    Mtab.of (k := k) s₁ = Mtab.of (k := k) s₂ := by
  unfold Mtab.of; rw [h]

/-- **Clash leg of the column-clash lemma (sorry-free).**  If two *distinct*
labels `a ≠ b` lie in a common column of `t` (`colPattern t a = colPattern t b`)
and a common row of `s` (`rowPattern s a = rowPattern s b`), then `κ_t {s} = 0`:
the transposition `τ = (a b)` is a sign-reversing involution of the `C_t`-sum
fixing every tabloid `{π • s}`, so the sum cancels in pairs. -/
theorem kap_of_mem_line_clash (μ : YoungDiagram) (t s : Tableau μ)
    (a b : Fin (nOf μ)) (hab : a ≠ b)
    (hcol : colPattern t a = colPattern t b)
    (hrow : rowPattern s a = rowPattern s b) :
    kapL (k := k) μ t (Mtab.of s) ∈ Submodule.span k {polytabloid (k := k) t} := by
  classical
  set τ : Equiv.Perm (Fin (nOf μ)) := Equiv.swap a b with hτ
  -- `τ` stabilizes the column pattern of `t`.
  have hτcol : τ ∈ colStab t := by
    rw [mem_colStab]
    funext l
    show colPattern t (τ.symm l) = colPattern t l
    rw [hτ, Equiv.symm_swap]
    rcases eq_or_ne l a with rfl | hla
    · rw [Equiv.swap_apply_left]; exact hcol.symm
    · rcases eq_or_ne l b with rfl | hlb
      · rw [Equiv.swap_apply_right]; exact hcol
      · rw [Equiv.swap_apply_of_ne_of_ne hla hlb]
  -- `τ` fixes the tabloid `{s}` (it stabilizes the row pattern of `s`).
  have hτrow : Tabloid.mk (τ • s) = Tabloid.mk s := by
    rw [Tabloid.mk, Tabloid.mk, Quotient.eq, rowEquiv_iff]
    funext l
    show rowPattern (τ • s) l = rowPattern s l
    rw [rowPattern_smul]
    show rowPattern s (τ.symm l) = rowPattern s l
    rw [hτ, Equiv.symm_swap]
    rcases eq_or_ne l a with rfl | hla
    · rw [Equiv.swap_apply_left]; exact hrow.symm
    · rcases eq_or_ne l b with rfl | hlb
      · rw [Equiv.swap_apply_right]; exact hrow
      · rw [Equiv.swap_apply_of_ne_of_ne hla hlb]
  rw [kapL_of]
  have hzero : (∑ π : colStab t, (Equiv.Perm.sign (π : Equiv.Perm (Fin (nOf μ))) : ℤ) •
      Mtab.of (k := k) ((π : Equiv.Perm (Fin (nOf μ))) • s)) = 0 := by
    refine Finset.sum_involution (fun π _ => π * ⟨τ, hτcol⟩) ?_ ?_ ?_ ?_
    · intro π _
      have hsgn : (Equiv.Perm.sign (((π * ⟨τ, hτcol⟩ : colStab t) :
              Equiv.Perm (Fin (nOf μ)))) : ℤ)
          = - (Equiv.Perm.sign (π : Equiv.Perm (Fin (nOf μ))) : ℤ) := by
        show (Equiv.Perm.sign ((π : Equiv.Perm (Fin (nOf μ))) * τ) : ℤ) = _
        rw [Equiv.Perm.sign_mul, hτ, Equiv.Perm.sign_swap hab]
        push_cast; ring
      have hof : Mtab.of (k := k)
            (((π * ⟨τ, hτcol⟩ : colStab t) : Equiv.Perm (Fin (nOf μ))) • s)
          = Mtab.of (k := k) ((π : Equiv.Perm (Fin (nOf μ))) • s) := by
        apply mtab_of_congr
        show Tabloid.mk (((π : Equiv.Perm (Fin (nOf μ))) * τ) • s) = _
        rw [mul_smul, ← Tabloid.smul_mk, hτrow, Tabloid.smul_mk]
      rw [hsgn, hof, neg_smul]; abel
    · intro π _ _ hcontra
      have hx1 : (⟨τ, hτcol⟩ : colStab t) = 1 :=
        mul_left_cancel (a := π) (by rw [mul_one]; exact hcontra)
      have hτ1 : τ = 1 := by
        have := congrArg (Subtype.val) hx1; simpa using this
      rw [hτ] at hτ1
      exact hab (Equiv.swap_eq_one_iff.1 hτ1)
    · intro π _; exact Finset.mem_univ _
    · intro π _
      show (π * ⟨τ, hτcol⟩) * ⟨τ, hτcol⟩ = π
      rw [mul_assoc,
        show (⟨τ, hτcol⟩ : colStab t) * ⟨τ, hτcol⟩ = 1 from by
          apply Subtype.ext; show τ * τ = 1; rw [hτ, Equiv.swap_mul_self],
        mul_one]
  rw [hzero]; exact Submodule.zero_mem _

/-- **No-clash matching leg (sorry-free).**  If some `π₀ ∈ C_t` carries the
tabloid `{s}` onto `{t}` (`{π₀ • s} = {t}`), then `κ_t {s} = sgn(π₀) · e_t`, hence
lies in `span {e_t}`.  Proved by reindexing the `C_t`-sum through right
multiplication by `π₀` (a bijection of `C_t`) and using that `{ρ • (π₀ • s)} =
{ρ • t}` for every `ρ`. -/
theorem kap_of_mem_line_match (μ : YoungDiagram) (t s : Tableau μ)
    (π₀ : Equiv.Perm (Fin (nOf μ))) (hπ₀ : π₀ ∈ colStab t)
    (hmk : Tabloid.mk (π₀ • s) = Tabloid.mk t) :
    kapL (k := k) μ t (Mtab.of s) ∈ Submodule.span k {polytabloid (k := k) t} := by
  classical
  rw [kapL_of]
  have hrel : ∀ ρ : Equiv.Perm (Fin (nOf μ)),
      Mtab.of (k := k) ((ρ * π₀) • s) = Mtab.of (k := k) (ρ • t) := by
    intro ρ
    apply mtab_of_congr
    rw [mul_smul, ← Tabloid.smul_mk, hmk, Tabloid.smul_mk]
  have key : (∑ π : colStab t, (Equiv.Perm.sign (π : Equiv.Perm (Fin (nOf μ))) : ℤ) •
        Mtab.of (k := k) ((π : Equiv.Perm (Fin (nOf μ))) • s))
      = (Equiv.Perm.sign π₀ : ℤ) • polytabloid (k := k) t := by
    rw [← Equiv.sum_comp (Equiv.mulRight (⟨π₀, hπ₀⟩ : colStab t))
        (fun π : colStab t => (Equiv.Perm.sign (π : Equiv.Perm (Fin (nOf μ))) : ℤ) •
          Mtab.of (k := k) ((π : Equiv.Perm (Fin (nOf μ))) • s))]
    rw [polytabloid, Finset.smul_sum]
    apply Finset.sum_congr rfl
    intro ρ _
    simp only [Equiv.coe_mulRight, Subgroup.coe_mul]
    rw [hrel (ρ : Equiv.Perm (Fin (nOf μ))), Equiv.Perm.sign_mul]
    push_cast
    rw [smul_smul, mul_comm]
  rw [key]
  exact zsmul_mem (Submodule.mem_span_singleton_self _) _

/-! ### 4.x. Pure-combinatorial core of `noclash_match_exists` (sorry-free)

The residual matching lemma below is discharged from four combinatorial helpers over
Mathlib's `YoungDiagram`, with **no** representation theory: a cardinality reindexer
through a tableau bijection (`filterCard_reindex`), the column-cell count
`min r (colLen c)` (`colCells_card`), the per-column label count `colLen c`
(`Col_card`), and the Gale–Ryser saturation `rowPattern s l < colLen (colPattern t l)`
(`row_lt_colLen`).  From saturation the label map `l ↦ (rowPattern s l, colPattern t l)`
is a bijection onto `μ.cells`; matching it against `t` produces the column permutation
`π₀ ∈ C_t` with `{π₀ • s} = {t}`. -/

/-- Reindex a label-filter cardinality through a tableau bijection to the corresponding
cell-filter on `μ.cells`. -/
theorem filterCard_reindex {μ : YoungDiagram} (e : Tableau μ) (P : ℕ × ℕ → Prop)
    [DecidablePred P] :
    (Finset.univ.filter (fun l => P ((e l : ℕ × ℕ)))).card = (μ.cells.filter P).card := by
  classical
  refine Finset.card_bij'
    (fun l _ => ((e l : ℕ × ℕ)))
    (fun c hc => e.symm ⟨c, (Finset.mem_filter.mp hc).1⟩)
    ?_ ?_ ?_ ?_
  · intro l hl; rw [Finset.mem_filter] at hl ⊢; exact ⟨(e l).2, hl.2⟩
  · intro c hc; rw [Finset.mem_filter] at hc ⊢
    refine ⟨Finset.mem_univ _, ?_⟩; rw [Equiv.apply_symm_apply]; exact hc.2
  · intro l hl; rw [Equiv.symm_apply_eq]
  · intro c hc; simp only [Equiv.apply_symm_apply]

/-- Cells of `μ` in column `c` and rows `< r` number `min r (colLen c)` (columns are
downward-closed initial segments of rows). -/
theorem colCells_card {μ : YoungDiagram} (r c : ℕ) :
    (μ.cells.filter (fun cell => cell.1 < r ∧ cell.2 = c)).card = min r (μ.colLen c) := by
  classical
  rw [← Finset.card_range (min r (μ.colLen c))]
  refine Finset.card_bij' (fun cell _ => cell.1) (fun a _ => (a, c)) ?_ ?_ ?_ ?_
  · intro cell hcell; rw [Finset.mem_filter] at hcell
    obtain ⟨hmem, hlt, hsnd⟩ := hcell
    rw [Finset.mem_range, lt_min_iff]; refine ⟨hlt, ?_⟩
    have : (cell.1, cell.2) ∈ μ := (YoungDiagram.mem_cells _).1 hmem
    rw [hsnd] at this; exact (YoungDiagram.mem_iff_lt_colLen).1 this
  · intro a ha; rw [Finset.mem_range, lt_min_iff] at ha; rw [Finset.mem_filter]
    exact ⟨(YoungDiagram.mem_cells _).2 ((YoungDiagram.mem_iff_lt_colLen).2 ha.2), ha.1, rfl⟩
  · intro cell hcell; rw [Finset.mem_filter] at hcell; exact Prod.ext rfl hcell.2.2.symm
  · intro a _; rfl

/-- The labels in column `c` of a tableau `t` number `colLen c`. -/
theorem Col_card {μ : YoungDiagram} (t : Tableau μ) (c : ℕ) :
    (Finset.univ.filter (fun l => colPattern t l = c)).card = μ.colLen c := by
  classical
  have h := filterCard_reindex t (fun cell => cell.2 = c)
  simp only [colPattern] at *
  rw [h, YoungDiagram.colLen_eq_card]
  congr 1

/-- **Gale–Ryser saturation.** Under the no-clash hypothesis, the `s`-row of every label
is below the height of its `t`-column: `rowPattern s l < colLen (colPattern t l)`.  Proof is
the classical prefix-counting / conjugate-partition majorization: for each row-threshold
`r`, the labels of each `t`-column with `s`-row `< r` number exactly `min r (colLen c)`
(the ≤ is no-clash injectivity within the column; the total forces equality against the
cell count `Σ_c min r (colLen c) = #cells in rows < r`).  Taking `r = colLen c` fills the
whole column. -/
private theorem row_lt_colLen {μ : YoungDiagram} (t s : Tableau μ)
    (hnoclash : ∀ a b : Fin (nOf μ),
      colPattern t a = colPattern t b → rowPattern s a = rowPattern s b → a = b)
    (l₀ : Fin (nOf μ)) :
    rowPattern s l₀ < μ.colLen (colPattern t l₀) := by
  classical
  have hmapT_univ : ∀ l : Fin (nOf μ), colPattern t l ∈ μ.cells.image Prod.snd := by
    intro l
    exact Finset.mem_image.2 ⟨(t l : ℕ × ℕ), (t l).2, rfl⟩
  have master : ∀ r : ℕ, ∀ c ∈ μ.cells.image Prod.snd,
      (Finset.univ.filter (fun l => rowPattern s l < r ∧ colPattern t l = c)).card
        = min r (μ.colLen c) := by
    intro r
    have hA_sum : (Finset.univ.filter (fun l => rowPattern s l < r)).card
        = ∑ c ∈ μ.cells.image Prod.snd,
            (Finset.univ.filter (fun l => rowPattern s l < r ∧ colPattern t l = c)).card := by
      rw [Finset.card_eq_sum_card_fiberwise
            (f := fun l => colPattern t l) (t := μ.cells.image Prod.snd)
            (by intro l _; exact hmapT_univ l)]
      simp only [Finset.filter_filter]
    have hCells_sum : (μ.cells.filter (fun cell => cell.1 < r)).card
        = ∑ c ∈ μ.cells.image Prod.snd, min r (μ.colLen c) := by
      rw [Finset.card_eq_sum_card_fiberwise
            (f := Prod.snd) (t := μ.cells.image Prod.snd)
            (by intro cell hcell
                exact Finset.mem_image.2 ⟨cell, (Finset.mem_filter.mp hcell).1, rfl⟩)]
      apply Finset.sum_congr rfl
      intro c _
      rw [Finset.filter_filter]
      exact colCells_card r c
    have hAC : (Finset.univ.filter (fun l => rowPattern s l < r)).card
        = (μ.cells.filter (fun cell => cell.1 < r)).card := by
      have h := filterCard_reindex s (fun cell => cell.1 < r)
      simpa only [rowPattern] using h
    have hsum_eq : ∑ c ∈ μ.cells.image Prod.snd,
          (Finset.univ.filter (fun l => rowPattern s l < r ∧ colPattern t l = c)).card
        = ∑ c ∈ μ.cells.image Prod.snd, min r (μ.colLen c) := by
      rw [← hA_sum, hAC, hCells_sum]
    have hle : ∀ c ∈ μ.cells.image Prod.snd,
        (Finset.univ.filter (fun l => rowPattern s l < r ∧ colPattern t l = c)).card
          ≤ min r (μ.colLen c) := by
      intro c _
      apply le_min
      · have hbound : (Finset.univ.filter
              (fun l => rowPattern s l < r ∧ colPattern t l = c)).card
            ≤ (Finset.range r).card := by
          apply Finset.card_le_card_of_injOn (fun l => rowPattern s l)
          · intro l hl
            simp only [Finset.coe_filter, Set.mem_setOf_eq, Finset.mem_univ, true_and,
              Finset.mem_coe, Finset.mem_range] at hl ⊢
            exact hl.1
          · intro l hl l' hl' heq
            simp only [Finset.coe_filter, Set.mem_setOf_eq, Finset.mem_univ, true_and] at hl hl'
            exact hnoclash l l' (hl.2.trans hl'.2.symm) heq
        rwa [Finset.card_range] at hbound
      · rw [← Col_card t c]
        apply Finset.card_le_card
        intro l hl
        rw [Finset.mem_filter] at hl ⊢
        exact ⟨hl.1, hl.2.2⟩
    exact fun c hc => (Finset.sum_eq_sum_iff_of_le hle).1 hsum_eq c hc
  have hc0T : colPattern t l₀ ∈ μ.cells.image Prod.snd := hmapT_univ l₀
  have hmaster := master (μ.colLen (colPattern t l₀)) (colPattern t l₀) hc0T
  rw [min_self] at hmaster
  have hsub :
      (Finset.univ.filter (fun l => rowPattern s l < μ.colLen (colPattern t l₀)
          ∧ colPattern t l = colPattern t l₀))
        ⊆ (Finset.univ.filter (fun l => colPattern t l = colPattern t l₀)) := by
    intro l hl
    rw [Finset.mem_filter] at hl ⊢
    exact ⟨hl.1, hl.2.2⟩
  have heq := Finset.eq_of_subset_of_card_le hsub
    (le_of_eq (by rw [Col_card, hmaster]))
  have hl0col : l₀ ∈ (Finset.univ.filter (fun l => colPattern t l = colPattern t l₀)) := by
    rw [Finset.mem_filter]; exact ⟨Finset.mem_univ _, rfl⟩
  rw [← heq, Finset.mem_filter] at hl0col
  exact hl0col.2.1


/-- **Core 1′ — the residual pure-combinatorial matching (no module theory).**
If no column of `t` shares two labels with a common row of `s` (the *no-clash*
hypothesis), then some column permutation `π₀ ∈ C_t` carries the tabloid `{s}`
onto `{t}`.  This is the Gale–Ryser / conjugate-partition matching fact
([sagan2001] §2.4, Lemma 2.4.4; [james1984representation] §8): the labels of each
column of `t` occupy, under `s`, exactly the rows `{0, …, h_c − 1}` — the unique
`0/1` matrix with the conjugate-partition margins is the Young diagram itself.
It was the sole remaining combinatorial obligation of `kap_of_mem_line`; it is now
discharged (§4.x) from the elementary `YoungDiagram` counting helpers, so — with the
clash leg and the reindexing leg both already `sorry`-free — `kap_of_mem_line` is
fully closed. -/
theorem noclash_match_exists {μ : YoungDiagram} (t s : Tableau μ)
    (hnoclash : ∀ a b : Fin (nOf μ),
      colPattern t a = colPattern t b → rowPattern s a = rowPattern s b → a = b) :
    ∃ π₀ ∈ colStab t, Tabloid.mk (π₀ • s) = Tabloid.mk t := by
  classical
  have hmem : ∀ l : Fin (nOf μ), (rowPattern s l, colPattern t l) ∈ μ.cells := by
    intro l
    exact (YoungDiagram.mem_cells _).2
      ((YoungDiagram.mem_iff_lt_colLen).2 (row_lt_colLen t s hnoclash l))
  set Gcell : Fin (nOf μ) → μ.cells := fun l => ⟨(rowPattern s l, colPattern t l), hmem l⟩
    with hGcell
  have hGinj : Function.Injective Gcell := by
    intro l l' h
    rw [hGcell] at h
    have h2 := Subtype.ext_iff.mp h
    simp only [Prod.mk.injEq] at h2
    exact hnoclash l l' h2.2 h2.1
  have hcard : Fintype.card (Fin (nOf μ)) = Fintype.card μ.cells := by
    rw [Fintype.card_fin, Fintype.card_coe]
  have hGbij : Function.Bijective Gcell :=
    (Fintype.bijective_iff_injective_and_card Gcell).2 ⟨hGinj, hcard⟩
  set Gequiv : Fin (nOf μ) ≃ μ.cells := Equiv.ofBijective Gcell hGbij with hGe
  set ρ : Equiv.Perm (Fin (nOf μ)) := t.trans Gequiv.symm with hρ
  -- key identity: the matched permutation sends each label to a `t`-cell whose row
  -- (in `t`) is the `s`-row and whose column (in `t`) is preserved.
  have hkey : ∀ l, (rowPattern s (ρ l), colPattern t (ρ l)) = ((t l : ℕ × ℕ)) := by
    intro l
    have hGl : Gequiv (ρ l) = t l := by
      rw [hρ]; simp only [Equiv.trans_apply, Equiv.apply_symm_apply]
    have hval := congrArg (Subtype.val) hGl
    rw [hGe, Equiv.ofBijective_apply, hGcell] at hval
    exact hval
  have hP1 : ∀ l, colPattern t (ρ l) = colPattern t l := by
    intro l; exact (Prod.ext_iff.mp (hkey l)).2
  have hP2 : ∀ l, rowPattern s (ρ l) = rowPattern t l := by
    intro l; exact (Prod.ext_iff.mp (hkey l)).1
  refine ⟨ρ.symm, ?_, ?_⟩
  · -- `ρ.symm ∈ colStab t`: `ρ` preserves the column pattern of `t` (P1).
    rw [mem_colStab]
    funext l
    show colPattern t (ρ.symm.symm l) = colPattern t l
    rw [Equiv.symm_symm]
    exact hP1 l
  · -- `{ρ.symm • s} = {t}`: `ρ` matches `s`-rows to `t`-rows (P2).
    rw [Tabloid.mk, Tabloid.mk, Quotient.eq, rowEquiv_iff]
    funext l
    show rowPattern (ρ.symm • s) l = rowPattern t l
    rw [rowPattern_smul]
    show rowPattern s (ρ.symm.symm l) = rowPattern t l
    rw [Equiv.symm_symm]
    exact hP2 l

/-- **Core 1 — the column-clash lemma (`κ_t` lands in the polytabloid line).**
For any tableaux `t, s`, the column-antisymmetrised basis vector
`κ_t {s} = Σ_{π ∈ C_t} sgn(π) {π•s}` is a scalar multiple of the polytabloid
`e_t`, i.e. it lies in `span_k {e_t}`.  This is the irreducible combinatorial
heart of James's submodule theorem ([james1984representation] §8; [sagan2001]
§2.4, the "sign-reversing involution" lemma).  **Two cases:**

* *Column clash* (`kap_of_mem_line_clash`, **sorry-free**) — if two labels lie in a
  common column of `t` and a common row of `s`, the transposition of those labels
  is a sign-reversing involution of the `C_t`-sum fixing every tabloid `{π•s}`, so
  `κ_t {s} = 0 ∈ span{e_t}`.
* *No clash* (`kap_of_mem_line_match`, **sorry-free**, applied to `π₀` from
  `noclash_match_exists`) — the labels in each column of `t` occupy distinct
  `s`-rows, so some `π₀ ∈ C_t` row-matches `s` to `t` (`{π₀•s} = {t}`), giving
  `κ_t {s} = sgn(π₀)·e_t`.

This lemma is thus **fully proved sorry-free**: both legs are discharged, and the
matching existence `noclash_match_exists` they consume is now proved (§4.x) from
elementary `YoungDiagram` counting.  Everything downstream — `kapL_mem_line`, and
hence `specht_submodule_dichotomy` (§4.5) — is therefore sorry-free, closing the
former opaque `specht_submodule_dichotomy` stub entirely (mirroring how
`SpechtDominanceCore` reduced brick 4's dominance content, but here with the residual
combinatorial obligation also carried out). -/
theorem kap_of_mem_line (μ : YoungDiagram) (t s : Tableau μ) :
    kapL (k := k) μ t (Mtab.of s) ∈ Submodule.span k {polytabloid (k := k) t} := by
  classical
  by_cases hcl : ∃ a b : Fin (nOf μ), a ≠ b ∧
      colPattern t a = colPattern t b ∧ rowPattern s a = rowPattern s b
  · -- column clash: `κ_t {s} = 0` (sign-reversing involution)
    obtain ⟨a, b, hab, hcol, hrow⟩ := hcl
    exact kap_of_mem_line_clash μ t s a b hab hcol hrow
  · -- no clash: match `{s}` to `{t}` via a column permutation, then `κ_t{s} = ±e_t`
    push_neg at hcl
    have hnoclash : ∀ a b : Fin (nOf μ),
        colPattern t a = colPattern t b → rowPattern s a = rowPattern s b → a = b := by
      intro a b hc hr
      by_contra hne
      exact hcl a b hne hc hr
    obtain ⟨π₀, hπ₀c, hmk⟩ := noclash_match_exists t s hnoclash
    exact kap_of_mem_line_match μ t s π₀ hπ₀c hmk

/-- `κ_t` lands in the polytabloid line for **every** input — sorry-free from the
core `kap_of_mem_line`, by `Finsupp` linearity over the tabloid basis
(`κ_t (Σ c_d {d}) = Σ c_d · κ_t {d}`, each `κ_t {d} ∈ span{e_t}`). -/
theorem kapL_mem_line (μ : YoungDiagram) (t : Tableau μ) (x : Mtab (k := k) μ) :
    kapL (k := k) μ t x ∈ Submodule.span k {polytabloid (k := k) t} := by
  refine Finsupp.induction x ?_ ?_
  · rw [map_zero]; exact Submodule.zero_mem _
  · intro d c f _ _ ih
    rw [map_add]
    refine Submodule.add_mem _ ?_ ih
    obtain ⟨s, hs⟩ := Quotient.exists_rep d
    subst hs
    show kapL (k := k) μ t (Finsupp.single (Tabloid.mk s) c) ∈ _
    have hsingle : (Finsupp.single (Tabloid.mk s) c : Mtab (k := k) μ) = c • Mtab.of s := by
      rw [Mtab.of, Finsupp.smul_single, smul_eq_mul, mul_one]
    rw [hsingle, map_smul]
    exact Submodule.smul_mem _ _ (kap_of_mem_line μ t s)

/-! ## 4.2. Gram-matrix helper lemmas for non-degeneracy

These two lemmas, together with `standardBasis`, drive the proof of
`specht_form_nondegenerate` (§4.3).  They give the diagonal and off-diagonal
entries of the Gram matrix of `bilinM` restricted to the standard-polytabloid basis.

* `specht_gram_diag` — `⟨e_T, e_T⟩ = |C_T|` (the size of the column stabilizer).
  Proved by expanding the polytabloid double-sum and observing that cross-terms
  `⟨{π•t}, {σ•t}⟩ = δ_{π,σ}` (two column-permuted tabloids are row-equivalent iff
  π⁻¹σ fixes the row pattern, i.e. π⁻¹σ ∈ rowStab ∩ colStab = {1}), so the only
  surviving terms are the diagonal ones where each contributes `sgn(π)^2 = 1`.
  Reference: [sagan2001] §2.4.
* `specht_gram_orthogonal` — `⟨e_S, e_T⟩ = 0` for distinct standard Young tableaux
  `S ≠ T`.  This is Lemma 2.4.7 of [sagan2001]: if `S ≠ T` are standard, then some
  pair of entries that are in the same row of one lies in the same column of the
  other, producing a sign-canceling transposition in `C_T` that kills the inner product.
-/

/-! ### `specht_gram_diag` and `kap_of_clash_eq_zero` — removed (broken orphans)

Two private lemmas stood here and are removed:

* `specht_gram_diag` : `⟨e_T, e_T⟩ = |C_T|` — **true** (independently confirmed
  by direct enumeration for every `μ ⊢ n`, `n ≤ 5`; e.g. `μ = (2,1)` gives
  diagonal `2 = |C_T|`, `μ = (2,1,1)` gives `6 = 3!`).
* `kap_of_clash_eq_zero` : the sign-reversing involution strengthening of
  `kap_of_mem_line_clash` to a literal `0` — also true.

Both were introduced to feed the refuted `specht_gram_orthogonal` below; with
that lemma withdrawn neither has a consumer, and the proof bodies left on this
branch did not typecheck (an application type mismatch in the first, a
`mul_left_cancel` step in the second).  Carrying broken dead code would leave
the module red for no benefit, so they are removed rather than repaired here.

**They should come back.**  `specht_gram_diag` in particular is exactly the part
of the Gram structure that survives the refutation, and Stage 2 of the corrected
`specht_form_nondegenerate` plan will want it.  Recover both from git history
(`git log -S specht_gram_diag`) and re-prove.  Tracked as a bean.
-/

/-! ### `sagan_row_col_clash` — removed (dead code)

A private lemma `sagan_row_col_clash` stood here: for distinct SYT `S ≠ T` of
the same shape there exist labels `a ≠ b` in the same **row** of `S` and the
same **column** of `T` ([sagan2001] Lemma 2.4.7).  The statement is **true**,
but its only consumer was the refuted `specht_gram_orthogonal` below, and the
proof body left on this branch did not typecheck.  It is removed rather than
carried as a broken dead lemma; recover it from git history
(`git log -S sagan_row_col_clash`) if a future consumer needs it, and re-prove
it against `SpechtDominanceCore.syt_rowPattern_strictMono_in_col`.

Note that Sagan §2.4 uses this clash lemma for **triangularity** with respect
to the dominance order — which this corpus already has, sorry-free, as
`SpechtTriangularCore.standardPolytabloid_triangular'` — and *not* for
orthogonality, which is false (next block).
-/

/-!
### ⚠ REFUTED: the standard-polytabloid Gram matrix is NOT diagonal

A lemma `specht_gram_orthogonal` asserting `⟨e_S, e_T⟩ = 0` for distinct
standard Young tableaux `S ≠ T` stood here across several commits, carrying a
`sorry` and a comment attributing the failure to "missing double-coset
machinery".  **The statement is false**, which is why every elementary route
failed.  Do not restate it.

Counterexample, `μ = (2,1)`, `n = 3` — the two SYT are

```
S = 1 2      T = 1 3
    3            2
```

with column stabilisers `C_S = {id, (13)}`, `C_T = {id, (12)}`, so

```
e_S = {12|3} − {23|1},      e_T = {13|2} − {23|1}.
```

Tabloids are orthonormal for `bilinM`, and the two polytabloids share exactly
the tabloid `{23|1}` with coefficient `−1` on each side, giving

```
⟨e_S, e_T⟩ = (−1)·(−1) = 1 ≠ 0.
```

The full Gram matrix is `[[2,1],[1,2]]` (determinant `3`).  Machine-checked by
direct enumeration for every `μ ⊢ n`, `n ≤ 5`: the off-diagonal is nonzero in
every partition with ≥ 2 standard tableaux (e.g. `μ = (2,1,1)` gives
`[[6,2,−2],[2,6,2],[−2,2,6]]`).  Only the **diagonal** claim survives, and it
is exactly `specht_gram_diag` above (`⟨e_T, e_T⟩ = |C_T|`), which is proved
sorry-free and independently confirmed by the same enumeration.

What Sagan §2.4 actually supplies is the *triangularity* of the standard
polytabloids with respect to the dominance order — already available here as
`SpechtTriangularCore.standardPolytabloid_triangular'` — not orthogonality.

Consequence for `specht_form_nondegenerate` below: the "off-diagonal entries
vanish, so `⟨e_T, x⟩ = c_T·|C_T|`" proof plan is invalid as stated and has been
replaced.  See the corrected plan in that theorem's docstring.
-/
-- Ref: [sagan2001] §2.4 (triangularity, NOT orthogonality — see above)

/-! ## 4.3-bis. Stage 1 of the corrected plan: ordered fields, no Gram theory

The `sorry` in `specht_form_nondegenerate` below now owes only **Stage 2** (a
general characteristic-zero field, e.g. `ℂ`).  **Stage 1 — every ordered field,
so in particular `ℚ` and `ℝ`, which is the archimedean evaluation the framework
actually uses — is discharged here, sorry-free.**  It needs neither standard
tableaux nor the James–Specht Gram determinant: only orthonormality of the
tabloid basis together with `a * a ≥ 0`.
-/

/-- **The form is positive definite over an ordered field.**  In the tabloid
basis `⟨x, x⟩ = Σ_d (x d)^2` is a sum of squares, so it vanishes exactly at
`x = 0`.  No Specht theory enters — this is a statement about `M^μ`. -/
theorem bilinM_self_eq_zero_iff {k : Type} [Field k] [LinearOrder k]
    [IsStrictOrderedRing k] (μ : YoungDiagram) (x : Mtab (k := k) μ) :
    bilinM (k := k) μ x x = 0 ↔ x = 0 := by
  constructor
  · intro h
    have hsum : ∑ d ∈ x.support, x d * x d = 0 := by
      rw [← h, bilinM_apply]
      rfl
    have hnn : ∀ d ∈ x.support, 0 ≤ x d * x d := fun d _ => mul_self_nonneg _
    have hz := (Finset.sum_eq_zero_iff_of_nonneg hnn).mp hsum
    ext d
    by_cases hd : d ∈ x.support
    · simpa using mul_self_eq_zero.mp (hz d hd)
    · simpa using Finsupp.notMem_support_iff.mp hd
  · rintro rfl
    simp

/-- **Stage 1 of the corrected plan for `specht_form_nondegenerate`.**  Over an
ordered field the form is positive definite on *all* of `M^μ`
(`bilinM_self_eq_zero_iff`), so `S^μ ⊓ (S^μ)ᗮ = ⊥` is immediate: an element of
the intersection is orthogonal to itself, hence zero.

Note this needs **no** `μ.card ≠ 0` hypothesis and no standard-basis or Gram
input, so on the fields it covers it is strictly stronger than the `CharZero`
statement below. -/
theorem specht_form_nondegenerate_ordered {k : Type} [Field k] [LinearOrder k]
    [IsStrictOrderedRing k] (μ : YoungDiagram) :
    SpechtSubmodule (k := k) μ ⊓ spechtPerp (k := k) μ = ⊥ := by
  rw [eq_bot_iff]
  rintro x ⟨hxS, hxP⟩
  simp only [SetLike.mem_coe] at hxS hxP
  rw [Submodule.mem_bot]
  rw [mem_spechtPerp_iff] at hxP
  exact (bilinM_self_eq_zero_iff (k := k) μ x).mp (hxP x hxS)

/-! ### 4.3-ter. The diagonal Gram entry, and what it does *not* buy

`⟨e_t, e_t⟩ = |C_t|` is genuine characteristic-zero content — it is the reason
the form is not identically zero on `S^μ`.  It is restored here (see the
provenance note on the lemma) because every route to Stage 2 needs it and it
was lost as collateral damage when a *different*, false, lemma was refuted.

It does **not**, however, close Stage 2, and the reason is worth recording so
the route is not re-attempted.  One might hope to feed
`R := S^μ ⊓ (S^μ)ᗮ` — which is `S_n`-stable — into the already-proved
`specht_submodule_dichotomy`, getting `S^μ ≤ R` or `R ≤ (S^μ)ᗮ`:

* the first branch **is** killed by the lemma below (it would force
  `⟨e_t, e_t⟩ = 0`, i.e. `|C_t| = 0`, false in char 0);
* but the second branch is **vacuous** — `R ≤ (S^μ)ᗮ` holds by construction, so
  it yields nothing.

And the vacuity is not an artifact of how the dichotomy is stated.  Unfolding
the `κ` side: by `kapL_mem_line`, `κ_t x = λ_t(x) · e_t` for a scalar `λ_t(x)`,
and by `kapL_selfadjoint` together with `⟨{t}, e_t⟩ = 1`,
`⟨e_t, x⟩ = ⟨κ_t {t}, x⟩ = ⟨{t}, κ_t x⟩ = λ_t(x)`.  So the dichotomy's
"`κ_t x = 0` for all `t`" branch says exactly `x ∈ (S^μ)ᗮ` — literally the
hypothesis one already has.  The dichotomy therefore *cannot* separate `R = ⊥`
from `R ≠ ⊥`, in any characteristic.  Stage 2 needs the rank/base-change input
described at the `sorry`, not another pass through James's theorem.
-/

/-- **Diagonal Gram entry:** `⟨e_t, e_t⟩ = |C_t|`, the order of the column
stabilizer — for *any* tableau `t`; standardness is not used.

The `|C_t|` tabloids `{π • t}` for `π ∈ C_t` are pairwise distinct, because
`{π • t} = {σ • t}` forces `σ⁻¹π ∈ R_t ⊓ C_t = {1}`
(`SpechtTriangularCore.colStab_inf_rowStab_eq_one`).  So the double sum
collapses onto its diagonal, where each term contributes `sgn(π)^2 = 1`.

**Provenance.**  Proved sorry-free in commit `2815c29a1` as a `private` lemma
about *standard* polytabloids, then removed when the neighbouring
`specht_gram_orthogonal` was refuted — the module docstring's "recover from git
history" note refers to exactly this.  The refutation concerned the
*off-diagonal* entries only; this diagonal computation was always correct.  It
is restored here for a general tableau, since the proof never used
standardness, and made public because both stages of the non-degeneracy plan
consume it. -/
theorem bilinM_polytabloid_self {k : Type} [CommRing k] (μ : YoungDiagram)
    (t : Tableau μ) :
    bilinM (k := k) μ (polytabloid (k := k) t) (polytabloid (k := k) t)
      = (Fintype.card (colStab t) : k) := by
  classical
  rw [polytabloid]
  simp_rw [map_sum, LinearMap.sum_apply, bilinM_zsmul_left, bilinM_zsmul_right,
    Mtab.of, bilinM_single_single, mul_one]
  have hmk_iff : ∀ (π σ : colStab t),
      (Tabloid.mk ((π : Equiv.Perm (Fin (nOf μ))) • t) =
       Tabloid.mk ((σ : Equiv.Perm (Fin (nOf μ))) • t)) ↔ π = σ := by
    intro π σ
    constructor
    · intro heq
      rw [Tabloid.mk, Tabloid.mk, Quotient.eq, rowEquiv_iff,
          rowPattern_smul, rowPattern_smul] at heq
      have hrow : (σ : Equiv.Perm (Fin (nOf μ)))⁻¹ * (π : Equiv.Perm (Fin (nOf μ)))
          ∈ rowStab t := by
        rw [mem_rowStab]
        calc ((σ : Equiv.Perm (Fin (nOf μ)))⁻¹ * (π : Equiv.Perm (Fin (nOf μ)))) • rowPattern t
            = (σ : Equiv.Perm (Fin (nOf μ)))⁻¹ • ((π : Equiv.Perm (Fin (nOf μ))) • rowPattern t) :=
                mul_smul _ _ _
          _ = (σ : Equiv.Perm (Fin (nOf μ)))⁻¹ • ((σ : Equiv.Perm (Fin (nOf μ))) • rowPattern t) := by
                rw [heq]
          _ = ((σ : Equiv.Perm (Fin (nOf μ)))⁻¹ * (σ : Equiv.Perm (Fin (nOf μ)))) • rowPattern t :=
                (mul_smul _ _ _).symm
          _ = rowPattern t := by rw [inv_mul_cancel, one_smul]
      have hcol : (σ : Equiv.Perm (Fin (nOf μ)))⁻¹ * (π : Equiv.Perm (Fin (nOf μ)))
          ∈ colStab t :=
        (colStab t).mul_mem (Subgroup.inv_mem _ σ.2) π.2
      have h1 : (σ : Equiv.Perm (Fin (nOf μ)))⁻¹ * (π : Equiv.Perm (Fin (nOf μ))) = 1 :=
        SpechtTriangularCore.colStab_inf_rowStab_eq_one t hcol hrow
      apply Subtype.ext
      exact mul_left_cancel (a := (σ : Equiv.Perm (Fin (nOf μ)))⁻¹)
        (h1.trans (inv_mul_cancel (σ : Equiv.Perm (Fin (nOf μ)))).symm)
    · intro heq
      rw [heq]
  -- Collapse each inner sum onto its diagonal term.  `hmk_iff` is applied as a
  -- function rather than used as a rewrite rule: the `if`-condition carries a
  -- subtype coercion that `simp_rw` does not match against syntactically.
  have hcard : (∑ _x : colStab t, (1 : k)) = (Fintype.card (colStab t) : k) := by
    rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul, mul_one]
  rw [← hcard]
  refine Finset.sum_congr rfl (fun x _ => ?_)
  rw [Finset.sum_eq_single x]
  · rw [if_pos rfl]
    have hunit : (Equiv.Perm.sign (x : Equiv.Perm (Fin (nOf μ)))) *
                 (Equiv.Perm.sign (x : Equiv.Perm (Fin (nOf μ)))) = 1 :=
      Int.units_mul_self _
    have hval : ((Equiv.Perm.sign (x : Equiv.Perm (Fin (nOf μ))) : ℤˣ) : ℤ) *
                ((Equiv.Perm.sign (x : Equiv.Perm (Fin (nOf μ))) : ℤˣ) : ℤ) = (1 : ℤ) := by
      rw [← Units.val_mul, hunit, Units.val_one]
    simp only [smul_smul, hval, one_smul]
  · intro b _ hb
    rw [if_neg (fun h => hb ((hmk_iff b x).mp h)), smul_zero, smul_zero]
  · intro h
    exact absurd (Finset.mem_univ x) h

/-- **In characteristic zero the form does not vanish on `S^μ`.**  Immediate
from `bilinM_polytabloid_self`: `⟨e_t, e_t⟩ = |C_t|`, and `|C_t| ≥ 1` is a
positive natural number, hence nonzero in a `CharZero` field.

This rules out the `S^μ ≤ R` branch when `specht_submodule_dichotomy` is
applied to the radical `R = S^μ ⊓ (S^μ)ᗮ`.  As the section note above explains,
the surviving branch is vacuous, so this is *not* a route to
`specht_form_nondegenerate` — it is the honest statement of how much the
diagonal Gram entry buys on its own. -/
theorem specht_not_le_perp {k : Type} [Field k] [CharZero k] (μ : YoungDiagram)
    (t : Tableau μ) :
    ¬ (SpechtSubmodule (k := k) μ ≤ spechtPerp (k := k) μ) := by
  intro hle
  have hmem : polytabloid (k := k) t ∈ SpechtSubmodule (k := k) μ :=
    polytabloid_mem_specht (k := k) t
  have h0 : bilinM (k := k) μ (polytabloid (k := k) t) (polytabloid (k := k) t) = 0 := by
    have hperp := hle hmem
    rw [mem_spechtPerp_iff] at hperp
    exact hperp _ hmem
  rw [bilinM_polytabloid_self] at h0
  haveI : Nonempty (colStab t) := ⟨1⟩
  exact (Nat.cast_ne_zero.mpr Fintype.card_ne_zero) h0

/-- **Non-degeneracy of the form on `S^μ`, every characteristic-zero field** —
`S^μ ⊓ (S^μ)ᗮ = ⊥`.  Formerly this module's last `sorry`; now proved.

**Historical warning, kept because the wrong route is tempting.**  An earlier
plan read

> `0 = ⟨e_T, x⟩ = Σ_S c_S ⟨e_T, e_S⟩ = c_T · |C_T|`, off-diagonal entries
> being `0`

which presumes the standard-polytabloid Gram matrix is diagonal.  It is not —
see the refutation block above: `μ = (2,1)` gives `[[2,1],[1,2]]`.  Do not
restate `specht_gram_orthogonal`.

**The proof, in five moves.**

*1. Thin the polytabloids over `ℚ`.*  `exists_linearIndepOn_extension` picks a
sub**set of tableaux** `b` whose polytabloids are `ℚ`-independent and still
cover the rest.  It is stated for `LinearIndepOn` over a `Set ι`, so what comes
back is a set of *tableaux*, not of vectors — which is why this step needs no
standard-basis theorem, no Garnir straightening, and no dominance core.

*2. Their coordinate matrix is an integer matrix.*  A polytabloid is a signed
sum of basis tabloids, so every coefficient is a sum of `±1`
(`SpechtBaseChange.polytabloid_apply_eq_intCast`).  Call it `Mz`.

*3. `det (Mz Mzᵀ) ≠ 0` over `k`.*  `RankMinor.exists_selector_det_ne_zero` turns
the `ℚ`-independence of `Mz`'s rows into a nonzero maximal minor, and
`CauchyBinet.det_gram_map_ne_zero` turns that into the Gram determinant being
nonzero in `k`.  **This is the step that reaches `ℂ`**: Cauchy–Binet writes
`det (Mz Mzᵀ) = Σ_f (det Mz_f)²`, a sum of squares *of integers*, so the
positivity argument happens entirely in `ℤ` and `k` is never ordered.

*4. That determinant is the Gram determinant of the form.*  The tabloid basis is
orthonormal for `bilinM` (`bilinM_apply`), so the Gram matrix of any family is
exactly `(coordinate matrix) · (coordinate matrix)ᵀ`.

*5. Invertible Gram ⇒ trivial radical.*
`GramNondegenerate.span_inf_orthogonalBilin_eq_bot`.

The family spans over `k` and not merely over `ℚ` because the coordinates are
integers, so the `ℚ`-relations found in step 1 survive base change
(`SpechtBaseChange.spechtSubmodule_eq_span_of_rat`).

**Relation to Stage 1.**  `specht_form_nondegenerate_ordered` (§4.3-bis) proves
the same statement over an ordered field by positive definiteness, in three
lines.  It remains as the cheap special case; it provably cannot reach `ℂ`,
where the form is bilinear rather than sesquilinear and has isotropic vectors
(`x = (1, i)` gives `⟨x, x⟩ = 0` with `x ≠ 0`).

**No `μ.card ≠ 0` hypothesis.**  Earlier versions carried one, to match the
brick-2 contract in `Specht.specht_isSimple`.  That stub has since been deleted
(it duplicated a proved theorem), and the proof never used the hypothesis, so it
is gone: the statement holds for the empty diagram too.  Dropping it matters
downstream — `isCompl_specht_perp` below could not be stated for every `μ` while
its input demanded a nonemptiness proof that `μ = ∅` cannot supply.
-/
theorem specht_form_nondegenerate {k : Type} [Field k] [CharZero k] (μ : YoungDiagram) :
    SpechtSubmodule (k := k) μ ⊓ spechtPerp (k := k) μ = ⊥ := by
  -- Ref: [sagan2001] §2.4 / [james1984representation] — Stage 2 of the corrected
  -- plan in the docstring above (ℤ-Gram determinant nonzero, base-changed to k).
  --
  -- The previous proof body is DELETED, not weakened: it discharged the
  -- off-diagonal sum by `rw [specht_gram_orthogonal …]`, and that lemma is
  -- false (see the refutation block above). A proof resting on a false lemma
  -- is not partial progress toward this theorem, so nothing of it is retained.
  --
  -- Stage 1 is now DONE and sorry-free, one section up: see
  -- `specht_form_nondegenerate_ordered` (§4.3-bis), which proves exactly this
  -- statement for `[Field k] [LinearOrder k] [IsStrictOrderedRing k]` — hence
  -- for ℚ and ℝ — via positive definiteness (`bilinM_self_eq_zero_iff`).
  -- Downstream, `specht_isSimple_ordered` (§5) is fully sorry-free.
  --
  -- GAP (Stage 2 only): the general `CharZero` case, i.e. fields with no
  -- compatible order — `ℂ` being the one that matters. Stage 1 provably cannot
  -- reach it: over `ℂ` the form is bilinear rather than sesquilinear and has
  -- isotropic vectors (`x = (1, i)` gives `⟨x, x⟩ = 0` with `x ≠ 0`), so
  -- `⟨x, x⟩ = 0` no longer forces `x = 0`.
  --
  -- Stage 2 is now DONE, by the route sketched above but with Cauchy–Binet
  -- doing the work of step (iii). Five moves, each supplied by a named lemma:
  --
  --   1. over ℚ, thin the polytabloids to an independent sub-family that still
  --      spans (`exists_linearIndepOn_extension` — a *set of tableaux*, so no
  --      standard-basis theorem and no Garnir straightening is involved);
  --   2. its integer coordinate matrix `Mz` has ℚ-independent rows;
  --   3. `RankMinor` turns that into a nonzero maximal minor, and
  --      `CauchyBinet` turns the minor into `det (N Nᵀ) ≠ 0` over `k` —
  --      the sum of squares lives over ℤ, so `k` is never ordered;
  --   4. `bilinM`'s Gram matrix on that family *is* `N Nᵀ`, because the
  --      tabloid basis is orthonormal (`bilinM_apply`);
  --   5. `GramNondegenerate` turns an invertible Gram into `W ⊓ Wᗮ = ⊥`.
  --
  -- The sub-family spans over `k` and not just ℚ because polytabloid
  -- coordinates are integers, so a ℚ-relation among them survives base change
  -- (`SpechtBaseChange.spechtSubmodule_eq_span_of_rat`).
  classical
  -- 1. thin the polytabloids over ℚ
  obtain ⟨b, -, -, hcover, hind⟩ :=
    exists_linearIndepOn_extension (K := ℚ) (v := polytabloid (k := ℚ) (μ := μ))
      (linearIndepOn_empty ℚ _) (Set.empty_subset (Set.univ : Set (Specht.Tableau μ)))
  haveI : Fintype b := Set.Finite.fintype (Set.toFinite b)
  have hQ : ∀ t : Specht.Tableau μ, polytabloid (k := ℚ) t ∈
      Submodule.span ℚ (Set.range (fun i : b => polytabloid (k := ℚ) (i : Specht.Tableau μ))) := by
    intro t
    rw [← Set.image_eq_range]
    exact hcover ⟨t, Set.mem_univ t, rfl⟩
  -- the same family spans over `k` — this is where integrality is used
  have hspan :
      Submodule.span k (Set.range (fun i : b => polytabloid (k := k) (i : Specht.Tableau μ)))
        = SpechtSubmodule (k := k) μ :=
    SpechtBaseChange.spechtSubmodule_eq_span_of_rat (k := k) (fun i : b => (i : Specht.Tableau μ)) hQ
  -- 2. the integer coordinate matrix, and its rows' ℚ-independence
  set Mz : Matrix b (Specht.Tabloid μ) ℤ :=
    SpechtBaseChange.coordMatrix (fun i : b => polytabloid (k := ℤ) (i : Specht.Tableau μ))
    with hMz
  have hrows : LinearIndependent ℚ (Mz.map (Int.cast : ℤ → ℚ)).row := by
    have hrow : (Mz.map (Int.cast : ℤ → ℚ)).row
        = (Finsupp.linearEquivFunOnFinite ℚ ℚ (Specht.Tabloid μ)) ∘
            (fun i : b => polytabloid (k := ℚ) (i : Specht.Tableau μ)) := by
      funext i d
      exact (SpechtBaseChange.polytabloid_apply_eq_intCast _ d).symm
    rw [hrow]
    refine hind.map' _ (LinearMap.ker_eq_bot.mpr ?_)
    exact (Finsupp.linearEquivFunOnFinite ℚ ℚ (Specht.Tabloid μ)).injective
  -- 3. + 4. the Gram matrix of the family is `N Nᵀ`, and its determinant is nonzero
  have hgram : QOU.MathlibExt.GramNondegenerate.gramMatrix (bilinM (k := k) μ)
        (fun i : b => polytabloid (k := k) (i : Specht.Tableau μ))
      = (Mz.map (Int.cast : ℤ → k)) * Matrix.transpose (Mz.map (Int.cast : ℤ → k)) := by
    ext i j
    rw [Matrix.mul_apply, QOU.MathlibExt.GramNondegenerate.gramMatrix_apply, bilinM_apply,
      Finsupp.sum_fintype _ _ (by simp)]
    refine Finset.sum_congr rfl (fun d _ => ?_)
    simp only [hMz, Matrix.map_apply, Matrix.transpose_apply, SpechtBaseChange.coordMatrix,
      ← SpechtBaseChange.polytabloid_apply_eq_intCast]
  have hdet : (QOU.MathlibExt.GramNondegenerate.gramMatrix (bilinM (k := k) μ)
      (fun i : b => polytabloid (k := k) (i : Specht.Tableau μ))).det ≠ 0 := by
    rw [hgram]
    exact QOU.MathlibExt.RankMinor.det_gram_map_ne_zero_of_linearIndependent' (k := k) Mz hrows
  -- 5. invertible Gram ⇒ the radical is trivial
  exact QOU.MathlibExt.GramNondegenerate.inf_orthogonalBilin_eq_bot _ _ _ hspan hdet

/-! ### 4.4-bis. The orthogonal decomposition `M^μ = S^μ ⊕ (S^μ)ᗮ`

An immediate consequence of §4.4, and the reason it is worth stating separately:
Sagan's **cross-shape** dominance theorem (§2.4.4 — `Hom(S^μ, M^ν) ≠ 0 ⇒ μ ⊵ ν`,
the open core of `SpechtClassification.spechtIso_imp_dom_both`) needs to extend a
homomorphism `S^μ → M^ν` to all of `M^μ` by declaring it zero on the complement.
That extension exists exactly when `S^μ` has an `S_n`-stable complement, which is
what this section supplies. -/

/-- **`M^μ = S^μ ⊕ (S^μ)ᗮ`.** The Specht module and its form-orthogonal
complement are complementary submodules of `M^μ`.

Mathlib supplies the implication
(`LinearMap.BilinForm.isCompl_orthogonal_of_restrict_nondegenerate`); what was
missing until §4.4 was its hypothesis, non-degeneracy of the form restricted to
`S^μ`, which over a general characteristic-zero field is exactly
`specht_form_nondegenerate`. -/
theorem isCompl_specht_perp {k : Type} [Field k] [CharZero k] (μ : YoungDiagram) :
    IsCompl (SpechtSubmodule (k := k) μ) (spechtPerp (k := k) μ) := by
  -- `BilinForm.orthogonal` and `Submodule.orthogonalBilin` are the same submodule
  have hrefl : (bilinM (k := k) μ).IsRefl := (bilinM_isSymm (k := k) μ).isRefl
  have hdisj : Disjoint (SpechtSubmodule (k := k) μ)
      (LinearMap.BilinForm.orthogonal (bilinM (k := k) μ) (SpechtSubmodule (k := k) μ)) := by
    rw [disjoint_iff]
    exact specht_form_nondegenerate (k := k) μ
  exact LinearMap.BilinForm.isCompl_orthogonal_of_restrict_nondegenerate
    (B := bilinM (k := k) μ) hrefl
    (LinearMap.BilinForm.nondegenerate_restrict_of_disjoint_orthogonal
      (bilinM (k := k) μ) hrefl hdisj)

/-- `(S^μ)ᗮ` is `S_n`-stable — the form is invariant, so the complement supplied
by `isCompl_specht_perp` is a complement **of representations**, not merely of
`k`-modules.  This is the half that makes the extension in Sagan §2.4.4 a
homomorphism of `k[S_n]`-modules. -/
theorem spechtPerp_stable {k : Type} [Field k] (μ : YoungDiagram)
    (σ : Equiv.Perm (Fin (nOf μ))) {x : Mtab (k := k) μ}
    (hx : x ∈ spechtPerp (k := k) μ) :
    Mtab.rep μ σ x ∈ spechtPerp (k := k) μ := by
  rw [mem_spechtPerp_iff] at hx ⊢
  intro y hy
  -- pull `σ` off both arguments: `⟨y, σ x⟩ = ⟨σ⁻¹ y, x⟩`, and `S^μ` is stable
  have hy' : Mtab.rep μ σ⁻¹ y ∈ SpechtSubmodule (k := k) μ := by
    rw [SpechtSubmodule] at hy ⊢
    induction hy using Submodule.span_induction with
    | mem z hz =>
        obtain ⟨t, rfl⟩ := hz
        rw [polytabloid_rep_equivariant]
        exact Submodule.subset_span ⟨σ⁻¹ • t, rfl⟩
    | zero => rw [map_zero]; exact Submodule.zero_mem _
    | add z w _ _ hz hw => rw [map_add]; exact Submodule.add_mem _ hz hw
    | smul a z _ hz => rw [map_smul]; exact Submodule.smul_mem _ a hz
  have hkey := hx (Mtab.rep μ σ⁻¹ y) hy'
  rwa [← bilinM_rep_invariant (k := k) μ σ, rep_mul_apply, mul_inv_cancel,
    map_one, Module.End.one_apply] at hkey

/-! ## 4.5. James's submodule theorem — proved from the single core -/

/-- **James's submodule theorem (the dichotomy)** — now proved **sorry-free modulo
the single core `kap_of_mem_line`**.  For any `S_n`-stable `k`-submodule `U ≤ M^μ`,
either `S^μ ≤ U` or `U ≤ (S^μ)ᗮ`.

**Proof.**  Split on whether `κ_s` annihilates all of `U`.
* If `κ_s x = 0` for every `x ∈ U`, `s`: then for each `x ∈ U`,
  `⟨e_s, x⟩ = ⟨κ_s {s}, x⟩ = ⟨{s}, κ_s x⟩ = 0` (`kapL_selfadjoint`), so `x ⊥ S^μ`,
  i.e. `U ≤ (S^μ)ᗮ`.
* Otherwise some `κ_s x ≠ 0` with `x ∈ U`.  Then `κ_s x ∈ U` (`kapL_mem_U`) and
  `κ_s x ∈ span{e_s}` (`kapL_mem_line`), so `κ_s x = c·e_s` with `c ≠ 0`, whence
  `e_s ∈ U`.  By `S_n`-equivariance (`polytabloid_rep_equivariant`) and
  transitivity (`tableau_transitive`) every polytabloid lies in `U`, so
  `S^μ ≤ U`. -/
theorem specht_submodule_dichotomy {k : Type} [Field k] (μ : YoungDiagram)
    (U : Submodule k (Mtab (k := k) μ))
    (hU : ∀ σ : Equiv.Perm (Fin (nOf μ)), ∀ x ∈ U, Mtab.rep μ σ x ∈ U) :
    SpechtSubmodule (k := k) μ ≤ U ∨ U ≤ spechtPerp (k := k) μ := by
  by_cases hcase : ∀ x ∈ U, ∀ s : Tableau μ, kapL (k := k) μ s x = 0
  · right
    intro x hx
    rw [mem_spechtPerp_iff]
    intro y hy
    have hle : SpechtSubmodule (k := k) μ ≤ LinearMap.ker ((bilinM (k := k) μ).flip x) := by
      rw [SpechtSubmodule, Submodule.span_le]
      rintro _ ⟨s, rfl⟩
      rw [SetLike.mem_coe, LinearMap.mem_ker, LinearMap.flip_apply, ← kapL_of_self,
          kapL_selfadjoint, hcase x hx s, map_zero]
    have hy' := hle hy
    rwa [LinearMap.mem_ker, LinearMap.flip_apply] at hy'
  · left
    push_neg at hcase
    obtain ⟨x, hx, s, hne⟩ := hcase
    have hmem_line := kapL_mem_line (k := k) μ s x
    have hmem_U : kapL (k := k) μ s x ∈ U := kapL_mem_U s U x hU hx
    rw [Submodule.mem_span_singleton] at hmem_line
    obtain ⟨c, hc⟩ := hmem_line
    have hc0 : c ≠ 0 := by rintro rfl; rw [zero_smul] at hc; exact hne hc.symm
    have hpoly : polytabloid (k := k) s ∈ U := by
      have hpe : polytabloid (k := k) s = c⁻¹ • (kapL (k := k) μ s x) := by
        rw [← hc, smul_smul, inv_mul_cancel₀ hc0, one_smul]
      rw [hpe]; exact Submodule.smul_mem _ _ hmem_U
    rw [SpechtSubmodule, Submodule.span_le]
    rintro _ ⟨t', rfl⟩
    obtain ⟨σ, rfl⟩ := tableau_transitive s t'
    rw [← polytabloid_rep_equivariant]
    exact hU σ _ hpoly

/-! ## 5. The reduction: `specht_isSimple` from the two cores -/

/-- **Irreducibility of `S^μ` over any characteristic-zero field — proved.**

Reduces to the two cores above, both of which are now sorry-free:
`specht_submodule_dichotomy` (James's submodule theorem) and
`specht_form_nondegenerate` (§4.4).  `#print axioms` reports
`[propext, Classical.choice, Quot.sound]`.

Reproduces the brick-2 statement `QOU.BraidKnot.Specht.specht_isSimple`
verbatim; that one is still a stub, because brick 2 cannot import this file. -/
theorem specht_isSimple {k : Type} [Field k] [CharZero k] (μ : YoungDiagram) :
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
    rw [eq_bot_iff, ← specht_form_nondegenerate (k := k) μ]
    exact le_inf hN_le hperp

/-- **Irreducibility of `S^μ` over an ordered field — fully `sorry`-free.**

The same reduction as `specht_isSimple`, but routed through
`specht_form_nondegenerate_ordered` (Stage 1) instead of the `CharZero` core,
so it carries **no** `sorry` at all: `specht_submodule_dichotomy` is sorry-free
and needs only `Field k`, and Stage 1 supplies the non-degeneracy outright.

This covers `ℚ` and `ℝ` — the archimedean evaluation the framework actually
uses.  It also needs no `μ.card ≠ 0` hypothesis.

`specht_isSimple` is the broader statement (every characteristic-zero field,
`ℂ` included) and is **also** sorry-free now, so this variant is kept for its
cheapness and its independence from the Cauchy–Binet chain, not because the
general case is still owed. -/
theorem specht_isSimple_ordered {k : Type} [Field k] [LinearOrder k]
    [IsStrictOrderedRing k] (μ : YoungDiagram) :
    ∀ N : Submodule k (Mtab (k := k) μ),
      N ≤ SpechtSubmodule (k := k) μ →
      (∀ σ : Equiv.Perm (Fin (nOf μ)), ∀ x ∈ N, Mtab.rep μ σ x ∈ N) →
      N = ⊥ ∨ N = SpechtSubmodule (k := k) μ := by
  intro N hN_le hN_stable
  rcases specht_submodule_dichotomy (k := k) μ N hN_stable with hsub | hperp
  · exact Or.inr (le_antisymm hN_le hsub)
  · left
    rw [eq_bot_iff, ← specht_form_nondegenerate_ordered (k := k) μ]
    exact le_inf hN_le hperp

end QOU.BraidKnot.SpechtIrreducible
