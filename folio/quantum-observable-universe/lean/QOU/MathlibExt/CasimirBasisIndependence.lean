import Mathlib.Algebra.Algebra.Bilinear
import Mathlib.LinearAlgebra.Basis.Defs

/-!
# QOU.MathlibExt.CasimirBasisIndependence — the Casimir does not depend on the dual pair

`Σ_i b_i b_i^∨` is the same element of the algebra for **any** dual pair.  This
is the link between the two halves of the Casimir story:

* `QOU.Hecke.TauDualBasis` proves the `T_w`-Casimir `Σ_w T_w T^∨_w` is central;
* `QOU.MathlibExt.CasimirBlockScalar` computes what a Casimir *is* in the
  matrix-unit basis of a product of matrix algebras, namely `d_i / c_i` on each
  block.

Neither statement mentions the other's basis, so on its own neither says
anything about the other's element.  This file supplies the bridge.

## The hypotheses are the expansions, not the bases

The proof needs exactly two facts, one per pair, and each is the statement that
*coordinates are values of the trace*:

  `hb : ∀ y, Σ_i t(y · b'_i) • b_i = y`      (expand on `b`, pair against `b'`)
  `hd : ∀ p, Σ_p t(d_p · y) • d'_p = y`      (expand on `d'`, pair against `d`)

Taking these as hypotheses rather than deriving them from "is a basis with
`t(b_i b'_j) = δ`" keeps the lemma applicable directly: both are already proved
on the Hecke side (`sum_tau_mul_TwDual_smul_Tw`, `sum_tau_Tw_mul_smul_TwDual`),
so nothing has to be re-derived there.

Note the asymmetry — one expansion pairs on the *right*, the other on the
*left*.  That is not a typo: it is what lets the middle step move `b_i` out to
the left of the inner sum, and it is why a "symmetrised" version of this lemma
would not compose with what the Hecke side proves.

## What is proved

* `casimir_eq_of_expansions` — `Σ_p d_p d'_p = Σ_i b_i b'_i`.

No trace property, no nondegeneracy, and no finiteness beyond the two index
types being `Fintype`; the two expansions carry all of it.  Generic over
`[CommSemiring K]`, `[Ring A]`, `[Algebra K A]` per §7c.
-/

namespace QOU.MathlibExt

section BasisIndependence

variable {K : Type*} [CommSemiring K]
variable {A : Type*} [Ring A] [Algebra K A]
variable {ι κ : Type*} [Fintype ι] [Fintype κ]

/-- **The Casimir is the same element for any dual pair.**

    Everything is carried by the two expansion hypotheses; the proof is the
    single interchange `Σ_p Σ_i = Σ_i Σ_p` with the scalars pulled through the
    product on the appropriate side. -/
theorem casimir_eq_of_expansions (t : A →ₗ[K] K) (b b' : ι → A) (d d' : κ → A)
    (hb : ∀ y : A, ∑ i, t (y * b' i) • b i = y)
    (hd : ∀ y : A, ∑ p, t (d p * y) • d' p = y) :
    ∑ p, d p * d' p = ∑ i, b i * b' i := by
  classical
  calc ∑ p, d p * d' p
      = ∑ p, (∑ i, t (d p * b' i) • b i) * d' p := by
        exact Finset.sum_congr rfl fun p _ => by rw [hb (d p)]
    _ = ∑ p, ∑ i, t (d p * b' i) • (b i * d' p) := by
        exact Finset.sum_congr rfl fun p _ => by
          rw [Finset.sum_mul]
          exact Finset.sum_congr rfl fun i _ => by rw [smul_mul_assoc]
    _ = ∑ i, ∑ p, t (d p * b' i) • (b i * d' p) := Finset.sum_comm
    _ = ∑ i, b i * (∑ p, t (d p * b' i) • d' p) := by
        refine Finset.sum_congr rfl fun i _ => ?_
        rw [Finset.mul_sum]
        exact Finset.sum_congr rfl fun p _ => by rw [mul_smul_comm]
    _ = ∑ i, b i * b' i := by
        exact Finset.sum_congr rfl fun i _ => by rw [hd (b' i)]

end BasisIndependence

end QOU.MathlibExt
