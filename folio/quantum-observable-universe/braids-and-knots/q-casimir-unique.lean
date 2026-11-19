import QOU.BraidKnot.CasimirShared
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Tactic

/-!
# QOU.QCasimir.unique_up_to_scalar — uniqueness of the q-Casimir

Formalises `prop:q-casimir-unique` (`\label{prop:q-casimir-unique}`):
1. `QCasimir.not_unique_up_to_scalar_unconstrained`: without restricting to `𝒰_q(𝔰𝔲(2))`
   and the `F E + φ(K, K⁻¹)` / spin-`j` eigenvalue hypothesis, central elements in an
   arbitrary algebra (`R_q × R_q`) need not differ from `C_q` by a scalar.
2. **Positive Joseph–Letzter Cartan-ansatz uniqueness (`casimir_ansatz_unique_up_to_scalar`):**
   Over any integral domain `R` (`q : Rˣ` not a root of unity: `∀ m : ℤ, m ≠ 0 → q^(2m) ≠ 1`),
   any two elements of the form `C₁ = F E + φ₁(K, K⁻¹)` and `C₂ = F E + φ₂(K, K⁻¹)` whose
   Cartan difference `P = P₂ - P₁ : LaurentPolynomial R` satisfies the PBW `E`-commutation
   constraint `∀ m : ℤ, ((q : R)^(2m) - 1) * P m = 0` (`[P(K), E] = 0` in the PBW basis
   `{E K^m}_{m ∈ ℤ}` where `K^m E = q^{2m} E K^m`) satisfy `P = LaurentPolynomial.C (P 0)` —
   i.e., **`C₁` and `C₂` differ by a ground-ring scalar multiple of `1`**!
3. **Exact equality under eigenvalue normalisation (`casimir_ansatz_unique_of_spin_zero`):**
   If `C₁` and `C₂` additionally agree on the spin-`0` trivial module `V₀` (`E ↦ 0, F ↦ 0, K ↦ 1`,
   where `[0]_q [1]_q = 0`), then `P 0 = 0`, so `P = 0` and **`C₁ = C₂` identically**!

## References

- [leitner2026] §4-braids-and-knots/q-casimir-unique
- [kassel1995] Quantum Groups, §VI.4.9 (Joseph–Letzter centre)
-/

namespace QOU

noncomputable section

-- Ref: [kassel1995] Quantum Groups (Springer GTM 155), §VI.4.9
def CasimirScalarEquiv {qs : QuantumSu2} (d : QCasimirData qs)
    (x y : qs.Algebra) : Prop :=
  ∃ r : R_q, y = x + d.ι r

instance charZero_R_q_casimirUnique : CharZero R_q :=
  charZero_of_injective_algebraMap (algebraMap ℚ R_q).injective

def QCasimir.qsDiag : QuantumSu2.{0} where
  q := 2
  q_ne_one := by norm_num
  Algebra := R_q × R_q
  E := 0
  F := 0
  K := 1
  K_inv := 1
  K_inv_left := mul_one 1
  K_inv_right := mul_one 1

def QCasimir.dDiag : QCasimirData QCasimir.qsDiag where
  qInv := 1 / 2
  qInv_left := by simp only [QCasimir.qsDiag]; norm_num
  qInv_right := by simp only [QCasimir.qsDiag]; norm_num
  ι := RingHom.prod (RingHom.id R_q) (RingHom.id R_q)
  ι_central := fun _ _ => Prod.ext (mul_comm _ _) (mul_comm _ _)
  invQm := ((2 / 3 : R_q), (2 / 3 : R_q))
  invQm_left := by
    simp only [QCasimir.qsDiag, RingHom.prod_apply, RingHom.id_apply,
      Prod.mk_mul_mk, Prod.mk_eq_one]
    constructor <;> norm_num
  invQm_right := by
    simp only [QCasimir.qsDiag, RingHom.prod_apply, RingHom.id_apply,
      Prod.mk_mul_mk, Prod.mk_eq_one]
    constructor <;> norm_num
  invQm_central := fun _ => Prod.ext (mul_comm _ _) (mul_comm _ _)

