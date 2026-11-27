import QOU.Core.TarskiSignKashaev
import Mathlib.Algebra.Order.Star.Basic
import Mathlib.Algebra.Star.BigOperators
import Mathlib.RingTheory.Polynomial.Cyclotomic.Basic
import Mathlib.RingTheory.RootsOfUnity.Complex
import Mathlib.Analysis.Complex.Basic

/-!
# Per-`N` Hermitian-square certificates for `⟨4₁⟩_N` (bean `qou-pc7n`)

The figure-eight Kashaev sum `kashaevFigureEight (q + q⁻¹) N`
(`QOU.Core.TarskiSignKashaev`) is, term by term, a **Hermitian square**:

  `⟨4₁⟩_N = ∑_{k<N} star((q;q)_k) · (q;q)_k`,   `(q;q)_k = ∏_{j=1}^{k} (1 - q^j)`,

in any field with an involution `star` sending `q` to `q⁻¹`
(`kashaev_eq_sum_hermitian`). Each term is a finite algebraic certificate,
so in any star-ordered field every term is `≥ 0` and `⟨4₁⟩_N` dominates each
of them (`kashaev_ge_term`). At a primitive `N`-th root of unity the last
term is `|N|² = N²` by the cyclotomic identity `∏_{j=1}^{N-1} (1 - q^j) = N`,
so `⟨4₁⟩_N ≥ 1 + N²` (`kashaev_ge_one_add_sq`). No analysis is done per `N`.

## The embedding caveat

The bean warns that Jones unitarity holds only at `ζ = e^{±2πi/N}`, so a
certificate built from unitarity is not Galois-invariant. **This certificate
does not use unitarity.** It is a sum of norms from `ℚ(ζ_N)` to
`ℚ(ζ_N)⁺`, and every embedding of the CM field `ℚ(ζ_N)` in `ℂ` commutes
with complex conjugation. So the bound holds at **every** primitive `N`-th
root of unity in `ℂ`, i.e. at every Galois conjugate: `⟨4₁⟩_N` is totally
positive, with all conjugates `≥ 1 + N²` (`kashaev_complex_ge`). For `4₁` the
caveat does not bite; it will for a knot whose state sum is not a sum of
norms.

## What this does not claim

The `N → ∞` growth (the volume conjecture proper) is not claimed here; it is
a coev statement on `[Coev E]` (`QOU/Core/LawvereCut.lean`). The bound
`1 + N²` is polynomial; the exponential growth comes from the middle terms
`k ≈ 5N/6`, whose certificates are the same Hermitian squares but whose
size is not bounded here.

No empirical value enters this file.
-/

namespace QOU.Core.KashaevHermitianCertificate

open Finset QOU.Core.TarskiSignKashaev

section Cyclotomic

open Polynomial

