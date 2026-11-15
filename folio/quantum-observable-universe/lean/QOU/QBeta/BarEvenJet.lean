import Mathlib.Algebra.DualNumber
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Tactic

/-!
# Bar-evenness forces stationarity — the algebraic statement

Categorify audit 2026-11-15, item 5 (`/mnt/project-files/qou-categorify-audit/`). The real
theorem `BarEvenForcesStationarity.deriv_at_one_eq_zero_of_barEven` is one instance of a
statement that needs no analysis.

* `FixedPointJet A K`: a ring `A` with an involution `ι` and a ring map `jet : A → K[ε]`
  (value plus first-order part at a fixed point) on which `ι` acts by `ε ↦ −ε`.
* `snd_jet_eq_zero_of_invariant`: if `ι f = f` and `2` is a unit in `K`, the first-order part
  of `jet f` is `0`. Pure algebra.
* **Algebraic instance** `laurentFixedPointJet`: Laurent polynomials over any commutative ring,
  `ι = invert` (`q ↦ q⁻¹`), `jet` = evaluation at `q = 1 + ε`.
* **Analytic instance** `realFixedPointJet` (in `BarEvenJetArchimedean`, split per §7c): real functions differentiable at `1`,
  `jet f = f(1) + f'(1) ε`. The analysis is exactly the product rule and `(q⁻¹)′(1) = −1`.
  `deriv_at_one_eq_zero_of_barEven'` recovers the original theorem (global form).

Not done here: vanishing orders `≥ 2` (`WeakVertexCouplingNormalisationArchimedean`) need
higher jets `K[ε]/(ε^{k+1})`, and the four separate `BarInvolution` structures in the library
are not unified (that refactor waits on the owner).

-- Ref: [leitner2026] /mnt/project-files/qou-categorify-audit/analytic-steps-ranked-2026-11-15.md item 5
-/
namespace QOU.QBeta.BarEvenJet

open DualNumber TrivSqZeroExt LaurentPolynomial

variable {K : Type*} [CommRing K]

/-- Conjugation on dual numbers, `a + bε ↦ a − bε`. -/
def dconj : DualNumber K →+* DualNumber K where
  toFun x := (x.fst, -x.snd)
  map_one' := by ext <;> simp
  map_mul' x y := by
    ext
    · simp
    · simp only [DualNumber.snd_mul, TrivSqZeroExt.fst_mul, TrivSqZeroExt.fst_mk,
        TrivSqZeroExt.snd_mk]
      ring
  map_zero' := by ext <;> simp
  map_add' x y := by ext <;> simp [add_comm]

@[simp] theorem fst_dconj (x : DualNumber K) : (dconj x).fst = x.fst := rfl
@[simp] theorem snd_dconj (x : DualNumber K) : (dconj x).snd = -x.snd := rfl

/-- **A first-order jet at a fixed point of an involution.**  `jet : A → K[ε]` reads off
value and first derivative at the fixed point, and the involution acts on the tangent line
by `−1`: `jet ∘ ι = dconj ∘ jet`. -/
structure FixedPointJet (A : Type*) [CommRing A] (K : Type*) [CommRing K] where
  ι : A →+* A
  jet : A →+* DualNumber K
  jet_ι : ∀ f, jet (ι f) = dconj (jet f)

/-- **Bar-evenness forces stationarity, for any jet.** If `ι f = f` and `2` is a unit,
the first-order part of the jet of `f` is zero. Pure algebra. -/
theorem snd_jet_eq_zero_of_invariant {A : Type*} [CommRing A] (J : FixedPointJet A K)
    (h2 : IsUnit (2 : K)) {f : A} (hf : J.ι f = f) : (J.jet f).snd = 0 := by
  have h := congrArg TrivSqZeroExt.snd (J.jet_ι f)
  rw [hf, snd_dconj] at h
  have h2s : (2 : K) * (J.jet f).snd = 0 := by linear_combination h
  exact (h2.mul_right_eq_zero).mp h2s

