import QOU.Core.KashaevHermitianCertificate

/-!
# The reflection identity for `⟨4₁⟩_N` and the bound `N² + (N-1)²` (bean `qou-pc7n`, stage 2)

Let `q` be a primitive `N`-th root of unity, `N = n + 1`, with `star q = q⁻¹`, and
write `P k = (q;q)_k`. Stage 1 (`QOU.Core.KashaevHermitianCertificate`) shows
`⟨4₁⟩_N = Σ_{k<N} star(P k)·P k`.

**Reflection.** `P k · star (P (n - k)) = N` for `k ≤ n` (`qPoch_mul_star_reflect`).
The tail `∏_{j=k+1}^{n} (1 - q^j)` of `P n = N` is, after `j ↦ N - j`,
`∏ (1 - q^{-i}) = star (P (n - k))`. Its logarithm at `ζ = e^{2πi/N}` is the
analytic reflection `s_k + s_{N-1-k} = -log N` of
`QOU.Knot.FigureEightVolume.sum_log_two_sin_reflect` (`KashaevProdEndpoint.lean`); the
version here is algebraic and holds at every Galois conjugate.

**Pairing.** Then `star(P k)·P k + star(P (n-k))·P (n-k) = 2N + star(u)·u` with
`u = P k - P (n - k)`, a further Hermitian square (`pair_eq`). Summing over `k` and
keeping only the two end certificates `u = ±(1 - N)` gives

  `⟨4₁⟩_N ≥ N² + (N - 1)²`   (`kashaev_ge_sq_add_sq`),

which improves stage 1's `1 + N²`. Everything is finite algebra in a star-ordered
field: no analysis, no order on `ℝ`, and no Jones unitarity. The complex corollary
holds at every primitive root, so the bound holds at every Galois conjugate.

The bound is still polynomial in `N`; the exponential growth of `⟨4₁⟩_N` sits in the
middle terms and its rate is the `N → ∞` statement, which stays on `[Coev E]`.
-/

namespace QOU.Core.KashaevHermitianCertificate

open Finset QOU.Core.TarskiSignKashaev

section Reflection

variable {F : Type*} [Field F] [StarRing F]

/-- **Reflection identity.** `(q;q)_k · star((q;q)_{n-k}) = n + 1` for `k ≤ n`. -/
theorem qPoch_mul_star_reflect {n k : ℕ} (hk : k ≤ n) {q : F}
    (hμ : IsPrimitiveRoot q (n + 1)) (hstar : star q = q⁻¹) :
    qPoch q k * star (qPoch q (n - k)) = (n : F) + 1 := by
  have hq : q ≠ 0 := hμ.ne_zero (Nat.succ_ne_zero n)
  have htop : qPoch q n = (n : F) + 1 := prod_one_sub_pow hμ
  rw [← htop]
  have hsplit : n = k + (n - k) := by omega
  conv_rhs => rw [qPoch, hsplit, prod_range_add]
  congr 1
  rw [star_qPoch hstar, ← prod_range_reflect]
  refine prod_congr rfl fun j hj => ?_
  have hj' : j < n - k := mem_range.1 hj
  have hexp : (k + j + 1) + (n - k - 1 - j + 1) = n + 1 := by omega
  have hpow : q ^ (k + j + 1) = q⁻¹ ^ (n - k - 1 - j + 1) := by
    rw [inv_pow]
    apply eq_inv_of_mul_eq_one_left
    rw [← pow_add, hexp, hμ.pow_eq_one]
  rw [hpow]

/-- **Pairing as a Hermitian square.** If `P · star Q = c` with `star c = c`, then
`star P·P + star Q·Q = 2c + star(P - Q)·(P - Q)`. -/
theorem pair_eq {P Q c : F} (h : P * star Q = c) (hc : star c = c) :
    star P * P + star Q * Q = 2 * c + star (P - Q) * (P - Q) := by
  have h1 : star Q * P = c := by rw [mul_comm]; exact h
  have h2 : star P * Q = c := by
    have := congrArg star h
    rw [star_mul, star_star, hc, mul_comm] at this
    exact this
  rw [star_sub]
  linear_combination h1 + h2

end Reflection

section Bound

variable {F : Type*} [Field F] [StarRing F] [CharZero F] [PartialOrder F] [StarOrderedRing F]