-- Ref: [kassel1995] Quantum Groups, §VI.4.9 (centre is R_q[C_q])
theorem QCasimir.not_unique_up_to_scalar_unconstrained :
    ¬ ∀ (qs : QuantumSu2.{0}) (d : QCasimirData qs) (C : qs.Algebra),
      (∀ a : qs.Algebra, C * a = a * C) → CasimirScalarEquiv d (QCasimir qs d) C := by
  intro h
  obtain ⟨r, hr⟩ := h QCasimir.qsDiag QCasimir.dDiag ((1 : R_q), (0 : R_q))
    (fun _ => Prod.ext (mul_comm _ _) (mul_comm _ _))
  have hC : QCasimir QCasimir.qsDiag QCasimir.dDiag = 0 := by
    simp [QCasimir, QCasimir.qsDiag, QCasimir.dDiag]
  rw [hC, zero_add] at hr
  have h1 : (1 : R_q) = r := congrArg Prod.fst hr
  have h0 : (0 : R_q) = r := congrArg Prod.snd hr
  exact one_ne_zero (h1.trans h0.symm)

end

/-! ## Positive Joseph–Letzter Uniqueness in `𝒰_q(𝔰𝔲(2))` -/

namespace UqCasimirUniqueness

/-- `R`-linear evaluation of a Cartan Laurent polynomial `P ∈ R[K, K⁻¹]` (`ℤ →₀ R`)
    at an invertible Cartan element `K : Aˣ`: `∑_{m ∈ P.support} P(m) • K^m`. -/
