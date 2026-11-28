import HeckeTemperleyLieb.TLBraidedModular

/-!
# The vacuum and `p_0, …, p_{k−1}` survive semisimplification; `p_k` does not

Bean `hkmt`. `TLBraidedModular` derives `S` and `T` on the vacuum and the Jones–Wenzl projectors
`p_0, …, p_{k−1}`. This file proves the facts about those objects that the semisimplified quotient
(the quotient by negligible morphisms, i.e. by the radical of the Markov trace form) needs.

Generic, over any field:

* `aug_jw`, `jw_ne_zero`: the augmentation of `p_n` is `1`, so `p_n ≠ 0`.
* `jw_corner`: `p_n · x · p_n = aug(x) · p_n`. The corner algebra `p_n TL p_n` is the scalars, so
  `p_n` is a primitive idempotent: `jw_corner_idempotent` says an idempotent in the corner is `0`
  or `p_n`.
* `jw_negligible_iff`: `p_n` is negligible (in the radical of the trace form) iff its trace is
  `0`. A simple object is killed by semisimplification exactly when its quantum dimension
  vanishes.

At a primitive `2(k+2)`-th root of unity `ζ`, `δ = ζ + ζ⁻¹`, for any Markov trace with `δε = 1`:

* `jwSpec_root`: `p_0, …, p_k` are all defined.
* `qint_root_top`: `[k+2] = 0`.
* `tau_jw_ne_zero`, `jw_not_negligible`: `p_n` has nonzero trace and is not negligible for
  `n + 1 ≤ k`, so it is a simple object of the quotient with endomorphisms the scalars.
* `nondegenerate_root`: the trace form is nondegenerate on `TL_{n+1}` for `n + 1 ≤ k`, so the
  quotient changes nothing on fewer than `k + 1` strands.
* `jw_top_ne_zero`, `jw_top_negligible`, `not_nondegenerate_top`: `p_k ≠ 0`, yet it is negligible
  at every level `k + m`, and the form on `TL_{k+1}` is degenerate. `p_k` is the first projector
  that the quotient kills.
* `braidS_row_ne`: the rows of the braid-derived `S`-matrix are pairwise distinct (from
  `det S ≠ 0`). Isomorphic objects have identical Hopf-link traces against every object, so the
  vacuum and `p_0, …, p_{k−1}` are pairwise non-isomorphic in the quotient.

Not proved here: that every simple object of the quotient is isomorphic to one of these `k + 1`.
That needs the rectangular Temperley–Lieb hom spaces `Hom(m, n)` and the decomposition of an
arbitrary idempotent, which the corpus does not yet have; the partial fact used by the Jones–Wenzl
recursion, `1 − p_n ∈ genIdeal` (everything orthogonal to `p_n` factors through fewer strands), is
in `TemperleyLiebMarkovNondegenerate`.

No empirical input; everything is over an arbitrary field.

-- Ref: [turaev1994] Quantum invariants of knots and 3-manifolds, ch. XII.
-- Ref: [kirbymelvin1991] https://doi.org/10.1007/BF01239527
-/

namespace QOU.HeckeTemperleyLieb.TLSemisimpleQuotient

open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebMarkov
open QOU.HeckeTemperleyLieb.TLRootOfUnity QOU.HeckeTemperleyLieb.TLVacuumRow
open QOU.HeckeTemperleyLieb.TLBraidedModular

variable {K : Type*} [Field K]

section Generic

variable (δ : K)

/-- The augmentation of `p_n` is `1`. -/
theorem aug_jw : ∀ n, augmentation K δ adjFin (jw δ n) = 1
  | 0 => by simp [jw]
  | n + 1 => by
    rw [jw_succ, map_sub, map_smul, map_mul, map_mul, aug_incl, aug_jw n, augmentation_e]
    simp

/-- `p_n ≠ 0`. -/
theorem jw_ne_zero (n : ℕ) : jw δ n ≠ 0 := by
  intro h
  have := aug_jw δ n
  rw [h, map_zero] at this
  exact zero_ne_one this

variable {δ}

/-- **The corner algebra is the scalars.** `p_n · x · p_n = aug(x) · p_n`. -/
theorem jw_corner {n : ℕ} (hS : JWSpec δ n) (x : TLFin K δ n) :
    jw δ n * x * jw δ n = augmentation K δ adjFin x • jw δ n := by
  rw [mul_eq_aug_smul hS.1 x, smul_mul_assoc, hS.2.2.1]

