import QCalculus.HabiroDoubleTwist

/-!
# QCalculus.HabiroBarInvolution — the bar involution `q ↦ q⁻¹` on the Habiro ring

Bean `qou-28qh`, phase 5. Over any commutative ring `R`.

At level `N` the substitution `q ↦ q⁻¹` (with `q⁻¹` the level inverse
`qInvPoly N`) kills `(q;q)_N`, because `(q⁻¹;q⁻¹)_N = (-1)^N q^{-N(N+1)/2} (q;q)_N`.
The level maps are compatible (inverses are unique), so they assemble to a ring
endomorphism `bar` of `R̂[q]` with `bar q = q⁻¹`, and `bar ∘ bar = id`.

On cyclotomic series, `bar (∑ a_n (q;q)_n) = ∑ bar(a_n) (q⁻¹;q⁻¹)_n`
(`bar_series`). Consequences:

* `bar_figureEight`: the figure-eight element is bar invariant, the algebraic
  form of the amphichirality of `4₁` (`J_N(K; q⁻¹) = J_N(K*; q)`,
  [lovejoy-osburn, eq. (1.3)]). At a root of unity with an involution
  `ζ ↦ ζ⁻¹` this is the reality of `⟨4₁⟩_N`, used on the analytic side by
  `KashaevReflection`/`KashaevHermitianCertificate`; here it holds in the ring.
* `bar_trefoil`: the trefoil element goes to `∑ (q⁻¹;q⁻¹)_n`, its mirror.

No analytic API, no empirical value.

-- Ref: [habiro2004cyclotomic]
-- Ref: [lovejoy-osburn]
-/

namespace QCalculus.HabiroSeries

open Polynomial Finset

variable {R : Type*} [CommRing R]

/-- In `R[q]/((q;q)_N)`, the level inverse `q⁻¹` substituted into `(q;q)_N` vanishes. -/
theorem aeval_qInvPoly_qPoch (N : ℕ) :
    aeval (Ideal.Quotient.mk (level R N) (qInvPoly N)) (qPoch R N) = 0 := by
  have hu : Ideal.Quotient.mk (level R N) X * Ideal.Quotient.mk (level R N) (qInvPoly N) = 1 :=
    mk_X_mul_qInvPoly N
  have h := poch_of_mul_eq_one hu N
  have hp : aeval (Ideal.Quotient.mk (level R N) (qInvPoly N)) (qPoch R N) =
      poch (Ideal.Quotient.mk (level R N) (qInvPoly N)) N := by
    simp [qPoch, poch, map_prod]
  have h0 : poch (Ideal.Quotient.mk (level R N) X) N = 0 := by
    rw [← mk_qPoch_eq_zero (R := R) (le_refl N), qPoch, poch, map_prod]; simp
  rw [hp, h, h0, mul_zero]

/-- The level map `q ↦ q⁻¹` on `R[q]/((q;q)_N)`. -/
noncomputable def barLevel (N : ℕ) : R[X] ⧸ level R N →+* R[X] ⧸ level R N :=
  Ideal.Quotient.lift (level R N)
    (aeval (Ideal.Quotient.mk (level R N) (qInvPoly N)) : R[X] →ₐ[R] R[X] ⧸ level R N).toRingHom
    (fun p hp => by
      obtain ⟨r, rfl⟩ := Ideal.mem_span_singleton.mp hp
      simp [aeval_qInvPoly_qPoch])

theorem barLevel_mk (N : ℕ) (p : R[X]) :
    barLevel N (Ideal.Quotient.mk (level R N) p) =
      aeval (Ideal.Quotient.mk (level R N) (qInvPoly N)) p := rfl

/-- The level inverses are compatible: `q⁻¹` at level `M` reduces to `q⁻¹` at level `N`. -/
theorem bond_mk_qInvPoly {N M : ℕ} (h : N ≤ M) :
    Ideal.Quotient.mk (level R N) (qInvPoly M) = Ideal.Quotient.mk (level R N) (qInvPoly N) := by
  have h1 := congrArg (bond (R := R) h) (mk_X_mul_qInvPoly (R := R) M)
  rw [map_mul, map_one, Ideal.Quotient.factor_mk, Ideal.Quotient.factor_mk] at h1
  have h2 := mk_X_mul_qInvPoly (R := R) N
  calc Ideal.Quotient.mk (level R N) (qInvPoly M)
      = Ideal.Quotient.mk (level R N) (qInvPoly M) *
          (Ideal.Quotient.mk (level R N) X * Ideal.Quotient.mk (level R N) (qInvPoly N)) := by
        rw [h2, mul_one]
    _ = (Ideal.Quotient.mk (level R N) X * Ideal.Quotient.mk (level R N) (qInvPoly M)) *
          Ideal.Quotient.mk (level R N) (qInvPoly N) := by ring
    _ = _ := by rw [h1, one_mul]

theorem bond_barLevel {N M : ℕ} (h : N ≤ M) (y : R[X] ⧸ level R M) :
    bond h (barLevel M y) = barLevel N (bond h y) := by
  obtain ⟨p, rfl⟩ := Ideal.Quotient.mk_surjective y
  rw [barLevel_mk, Ideal.Quotient.factor_mk, barLevel_mk]
  have : (bond (R := R) h).comp
      ((aeval (Ideal.Quotient.mk (level R M) (qInvPoly M)) :
        R[X] →ₐ[R] R[X] ⧸ level R M) : R[X] →+* R[X] ⧸ level R M) =
      ((aeval (Ideal.Quotient.mk (level R N) (qInvPoly N)) :
        R[X] →ₐ[R] R[X] ⧸ level R N) : R[X] →+* R[X] ⧸ level R N) := by
    apply Polynomial.ringHom_ext
    · intro r
      simp only [RingHom.comp_apply, RingHom.coe_coe, aeval_C]
      rfl
    · simp only [RingHom.comp_apply, RingHom.coe_coe, aeval_X, Ideal.Quotient.factor_mk]
      exact bond_mk_qInvPoly h
  exact congrArg (fun f : R[X] →+* R[X] ⧸ level R N => f p) this

