/-
  `∏_{ζ ≠ 1} (1 - ζ) = n` over the `n`-th roots of unity — bean `qou-snpr`.

  THE MATHLIB GAP.  Mathlib has the `n`-th roots of unity as a multiset
  (`Polynomial.nthRoots`), their cardinality (`IsPrimitiveRoot.card_nthRoots_one`)
  and the factorisation `X^n - 1 = ∏ (X - ζ)`
  (`prod_multiset_X_sub_C_of_monic_of_roots_card_eq`), but NOT the value of the
  product `∏_{ζ ≠ 1}(1 - ζ)`.  Searched across all 6990 modules by grepping the
  `.ilean` declaration index — the mathlib package here is cache-only, so
  grepping source finds nothing and that is not evidence.  The related sine
  identity `∏_{k=1}^{n-1} sin(kπ/n) = n/2^{n-1}` is likewise absent.

  WHY THIS CORPUS WANTS IT.  Writing `s_k := -∑_{j=1}^k log(2 sin(jπ/N))`, the
  figure-eight one-loop expansion needs

      s_k = (N/π)·Λ(kπ/N) - ½·log(2N·sin(kπ/N)) + O(1/N)

  whereas `QOU.Knot.abs_deviation_le` currently gives only the leading term with
  an `O(log N)` error — and the missing correction is ITSELF `O(log N)`, so the
  existing bound is exactly one order too coarse to see it.  The identity below
  is the endpoint that pins the additive constant: at `k = N-1` it says
  `s_{N-1} = -log N`, which is where the `N` inside `log(2N sin)` comes from.
  Without it that constant is free, and `c_σ(4₁) = 3^{-1/4}` depends on it.

  THE PROOF is the classical derivative trick, and it avoids all `Finset`
  surgery on `nthRootsFinset` (whose API here is thin — `card`, `mem`, `def`,
  and no image lemma).  Differentiating `X^n - 1 = ∏_{ζ}(X - ζ)` and evaluating
  at the root `1` kills every factor except those with `ζ ≠ 1`:

      n = eval 1 (d/dX (X^n - 1)) = ∏_{ζ ≠ 1} (1 - ζ).

  `Polynomial.eval_multiset_prod_X_sub_C_derivative` is exactly this step.

  -- Ref: [leitner2026] QOU/Knot/Clausen.lean          (what consumes the constant)
  -- Ref: [leitner2026] QOU/OneLoopPrefactorInvariance.lean
  -- Ref: [leitner2026] computations/probes/one_loop_c_sigma_tetrahedral_probe.py
-/
import Mathlib.RingTheory.RootsOfUnity.PrimitiveRoots
import Mathlib.RingTheory.Polynomial.Cyclotomic.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Circle

namespace QOU.MathlibExt

open Polynomial Complex

/-- **`∏_{ζ ≠ 1}(1 - ζ) = n`** over the `n`-th roots of unity in `ℂ`.

The product is over `(nthRoots n 1).erase 1`, i.e. every `n`-th root of unity
except `1` itself, each counted once (the roots are distinct since `n ≠ 0` in
`ℂ`, which is what `card_nthRoots_one` encodes). -/
theorem prod_one_sub_nthRoots_erase_one {n : ℕ} (hn : n ≠ 0) :
    (Multiset.map (fun a : ℂ => 1 - a)
        ((Polynomial.nthRoots n (1 : ℂ)).erase 1)).prod = (n : ℂ) := by
  classical
  have hζ : IsPrimitiveRoot (Complex.exp (2 * (Real.pi : ℂ) * Complex.I / n)) n :=
    Complex.isPrimitiveRoot_exp n hn
  set p : ℂ[X] := X ^ n - C 1 with hp
  have hmonic : p.Monic := Polynomial.monic_X_pow_sub_C (1 : ℂ) hn
  have hroots : p.roots = Polynomial.nthRoots n (1 : ℂ) := rfl
  have hdeg : p.natDegree = n := by
    simpa [hp] using Polynomial.natDegree_X_pow_sub_C (R := ℂ) (r := (1 : ℂ)) (n := n)
  have hcard : p.roots.card = p.natDegree := by
    rw [hroots, hdeg]; exact hζ.card_nthRoots_one
  have hfact : (Multiset.map (fun a : ℂ => X - C a) p.roots).prod = p :=
    Polynomial.prod_multiset_X_sub_C_of_monic_of_roots_card_eq hmonic hcard
  have hmem : (1 : ℂ) ∈ p.roots := by
    rw [hroots, Polynomial.mem_nthRoots (Nat.pos_of_ne_zero hn)]
    exact one_pow n
  have key := Polynomial.eval_multiset_prod_X_sub_C_derivative hmem
  rw [hfact] at key
  rw [hroots] at key
  rw [← key, hp]
  simp [Polynomial.derivative_X_pow]

/-- **`∏_{j=1}^{n-1}(1 - ζ^j) = n`** for a primitive `n`-th root of unity `ζ`.