/-- `∏_{k=1}^{n} (1 - μ^k) = n + 1` for a primitive `(n+1)`-th root of unity `μ`.
This is Mathlib's `IsPrimitiveRoot.prod_one_sub_pow_eq_order`, reproved from
`X_pow_sub_one_eq_prod` so as not to import `KummerExtension`. -/
theorem prod_one_sub_pow {R : Type*} [CommRing R] [IsDomain R] {n : ℕ} {μ : R}
    (hμ : IsPrimitiveRoot μ (n + 1)) : ∏ k ∈ range n, (1 - μ ^ (k + 1)) = n + 1 := by
  classical
  have this : (X ^ (n + 1) - C 1 : R[X]) = ∏ i ∈ range (n + 1), (X - C (μ ^ i)) := by
    rw [C_1, X_pow_sub_one_eq_prod n.succ_pos hμ, nthRootsFinset,
      ← Multiset.toFinset_eq (IsPrimitiveRoot.nthRoots_one_nodup hμ)]
    simp only [Finset.prod_mk]
    rw [hμ.nthRoots_eq (one_pow (n + 1)), Multiset.map_map]
    simp only [Function.comp_def, mul_one]
    rfl
  rw [C_1, ← mul_geom_sum, prod_range_succ', pow_zero, mul_comm, eq_comm] at this
  replace this := mul_right_cancel₀ (Polynomial.X_sub_C_ne_zero 1) this
  apply_fun Polynomial.eval 1 at this
  simpa only [mul_one, map_pow, eval_prod, eval_sub, eval_X, eval_pow, eval_C, eval_geom_sum,
    one_pow, sum_const, card_range, nsmul_eq_mul, Nat.cast_add, Nat.cast_one] using this

end Cyclotomic

section Star

variable {F : Type*} [Field F] [StarRing F]

/-- The `q`-Pochhammer symbol `(q;q)_k = ∏_{j=1}^{k} (1 - q^j)`. -/
def qPoch (q : F) (k : ℕ) : F := ∏ j ∈ range k, (1 - q ^ (j + 1))

theorem star_qPoch {q : F} (hstar : star q = q⁻¹) (k : ℕ) :
    star (qPoch q k) = ∏ j ∈ range k, (1 - q⁻¹ ^ (j + 1)) := by
  simp [qPoch, star_prod, star_sub, star_pow, hstar]

/-- **The Hermitian-square form of the figure-eight Kashaev sum.** -/
theorem kashaev_eq_sum_hermitian {q : F} (hq : q ≠ 0) (hstar : star q = q⁻¹) (N : ℕ) :
    kashaevFigureEight (q + q⁻¹) N = ∑ k ∈ range N, star (qPoch q k) * qPoch q k := by
  unfold kashaevFigureEight
  refine sum_congr rfl fun k _ => ?_
  rw [star_qPoch hstar, qPoch, ← prod_mul_distrib]
  refine prod_congr rfl fun j _ => ?_
  rw [mul_comm, kashaev_factor hq]

variable [PartialOrder F] [StarOrderedRing F]

/-- In a star-ordered field each Kashaev term is a nonnegative certificate and
`⟨4₁⟩_N` dominates it. -/
theorem kashaev_ge_term {q : F} (hq : q ≠ 0) (hstar : star q = q⁻¹) {N k : ℕ} (hk : k < N) :
    star (qPoch q k) * qPoch q k ≤ kashaevFigureEight (q + q⁻¹) N := by
  rw [kashaev_eq_sum_hermitian hq hstar]
  exact single_le_sum (f := fun i => star (qPoch q i) * qPoch q i)
    (fun i _ => star_mul_self_nonneg _) (mem_range.2 hk)

theorem kashaev_nonneg {q : F} (hq : q ≠ 0) (hstar : star q = q⁻¹) (N : ℕ) :
    0 ≤ kashaevFigureEight (q + q⁻¹) N := by
  rw [kashaev_eq_sum_hermitian hq hstar]
  exact sum_nonneg fun i _ => star_mul_self_nonneg _

/-- **Per-`N` lower bound.** At a primitive `(n+1)`-th root of unity with
`star q = q⁻¹` and `n ≥ 1`: `⟨4₁⟩_{n+1} ≥ 1 + (n+1)²`. The two certificates
used are the `k = 0` term `1` and the `k = n` term `star(n+1)·(n+1)`. -/
theorem kashaev_ge_one_add_sq {n : ℕ} (hn : 1 ≤ n) {q : F} (hμ : IsPrimitiveRoot q (n + 1))
    (hstar : star q = q⁻¹) :
    1 + ((n : F) + 1) ^ 2 ≤ kashaevFigureEight (q + q⁻¹) (n + 1) := by
  have hq : q ≠ 0 := hμ.ne_zero (Nat.succ_ne_zero n)
  rw [kashaev_eq_sum_hermitian hq hstar]
  have hsub : ({0, n} : Finset ℕ) ⊆ range (n + 1) := by
    intro x hx; simp only [mem_insert, mem_singleton] at hx; rcases hx with rfl | rfl <;> simp
  have hle := sum_le_sum_of_subset_of_nonneg (f := fun i => star (qPoch q i) * qPoch q i) hsub
    (fun i _ _ => star_mul_self_nonneg _)
  have h0n : (0 : ℕ) ∉ ({n} : Finset ℕ) := by simp; omega
  rw [sum_insert h0n, sum_singleton] at hle
  have htop : qPoch q n = (n : F) + 1 := prod_one_sub_pow hμ
  have h0 : qPoch q 0 = 1 := by simp [qPoch]
  simp only [htop, h0, star_one, star_add, star_natCast, one_mul] at hle
  simpa [pow_two] using hle

end Star

section Complex

open scoped ComplexOrder

/-- **Total positivity.** At every primitive `N`-th root of unity `ζ ∈ ℂ`
(every Galois conjugate of `e^{2πi/N}`), `⟨4₁⟩_N(ζ + ζ⁻¹) ≥ 1 + N²`. -/
theorem kashaev_complex_ge {n : ℕ} (hn : 1 ≤ n) {ζ : ℂ} (hμ : IsPrimitiveRoot ζ (n + 1)) :
    1 + ((n : ℂ) + 1) ^ 2 ≤ kashaevFigureEight (ζ + ζ⁻¹) (n + 1) := by
  have hnorm : ‖ζ‖ = 1 := hμ.norm'_eq_one (Nat.succ_ne_zero n)
  have hstar : star ζ = ζ⁻¹ := by
    rw [Complex.inv_def, Complex.normSq_eq_norm_sq, hnorm]; simp
  exact kashaev_ge_one_add_sq hn hμ hstar

end Complex

end QOU.Core.KashaevHermitianCertificate
