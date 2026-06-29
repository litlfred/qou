import QOU.BraidKnot.SpechtIrreducible
import QOU.BraidKnot.SpechtClassification
import QOU.BraidKnot.SpechtTriangularCore

/-!
# QOU.BraidKnot.SpechtIrreducibleCore — reduction of the two B1 irreducibility cores

`QOU.BraidKnot.SpechtIrreducible` reduces brick-2's `specht_isSimple` to two deep
cores via the `M^μ` bilinear form (James's submodule theorem):

* `specht_submodule_dichotomy` — for `S_n`-stable `U ≤ M^μ`, either `S^μ ≤ U` or
  `U ≤ (S^μ)ᗮ` (James, *Representation Theory of the Symmetric Groups*, §8).
* `specht_form_nondegenerate` — `S^μ ⊓ (S^μ)ᗮ = ⊥` in char 0 (the Gram form).

This module is an **independent** further reduction of the **dichotomy** core. It
imports `SpechtIrreducible` and `SpechtClassification` read-only and modifies
neither. It builds the **column antisymmetrizer** endomorphism `κ_t` on `M^μ`
sorry-free, isolates the irreducible James content as a single
**sign-lemma** core, and derives the full dichotomy `sorry`-free from it:

> `james_kernel_core` — for every tableau `t` and every `u ∈ M^μ`,
> `κ_t u = ⟨u, e_t⟩ · e_t`. This is James's §4 sign lemma: applying the column
> antisymmetrizer to any tabloid yields `0` (when two same-row labels share a
> column of `t`) or `±e_t`; assembled over the tabloid basis this is the stated
> scalar identity. It is the genuine combinatorial heart of the submodule
> theorem.

Everything around it is `sorry`-free: the antisymmetrizer is a finite signed sum
of the representation operators (`κ_t u ∈ U` whenever `U` is `S_n`-stable and
`u ∈ U`), the `S^μ ≤ U` half is the orbit argument (`e_t ∈ U` ⟹ all `e_s ∈ U` via
transitivity of `S_n` on tableaux + `rep_polytabloid`), and the `U ≤ (S^μ)ᗮ` half
is the kernel-of-the-flipped-form argument.

The **char-0 Gram** core (`specht_form_nondegenerate`) is reused verbatim from
`SpechtIrreducible`. So this module reduces brick-2 irreducibility from *two* deep
cores to **one** deep core (`james_kernel_core`) plus the already-stated Gram core.
The **diagonal** of that Gram core is discharged sorry-free here
(`polytabloid_self_pairing` : `⟨e_t,e_t⟩ = |C_t|`, hence `e_t ∉ (S^μ)ᗮ` in char 0).

## sorry-free ↔ stubbed map

| Declaration | Status |
|---|---|
| `colAntisym`, `colAntisym_mem` (the antisymmetrizer + stability) | **sorry-free** |
| `tableau_exists_smul` (transitivity of `S_n` on tableaux) | **sorry-free** |
| `james_kernel_core` (James §4 sign lemma) | **STUB** `sorry` — `-- Ref: [james1984representation]` §4 |
| `specht_submodule_dichotomy'` (verbatim dichotomy target) | **sorry-free MODULO `james_kernel_core`** |
| `bilinM_apply_of`, `mk_smul_eq_iff`, `polytabloid_coeff` (Gram plumbing) | **sorry-free** |
| `polytabloid_self_pairing` (`⟨e_t,e_t⟩ = |C_t|`) | **sorry-free** |
| `polytabloid_not_mem_spechtPerp` (`e_t ∉ (S^μ)ᗮ`, char 0) | **sorry-free** |
| `specht_isSimple'` (the reduction) | **sorry-free MODULO `james_kernel_core` + `specht_form_nondegenerate`** |

## References
- [james1984representation] James, *The Representation Theory of the Symmetric
  Groups* — §4 (the sign lemma), §8 (the submodule theorem, the Gram form).
- [sagan2001] Sagan, *The Symmetric Group*, §2.4 (κ_t and the bilinear form).
-/

open scoped BigOperators

namespace QOU.BraidKnot.SpechtIrreducibleCore

open QOU.BraidKnot
open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtIrreducible
open QOU.BraidKnot.SpechtTriangularCore
open Equiv (Perm)

variable {k : Type} [Field k] [CharZero k]
variable {μ : YoungDiagram}

/-! ## 1. The column antisymmetrizer (sorry-free) -/

omit [CharZero k] in
/-- The **column antisymmetrizer** `κ_t u = Σ_{π ∈ C_t} sgn(π) · (π · u)` acting on
`M^μ`. A finite signed sum of the representation operators `rep π`. -/
noncomputable def colAntisym (t : Tableau μ) (u : Mtab (k := k) μ) : Mtab (k := k) μ :=
  ∑ π : colStab t,
    (Equiv.Perm.sign (π : Perm (Fin (nOf μ))) : ℤ) • Mtab.rep μ (π : Perm (Fin (nOf μ))) u

omit [CharZero k] in
/-- **Stability of `κ_t`.** If `U` is `S_n`-stable and `u ∈ U`, then `κ_t u ∈ U`
(a finite signed sum of `rep π u ∈ U`). -/
theorem colAntisym_mem {U : Submodule k (Mtab (k := k) μ)}
    (hU : ∀ σ : Perm (Fin (nOf μ)), ∀ x ∈ U, Mtab.rep μ σ x ∈ U)
    (t : Tableau μ) {u : Mtab (k := k) μ} (hu : u ∈ U) :
    colAntisym (k := k) t u ∈ U := by
  apply Submodule.sum_mem
  intro π _
  exact zsmul_mem (hU (π : Perm (Fin (nOf μ))) u hu) _

/-! ## 2. Transitivity of `S_n` on tableaux (sorry-free) -/

omit [CharZero k] in
/-- **`S_n` acts transitively on `μ`-tableaux.** For any `s t`, there is a
permutation `σ` with `σ • t = s` (concretely `σ = (s ∘ t⁻¹)⁻¹` on labels). -/
theorem tableau_exists_smul (s t : Tableau μ) :
    ∃ σ : Perm (Fin (nOf μ)), σ • t = s := by
  refine ⟨(s.trans t.symm).symm, Equiv.ext fun l => ?_⟩
  rw [Tableau.smul_apply, Equiv.symm_symm, Equiv.trans_apply, Equiv.apply_symm_apply]

/-! ## 3. The single James sign-lemma core (one cited `sorry`) -/

omit [CharZero k] in
/-- **STUB — James's §4 sign lemma (the irreducible dichotomy core).** Applying
the column antisymmetrizer `κ_t` to any `u ∈ M^μ` yields a scalar multiple of the
polytabloid `e_t`, with scalar the form pairing `⟨u, e_t⟩`:
`κ_t u = ⟨u, e_t⟩ · e_t`.

On a tabloid `{s}`, `κ_t {s}` is `0` (when two labels of the same row of `s` lie
in one column of `t`) or `± e_t` (when `{s}` is in the column-orbit of `{t}`);
the orthonormality of tabloids gives the scalar as `⟨{s}, e_t⟩`, and the identity
extends `k`-linearly. The single combinatorial heart of the submodule theorem. -/
theorem james_kernel_core (t : Tableau μ) (u : Mtab (k := k) μ) :
    colAntisym (k := k) t u
      = bilinM (k := k) μ u (Specht.polytabloid (k := k) t) • Specht.polytabloid (k := k) t := by
  -- Ref: [james1984representation] §4 (the sign lemma: κ_t u = ⟨u,e_t⟩ e_t). See
  -- also [sagan2001] §2.4. The irreducible combinatorial core of James's
  -- submodule theorem, with the basis assembly bundled in.
  sorry

/-! ## 4. The dichotomy (sorry-free modulo the single core) -/

omit [CharZero k] in
/-- **James's submodule theorem (the dichotomy), reduced.** Verbatim restatement
of `SpechtIrreducible.specht_submodule_dichotomy`, proved **sorry-free modulo**
the single core `james_kernel_core`. -/
theorem specht_submodule_dichotomy' (μ : YoungDiagram)
    (U : Submodule k (Mtab (k := k) μ))
    (hU : ∀ σ : Perm (Fin (nOf μ)), ∀ x ∈ U, Mtab.rep μ σ x ∈ U) :
    Specht.SpechtSubmodule (k := k) μ ≤ U ∨ U ≤ spechtPerp (k := k) μ := by
  classical
  by_cases h : ∃ u ∈ U, ∃ t : Tableau μ,
      bilinM (k := k) μ u (Specht.polytabloid (k := k) t) ≠ 0
  · -- some `u ∈ U` is not orthogonal to some `e_t` ⟹ `e_t ∈ U` ⟹ `S^μ ≤ U`
    left
    obtain ⟨u, huU, t, hbil⟩ := h
    have hmem : colAntisym (k := k) t u ∈ U := colAntisym_mem hU t huU
    rw [james_kernel_core] at hmem
    have het : Specht.polytabloid (k := k) t ∈ U := by
      have := U.smul_mem (bilinM (k := k) μ u (Specht.polytabloid (k := k) t))⁻¹ hmem
      rwa [smul_smul, inv_mul_cancel₀ hbil, one_smul] at this
    rw [Specht.SpechtSubmodule, Submodule.span_le]
    rintro _ ⟨s, rfl⟩
    obtain ⟨σ, hσ⟩ := tableau_exists_smul s t
    have hrep : Specht.polytabloid (k := k) s
        = Mtab.rep μ σ (Specht.polytabloid (k := k) t) := by
      rw [SpechtClassification.rep_polytabloid, hσ]
    rw [SetLike.mem_coe, hrep]
    exact hU σ _ het
  · -- no `u ∈ U` pairs with any `e_t` ⟹ `U ≤ (S^μ)ᗮ`
    right
    push_neg at h
    intro x hx
    rw [mem_spechtPerp_iff]
    intro y hy
    have hsub : Specht.SpechtSubmodule (k := k) μ
        ≤ LinearMap.ker ((bilinM (k := k) μ).flip x) := by
      rw [Specht.SpechtSubmodule, Submodule.span_le]
      rintro _ ⟨t, rfl⟩
      rw [SetLike.mem_coe, LinearMap.mem_ker, LinearMap.flip_apply, bilinM_symm]
      exact h x hx t
    have := hsub hy
    rwa [LinearMap.mem_ker, LinearMap.flip_apply] at this

/-! ## 5. A sorry-free advance on the char-0 Gram core: the diagonal self-pairing

The full Gram core `specht_form_nondegenerate` (`S^μ ⊓ (S^μ)ᗮ = ⊥`) needs the
Gram **determinant** (a product of hook lengths, nonzero in char 0). Its
**diagonal** is provable sorry-free here: `⟨e_t, e_t⟩ = |C_t|`, so `e_t ∉ (S^μ)ᗮ`
in char 0 — the easy "form is not identically zero on `S^μ`" half. -/

omit [CharZero k] in
/-- `⟨f, ⟦d⟧⟩ = f ⟦d⟧`: pairing a vector with a basis tabloid reads its coefficient. -/
theorem bilinM_apply_of (f : Mtab (k := k) μ) (d : Tableau μ) :
    bilinM (k := k) μ f (Mtab.of (k := k) d) = f (Tabloid.mk d) := by
  rw [bilinM_symm, bilinM_apply, Mtab.of, Finsupp.sum_single_index (by rw [zero_mul]), one_mul]

omit [CharZero k] in
/-- For `π, ρ ∈ C_t`, `⟦π•t⟧ = ⟦ρ•t⟧ ↔ π = ρ` (column-orbit injectivity; the
`C_t ∩ R_t = {1}` fact from `SpechtTriangularCore`). -/
theorem mk_smul_eq_iff (t : Tableau μ) (π ρ : colStab t) :
    Tabloid.mk ((π : Perm (Fin (nOf μ))) • t) = Tabloid.mk ((ρ : Perm (Fin (nOf μ))) • t)
      ↔ π = ρ := by
  rw [Tabloid.mk, Tabloid.mk, Quotient.eq, rowEquiv_iff, rowPattern_smul, rowPattern_smul]
  constructor
  · intro h
    have hmul : ((π : Perm (Fin (nOf μ)))⁻¹ * (ρ : Perm (Fin (nOf μ)))) ∈ rowStab t := by
      rw [mem_rowStab, mul_smul, ← h, inv_smul_smul]
    have hcol : ((π : Perm (Fin (nOf μ)))⁻¹ * (ρ : Perm (Fin (nOf μ)))) ∈ colStab t :=
      mul_mem (inv_mem π.2) ρ.2
    have h1 : (π : Perm (Fin (nOf μ)))⁻¹ * (ρ : Perm (Fin (nOf μ))) = 1 :=
      colStab_inf_rowStab_eq_one t hcol hmul
    apply Subtype.ext
    have h2 : ((π : Perm (Fin (nOf μ))))⁻¹ = ((ρ : Perm (Fin (nOf μ))))⁻¹ :=
      mul_eq_one_iff_eq_inv.1 h1
    exact inv_injective h2
  · rintro rfl; rfl

omit [CharZero k] in
/-- The coefficient of `⟦ρ•t⟧` in `e_t` is `sgn ρ` (for `ρ ∈ C_t`). -/
theorem polytabloid_coeff (t : Tableau μ) (ρ : colStab t) :
    (Specht.polytabloid (k := k) t) (Tabloid.mk ((ρ : Perm (Fin (nOf μ))) • t))
      = ((Equiv.Perm.sign (ρ : Perm (Fin (nOf μ))) : ℤ) : k) := by
  classical
  rw [Specht.polytabloid, Finsupp.finset_sum_apply]
  have hterm : ∀ π : colStab t,
      ((Equiv.Perm.sign (π : Perm (Fin (nOf μ))) : ℤ) •
        Mtab.of (k := k) ((π : Perm (Fin (nOf μ))) • t))
          (Tabloid.mk ((ρ : Perm (Fin (nOf μ))) • t))
        = if π = ρ then ((Equiv.Perm.sign (π : Perm (Fin (nOf μ))) : ℤ) : k) else 0 := by
    intro π
    rw [Finsupp.smul_apply, Mtab.of, Finsupp.single_apply]
    by_cases h : π = ρ
    · rw [if_pos ((mk_smul_eq_iff t π ρ).2 h), if_pos h, zsmul_eq_mul, mul_one]
    · rw [if_neg (fun heq => h ((mk_smul_eq_iff t π ρ).1 heq)), if_neg h, smul_zero]
  simp_rw [hterm]
  rw [Finset.sum_ite_eq' Finset.univ ρ, if_pos (Finset.mem_univ _)]

omit [CharZero k] in
/-- **Diagonal self-pairing `⟨e_t, e_t⟩ = |C_t|`** (sorry-free). Expanding the
second polytabloid, each cross term reads off a coefficient `sgn ρ` (the others
vanish by column-orbit injectivity) and `(sgn ρ)² = 1`, leaving `|C_t|` ones. -/
theorem polytabloid_self_pairing (t : Tableau μ) :
    bilinM (k := k) μ (Specht.polytabloid (k := k) t) (Specht.polytabloid (k := k) t)
      = (Fintype.card (colStab t) : k) := by
  classical
  nth_rewrite 2 [show (Specht.polytabloid (k := k) t)
      = ∑ ρ : colStab t, (Equiv.Perm.sign (ρ : Perm (Fin (nOf μ))) : ℤ) •
          Mtab.of (k := k) ((ρ : Perm (Fin (nOf μ))) • t) from rfl]
  rw [map_sum]
  have hone : ∀ ρ : colStab t,
      (bilinM (k := k) μ (Specht.polytabloid (k := k) t))
        ((Equiv.Perm.sign (ρ : Perm (Fin (nOf μ))) : ℤ) •
          Mtab.of (k := k) ((ρ : Perm (Fin (nOf μ))) • t)) = 1 := by
    intro ρ
    rw [map_zsmul, bilinM_apply_of, polytabloid_coeff, zsmul_eq_mul, ← Int.cast_mul]
    rcases Int.units_eq_one_or (Equiv.Perm.sign (ρ : Perm (Fin (nOf μ)))) with h | h <;>
      rw [h] <;> norm_num
  rw [Finset.sum_congr rfl (fun ρ _ => hone ρ), Finset.sum_const, Finset.card_univ,
    nsmul_eq_mul, mul_one]

/-- **`e_t ∉ (S^μ)ᗮ` in characteristic zero** (sorry-free): `⟨e_t, e_t⟩ = |C_t| ≠ 0`.
A witness that the Gram form is not identically zero on `S^μ` — the easy half of
`specht_form_nondegenerate`. -/
theorem polytabloid_not_mem_spechtPerp (t : Tableau μ) :
    Specht.polytabloid (k := k) t ∉ spechtPerp (k := k) μ := by
  rw [mem_spechtPerp_iff]
  push_neg
  refine ⟨Specht.polytabloid (k := k) t, Specht.polytabloid_mem_specht t, ?_⟩
  rw [polytabloid_self_pairing]
  exact_mod_cast (Nat.cast_ne_zero (R := k)).mpr Fintype.card_ne_zero

/-! ## 6. The reduction: `specht_isSimple` from the dichotomy core + the Gram core -/

/-- **Irreducibility of `S^μ` (char 0)** — reduced `sorry`-free to
`james_kernel_core` (the dichotomy) and `SpechtIrreducible.specht_form_nondegenerate`
(the char-0 Gram core). Reproduces the brick-2 statement
`QOU.BraidKnot.Specht.specht_isSimple` verbatim. -/
theorem specht_isSimple' (μ : YoungDiagram) (hμ : μ.card ≠ 0) :
    ∀ N : Submodule k (Mtab (k := k) μ),
      N ≤ Specht.SpechtSubmodule (k := k) μ →
      (∀ σ : Perm (Fin (nOf μ)), ∀ x ∈ N, Mtab.rep μ σ x ∈ N) →
      N = ⊥ ∨ N = Specht.SpechtSubmodule (k := k) μ := by
  intro N hN_le hN_stable
  rcases specht_submodule_dichotomy' (k := k) μ N hN_stable with hsub | hperp
  · exact Or.inr (le_antisymm hN_le hsub)
  · left
    rw [eq_bot_iff, ← specht_form_nondegenerate (k := k) μ hμ]
    exact le_inf hN_le hperp

end QOU.BraidKnot.SpechtIrreducibleCore
