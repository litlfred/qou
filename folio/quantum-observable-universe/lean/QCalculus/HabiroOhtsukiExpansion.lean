import QCalculus.HabiroCyclotomicSeries

/-!
# QCalculus.HabiroOhtsukiExpansion — the expansion of a Habiro element at `q = 1 + h`

Bean `qou-28qh`, phase 4. Over any commutative ring `R`.

Substituting `q = 1 + h` sends `(q;q)_N` into `(h^N)`, because every factor
`1 - (1+h)^k` is divisible by `h`. So each level `R[q]/((q;q)_N)` maps to
`R[h]/(h^N)`, compatibly in `N`, and the Habiro ring maps to the `h`-adic
inverse limit

  `ohtsuki : R̂[q] →+* lim_N R[h]/(h^N)`   (the latter is `R[[h]]`).

This is the expansion of a Habiro element around the trivial connection
(`q = 1`). For the Kashaev elements it is the Ohtsuki series of the trivial
connection [habiro2004cyclotomic]. It is **not** the asymptotic series at the
hyperbolic saddle (the `κ₁, κ₂` of `QOU.BringsSurface.OhtsukiKappaFormal`); the
two are related only through the modularity of the Kashaev invariant
(Garoufalidis–Zagier), which is not algebraic and is not claimed here.

The map is a ring homomorphism, so every algebraic identity between Habiro
elements is inherited by the expansions, with no convergence argument: the
`h`-adic "limit" is again an inverse limit of rings.

## Results (sorry-free)

* `x_pow_dvd_qPoch_comp`: `h^N ∣ (q;q)_N(1+h)`.
* `ohtsuki : Habiro R →+* Ohtsuki R`.
* `ohtsuki_series_apply`: at level `N`, a cyclotomic series becomes the finite
  sum `∑_{n<N} a_n(1+h) (q;q)_n(1+h)`.
* `ohtsuki_q`: `q ↦ 1 + h`.
* Non-vacuity at level 2: `trefoil ↦ 1 - h` and `figureEight ↦ 1` mod `h²`.

No analytic API, no empirical value.

-- Ref: [habiro2004cyclotomic]
-- Ref: [zagier2001strange]
-/

namespace QCalculus.HabiroSeries

open Polynomial Finset

variable {R : Type*} [CommRing R]

/-- The substitution `q ↦ 1 + h` on polynomials. -/
noncomputable def shiftOne : R[X] →+* R[X] := compRingHom (X + 1)

theorem shiftOne_apply (p : R[X]) : shiftOne p = p.comp (X + 1) := rfl

/-- `h ∣ 1 - (1+h)^k`. -/
theorem x_dvd_one_sub_shift (k : ℕ) : (X : R[X]) ∣ 1 - (X + 1) ^ k := by
  have h := sub_dvd_pow_sub_pow (X + 1 : R[X]) 1 k
  rw [add_sub_cancel_right, one_pow] at h
  rw [← neg_sub]; exact dvd_neg.mpr h

/-- **`h^N ∣ (q;q)_N(1+h)`.** -/
theorem x_pow_dvd_qPoch_comp (N : ℕ) : (X : R[X]) ^ N ∣ shiftOne (qPoch R N) := by
  rw [qPoch, map_prod]
  have : (X : R[X]) ^ N = ∏ _k ∈ range N, (X : R[X]) := by rw [prod_const, card_range]
  rw [this]
  refine prod_dvd_prod_of_dvd _ _ fun k _ => ?_
  simp only [shiftOne, coe_compRingHom_apply, sub_comp, one_comp, pow_comp, X_comp]
  exact x_dvd_one_sub_shift (k + 1)

variable (R)

/-- The `h`-adic level ideal `(h^N)`. -/
noncomputable abbrev hLevel (N : ℕ) : Ideal R[X] := Ideal.span {X ^ N}

variable {R}

theorem hLevel_le {N M : ℕ} (h : N ≤ M) : hLevel R M ≤ hLevel R N :=
  Ideal.span_singleton_le_span_singleton.mpr (pow_dvd_pow X h)

variable (R)

