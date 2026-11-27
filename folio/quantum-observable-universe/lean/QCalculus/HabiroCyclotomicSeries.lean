import Mathlib.RingTheory.Polynomial.Cyclotomic.Basic
import Mathlib.RingTheory.Ideal.Quotient.Operations
import Mathlib.Algebra.Ring.Subring.Basic
import Mathlib.Algebra.Polynomial.Inductions
import Mathlib.Algebra.BigOperators.Intervals

/-!
# QCalculus.HabiroCyclotomicSeries — Kashaev invariants as elements of the Habiro ring

Bean `qou-28qh` (option 5.1 of `qou-gfsr`, epic `qou-dk7p`), phase 1.

Over any commutative ring `R` this file builds the Habiro completion

  `R̂[q] = varprojlim_N R[q] ⧸ ((q;q)_N)`,   `(q;q)_N = ∏_{k=1}^{N} (1 - q^k)`,

as the subring of compatible threads, and the **cyclotomic series**
`∑_n a_n (q;q)_n` with coefficients `a_n` in `R̂[q]` itself. Every such series
is an honest element: its level-`N` component is the finite sum over `n < N`,
because `(q;q)_n ≡ 0` modulo `(q;q)_N` once `n ≥ N`. No limit, no norm and no
convergence enters; the "completion" is the inverse limit of rings.

Two elements are named:

* `trefoil = ∑_n (q;q)_n`, the Kontsevich–Zagier series [zagier2001strange],
  whose values at roots of unity are the Kashaev invariants of the trefoil;
* `figureEight = ∑_n (q;q)_n (q⁻¹;q⁻¹)_n`, Habiro's cyclotomic expansion of
  the figure-eight knot at colour `N` read at `q = ζ_N` [habiro2000].

`q` is a unit of `R̂[q]` (`isUnit_q`): `(q;q)_N` has constant term `1`, so
`q · (−divX((q;q)_N − 1)) ≡ 1` at every level, and inverses are unique.

## Evaluation at a root of unity

For `N ≠ 0`, an `R`-algebra `S` and `ζ : S` with `Φ_N(ζ) = 0`, `evalRoot`
is a ring map `R̂[q] →+* S` (read level `N`, reduce mod `Φ_N`, substitute
`ζ`). On a cyclotomic series it gives the finite sum
`∑_{n<N} a_n(ζ) ∏_{k=1}^{n} (1 - ζ^k)` (`evalRoot_series`), and this sum can be
cut at any `M ≥ N` (`evalRoot_series_eq_sum_of_le`), because `ζ^N = 1` kills
`(ζ;ζ)_n` for `n ≥ N`. So the Kashaev invariants are the images of two ring
elements under ring maps:

* `evalRoot_trefoil`: `∑_{n<N} (ζ;ζ)_n`;
* `evalRoot_figureEight`: `∑_{n<N} (ζ;ζ)_n (ζ';ζ')_n` with `ζ' ζ = 1`.

## What is NOT proved here

* That `figureEight` is the colored Jones / Kashaev invariant of `4₁`: that is
  Habiro's theorem (and Kashaev's definition), cited, not formalized. The
  file proves the algebra of the elements only.
* Injectivity of the joint evaluation map (Habiro's theorem that an element of
  `ℤ̂[q]` is determined by its values at all roots of unity).
* Any archimedean statement: no embedding of `ζ` into `ℂ` is chosen here.
  The comparison with `2 - 2 cos(2πj/N)` belongs behind
  `QOU/Transcendental/` (phase 3 of `qou-28qh`).

No empirical value enters this file.

-- Ref: [habiro2004cyclotomic]
-- Ref: [habiro2000]
-- Ref: [kashaev1997]
-- Ref: [zagier2001strange]
-/

namespace QCalculus.HabiroSeries

open Polynomial Finset

variable (R : Type*) [CommRing R]

/-! ### The filtration `((q;q)_N)` -/

/-- The q-Pochhammer polynomial `(q;q)_N = ∏_{k=1}^{N} (1 - q^k)` in `R[q]`. -/
noncomputable def qPoch (N : ℕ) : R[X] :=
  ∏ k ∈ range N, (1 - X ^ (k + 1))

variable {R}

@[simp] theorem qPoch_zero : qPoch R 0 = 1 := by simp [qPoch]

theorem qPoch_succ (N : ℕ) : qPoch R (N + 1) = qPoch R N * (1 - X ^ (N + 1)) := by
  simp [qPoch, prod_range_succ]