/-! ## Instance 1 (algebraic): Laurent polynomials over any commutative ring -/

/-- `1 + ε`, a unit of `K[ε]` with inverse `1 − ε`. -/
def onePlusEps : (DualNumber K)ˣ where
  val := 1 + ε
  inv := 1 - ε
  val_inv := by ext <;> simp [TrivSqZeroExt.fst_mul]
  inv_val := by ext <;> simp [TrivSqZeroExt.fst_mul]

theorem dconj_onePlusEps : dconj ((onePlusEps : (DualNumber K)ˣ) : DualNumber K)
    = ((onePlusEps⁻¹ : (DualNumber K)ˣ) : DualNumber K) := by
  ext <;> simp [onePlusEps, dconj]

/-- `dconj` sends `(1+ε)^n` to `(1+ε)^(−n)`. -/
theorem dconj_zpow (n : ℤ) : dconj (((onePlusEps : (DualNumber K)ˣ) ^ n : (DualNumber K)ˣ) :
    DualNumber K) = ((onePlusEps ^ (-n) : (DualNumber K)ˣ) : DualNumber K) := by
  -- map the unit through the ring hom
  have key : (Units.map (dconj (K := K)).toMonoidHom) onePlusEps = onePlusEps⁻¹ := by
    exact Units.ext (dconj_onePlusEps (K := K))
  have hz : (Units.map (dconj (K := K)).toMonoidHom) ((onePlusEps (K := K)) ^ n)
      = ((Units.map (dconj (K := K)).toMonoidHom) (onePlusEps (K := K))) ^ n :=
    map_zpow _ _ n
  rw [key] at hz
  have := congrArg (fun u : (DualNumber K)ˣ => (u : DualNumber K)) hz
  simp only [Units.coe_map] at this
  calc dconj (((onePlusEps : (DualNumber K)ˣ) ^ n : (DualNumber K)ˣ) : DualNumber K)
      = ((onePlusEps⁻¹ ^ n : (DualNumber K)ˣ) : DualNumber K) := this
    _ = ((onePlusEps ^ (-n) : (DualNumber K)ˣ) : DualNumber K) := by rw [inv_zpow']

/-- The jet at `q = 1` of a Laurent polynomial: evaluate at `q = 1 + ε`. -/
noncomputable def laurentJet : K[T;T⁻¹] →+* DualNumber K :=
  eval₂ (algebraMap K (DualNumber K)) onePlusEps

/-- **The Laurent instance.** The bar involution `q ↦ q⁻¹` and evaluation at `1 + ε`. -/
noncomputable def laurentFixedPointJet : FixedPointJet K[T;T⁻¹] K where
  ι := (invert : K[T;T⁻¹] ≃ₐ[K] K[T;T⁻¹]).toRingEquiv.toRingHom
  jet := laurentJet
  jet_ι f := by
    induction f using LaurentPolynomial.induction_on' with
    | add p q hp hq =>
        simp only [map_add] at hp hq ⊢
        rw [hp, hq]
    | C_mul_T n a =>
        have hι : ∀ p : K[T;T⁻¹],
            (invert : K[T;T⁻¹] ≃ₐ[K] K[T;T⁻¹]).toRingEquiv.toRingHom p = invert p := fun _ => rfl
        simp only [hι, map_mul, invert_C, invert_T, laurentJet, eval₂_C, eval₂_T]
        rw [dconj_zpow]
        congr 1
        ext <;> simp [dconj, TrivSqZeroExt.algebraMap_eq_inl]

/-- **Corollary.** A bar-even Laurent polynomial (`f(q⁻¹) = f(q)`) over a ring where `2` is a
unit has zero first-order part at `q = 1`. No analysis. -/
theorem laurent_snd_jet_eq_zero_of_barEven (h2 : IsUnit (2 : K)) {f : K[T;T⁻¹]}
    (hf : invert f = f) : (laurentJet f).snd = 0 :=
  snd_jet_eq_zero_of_invariant laurentFixedPointJet h2 hf


end QOU.QBeta.BarEvenJet
