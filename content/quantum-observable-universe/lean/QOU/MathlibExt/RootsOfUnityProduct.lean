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

  -- Ref: [manuscript] QOU/Knot/Clausen.lean          (what consumes the constant)
  -- Ref: [manuscript] QOU/OneLoopPrefactorInvariance.lean
  -- Ref: [manuscript] computations/probes/one_loop_c_sigma_tetrahedral_probe.py
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

end QOU.MathlibExt
