import BraidKnotOctonion.WhiteheadLemma1RootOfUnity
import Mathlib.Algebra.Polynomial.Laurent
import QCalculus.GaussianBinomial

/-!
# The normalised coloured Jones of the braid `σ₁⁻²σ₂σ₁⁻¹σ₂` is an integer Laurent polynomial

Throughout, "the Whitehead braid" means `whiteheadWord = σ₁⁻²σ₂σ₁⁻¹σ₂ ∈ B₃`, and the invariant is
the RT coloured Jones of its **Markov class** (`braidJonesRT`). The statements here are about that
braid class. They become statements about the Whitehead *link* only with Markov's theorem (closures
are isotopic iff the braids are Markov-equivalent), which this repository does not yet prove
(issue #8902).

`WhiteheadBraidVolumeConjecture` defines the value of `[N]⁻¹ J_N(β)` at the Kashaev point as a
punctured limit, because `[N] = 0` there. This file removes that caveat: there is an integer
Laurent polynomial `P_N ∈ ℤ[s, s⁻¹]` (`s = q`) such that

* at every `σ` where the braid-closure construction is defined, `[N]⁻¹ J_N(p)(σ) = P_N(σ²)` for
  every braid `p` Markov-equivalent to `whiteheadWord` (`braidJonesRT_eq_laurent`);
* `P_N(e^{πi/N}) = whiteheadLinkKashaev N` (`laurent_at_kashaev_point`).

This file holds the algebraic part: `whiteheadLaurent` and its evaluation identity
`vdvWhiteheadLinkJones_eq_laurent`. The braid-class identity, the Kashaev-point value and the
volume limit are in the transcendental companion
`QOU/Transcendental/BraidKnotOctonion/WhiteheadJonesLaurentKashaev.lean`.

So the value at the Kashaev point is the evaluation of a Laurent polynomial, as in the standard
definition of the Kashaev invariant, and the volume limit is a statement about that evaluation
(`whiteheadLaurent_volume_conjecture`).

**Variables.** `ℤ[s, s⁻¹]` with `s = q` is `ℤ[t^{±1/2}]` in van der Veen's variable `t = s²`.
Integrality of the normalised coloured Jones of a link is known in general (Lê 2000; Habiro's
universal invariant for bottom tangles). This file proves it directly for this braid class from
van der Veen's formula, and does not use those results.

The only non-polynomial piece of van der Veen's formula is the clasp ratio
`∏_{j<n} (1 − t^{k+j+1}) / (1 − t^{j+1})`, which is the Gaussian binomial `[n+k choose n]_t`
(`QOU.MathlibExt.gaussG`, over any commutative ring).

-- Ref: [vanderveen2008] van der Veen, AGT 8 (2008) 603–624, Lemma 1
-- Ref: [le2000] Lê, "Integrality and symmetry of quantum link invariants", Duke Math. J. 102 (2000)
-- Ref: [habiro2002] Habiro, "Bottom tangles and universal invariants", AGT 6 (2006)
-/

namespace QOU.Knot.FigureEightVolume

open Polynomial Finset
open QOU.MathlibExt (gaussG prod_mul_gaussG clasp_prod_eq)

/-! ### The Laurent polynomial -/

open LaurentPolynomial in
/-- van der Veen's formula as an integer Laurent polynomial in `s` (`s = q`, `t = s²`). -/
noncomputable def whiteheadLaurent (N : ℕ) : LaurentPolynomial ℤ :=
  ∑ n ∈ range N,
    (∑ j ∈ range (2 * n + 1), T ((N : ℤ) * (2 * (n : ℤ) - 2 * (j : ℤ)))) *
      (T (((N : ℤ) ^ 2 - 1) + (N : ℤ) * ((N : ℤ) - 1)) *
        ∑ k ∈ range (N - n), T (-(2 * (N : ℤ) * ((n : ℤ) + k))) *
          ((∏ j ∈ range n, (1 - T (2 * ((N : ℤ) - ((j : ℤ) + 1) - k)))) *
            Polynomial.toLaurent ((gaussG n k).comp (X ^ 2))))

/-- Evaluation of a Laurent polynomial at a nonzero complex number. -/
noncomputable def evalL (s : ℂ) (hs : s ≠ 0) : LaurentPolynomial ℤ →+* ℂ :=
  LaurentPolynomial.eval₂ (Int.castRingHom ℂ) (Units.mk0 s hs)

theorem evalL_T (s : ℂ) (hs : s ≠ 0) (m : ℤ) : evalL s hs (LaurentPolynomial.T m) = s ^ m := by
  rw [evalL, LaurentPolynomial.eval₂_T, Units.val_zpow_eq_zpow_val, Units.val_mk0]

/-- **van der Veen's formula is the evaluation of `whiteheadLaurent N`** at every `s ≠ 0` with
`s^{2i} ≠ 1` for `1 ≤ i < N`. -/
theorem vdvWhiteheadLinkJones_eq_laurent {s : ℂ} (hs : s ≠ 0) {N : ℕ}
    (hroot : ∀ i : ℕ, 1 ≤ i → i < N → 1 - s ^ (2 * (i : ℤ)) ≠ 0) :
    vdvWhiteheadLinkJones s N = evalL s hs (whiteheadLaurent N) := by
  unfold vdvWhiteheadLinkJones whiteheadLaurent
  rw [map_sum]
  refine sum_congr rfl fun n hn => ?_
  have hn := mem_range.mp hn
  unfold vdvBeltFused vdvClasp
  simp only [map_mul, map_sum, map_prod, map_sub, map_one, evalL_T]
  congr 2
  refine sum_congr rfl fun k _ => ?_
  congr 1
  rw [clasp_prod_eq fun j hj => by
    have := hroot (j + 1) (by omega) (by have := mem_range.mp hj; omega)
    push_cast at this
    exact this]
  congr 1
  rw [evalL, LaurentPolynomial.eval₂_toLaurent, Polynomial.eval₂_comp]
  simp [Units.val_mk0]

end QOU.Knot.FigureEightVolume
