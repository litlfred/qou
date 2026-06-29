import QOU.BraidKnot.SpechtIrreducible
import QOU.BraidKnot.SpechtClassification
import QOU.BraidKnot.SpechtTriangularCore
import QOU.BraidKnot.YoungStaircaseBound

/-!
# QOU.BraidKnot.SpechtIrreducibleCore — reduction of the two B1 irreducibility cores

`QOU.BraidKnot.SpechtIrreducible` reduces brick-2's `specht_isSimple` to two deep
cores via the `M^μ` bilinear form (James's submodule theorem):

* `specht_submodule_dichotomy` — for `S_n`-stable `U ≤ M^μ`, either `S^μ ≤ U` or
  `U ≤ (S^μ)ᗮ` (James, *Representation Theory of the Symmetric Groups*, §8).
* `specht_form_nondegenerate` — `S^μ ⊓ (S^μ)ᗮ = ⊥` in char 0 (the Gram form).

This module is an **independent** further reduction of the **dichotomy** core. It
imports `SpechtIrreducible`, `SpechtClassification` and `SpechtTriangularCore`
read-only and modifies none. It builds the **column antisymmetrizer** `κ_t`
sorry-free, proves James's sign lemma `κ_t u = ⟨u, e_t⟩·e_t` **sorry-free apart
from a single elementary combinatorial existence lemma** (`sdr_core`), and derives
the full dichotomy from it.

## The James dichotomy is now fully sorry-free

`james_kernel_core` (the sign lemma) and `specht_submodule_dichotomy'` (James's
submodule theorem) are **completely sorry-free** (`#print axioms`:
`[propext, Classical.choice, Quot.sound]`). The SDR/Hall existence that used to be
the residual is discharged by `QOU.BraidKnot.YoungStaircaseBound`
(`exists_colStab_smul`), itself proved sorry-free from the conjugate-marginal
staircase bound — **with no Hall's-marriage theorem**, by a clean extremality
count. So `sdr_pattern_core` / `sdr_core` are now theorems, not stubs.

The **only** remaining `sorry` reachable from `specht_isSimple'` is the imported
char-0 Gram core `SpechtIrreducible.specht_form_nondegenerate` (the hook-length
Gram determinant). Its diagonal is discharged sorry-free here
(`polytabloid_self_pairing`).

From `sdr_core` the sign lemma follows sorry-free: the per-tabloid identity
`combId` splits into the column-orbit case (a sign-preserving reindex against
`polytabloid_coeff`) and the off-orbit case (a sign-reversing involution
`π ↦ π·τ` whose summand cancels, `Finset.sum_involution`), and `k`-linearity in
`u` (`james_kernel_core'` ⇒ `james_kernel_core`) lifts it to all of `M^μ`.

## sorry-free ↔ stubbed map

| Declaration | Status |
|---|---|
| `colAntisym`, `colAntisym_mem`, `tableau_exists_smul` | **sorry-free** |
| `bilinM_apply_of`, `bilinM_single_left`, `mk_smul_eq_iff`, `polytabloid_coeff`, `poly_kcast` | **sorry-free** |
| `swap_smul_arrow_eq_iff`, `swap_mem_colStab_iff`, `swap_smul_mk_eq_iff` (swap↔pattern) | **sorry-free** |
| `sdr_pattern_core` (the pigeonhole / SDR existence) | **sorry-free** (via `YoungStaircaseBound.exists_colStab_smul`) |
| `sdr_core` (tabloid/transposition form) | **sorry-free** |
| `combId`, `colAntisym_zero`, `colAntisym_add` | **sorry-free** |
| `james_kernel_core` (James §4 sign lemma) | **sorry-free** |
| `specht_submodule_dichotomy'` (the James submodule theorem) | **sorry-free** |
| `polytabloid_self_pairing` (`⟨e_t,e_t⟩ = |C_t|`), `polytabloid_not_mem_spechtPerp` | **sorry-free** |
| `specht_isSimple'` (the reduction) | **sorry-free MODULO `sdr_core` + `specht_form_nondegenerate`** |

The **char-0 Gram** core (`specht_form_nondegenerate`) is reused verbatim from
`SpechtIrreducible`; its **diagonal** is discharged sorry-free here
(`polytabloid_self_pairing`).

## References
- [james1984representation] James, *The Representation Theory of the Symmetric
  Groups* — §4 (the sign lemma), §8 (the submodule theorem, the Gram form).
- [sagan2001] Sagan, *The Symmetric Group*, §2.4 (κ_t, the bilinear form, the sign
  lemma / SDR existence).
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

/-! ## 3. Form / column-orbit plumbing (sorry-free) -/

omit [CharZero k] in
/-- `⟨f, ⟦d⟧⟩ = f ⟦d⟧`: pairing a vector with a basis tabloid reads its coefficient. -/
theorem bilinM_apply_of (f : Mtab (k := k) μ) (d : Tableau μ) :
    bilinM (k := k) μ f (Mtab.of (k := k) d) = f (Tabloid.mk d) := by
  rw [bilinM_symm, bilinM_apply, Mtab.of, Finsupp.sum_single_index (by rw [zero_mul]), one_mul]

omit [CharZero k] in
/-- `⟨single d c, g⟩ = c · g d`. -/
theorem bilinM_single_left (d : Tabloid μ) (c : k) (g : Mtab (k := k) μ) :
    bilinM (k := k) μ (Finsupp.single d c) g = c * g d := by
  rw [bilinM_apply, Finsupp.sum_single_index (by rw [zero_mul])]

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
/-- `e_t` written with `k`-cast signs and `single`-of-tabloid form. -/
theorem poly_kcast (t : Tableau μ) :
    Specht.polytabloid (k := k) t
      = ∑ ν : colStab t, ((Equiv.Perm.sign (ν : Perm (Fin (nOf μ))) : ℤ) : k) •
          Finsupp.single ((ν : Perm (Fin (nOf μ))) • (Tabloid.mk t)) (1 : k) := by
  rw [Specht.polytabloid]
  apply Finset.sum_congr rfl
  intro ν _
  rw [← Int.cast_smul_eq_zsmul k, Mtab.of, ← Tabloid.smul_mk]

/-! ## 4. James's sign lemma — sorry-free modulo the single SDR core -/

/-- A transposition fixes a label-indexed pattern iff it identifies the two labels. -/
theorem swap_smul_arrow_eq_iff (f : Fin (nOf μ) → ℕ) (a b : Fin (nOf μ)) :
    (Equiv.swap a b • f) = f ↔ f a = f b := by
  constructor
  · intro h
    have ha := congrFun h a
    rw [arrow_smul_apply, Equiv.symm_swap, Equiv.swap_apply_left] at ha
    exact ha.symm
  · intro h
    funext l
    rw [arrow_smul_apply, Equiv.symm_swap]
    rcases eq_or_ne l a with rfl | hla
    · rw [Equiv.swap_apply_left]; exact h.symm
    · rcases eq_or_ne l b with rfl | hlb
      · rw [Equiv.swap_apply_right]; exact h
      · rw [Equiv.swap_apply_of_ne_of_ne hla hlb]

/-- `swap a b ∈ C_t ↔ a, b share a column of `t`. -/
theorem swap_mem_colStab_iff (t : Tableau μ) (a b : Fin (nOf μ)) :
    Equiv.swap a b ∈ colStab t ↔ colPattern t a = colPattern t b := by
  rw [mem_colStab]; exact swap_smul_arrow_eq_iff _ a b

/-- `swap a b • ⟦s⟧ = ⟦s⟧ ↔ a, b share a row of `s`. -/
theorem swap_smul_mk_eq_iff (s : Tableau μ) (a b : Fin (nOf μ)) :
    (Equiv.swap a b) • (Tabloid.mk s) = Tabloid.mk s ↔ rowPattern s a = rowPattern s b := by
  rw [Tabloid.smul_mk, Tabloid.mk, Tabloid.mk, Quotient.eq, rowEquiv_iff, rowPattern_smul]
  exact swap_smul_arrow_eq_iff _ a b

/-- **STUB — the pure pigeonhole / SDR residual core.** If no column-permutation of
`t` is row-equivalent to `s`, then two labels share a column of `t` and a row of
`s`. A system-of-distinct-representatives / Hall-type existence statement at the
level of the `colPattern`/`rowPattern` functions — no tabloids, no swaps, no
representation theory. This is the single irreducible combinatorial residual of the
entire James submodule theorem. (Mathlib has no Hall's-marriage theorem and QOU no
column-length / staircase tableau infrastructure, so it is left cited here.) -/
theorem sdr_pattern_core (t s : Tableau μ)
    (hd : ∀ σ : colStab t, (σ : Perm (Fin (nOf μ))) • (Tabloid.mk t) ≠ Tabloid.mk s) :
    ∃ a b : Fin (nOf μ), a ≠ b ∧
      colPattern t a = colPattern t b ∧ rowPattern s a = rowPattern s b := by
  by_contra hcon
  push_neg at hcon
  have Hinj : Function.Injective
      (fun m : Fin (nOf μ) => (rowPattern s m, colPattern t m)) := by
    intro a b h
    by_contra hab
    obtain ⟨h1, h2⟩ := Prod.ext_iff.1 h
    exact hcon a b hab h2 h1
  obtain ⟨σ, hσcol, hσsmul⟩ := YoungStaircaseBound.exists_colStab_smul s t Hinj
  exact hd ⟨σ, hσcol⟩ hσsmul

omit [CharZero k] in
/-- **SDR existence at tabloid level**, derived sorry-free from `sdr_pattern_core`:
if `d` is not in the column-orbit of `t`, a transposition in `C_t` fixes `d`. -/
theorem sdr_core (t : Tableau μ) (d : Tabloid μ)
    (hd : ∀ σ : colStab t, (σ : Perm (Fin (nOf μ))) • (Tabloid.mk t) ≠ d) :
    ∃ a b : Fin (nOf μ), a ≠ b ∧ Equiv.swap a b ∈ colStab t ∧ (Equiv.swap a b) • d = d := by
  obtain ⟨s, rfl⟩ := d.exists_rep
  obtain ⟨a, b, hab, hcol, hrow⟩ := sdr_pattern_core t s hd
  exact ⟨a, b, hab, (swap_mem_colStab_iff t a b).2 hcol, (swap_smul_mk_eq_iff s a b).2 hrow⟩

omit [CharZero k] in
/-- The per-tabloid identity `Σ_{π∈C_t} sgn(π)·{π·d} = (e_t d)·e_t`, reduced
sorry-free-modulo-`sdr_core`. -/
theorem combId (t : Tableau μ) (d : Tabloid μ) :
    (∑ π : colStab t, ((Equiv.Perm.sign (π : Perm (Fin (nOf μ))) : ℤ) : k) •
        Finsupp.single ((π : Perm (Fin (nOf μ))) • d) (1 : k))
      = (Specht.polytabloid (k := k) t d) • Specht.polytabloid (k := k) t := by
  classical
  by_cases hA : ∃ σ : colStab t, (σ : Perm (Fin (nOf μ))) • (Tabloid.mk t) = d
  · -- Case A: `d = σ·{t}` for some `σ ∈ C_t`
    obtain ⟨σ, rfl⟩ := hA
    have hcoeff : Specht.polytabloid (k := k) t ((σ : Perm (Fin (nOf μ))) • (Tabloid.mk t))
        = ((Equiv.Perm.sign (σ : Perm (Fin (nOf μ))) : ℤ) : k) := by
      rw [Tabloid.smul_mk, polytabloid_coeff]
    rw [hcoeff, poly_kcast, Finset.smul_sum]
    rw [← Equiv.sum_comp (Equiv.mulRight σ⁻¹)
      (fun i : colStab t => ((Equiv.Perm.sign (i : Perm (Fin (nOf μ))) : ℤ) : k) •
        Finsupp.single ((i : Perm (Fin (nOf μ))) • ((σ : Perm (Fin (nOf μ))) • Tabloid.mk t)) (1 : k))]
    apply Finset.sum_congr rfl
    intro i _
    rw [show (Equiv.mulRight σ⁻¹) i = i * σ⁻¹ from rfl]
    have hidx : ((i * σ⁻¹ : colStab t) : Perm (Fin (nOf μ))) •
          ((σ : Perm (Fin (nOf μ))) • Tabloid.mk t)
        = (i : Perm (Fin (nOf μ))) • Tabloid.mk t := by
      rw [Subgroup.coe_mul, Subgroup.coe_inv, mul_smul, inv_smul_smul]
    have hsgn : ((Equiv.Perm.sign ((i * σ⁻¹ : colStab t) : Perm (Fin (nOf μ))) : ℤ) : k)
        = ((Equiv.Perm.sign (σ : Perm (Fin (nOf μ))) : ℤ) : k) *
            ((Equiv.Perm.sign (i : Perm (Fin (nOf μ))) : ℤ) : k) := by
      rw [Subgroup.coe_mul, Subgroup.coe_inv, map_mul, map_inv]
      rcases Int.units_eq_one_or (Equiv.Perm.sign (σ : Perm (Fin (nOf μ)))) with hσ | hσ <;>
        rcases Int.units_eq_one_or (Equiv.Perm.sign (i : Perm (Fin (nOf μ)))) with hi | hi <;>
        rw [hσ, hi] <;> norm_num
    rw [hidx, hsgn, smul_smul]
  · -- Case B: `d` not in the column orbit ⟹ both sides vanish
    push_neg at hA
    have hcoeff : Specht.polytabloid (k := k) t d = 0 := by
      rw [poly_kcast, Finsupp.finset_sum_apply]
      apply Finset.sum_eq_zero
      intro ν _
      rw [Finsupp.smul_apply, Finsupp.single_apply, if_neg (hA ν), smul_zero]
    rw [hcoeff, zero_smul]
    obtain ⟨a, b, hab, hmem, hfix⟩ := sdr_core t d hA
    set τ : colStab t := ⟨Equiv.swap a b, hmem⟩ with hτ
    refine Finset.sum_involution (fun π _ => π * τ) ?_ ?_ (fun π _ => Finset.mem_univ _) ?_
    · intro π _
      have hsign : (Equiv.Perm.sign ((π * τ : colStab t) : Perm (Fin (nOf μ))) : ℤ)
          = - (Equiv.Perm.sign (π : Perm (Fin (nOf μ))) : ℤ) := by
        rw [Subgroup.coe_mul, map_mul]
        show ((Equiv.Perm.sign (π : Perm (Fin (nOf μ))) * Equiv.Perm.sign (Equiv.swap a b)) : ℤ) = _
        rw [Equiv.Perm.sign_swap hab]
        push_cast
        ring
      have hsmul : ((π * τ : colStab t) : Perm (Fin (nOf μ))) • d = (π : Perm (Fin (nOf μ))) • d := by
        rw [Subgroup.coe_mul, mul_smul, hτ]
        show (π : Perm (Fin (nOf μ))) • ((Equiv.swap a b) • d) = _
        rw [hfix]
      rw [hsmul, hsign]
      rw [Int.cast_neg, neg_smul, add_neg_cancel]
    · intro π _ _ hcontra
      have hτ1 : τ = 1 := mul_left_cancel (a := π) (by rw [mul_one]; exact hcontra)
      have hswap : Equiv.swap a b = 1 := by
        have h : ((τ : colStab t) : Perm (Fin (nOf μ))) = 1 := by
          rw [hτ1]; exact OneMemClass.coe_one _
        simpa [hτ] using h
      exact hab (Equiv.swap_eq_one_iff.mp hswap)
    · intro π _
      ext1
      rw [Subgroup.coe_mul, Subgroup.coe_mul, hτ]
      show (π : Perm (Fin (nOf μ))) * (Equiv.swap a b) * (Equiv.swap a b) = (π : Perm (Fin (nOf μ)))
      rw [mul_assoc, Equiv.swap_mul_self, mul_one]

omit [CharZero k] in
theorem colAntisym_zero (t : Tableau μ) : colAntisym (k := k) t 0 = 0 := by
  simp only [colAntisym, map_zero, smul_zero, Finset.sum_const_zero]

omit [CharZero k] in
theorem colAntisym_add (t : Tableau μ) (u v : Mtab (k := k) μ) :
    colAntisym (k := k) t (u + v) = colAntisym (k := k) t u + colAntisym (k := k) t v := by
  simp only [colAntisym, map_add, smul_add, Finset.sum_add_distrib]

omit [CharZero k] in
/-- **James's sign lemma `κ_t u = ⟨u, e_t⟩ · e_t`** — `k`-linear-in-`u` lift of the
per-tabloid identity `combId`. Sorry-free modulo `sdr_core`. -/
theorem james_kernel_core (t : Tableau μ) (u : Mtab (k := k) μ) :
    colAntisym (k := k) t u
      = bilinM (k := k) μ u (Specht.polytabloid (k := k) t) • Specht.polytabloid (k := k) t := by
  refine Finsupp.induction_linear u ?_ ?_ ?_
  · rw [colAntisym_zero, map_zero, LinearMap.zero_apply, zero_smul]
  · intro u v hu hv
    rw [colAntisym_add, hu, hv, ← add_smul, ← LinearMap.add_apply, ← map_add]
  · intro d c
    rw [bilinM_single_left]
    simp only [colAntisym, Mtab.rep_single]
    have hterm : ∀ π : colStab t,
        ((Equiv.Perm.sign (π : Perm (Fin (nOf μ))) : ℤ)) •
            Finsupp.single ((π : Perm (Fin (nOf μ))) • d) c
          = c • (((Equiv.Perm.sign (π : Perm (Fin (nOf μ))) : ℤ) : k) •
              Finsupp.single ((π : Perm (Fin (nOf μ))) • d) (1 : k)) := by
      intro π
      rw [show Finsupp.single ((π : Perm (Fin (nOf μ))) • d) c
            = c • Finsupp.single ((π : Perm (Fin (nOf μ))) • d) (1 : k) by
            rw [Finsupp.smul_single, smul_eq_mul, mul_one],
        ← Int.cast_smul_eq_zsmul k, smul_comm]
    rw [Finset.sum_congr rfl (fun π _ => hterm π), ← Finset.smul_sum, combId, smul_smul]

/-! ## 5. The dichotomy (sorry-free modulo `sdr_core`) -/

omit [CharZero k] in
/-- **James's submodule theorem (the dichotomy), reduced.** Verbatim restatement
of `SpechtIrreducible.specht_submodule_dichotomy`, proved **sorry-free modulo**
the single elementary core `sdr_core` (via `james_kernel_core`). -/
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

/-! ## 6. The diagonal of the char-0 Gram core (sorry-free)

The full Gram core `specht_form_nondegenerate` needs the Gram **determinant**
(a product of hook lengths, nonzero in char 0). Its **diagonal** is sorry-free
here: `⟨e_t, e_t⟩ = |C_t|`, so `e_t ∉ (S^μ)ᗮ` in char 0. -/

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

/-! ## 7. The reduction: `specht_isSimple` from the dichotomy core + the Gram core -/

/-- **Irreducibility of `S^μ` (char 0)** — reduced `sorry`-free to `sdr_core`
(through the dichotomy) and `SpechtIrreducible.specht_form_nondegenerate` (the
char-0 Gram core). Reproduces the brick-2 statement
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