/-- **`p_n` is primitive.** An idempotent of the corner `p_n TL p_n` is `0` or `p_n`. -/
theorem jw_corner_idempotent {n : ℕ} (hS : JWSpec δ n) (x : TLFin K δ n)
    (hf : (jw δ n * x * jw δ n) * (jw δ n * x * jw δ n) = jw δ n * x * jw δ n) :
    jw δ n * x * jw δ n = 0 ∨ jw δ n * x * jw δ n = jw δ n := by
  rw [jw_corner hS] at hf ⊢
  set a := augmentation K δ adjFin x
  rw [smul_mul_smul_comm, hS.2.2.1] at hf
  have h : (a * a - a) • jw δ n = 0 := by rw [sub_smul, hf, sub_self]
  rcases smul_eq_zero.mp h with h | h
  · have : a * (a - 1) = 0 := by rw [mul_sub, mul_one]; exact h
    rcases mul_eq_zero.mp this with h0 | h1
    · left; rw [h0, zero_smul]
    · right; rw [sub_eq_zero.mp h1, one_smul]
  · exact absurd h (jw_ne_zero δ n)

end Generic

section Markov

variable {δ ε : K} (T : MarkovTower δ ε)

/-- **Negligible iff trace zero.** `p_n` lies in the radical of the trace form iff
`τ(p_n) = 0`. -/
theorem jw_negligible_iff {n : ℕ} (hS : JWSpec δ n) :
    (∀ y, T.τ n (jw δ n * y) = 0) ↔ T.τ n (jw δ n) = 0 := by
  constructor
  · intro h; simpa using h 1
  · intro h y; rw [mul_eq_aug_smul hS.1, map_smul, h, smul_zero]

/-- A negligible `p_n` stays negligible at every higher level. -/
theorem jw_negligible_up {n : ℕ} (hS : JWSpec δ n) (hτ : T.τ n (jw δ n) = 0) (m : ℕ)
    (y : TLFin K δ (n + m)) : T.τ (n + m) (inclIter (δ := δ) n m (jw δ n) * y) = 0 :=
  tau_inclIter_mul T hS.1 hτ m y

end Markov

section RootOfUnity

variable {ζ : Kˣ} (k : ℕ) (hζ : IsPrimitiveRoot ζ (2 * (k + 2)))
include hζ

/-- `[m] ≠ 0` for `0 < m < k + 2`. -/
theorem qint_root_ne_zero {m : ℕ} (hm0 : 0 < m) (hm : m < k + 2) :
    qint ((ζ : K) + ((ζ⁻¹ : Kˣ) : K)) m ≠ 0 := by
  rw [qint_eq_qInt]; exact qInt_ne_zero k hζ hm0 hm

/-- `[k + 2] = 0`. -/
theorem qint_root_top : qint ((ζ : K) + ((ζ⁻¹ : Kˣ) : K)) (k + 2) = 0 := by
  rw [qint_eq_qInt]
  have h := qDelta_mul_qInt ζ (k + 2)
  have hp : ζ ^ (k + 2) = -1 := pow_half_eq_neg_one (by omega) hζ
  have hpos : ζ ^ (((k + 2 : ℕ)) : ℤ) = -1 := by rw [zpow_natCast, hp]
  have hneg : ζ ^ (-((k + 2 : ℕ) : ℤ)) = -1 := by rw [zpow_neg, hpos, inv_neg_one]
  rw [hpos, hneg, sub_self] at h
  exact (mul_eq_zero.mp h).resolve_left (qDelta_ne_zero k hζ)

/-- `p_0, …, p_k` are defined. -/
theorem jwSpec_root {n : ℕ} (hn : n ≤ k) : JWSpec ((ζ : K) + ((ζ⁻¹ : Kˣ) : K)) n :=
  jw_spec _ n fun j hj => qint_root_ne_zero k hζ (by omega) (by omega)

variable {ε : K} (T : MarkovTower ((ζ : K) + ((ζ⁻¹ : Kˣ) : K)) ε)
  (hε : ((ζ : K) + ((ζ⁻¹ : Kˣ) : K)) * ε = 1)