theorem qPoch_dvd_of_le {N M : ℕ} (h : N ≤ M) : qPoch R N ∣ qPoch R M :=
  prod_dvd_prod_of_subset _ _ _ (range_subset_range.mpr h)

/-- The constant term of `(q;q)_N` is `1`. -/
theorem qPoch_coeff_zero (N : ℕ) : (qPoch R N).coeff 0 = 1 := by
  rw [coeff_zero_eq_eval_zero, qPoch, eval_prod]
  simp

variable (R)

/-- The level-`N` ideal `((q;q)_N)`. -/
noncomputable abbrev level (N : ℕ) : Ideal R[X] := Ideal.span {qPoch R N}

variable {R}

theorem level_le {N M : ℕ} (h : N ≤ M) : level R M ≤ level R N :=
  Ideal.span_singleton_le_span_singleton.mpr (qPoch_dvd_of_le h)

/-- The bonding map `R[q]/((q;q)_M) → R[q]/((q;q)_N)`, `N ≤ M`. -/
noncomputable abbrev bond {N M : ℕ} (h : N ≤ M) :
    R[X] ⧸ level R M →+* R[X] ⧸ level R N :=
  Ideal.Quotient.factor (level_le h)

/-- `(q;q)_n ≡ 0` modulo `(q;q)_N` once `N ≤ n`. -/
theorem mk_qPoch_eq_zero {N n : ℕ} (h : N ≤ n) :
    Ideal.Quotient.mk (level R N) (qPoch R n) = 0 :=
  Ideal.Quotient.eq_zero_iff_mem.mpr (Ideal.mem_span_singleton.mpr (qPoch_dvd_of_le h))

/-! ### The Habiro ring -/

variable (R)

/-- **The Habiro completion** `R̂[q] = varprojlim_N R[q]/((q;q)_N)`: the subring of
    threads `x` with `bond h (x M) = x N` for every `N ≤ M`. -/
noncomputable def Habiro : Subring (∀ N, R[X] ⧸ level R N) where
  carrier := { x | ∀ N M (h : N ≤ M), bond h (x M) = x N }
  mul_mem' {x y} hx hy N M h := by simp only [Pi.mul_apply, map_mul, hx N M h, hy N M h]
  one_mem' N M h := by simp only [Pi.one_apply, map_one]
  add_mem' {x y} hx hy N M h := by simp only [Pi.add_apply, map_add, hx N M h, hy N M h]
  zero_mem' N M h := by simp only [Pi.zero_apply, map_zero]
  neg_mem' {x} hx N M h := by simp only [Pi.neg_apply, map_neg, hx N M h]

variable {R}

theorem compat (x : Habiro R) {N M : ℕ} (h : N ≤ M) :
    bond h ((x : ∀ N, R[X] ⧸ level R N) M) = (x : ∀ N, R[X] ⧸ level R N) N :=
  x.2 N M h

theorem val_sum {ι : Type*} (s : Finset ι) (f : ι → Habiro R) (N : ℕ) :
    ((∑ i ∈ s, f i : Habiro R) : ∀ N, R[X] ⧸ level R N) N =
      ∑ i ∈ s, (f i : ∀ N, R[X] ⧸ level R N) N :=
  (congrFun (map_sum (Habiro R).subtype f s) N).trans (Finset.sum_apply _ _ _)

theorem val_mul (x y : Habiro R) (N : ℕ) :
    ((x * y : Habiro R) : ∀ N, R[X] ⧸ level R N) N =
      (x : ∀ N, R[X] ⧸ level R N) N * (y : ∀ N, R[X] ⧸ level R N) N := rfl

theorem val_add (x y : Habiro R) (N : ℕ) :
    ((x + y : Habiro R) : ∀ N, R[X] ⧸ level R N) N =
      (x : ∀ N, R[X] ⧸ level R N) N + (y : ∀ N, R[X] ⧸ level R N) N := rfl

/-- Polynomials as constant threads. -/
noncomputable def ofPoly : R[X] →+* Habiro R :=
  RingHom.codRestrict (Pi.ringHom fun N => Ideal.Quotient.mk (level R N)) (Habiro R)
    (fun p N M h => by simp only [Pi.ringHom_apply, Ideal.Quotient.factor_mk])

@[simp] theorem ofPoly_apply (p : R[X]) (N : ℕ) :
    ((ofPoly p : Habiro R) : ∀ N, R[X] ⧸ level R N) N = Ideal.Quotient.mk (level R N) p :=
  rfl