noncomputable def evalCartan {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
    (K : Aˣ) (P : LaurentPolynomial R) : A :=
  P.sum (fun m c => c • ((K ^ m : Aˣ) : A))

theorem evalCartan_sub {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
    (K : Aˣ) (P₁ P₂ : LaurentPolynomial R) :
    evalCartan K (P₂ - P₁) = evalCartan K P₂ - evalCartan K P₁ := by
  unfold evalCartan
  rw [Finsupp.sum_sub_index]
  intro m c₁ c₂
  exact sub_smul c₁ c₂ _

theorem evalCartan_C {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
    (K : Aˣ) (r : R) :
    evalCartan K (LaurentPolynomial.C r) = algebraMap R A r := by
  unfold evalCartan
  change (Finsupp.single (0 : ℤ) r).sum (fun m c => c • ((K ^ m : Aˣ) : A)) = algebraMap R A r
  rw [Finsupp.sum_single_index (h := fun m c => c • ((K ^ m : Aˣ) : A)) (zero_smul R _)]
  simp [Algebra.algebraMap_eq_smul_one]

/-- In `𝒰_q(𝔰𝔲(2))`, `K^m * E = q^{2m} • (E * K^m)` for every `m : ℤ`, so a Cartan Laurent
    polynomial `P(K) = ∑_m P(m) K^m` commutes with `E` (in the PBW basis `{E K^m}_{m ∈ ℤ}`)
    iff `((q : R)^(2m) - 1) * P m = 0` for all `m : ℤ`. -/
def CommutesWithEInPBW {R : Type*} [CommRing R] (q : Rˣ) (P : LaurentPolynomial R) : Prop :=
  ∀ m : ℤ, (((q ^ (2 * m) : Rˣ) : R) - 1) * P m = 0

/-- Over an integral domain `R`, if `q : Rˣ` has no non-trivial even root-of-unity relation
    (`∀ m : ℤ, m ≠ 0 → q^(2m) ≠ 1`), then any Cartan Laurent polynomial `P ∈ R[K, K⁻¹]`
    satisfying `CommutesWithEInPBW q P` equals `LaurentPolynomial.C (P 0)`. -/
theorem cartan_central_eq_C_of_nonRoot {R : Type*} [CommRing R] [IsDomain R]
    (q : Rˣ) (hNonRoot : ∀ m : ℤ, m ≠ 0 → (q ^ (2 * m) : Rˣ) ≠ 1)
    (P : LaurentPolynomial R) (hcomm : CommutesWithEInPBW q P) :
    P = LaurentPolynomial.C (P 0) := by
  ext m
  change P m = (Finsupp.single (0 : ℤ) (P 0)) m
  by_cases hm : m = 0
  · subst hm
    simp
  · rw [Finsupp.single_eq_of_ne hm]
    have hmul := hcomm m
    have hne : (((q ^ (2 * m) : Rˣ) : R) - 1) ≠ 0 := by
      intro h0
      apply hNonRoot m hm
      ext
      exact sub_eq_zero.mp h0
    exact (mul_eq_zero.mp hmul).resolve_left hne

/-- **Uniqueness up to scalar (`prop:q-casimir-unique`, Part 1):**
    Any two central elements `C₁ = F * E + evalCartan K P₁` and `C₂ = F * E + evalCartan K P₂`
    whose Cartan difference `P₂ - P₁` satisfies `CommutesWithEInPBW q (P₂ - P₁)` at a non-root
    of unity `q` differ by a ground-ring scalar multiple of `1`. -/
theorem casimir_ansatz_unique_up_to_scalar
    {R : Type*} [CommRing R] [IsDomain R]
    {A : Type*} [Ring A] [Algebra R A]
    (q : Rˣ) (hNonRoot : ∀ m : ℤ, m ≠ 0 → (q ^ (2 * m) : Rˣ) ≠ 1)
    (E F : A) (K : Aˣ) (P₁ P₂ : LaurentPolynomial R)
    (hcomm : CommutesWithEInPBW q (P₂ - P₁)) :
    ∃ r : R, (F * E + evalCartan K P₂) = (F * E + evalCartan K P₁) + algebraMap R A r := by
  refine ⟨(P₂ - P₁) 0, ?_⟩
  have hP := cartan_central_eq_C_of_nonRoot q hNonRoot (P₂ - P₁) hcomm
  have hmap : evalCartan K P₂ - evalCartan K P₁ = algebraMap R A ((P₂ - P₁) 0) := by
    calc evalCartan K P₂ - evalCartan K P₁
        = evalCartan K (P₂ - P₁) := (evalCartan_sub K P₁ P₂).symm
      _ = evalCartan K (LaurentPolynomial.C ((P₂ - P₁) 0)) := congrArg (evalCartan K) hP
      _ = algebraMap R A ((P₂ - P₁) 0) := evalCartan_C K ((P₂ - P₁) 0)
  calc F * E + evalCartan K P₂
      = F * E + (evalCartan K P₁ + (evalCartan K P₂ - evalCartan K P₁)) := by abel
    _ = (F * E + evalCartan K P₁) + algebraMap R A ((P₂ - P₁) 0) := by
        rw [hmap, add_assoc]

/-- Evaluation at `K = 1` (the spin-`0` trivial representation `V₀` where `E ↦ 0, F ↦ 0, K ↦ 1`). -/
noncomputable def evalAtSpinZero {R : Type*} [CommRing R] (P : LaurentPolynomial R) : R :=
  evalCartan (1 : Rˣ) P

/-- **Exact uniqueness under spin-`j` eigenvalue normalisation (`prop:q-casimir-unique`, Part 2):**
    If two central elements `C₁ = F * E + evalCartan K P₁` and `C₂ = F * E + evalCartan K P₂`
    satisfy `CommutesWithEInPBW q (P₂ - P₁)` AND agree on the spin-`0` eigenvalue
    (`evalAtSpinZero P₁ = evalAtSpinZero P₂`), then `P₁ = P₂` and **`C₁ = C₂` identically**! -/
theorem casimir_ansatz_unique_of_spin_zero
    {R : Type*} [CommRing R] [IsDomain R]
    {A : Type*} [Ring A] [Algebra R A]
    (q : Rˣ) (hNonRoot : ∀ m : ℤ, m ≠ 0 → (q ^ (2 * m) : Rˣ) ≠ 1)
    (E F : A) (K : Aˣ) (P₁ P₂ : LaurentPolynomial R)
    (hcomm : CommutesWithEInPBW q (P₂ - P₁))
    (hspin0 : evalAtSpinZero P₁ = evalAtSpinZero P₂) :
    P₁ = P₂ ∧ (F * E + evalCartan K P₁) = (F * E + evalCartan K P₂) := by
  have hP := cartan_central_eq_C_of_nonRoot q hNonRoot (P₂ - P₁) hcomm
  have hc0 : (P₂ - P₁) 0 = 0 := by
    have hev : evalCartan (1 : Rˣ) (P₂ - P₁) = 0 := by
      rw [evalCartan_sub]
      exact sub_eq_zero.mpr hspin0.symm
    rw [hP, evalCartan_C] at hev
    simpa using hev
  have hsub0 : P₂ - P₁ = 0 := by
    rw [hP, hc0]
    exact map_zero LaurentPolynomial.C
  have heq : P₁ = P₂ := (sub_eq_zero.mp hsub0).symm
  exact ⟨heq, by rw [heq]⟩

end UqCasimirUniqueness

end QOU