include hε

theorem tau_jw_root {n : ℕ} (hn : n ≤ k) :
    T.τ n (jw _ n) = qint ((ζ : K) + ((ζ⁻¹ : Kˣ) : K)) (n + 2) * ε ^ (n + 1) :=
  tau_jw T hε n (fun j hj => qint_root_ne_zero k hζ (by omega) (by omega))
    (fun m hm => jwSpec_root k hζ (by omega))

/-- **`p_n` has nonzero quantum dimension for `n + 1 ≤ k`.** -/
theorem tau_jw_ne_zero {n : ℕ} (hn : n + 1 ≤ k) : T.τ n (jw _ n) ≠ 0 := by
  rw [tau_jw_root k hζ T hε (by omega)]
  exact mul_ne_zero (qint_root_ne_zero k hζ (by omega) (by omega))
    (pow_ne_zero _ (right_ne_zero_of_mul_eq_one hε))

/-- **`p_n` survives semisimplification for `n + 1 ≤ k`.** -/
theorem jw_not_negligible {n : ℕ} (hn : n + 1 ≤ k) :
    ¬ ∀ y, T.τ n (jw ((ζ : K) + ((ζ⁻¹ : Kˣ) : K)) n * y) = 0 := by
  rw [jw_negligible_iff T (jwSpec_root k hζ (by omega))]
  exact tau_jw_ne_zero k hζ T hε hn

/-- **No negligible morphisms below `k + 1` strands.** -/
theorem nondegenerate_root {n : ℕ} (hn : n + 1 ≤ k) : Nondegenerate T n :=
  (nondegenerate_iff T hε n).mpr fun j hj3 hjn => qint_root_ne_zero k hζ (by omega) (by omega)

/-- `τ(p_k) = 0`. -/
theorem tau_jw_top : T.τ k (jw _ k) = 0 := by
  rw [tau_jw_root k hζ T hε le_rfl, qint_root_top k hζ, zero_mul]

omit hζ hε in
/-- `p_k ≠ 0`. -/
theorem jw_top_ne_zero : jw ((ζ : K) + ((ζ⁻¹ : Kˣ) : K)) k ≠ 0 := jw_ne_zero _ k

/-- **`p_k` is negligible at every level `k + m`**, so the quotient kills it. -/
theorem jw_top_negligible (m : ℕ) (y : TLFin K ((ζ : K) + ((ζ⁻¹ : Kˣ) : K)) (k + m)) :
    T.τ (k + m) (inclIter (δ := (ζ : K) + ((ζ⁻¹ : Kˣ) : K)) k m (jw _ k) * y) = 0 :=
  jw_negligible_up T (jwSpec_root k hζ le_rfl) (tau_jw_top k hζ T hε) m y

/-- **The trace form on `TL_{k+1}` is degenerate.** -/
theorem not_nondegenerate_top : ¬ Nondegenerate T k := by
  apply not_nondegenerate T hε k
  refine ⟨k + 2, ?_, le_rfl, qint_root_top k hζ⟩
  by_contra h
  have hk : k = 0 := by omega
  have h2 := qint_root_top k hζ
  rw [hk, qint_two] at h2
  rw [h2, zero_mul] at hε
  exact zero_ne_one hε

end RootOfUnity

/-- **The simples are pairwise distinct.** The rows of the braid-derived `S`-matrix (Hopf-link
traces of the vacuum and `p_0, …, p_{k−1}` against each of them) are pairwise distinct. -/
theorem braidS_row_ne (ω : Kˣ) (k : ℕ) (hζ : IsPrimitiveRoot (ω ^ 2) (2 * (k + 2))) {ε : K}
    (T : MarkovTower (((ω ^ 2 : Kˣ) : K) + (((ω ^ 2)⁻¹ : Kˣ) : K)) ε)
    (hε : (((ω ^ 2 : Kˣ) : K) + (((ω ^ 2)⁻¹ : Kˣ) : K)) * ε = 1)
    {i j : Fin (k + 1)} (hij : i ≠ j) :
    braidS (ω : K) T k i ≠ braidS (ω : K) T k j := fun h =>
  braidS_det_ne_zero ω k hζ T hε (Matrix.det_zero_of_row_eq hij h)

end QOU.HeckeTemperleyLieb.TLSemisimpleQuotient