/-- The variable `q ∈ R̂[q]`. -/
noncomputable def q : Habiro R := ofPoly X

/-! ### `q` is a unit -/

/-- The level-`N` inverse of `q`: `−divX((q;q)_N − 1)`. -/
noncomputable def qInvPoly (N : ℕ) : R[X] := -divX (qPoch R N - 1)

theorem x_mul_qInvPoly (N : ℕ) : X * qInvPoly (R := R) N = 1 - qPoch R N := by
  have h := X_mul_divX_add (qPoch R N - 1)
  rw [coeff_sub, qPoch_coeff_zero, coeff_one_zero, sub_self, map_zero, add_zero] at h
  rw [qInvPoly, mul_neg, h]; ring

theorem mk_X_mul_qInvPoly (N : ℕ) :
    Ideal.Quotient.mk (level R N) X * Ideal.Quotient.mk (level R N) (qInvPoly N) = 1 := by
  rw [← map_mul, x_mul_qInvPoly, map_sub, map_one,
    Ideal.Quotient.eq_zero_iff_mem.mpr (Ideal.mem_span_singleton_self _), sub_zero]

private theorem eq_of_mul_eq_one {A : Type*} [CommRing A] {a b c : A}
    (hb : a * b = 1) (hc : a * c = 1) : b = c := by
  calc b = b * (a * c) := by rw [hc, mul_one]
    _ = (a * b) * c := by ring
    _ = c := by rw [hb, one_mul]

/-- `q⁻¹ ∈ R̂[q]`, the thread of level inverses. -/
noncomputable def qInv : Habiro R :=
  ⟨fun N => Ideal.Quotient.mk (level R N) (qInvPoly N), fun N M h => by
    apply eq_of_mul_eq_one (a := Ideal.Quotient.mk (level R N) X)
    · rw [← Ideal.Quotient.factor_mk (level_le h) X, ← map_mul, mk_X_mul_qInvPoly, map_one]
    · exact mk_X_mul_qInvPoly N⟩

theorem q_mul_qInv : (q : Habiro R) * qInv = 1 := by
  apply Subtype.ext; funext N
  exact mk_X_mul_qInvPoly N

theorem isUnit_q : IsUnit (q : Habiro R) := isUnit_of_mul_eq_one _ _ q_mul_qInv

/-! ### Cyclotomic series -/

/-- `(z;z)_n = ∏_{k=1}^{n} (1 - z^k)` in any commutative ring. -/
def poch {A : Type*} [CommRing A] (z : A) (n : ℕ) : A :=
  ∏ k ∈ range n, (1 - z ^ (k + 1))

theorem map_poch {A B : Type*} [CommRing A] [CommRing B] (f : A →+* B) (z : A) (n : ℕ) :
    f (poch z n) = poch (f z) n := by
  simp [poch, map_prod]

theorem ofPoly_qPoch (n : ℕ) : ofPoly (qPoch R n) = poch (q : Habiro R) n := by
  rw [qPoch, poch, map_prod]; simp [q]

/-- The level-`N` partial sum `∑_{n<N} a_n (q;q)_n`. -/
noncomputable def seriesLevel (a : ℕ → Habiro R) (N : ℕ) : R[X] ⧸ level R N :=
  ∑ n ∈ range N, (a n : ∀ N, R[X] ⧸ level R N) N * Ideal.Quotient.mk (level R N) (qPoch R n)

theorem seriesLevel_compat (a : ℕ → Habiro R) {N M : ℕ} (h : N ≤ M) :
    bond h (seriesLevel a M) = seriesLevel a N := by
  rw [seriesLevel, map_sum, ← sum_range_add_sum_Ico _ h, seriesLevel]
  rw [add_eq_left.mpr ?_]
  · refine sum_congr rfl fun n _ => ?_
    rw [map_mul, compat, Ideal.Quotient.factor_mk]
  · refine sum_eq_zero fun n hn => ?_
    rw [map_mul, Ideal.Quotient.factor_mk, mk_qPoch_eq_zero (mem_Ico.mp hn).1, mul_zero]

/-- **The cyclotomic series** `∑_n a_n (q;q)_n ∈ R̂[q]`, for any coefficients
    `a_n ∈ R̂[q]`. -/
noncomputable def series (a : ℕ → Habiro R) : Habiro R :=
  ⟨seriesLevel a, fun _ _ h => seriesLevel_compat a h⟩

theorem series_apply (a : ℕ → Habiro R) (N : ℕ) :
    ((series a : Habiro R) : ∀ N, R[X] ⧸ level R N) N = seriesLevel a N := rfl