/-- **The bar involution** `q ↦ q⁻¹` on `R̂[q]`. -/
noncomputable def bar : Habiro R →+* Habiro R :=
  RingHom.codRestrict
    ((Pi.ringHom fun N => (barLevel N).comp
      ((Pi.evalRingHom (fun N => R[X] ⧸ level R N) N))).comp (Habiro R).subtype)
    (Habiro R)
    (fun x N M h => by
      simp only [RingHom.comp_apply, Pi.ringHom_apply, Pi.evalRingHom_apply,
        Subring.coe_subtype]
      rw [bond_barLevel, compat])

theorem bar_apply (x : Habiro R) (N : ℕ) :
    ((bar x : Habiro R) : ∀ N, R[X] ⧸ level R N) N =
      barLevel N ((x : ∀ N, R[X] ⧸ level R N) N) := rfl

theorem bar_q : bar (q : Habiro R) = qInv := by
  apply Subtype.ext; funext N
  rw [bar_apply, q, ofPoly_apply, barLevel_mk, aeval_X]; rfl

theorem bar_qInv : bar (qInv : Habiro R) = q := by
  have h := congrArg bar (q_mul_qInv (R := R))
  rw [map_mul, map_one, bar_q] at h
  have h2 : (qInv : Habiro R) * q = 1 := by rw [mul_comm]; exact q_mul_qInv
  calc bar (qInv : Habiro R) = bar qInv * (qInv * q) := by rw [h2, mul_one]
    _ = (qInv * bar qInv) * q := by ring
    _ = q := by rw [h, one_mul]

theorem bar_poch_q (n : ℕ) : bar (poch (q : Habiro R) n) = poch qInv n := by
  rw [map_poch, bar_q]

/-- **Bar on cyclotomic series**: `bar (∑ a_n (q;q)_n) = ∑ bar(a_n) (q⁻¹;q⁻¹)_n`,
    which is again a cyclotomic series by `poch_qInv`. -/
theorem bar_series (a : ℕ → Habiro R) :
    bar (series a) =
      series fun n => bar (a n) * ((-1) ^ n * qInv ^ (n * (n + 1) / 2)) := by
  apply Subtype.ext; funext N
  rw [bar_apply, series_apply, series_apply_eq_trunc _ (le_refl N), seriesLevel, map_sum,
    val_sum]
  refine sum_congr rfl fun n _ => ?_
  rw [map_mul, val_mul, val_mul, ← bar_apply, ← ofPoly_qPoch]
  have hq : barLevel N (Ideal.Quotient.mk (level R N) (qPoch R n)) =
      ((bar (ofPoly (qPoch R n)) : Habiro R) : ∀ N, R[X] ⧸ level R N) N := rfl
  rw [hq, ofPoly_qPoch, bar_poch_q, poch_qInv, val_mul, val_mul]
  ring

/-- **The figure-eight element is bar invariant** (amphichirality of `4₁`). -/
theorem bar_figureEight : bar (figureEight : Habiro R) = figureEight := by
  rw [figureEight, bar_series]
  congr 1; funext n
  rw [map_poch, bar_qInv, poch_qInv]
  ring

/-- **The trefoil goes to its mirror**: `bar (∑ (q;q)_n) = ∑ (q⁻¹;q⁻¹)_n`. -/
theorem bar_trefoil :
    bar (trefoil : Habiro R) = series fun n => (-1) ^ n * qInv ^ (n * (n + 1) / 2) := by
  rw [trefoil, bar_series]
  congr 1; funext n
  rw [map_one, one_mul]

/-- `bar` is an involution. -/
theorem bar_bar (x : Habiro R) : bar (bar x) = x := by
  apply Subtype.ext; funext N
  rw [bar_apply, bar_apply]
  obtain ⟨p, hp⟩ := Ideal.Quotient.mk_surjective ((x : ∀ N, R[X] ⧸ level R N) N)
  rw [← hp, barLevel_mk]
  have : (barLevel (R := R) N).comp
      ((aeval (Ideal.Quotient.mk (level R N) (qInvPoly N)) :
        R[X] →ₐ[R] R[X] ⧸ level R N) : R[X] →+* R[X] ⧸ level R N) =
      Ideal.Quotient.mk (level R N) := by
    apply Polynomial.ringHom_ext
    · intro r
      simp only [RingHom.comp_apply, RingHom.coe_coe, aeval_C]
      rw [show (algebraMap R (R[X] ⧸ level R N)) r = Ideal.Quotient.mk (level R N) (C r) from rfl,
        barLevel_mk, aeval_C]
      rfl
    · simp only [RingHom.comp_apply, RingHom.coe_coe, aeval_X]
      have h := congrArg (fun x : Habiro R => (x : ∀ N, R[X] ⧸ level R N) N)
        (bar_qInv (R := R))
      simpa [bar_apply, q, qInv] using h
  exact congrArg (fun f : R[X] →+* R[X] ⧸ level R N => f p) this

end QCalculus.HabiroSeries
