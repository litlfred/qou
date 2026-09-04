import QOU.Hecke.TwGramDetNonzero
import QOU.MathlibExt.RegTraceGramBasisChange

/-!
# QOU.Hecke.TwGramDetSquareClass — the `T_w` Gram determinant's square class

Bean `qou-kwoa`, the determinant's **value**, specialised to the object the corpus actually
uses.

`QOU.MathlibExt.RegTraceGramProduct` derives the integer constant `∏_λ d_λ^(d_λ²)` for the
Gram determinant of a semisimple algebra **in a product basis**, and
`QOU.MathlibExt.RegTraceGramBasisChange` transports a Gram determinant between bases at the
cost of a square.  This file instantiates the two at the Hecke algebra, so the left-hand side
is literally `(twGram K (q ^ 2) n).det`.

## The statement, and why it is an `∃`

    (twGram K (q ^ 2) n).det = (det P)² · ∏_λ ± d_λ^(d_λ²)

The `∃ P` is not vagueness — it is the correct strength.  A Gram determinant is an invariant
of a bilinear form only **up to squares of units**, because congruence `G ↦ PᵀGP` is the
transformation law.  So no theorem of this shape can pin an integer on the nose, and what is
true is that `∏_λ d_λ^(d_λ²)` is exactly the **square class** of `det(twGram)`.  The witness
is explicit in the proof — the change of basis from `T_w` to the matrix-unit basis pulled back
along the Wedderburn isomorphism — and is not evaluated.

`d_λ` is the number of standard Young tableaux of shape `λ`, i.e. the dimension of the
Wedderburn block, so the constant is the one
`computations/hecke/tw_gram_determinant_probe.py` measured at `n = 1, 2, 3` as `1`, `2⁴` and
`2⁴·3¹⁸`.

## Relation to `twGram_det_ne_zero`

`QOU.Hecke.TwGramDetNonzero` reaches `det(twGram) ≠ 0` by a route that never computes a
determinant at all.  This file gets the same non-vanishing as a **corollary of the formula**,
by a completely different argument: the change-of-basis factor is a unit and each block
contributes `± d_λ^(d_λ²)`.  The two agreeing is a real cross-check, and neither is derived
from the other.

That corollary carries a **hypothesis** — that no block dimension dies in `K` — which is
*not* discharged here.  It is true in characteristic zero, since every shape admits at least
one standard tableau, but proving `0 < d_λ` is separate work and is not done.

## What is NOT claimed

**`det P` is not evaluated.**  This does *not* say `det(twGram) = ∏_λ d_λ^(d_λ²)`; it says the
two differ by a square.  Nothing here touches the `q`-part of the determinant, where the Schur
elements live, so this is **not** a proof of Geck–Pfeiffer 7.2.6.
-/

namespace QOU.Hecke.TwBasis

open QOU.MathlibExt QOU.SchurWeyl
open QOU.Mathlib (StandardYoungTableau)

/-- **The Wedderburn block index at `λ`** — standard Young tableaux of shape `λ`, whose
cardinality `d_λ` is the block dimension.  A `reducible` abbreviation, so it unifies with the
`heckeWedderburn` codomain definitionally; it exists to keep the statement below readable. -/
abbrev blockIdx {n : ℕ} (lam : Nat.Partition (n + 1)) : Type :=
  StandardYoungTableau (QOU.Mathlib.partitionShape lam)

/-- **The `T_w` Gram determinant is a square times the derived integer constant.**

The Wedderburn blocks of `H_{n+1}` are indexed by partitions `λ` of `n + 1`, with block
dimension `d_λ` the number of standard Young tableaux of shape `λ`; the constant is
`∏_λ ± d_λ^(d_λ²)`.

The square is the change of basis from `T_w` to the matrix-unit basis pulled back along
`(skeinIwahoriEquiv).symm.trans heckeWedderburn` — the same composition
`twGram_det_ne_zero` feeds to the non-vanishing criterion.  It is **not evaluated**; see the
module docstring on why no statement of this shape can remove it. -/
theorem twGram_det_eq_sq_mul_prod {K : Type*} [Field K] [CharZero K] (q : K)
    (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
    ∃ P : Matrix (Equiv.Perm (Fin (n + 1))) (Equiv.Perm (Fin (n + 1))) K, IsUnit P.det ∧
      (twGram K (q ^ 2) n).det
        = P.det ^ 2 * ∏ lam : Nat.Partition (n + 1),
            (Equiv.Perm.sign (Equiv.prodComm (blockIdx lam) (blockIdx lam)) : K)
              * (Fintype.card (blockIdx lam) : K)
                  ^ (Fintype.card (blockIdx lam) * Fintype.card (blockIdx lam)) := by
  haveI : FiniteDimensional K (QOU.Hecke.IwahoriHecke K (q ^ 2) n) :=
    FiniteDimensional.of_fintype_basis (basisTwOfField K (q ^ 2) n)
  set E := (skeinIwahoriEquiv q hq0 n).symm.trans (heckeWedderburn q hq0 hq2 n) with hE
  set bProd := Pi.basis fun lam : Nat.Partition (n + 1) =>
    Matrix.stdBasis K (blockIdx lam) (blockIdx lam) with hbProd
  set bPulled := bProd.map E.symm.toLinearEquiv with hbPulled
  refine ⟨((bPulled.reindex (bPulled.indexEquiv (basisTwOfField K (q ^ 2) n))).toMatrix
    (basisTwOfField K (q ^ 2) n)), isUnit_det_basis_toMatrix _ _, ?_⟩
  exact regTraceGram_det_eq_sq_mul_prod_matrix E (basisTwOfField K (q ^ 2) n)
    (bPulled.indexEquiv (basisTwOfField K (q ^ 2) n))

/-- **Non-vanishing, by a route that goes THROUGH the determinant.**

`QOU.Hecke.TwGramDetNonzero.twGram_det_ne_zero` reaches the same conclusion without ever
computing a determinant, via semisimplicity and the converse of the Gram criterion.  This
derives it from the square-class formula instead: the change-of-basis factor is a unit
(`isUnit_det_basis_toMatrix`) and each block contributes `± d_λ^(d_λ²)`, so the product is
nonzero as soon as no block dimension dies in `K`.

The hypothesis is exactly the one `regTraceGram_pi_matrix_det_ne_zero_iff` shows is *sharp*.
It is true in characteristic zero — every shape admits a standard tableau, so `0 < d_λ` — but
that is **not proved here**, which is why it is a hypothesis rather than an instance argument.
Two independent arguments landing on the same conclusion is a real cross-check; neither is
derived from the other. -/
theorem twGram_det_ne_zero_of_blocks {K : Type*} [Field K] [CharZero K] (q : K)
    (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ)
    (h : ∀ lam : Nat.Partition (n + 1), (Fintype.card (blockIdx lam) : K) ≠ 0) :
    (twGram K (q ^ 2) n).det ≠ 0 := by
  obtain ⟨P, hP, hdet⟩ := twGram_det_eq_sq_mul_prod q hq0 hq2 n
  rw [hdet]
  refine mul_ne_zero (pow_ne_zero _ hP.ne_zero) (Finset.prod_ne_zero_iff.mpr fun lam _ => ?_)
  refine mul_ne_zero ?_ (pow_ne_zero _ (h lam))
  rcases Int.units_eq_one_or (Equiv.Perm.sign (Equiv.prodComm (blockIdx lam) (blockIdx lam)))
    with hs | hs <;> simp [hs]

end QOU.Hecke.TwBasis