/-- **The `h`-adic completion** `lim_N R[h]/(h^N)` as compatible threads. -/
noncomputable def Ohtsuki : Subring (∀ N, R[X] ⧸ hLevel R N) where
  carrier := { x | ∀ N M (h : N ≤ M), Ideal.Quotient.factor (hLevel_le h) (x M) = x N }
  mul_mem' {x y} hx hy N M h := by simp only [Pi.mul_apply, map_mul, hx N M h, hy N M h]
  one_mem' N M h := by simp only [Pi.one_apply, map_one]
  add_mem' {x y} hx hy N M h := by simp only [Pi.add_apply, map_add, hx N M h, hy N M h]
  zero_mem' N M h := by simp only [Pi.zero_apply, map_zero]
  neg_mem' {x} hx N M h := by simp only [Pi.neg_apply, map_neg, hx N M h]

variable {R}

/-- The level map `R[q]/((q;q)_N) → R[h]/(h^N)`, `q ↦ 1 + h`. -/
noncomputable def levelShift (N : ℕ) : R[X] ⧸ level R N →+* R[X] ⧸ hLevel R N :=
  Ideal.Quotient.lift (level R N) ((Ideal.Quotient.mk (hLevel R N)).comp shiftOne)
    (fun p hp => by
      obtain ⟨r, rfl⟩ := Ideal.mem_span_singleton.mp hp
      rw [RingHom.comp_apply, map_mul, Ideal.Quotient.eq_zero_iff_mem]
      exact Ideal.mul_mem_right _ _ (Ideal.mem_span_singleton.mpr (x_pow_dvd_qPoch_comp N)))

theorem levelShift_mk (N : ℕ) (p : R[X]) :
    levelShift N (Ideal.Quotient.mk (level R N) p) =
      Ideal.Quotient.mk (hLevel R N) (shiftOne p) := rfl

/-- **The expansion at `q = 1 + h`** as a ring map `R̂[q] →+* lim R[h]/(h^N)`. -/
noncomputable def ohtsuki : Habiro R →+* Ohtsuki R :=
  RingHom.codRestrict
    ((Pi.ringHom fun N => (levelShift N).comp
      ((Pi.evalRingHom (fun N => R[X] ⧸ level R N) N))).comp (Habiro R).subtype)
    (Ohtsuki R)
    (fun x N M h => by
      simp only [RingHom.comp_apply, Pi.ringHom_apply, Pi.evalRingHom_apply,
        Subring.coe_subtype]
      rw [← compat x h]
      obtain ⟨p, hp⟩ := Ideal.Quotient.mk_surjective ((x : ∀ N, R[X] ⧸ level R N) M)
      rw [← hp, levelShift_mk, Ideal.Quotient.factor_mk, Ideal.Quotient.factor_mk, levelShift_mk])

/-- The level-`N` component of `ohtsuki`, as a ring map. -/
noncomputable def ohtsukiLevel (N : ℕ) : Habiro R →+* R[X] ⧸ hLevel R N :=
  (levelShift N).comp ((Pi.evalRingHom (fun N => R[X] ⧸ level R N) N).comp (Habiro R).subtype)

theorem ohtsuki_apply (x : Habiro R) (N : ℕ) :
    ((ohtsuki x : Ohtsuki R) : ∀ N, R[X] ⧸ hLevel R N) N =
      levelShift N ((x : ∀ N, R[X] ⧸ level R N) N) := rfl

theorem ohtsuki_ofPoly (p : R[X]) (N : ℕ) :
    ((ohtsuki (ofPoly p) : Ohtsuki R) : ∀ N, R[X] ⧸ hLevel R N) N =
      Ideal.Quotient.mk (hLevel R N) (shiftOne p) := rfl

/-- `q ↦ 1 + h`. -/
theorem ohtsuki_q (N : ℕ) :
    ((ohtsuki q : Ohtsuki R) : ∀ N, R[X] ⧸ hLevel R N) N =
      Ideal.Quotient.mk (hLevel R N) (X + 1) := by
  rw [q, ohtsuki_ofPoly, shiftOne_apply, X_comp]