The index conversion needs no injectivity: `Multiset.map_erase_of_mem` holds for
any `f`, because multiset `erase` removes a single occurrence. -/
theorem prod_one_sub_zeta_pow {n : ℕ} (hn : n ≠ 0) {ζ : ℂ}
    (hζ : IsPrimitiveRoot ζ n) :
    ∏ j ∈ Finset.Ico 1 n, (1 - ζ ^ j) = (n : ℂ) := by
  classical
  have h := prod_one_sub_nthRoots_erase_one hn
  have hmap : Polynomial.nthRoots n (1 : ℂ)
      = Multiset.map (fun j => ζ ^ j) (Multiset.range n) := by
    simpa using hζ.nthRoots_eq (α := (1 : ℂ)) (a := (1 : ℂ)) (one_pow n)
  have h0 : (0 : ℕ) ∈ Multiset.range n := by
    simp [Nat.pos_of_ne_zero hn]
  have herase : (Polynomial.nthRoots n (1 : ℂ)).erase 1
      = Multiset.map (fun j => ζ ^ j) ((Multiset.range n).erase 0) := by
    rw [hmap, Multiset.map_erase_of_mem _ _ h0]
    simp
  rw [herase, Multiset.map_map] at h
  have hidx : (Finset.Ico 1 n).val = (Multiset.range n).erase 0 := by
    have : (Finset.range n).erase 0 = Finset.Ico 1 n := by
      ext j; simp [Finset.mem_erase, Finset.mem_Ico]; omega
    rw [← this]; rfl
  rw [Finset.prod_eq_multiset_prod, hidx]
  simpa [Function.comp] using h

/-- **`∏_{j=1}^{n-1} 2 sin(jπ/n) = n`.**

The real form, obtained from `prod_one_sub_zeta_pow` at `ζ = e^{2πi/n}` by
taking norms, using `‖1 - e^{iθ}‖ = 2 sin(θ/2)` on `(0, 2π)`.

At `k = n-1` this is `s_{n-1} = -log n` for
`s_k = -∑_{j=1}^k log(2 sin(jπ/n))`, the endpoint that pins the additive
constant in the one-loop expansion of `QOU.Knot.kashaev`. -/
theorem prod_two_sin_pi_div (n : ℕ) (hn : n ≠ 0) :
    ∏ j ∈ Finset.Ico 1 n, (2 * Real.sin ((j : ℝ) * Real.pi / n)) = (n : ℝ) := by
  classical
  have hnR : (0 : ℝ) < n := by exact_mod_cast Nat.pos_of_ne_zero hn
  set ζ : ℂ := Complex.exp (2 * (Real.pi : ℂ) * Complex.I / n) with hζdef
  have hζ : IsPrimitiveRoot ζ n := Complex.isPrimitiveRoot_exp n hn
  -- each factor: ‖1 - ζ^j‖ = 2 sin(jπ/n)
  have hfac : ∀ j ∈ Finset.Ico 1 n,
      ‖1 - ζ ^ j‖ = 2 * Real.sin ((j : ℝ) * Real.pi / n) := by
    intro j hj
    rw [Finset.mem_Ico] at hj
    have hjpos : (0 : ℝ) < (j : ℝ) * Real.pi / n := by
      have : (0 : ℝ) < (j : ℝ) := by exact_mod_cast hj.1
      positivity
    have hjlt : (j : ℝ) * Real.pi / n < Real.pi := by
      rw [div_lt_iff₀ hnR]
      have : (j : ℝ) < n := by exact_mod_cast hj.2
      nlinarith [Real.pi_pos]
    have hsin : 0 < Real.sin ((j : ℝ) * Real.pi / n) :=
      Real.sin_pos_of_pos_of_lt_pi hjpos hjlt
    set x : ℝ := (j : ℝ) * Real.pi / n with hx
    have hpow : ζ ^ j = Complex.exp (((2 * x : ℝ) : ℂ) * Complex.I) := by
      rw [hζdef, ← Complex.exp_nat_mul]
      congr 1
      push_cast [hx]
      ring
    rw [hpow]
    have hre : (Complex.exp (((2 * x : ℝ) : ℂ) * Complex.I)).re = Real.cos (2 * x) :=
      Complex.exp_ofReal_mul_I_re _
    have him : (Complex.exp (((2 * x : ℝ) : ℂ) * Complex.I)).im = Real.sin (2 * x) :=
      Complex.exp_ofReal_mul_I_im _
    have hsq : ‖1 - Complex.exp (((2 * x : ℝ) : ℂ) * Complex.I)‖ ^ 2
        = (2 * Real.sin x) ^ 2 := by
      rw [← Complex.normSq_eq_norm_sq, Complex.normSq_apply]
      simp only [Complex.sub_re, Complex.sub_im, Complex.one_re, Complex.one_im,
        hre, him]
      nlinarith [Real.sin_sq_add_cos_sq (2 * x), Real.sin_sq_eq_half_sub x]
    have h1 : (0 : ℝ) ≤ ‖1 - Complex.exp (((2 * x : ℝ) : ℂ) * Complex.I)‖ :=
      norm_nonneg _
    have h2 : (0 : ℝ) ≤ 2 * Real.sin x := by linarith
    nlinarith [hsq, h1, h2]
  calc ∏ j ∈ Finset.Ico 1 n, (2 * Real.sin ((j : ℝ) * Real.pi / n))
      = ∏ j ∈ Finset.Ico 1 n, ‖1 - ζ ^ j‖ := by
        exact (Finset.prod_congr rfl hfac).symm
    _ = ‖∏ j ∈ Finset.Ico 1 n, (1 - ζ ^ j)‖ := (norm_prod _ _).symm
    _ = ‖(n : ℂ)‖ := by rw [prod_one_sub_zeta_pow hn hζ]
    _ = (n : ℝ) := by simp

end QOU.MathlibExt