/-- The series agrees at level `N` with its finite truncation `∑_{n<M} a_n (q;q)_n`
    for every `M ≥ N`: the tail lies in `((q;q)_N)`. -/
theorem series_apply_eq_trunc (a : ℕ → Habiro R) {N M : ℕ} (h : N ≤ M) :
    ((series a : Habiro R) : ∀ N, R[X] ⧸ level R N) N =
      ((∑ n ∈ range M, a n * poch q n : Habiro R) : ∀ N, R[X] ⧸ level R N) N := by
  rw [series_apply, ← sum_range_add_sum_Ico _ h]
  have hz : ((∑ n ∈ Ico N M, a n * poch q n : Habiro R) : ∀ N, R[X] ⧸ level R N) N = 0 := by
    rw [val_sum]
    refine sum_eq_zero fun n hn => ?_
    rw [val_mul, ← ofPoly_qPoch, ofPoly_apply,
      mk_qPoch_eq_zero (mem_Ico.mp hn).1, mul_zero]
  rw [val_add, hz, add_zero, val_sum, seriesLevel]
  refine sum_congr rfl fun n _ => ?_
  rw [val_mul, ← ofPoly_qPoch, ofPoly_apply]

/-! ### The two knots -/

/-- **Trefoil**: the Kontsevich–Zagier series `F(q) = ∑_n (q;q)_n`. -/
noncomputable def trefoil : Habiro R := series fun _ => 1

/-- **Figure-eight**: `∑_n (q;q)_n (q⁻¹;q⁻¹)_n`. -/
noncomputable def figureEight : Habiro R := series fun n => poch qInv n

/-! ### Evaluation at a root of `Φ_N` -/

theorem cyclotomic_dvd_qPoch {N : ℕ} (hN : N ≠ 0) : cyclotomic N R ∣ qPoch R N := by
  have h1 : cyclotomic N R ∣ 1 - X ^ N := by
    rw [← neg_sub]; exact dvd_neg.mpr (cyclotomic.dvd_X_pow_sub_one N R)
  have hmem : N - 1 ∈ range N := mem_range.mpr (by omega)
  have h2 : (1 - X ^ (N - 1 + 1) : R[X]) ∣ qPoch R N :=
    dvd_prod_of_mem (fun k => (1 - X ^ (k + 1) : R[X])) hmem
  rw [Nat.sub_add_cancel (Nat.one_le_iff_ne_zero.mpr hN)] at h2
  exact h1.trans h2

variable {S : Type*} [CommRing S] [Algebra R S]

/-- **Evaluation at a root of `Φ_N`**: read the thread at level `N` and substitute
    `q = ζ`. Well defined because `Φ_N ∣ (q;q)_N`. -/
noncomputable def evalRoot {N : ℕ} (hN : N ≠ 0) (ζ : S) (hζ : aeval ζ (cyclotomic N R) = 0) :
    Habiro R →+* S :=
  (Ideal.Quotient.lift (level R N) (aeval ζ : R[X] →ₐ[R] S).toRingHom (fun p hp => by
      obtain ⟨r, rfl⟩ := Ideal.mem_span_singleton.mp hp
      obtain ⟨s, hs⟩ := cyclotomic_dvd_qPoch (R := R) hN
      simp [hs, hζ])).comp
    ((Pi.evalRingHom (fun N => R[X] ⧸ level R N) N).comp (Habiro R).subtype)

/-- `ζ^N = 1`, read off from `Φ_N ∣ X^N - 1`. -/
theorem pow_eq_one_of_aeval_cyclotomic {N : ℕ} {ζ : S} (hζ : aeval ζ (cyclotomic N R) = 0) :
    ζ ^ N = 1 := by
  obtain ⟨s, hs⟩ := cyclotomic.dvd_X_pow_sub_one N R
  have := congrArg (aeval ζ) hs
  simp only [map_sub, map_pow, aeval_X, map_one, map_mul, hζ, zero_mul] at this
  exact sub_eq_zero.mp this

/-- `(ζ;ζ)_n = 0` once `n ≥ N`. -/
theorem poch_eq_zero_of_aeval_cyclotomic {N : ℕ} (hN : N ≠ 0) {ζ : S}
    (hζ : aeval ζ (cyclotomic N R) = 0) {n : ℕ} (hn : N ≤ n) : poch ζ n = 0 := by
  apply prod_eq_zero (i := N - 1) (mem_range.mpr (by omega))
  rw [Nat.sub_add_cancel (Nat.one_le_iff_ne_zero.mpr hN),
    pow_eq_one_of_aeval_cyclotomic hζ, sub_self]