/-- **A cyclotomic series at level `N`**: `∑_{n<N} a_n(1+h) · (q;q)_n(1+h)`. -/
theorem ohtsuki_series_apply (a : ℕ → Habiro R) (N : ℕ) :
    ((ohtsuki (series a) : Ohtsuki R) : ∀ N, R[X] ⧸ hLevel R N) N =
      ∑ n ∈ range N, ((ohtsuki (a n) : Ohtsuki R) : ∀ N, R[X] ⧸ hLevel R N) N *
        Ideal.Quotient.mk (hLevel R N) (shiftOne (qPoch R n)) := by
  rw [ohtsuki_apply, series_apply, seriesLevel, map_sum]
  refine sum_congr rfl fun n _ => ?_
  rw [map_mul, levelShift_mk, ohtsuki_apply]

theorem ohtsuki_apply_eq_level (x : Habiro R) (N : ℕ) :
    ((ohtsuki x : Ohtsuki R) : ∀ N, R[X] ⧸ hLevel R N) N = ohtsukiLevel N x := rfl

theorem ohtsukiLevel_ofPoly (N : ℕ) (p : R[X]) :
    ohtsukiLevel N (ofPoly p) = Ideal.Quotient.mk (hLevel R N) (shiftOne p) := rfl

theorem ohtsukiLevel_series (a : ℕ → Habiro R) (N : ℕ) :
    ohtsukiLevel N (series a) =
      ∑ n ∈ range N, ohtsukiLevel N (a n) * Ideal.Quotient.mk (hLevel R N) (shiftOne (qPoch R n)) :=
  ohtsuki_series_apply a N

/-! ### Non-vacuity at level 2 -/

private theorem mk_X_sq : Ideal.Quotient.mk (hLevel R 2) X ^ 2 = 0 := by
  rw [← map_pow]; exact Ideal.Quotient.eq_zero_iff_mem.mpr (Ideal.mem_span_singleton_self _)

/-- `F(1 + h) ≡ 1 - h (mod h²)` for the Kontsevich–Zagier element. -/
theorem ohtsuki_trefoil_two :
    ohtsukiLevel 2 (trefoil : Habiro R) = Ideal.Quotient.mk (hLevel R 2) (1 - X) := by
  rw [trefoil, ohtsukiLevel_series]
  simp only [sum_range_succ, sum_range_zero, map_one, one_mul, zero_add, qPoch,
    prod_range_succ, prod_range_zero, shiftOne_apply, one_comp, sub_comp, pow_comp, X_comp,
    map_sub, map_add, map_pow]
  ring

/-- `(1+h)⁻¹ ≡ 1 - h (mod h²)`. -/
theorem ohtsuki_qInv_two :
    ohtsukiLevel 2 (qInv : Habiro R) = Ideal.Quotient.mk (hLevel R 2) (1 - X) := by
  have h1 := congrArg (ohtsukiLevel 2) (q_mul_qInv (R := R))
  rw [map_mul, map_one, q, ohtsukiLevel_ofPoly, shiftOne_apply, X_comp, map_add, map_one] at h1
  have hX2 := mk_X_sq (R := R)
  rw [map_sub, map_one]
  linear_combination (ohtsukiLevel 2 (qInv : Habiro R)) * hX2 +
    (1 - Ideal.Quotient.mk (hLevel R 2) X) * h1

/-- `figureEight(1 + h) ≡ 1 (mod h²)`. -/
theorem ohtsuki_figureEight_two :
    ohtsukiLevel 2 (figureEight : Habiro R) = 1 := by
  rw [figureEight, ohtsukiLevel_series, sum_range_succ, sum_range_succ, sum_range_zero,
    zero_add]
  have e0 : poch (qInv : Habiro R) 0 = 1 := by simp [poch]
  have e1 : poch (qInv : Habiro R) 1 = 1 - qInv := by simp [poch]
  have q0 : shiftOne (qPoch R 0) = 1 := by simp [qPoch, shiftOne_apply]
  have q1 : shiftOne (qPoch R 1) = 1 - (X + 1) := by simp [qPoch, shiftOne_apply]
  have hs : ohtsukiLevel 2 (1 - (qInv : Habiro R)) =
      1 - Ideal.Quotient.mk (hLevel R 2) (1 - X) := by
    rw [RingHom.map_sub, RingHom.map_one, ohtsuki_qInv_two]
  rw [e0, e1, q0, q1, RingHom.map_one, hs]
  have hX2 := mk_X_sq (R := R)
  simp only [map_sub, map_one, map_add]
  linear_combination (-1 : R[X] ⧸ hLevel R 2) * hX2

end QCalculus.HabiroSeries