/-- **Per-`N` lower bound, stage 2.** At a primitive `(n+1)`-th root of unity with
`star q = q⁻¹` and `n ≥ 1`: `⟨4₁⟩_{n+1} ≥ (n+1)² + n²`. -/
theorem kashaev_ge_sq_add_sq {n : ℕ} (hn : 1 ≤ n) {q : F} (hμ : IsPrimitiveRoot q (n + 1))
    (hstar : star q = q⁻¹) :
    ((n : F) + 1) ^ 2 + (n : F) ^ 2 ≤ kashaevFigureEight (q + q⁻¹) (n + 1) := by
  have hq : q ≠ 0 := hμ.ne_zero (Nat.succ_ne_zero n)
  rw [kashaev_eq_sum_hermitian hq hstar]
  set N : F := (n : F) + 1 with hN
  set a : ℕ → F := fun k => star (qPoch q k) * qPoch q k with ha
  set h : ℕ → F := fun k => star (qPoch q k - qPoch q (n - k)) * (qPoch q k - qPoch q (n - k))
    with hh
  have hNstar : star N = N := by simp [hN]
  -- the reflected sum is the same sum
  have hrefl : ∑ k ∈ range (n + 1), a (n - k) = ∑ k ∈ range (n + 1), a k := by
    simpa using sum_range_reflect a (n + 1)
  -- pairwise identity
  have hpair : ∀ k ∈ range (n + 1), a k + a (n - k) = 2 * N + h k := by
    intro k hk
    have hk' : k ≤ n := Nat.lt_succ_iff.1 (mem_range.1 hk)
    exact pair_eq (qPoch_mul_star_reflect hk' hμ hstar) hNstar
  have h2S : 2 * ∑ k ∈ range (n + 1), a k
      = 2 * N * N + ∑ k ∈ range (n + 1), h k := by
    have : ∑ k ∈ range (n + 1), (a k + a (n - k))
        = ∑ k ∈ range (n + 1), (2 * N + h k) := sum_congr rfl hpair
    rw [sum_add_distrib, hrefl, sum_add_distrib, sum_const, card_range, nsmul_eq_mul] at this
    rw [two_mul, this]; push_cast [hN]; ring
  -- the two end certificates
  have hP0 : qPoch q 0 = 1 := by simp [qPoch]
  have hPn : qPoch q n = N := prod_one_sub_pow hμ
  have hh0 : h 0 = (n : F) ^ 2 := by
    simp only [hh, Nat.sub_zero, hP0, hPn, hN, star_sub, star_one, star_add, star_natCast]; ring
  have hhn : h n = (n : F) ^ 2 := by
    simp only [hh, Nat.sub_self, hP0, hPn, hN, star_sub, star_one, star_add, star_natCast]; ring
  have hsub : ({0, n} : Finset ℕ) ⊆ range (n + 1) := by
    intro x hx; simp only [mem_insert, mem_singleton] at hx; rcases hx with rfl | rfl <;> simp
  have hle := sum_le_sum_of_subset_of_nonneg (f := h) hsub (fun i _ _ => star_mul_self_nonneg _)
  have h0n : (0 : ℕ) ∉ ({n} : Finset ℕ) := by simp; omega
  rw [sum_insert h0n, sum_singleton, hh0, hhn] at hle
  -- 2·(S - T) ≥ 0, then halve by conjugating with 2⁻¹
  set S := ∑ k ∈ range (n + 1), a k
  have hdiff : 0 ≤ 2 * (S - (N ^ 2 + (n : F) ^ 2)) := by
    have : 2 * (S - (N ^ 2 + (n : F) ^ 2))
        = (∑ k ∈ range (n + 1), h k) - ((n : F) ^ 2 + (n : F) ^ 2) := by
      rw [mul_sub, h2S]; ring
    rw [this]; exact sub_nonneg.2 hle
  have hc : star ((2 : F)⁻¹) = (2 : F)⁻¹ := by simp
  have hhalf : 0 ≤ star ((2 : F)⁻¹) * (2 * (S - (N ^ 2 + (n : F) ^ 2))) * (2 : F)⁻¹ :=
    conjugate_nonneg hdiff _
  have h2 : (2 : F) ≠ 0 := two_ne_zero
  have hq4 : star ((2 : F)⁻¹) * (2 * (S - (N ^ 2 + (n : F) ^ 2))) * (2 : F)⁻¹
      = (S - (N ^ 2 + (n : F) ^ 2)) * (2 : F)⁻¹ := by
    rw [hc]; field_simp
  rw [hq4] at hhalf
  have : S - (N ^ 2 + (n : F) ^ 2)
      = (S - (N ^ 2 + (n : F) ^ 2)) * (2 : F)⁻¹ + (S - (N ^ 2 + (n : F) ^ 2)) * (2 : F)⁻¹ := by
    field_simp; ring
  exact sub_nonneg.1 (this ▸ add_nonneg hhalf hhalf)

end Bound

section Complex

open scoped ComplexOrder

/-- **Total positivity, stage 2.** At every primitive `N`-th root of unity `ζ ∈ ℂ`
(every Galois conjugate of `e^{2πi/N}`), `⟨4₁⟩_N(ζ + ζ⁻¹) ≥ N² + (N - 1)²`. -/
theorem kashaev_complex_ge_sq_add_sq {n : ℕ} (hn : 1 ≤ n) {ζ : ℂ}
    (hμ : IsPrimitiveRoot ζ (n + 1)) :
    ((n : ℂ) + 1) ^ 2 + (n : ℂ) ^ 2 ≤ kashaevFigureEight (ζ + ζ⁻¹) (n + 1) := by
  have hnorm : ‖ζ‖ = 1 := hμ.norm'_eq_one (Nat.succ_ne_zero n)
  have hstar : star ζ = ζ⁻¹ := by
    rw [Complex.inv_def, Complex.normSq_eq_norm_sq, hnorm]; simp
  exact kashaev_ge_sq_add_sq hn hμ hstar

end Complex

end QOU.Core.KashaevHermitianCertificate