section Eval

variable {N : ℕ} (hN : N ≠ 0) {ζ : S} (hζ : aeval ζ (cyclotomic N R) = 0)

theorem evalRoot_ofPoly (p : R[X]) : evalRoot hN ζ hζ (ofPoly p) = aeval ζ p := rfl

theorem evalRoot_q : evalRoot hN ζ hζ q = ζ := by
  rw [q, evalRoot_ofPoly, aeval_X]

theorem evalRoot_q_mul_qInv : ζ * evalRoot hN ζ hζ qInv = 1 := by
  have h := congrArg (evalRoot hN ζ hζ) (q_mul_qInv (R := R))
  rwa [map_mul, map_one, evalRoot_q] at h

theorem evalRoot_apply (x : Habiro R) :
    evalRoot hN ζ hζ x =
      Ideal.Quotient.lift (level R N) (aeval ζ : R[X] →ₐ[R] S).toRingHom
        (fun p hp => by
          obtain ⟨r, rfl⟩ := Ideal.mem_span_singleton.mp hp
          obtain ⟨s, hs⟩ := cyclotomic_dvd_qPoch (R := R) hN
          simp [hs, hζ]) ((x : ∀ N, R[X] ⧸ level R N) N) := rfl

/-- **Evaluation of a cyclotomic series**: the finite sum
    `∑_{n<N} a_n(ζ) (ζ;ζ)_n`. -/
theorem evalRoot_series (a : ℕ → Habiro R) :
    evalRoot hN ζ hζ (series a) = ∑ n ∈ range N, evalRoot hN ζ hζ (a n) * poch ζ n := by
  rw [evalRoot_apply, series_apply_eq_trunc a (le_refl N), val_sum, map_sum]
  refine sum_congr rfl fun n _ => ?_
  rw [val_mul, map_mul, ← ofPoly_qPoch, ofPoly_apply, Ideal.Quotient.lift_mk, ← evalRoot_apply hN hζ]
  congr 1
  simp [qPoch, poch, map_prod]

/-- The Kashaev sum is insensitive to the cut: any `M ≥ N` gives the same value. -/
theorem evalRoot_series_eq_sum_of_le (a : ℕ → Habiro R) {M : ℕ} (hM : N ≤ M) :
    evalRoot hN ζ hζ (series a) = ∑ n ∈ range M, evalRoot hN ζ hζ (a n) * poch ζ n := by
  rw [evalRoot_series, ← sum_range_add_sum_Ico _ hM, left_eq_add]
  exact sum_eq_zero fun n hn => by
    rw [poch_eq_zero_of_aeval_cyclotomic hN hζ (mem_Ico.mp hn).1, mul_zero]

/-- **Trefoil Kashaev sum**: `F(ζ) = ∑_{n<N} (ζ;ζ)_n`. -/
theorem evalRoot_trefoil : evalRoot hN ζ hζ trefoil = ∑ n ∈ range N, poch ζ n := by
  rw [trefoil, evalRoot_series]; simp

/-- **Figure-eight Kashaev sum**: `∑_{n<N} (ζ';ζ')_n (ζ;ζ)_n`, where
    `ζ' = evalRoot qInv` satisfies `ζ ζ' = 1` (`evalRoot_q_mul_qInv`). -/
theorem evalRoot_figureEight :
    evalRoot hN ζ hζ figureEight =
      ∑ n ∈ range N, poch (evalRoot hN ζ hζ qInv) n * poch ζ n := by
  rw [figureEight, evalRoot_series]
  simp only [map_poch]

end Eval

/-- Over a field the figure-eight value is `∑_{n<N} (ζ⁻¹;ζ⁻¹)_n (ζ;ζ)_n`. -/
theorem evalRoot_figureEight_field {K : Type*} [Field K] [Algebra R K] {N : ℕ} (hN : N ≠ 0)
    {ζ : K} (hζ : aeval ζ (cyclotomic N R) = 0) :
    evalRoot hN ζ hζ figureEight = ∑ n ∈ range N, poch ζ⁻¹ n * poch ζ n := by
  have h1 := evalRoot_q_mul_qInv hN hζ
  have hz : ζ ≠ 0 := left_ne_zero_of_mul_eq_one h1
  rw [evalRoot_figureEight, eq_inv_of_mul_eq_one_right h1]

end QCalculus.HabiroSeries
