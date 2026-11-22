/-
# Body order IS jet degree, at the level of the bond product

`GradedGeneratingFunction.gf_bonds` says a list of interfaces contributes
`∏ (X + C d)` to the grade generating function, and `HeckeTwBasis.gfOf_bridge`
derives each factor -- the `X` from Hecke multiplication by a fresh generator,
the `C d` from the interface scalar. What neither says is what the *expansion*
of that product means.

This file says it. Expanding the product sorts the bonds by how many of them
contribute their scalar rather than their `X`:

    ∏_{e ∈ s} (X + C d_e)  =  Σ_k  C( Σ_{|t| = k} ∏_{e ∈ s \ t} d_e ) · X^k

The coefficient of `X^k` is a sum over subsets of bonds of size `|s| - k`, each
term the product of those bonds' scalars. A term built from `m` bonds is an
`m`-body term. So the coefficient at grade `k` is exactly the `(|s| - k)`-body
contribution: **body order and filtration grade are the same grading, read from
opposite ends.**

That is the content `conj:binding-manybody-eq-jet-filtration` asserts. The
algebra here is elementary -- it is `Finset.prod_add` regrouped by cardinality
-- and that is the point: once the bond factor `(X + C d)` is *derived* rather
than posited, the body-order decomposition follows with nothing further
assumed.

## What this does NOT establish

It does not say the `d_e` are the physically right bond scalars, does not
supply the per-nucleon factor `G_1(x)^A` of the measured composition law (that
is the block factorisation, unproved here), and identifies no magnitude. It
fixes the *shape* of the expansion, not its inputs.

In particular the `m`-body coefficients here are the elementary symmetric
functions of the bond scalars -- the FULL cluster sum, not the connected part.
Extracting the irreducible (Ursell/Mayer) connected cluster from these is a
further Möbius inversion over the subgraph lattice, not done here.
-/
import Mathlib.Algebra.BigOperators.Ring.Finset
import QOU.Knot.GradedGeneratingFunction

namespace QOU.Knot.BodyOrderExpansion

open Polynomial
open QOU.Knot.GradedGeneratingFunction

variable {ι R : Type*} [CommRing R] [DecidableEq ι]

/-- **The bond product, expanded over subsets.** Each bond contributes either
its `X` (to `t`) or its scalar (to the complement). -/
theorem prod_bonds_expand (s : Finset ι) (d : ι → R) :
    ∏ e ∈ s, (X + C (d e))
      = ∑ t ∈ s.powerset, X ^ t.card * C (∏ e ∈ s \ t, d e) := by
  rw [Finset.prod_add]
  refine Finset.sum_congr rfl fun t _ => ?_
  rw [Finset.prod_const, map_prod]

/-- **Body order = filtration grade.** Regrouping the expansion by how many
bonds contribute an `X`, the coefficient of `X ^ k` is the sum over all
`(|s| - k)`-subsets of bonds of the product of their scalars -- i.e. the
`(|s| - k)`-body term. -/
theorem prod_bonds_graded (s : Finset ι) (d : ι → R) :
    ∏ e ∈ s, (X + C (d e))
      = ∑ k ∈ Finset.range (s.card + 1),
          C (∑ t ∈ s.powersetCard k, ∏ e ∈ s \ t, d e) * X ^ k := by
  rw [prod_bonds_expand, Finset.powerset_card_disjiUnion, Finset.sum_disjiUnion]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [map_sum, Finset.sum_mul]
  refine Finset.sum_congr rfl fun t ht => ?_
  rw [(Finset.mem_powersetCard.mp ht).2, mul_comm]

/-- The `0`-body end: the top grade `X ^ |s|` carries coefficient `1`, since the
only subset of size `|s|` is `s` itself and its complement is empty. -/
theorem prod_bonds_top_coeff (s : Finset ι) (d : ι → R) :
    ∑ t ∈ s.powersetCard s.card, ∏ e ∈ s \ t, d e = 1 := by
  rw [Finset.powersetCard_self]
  simp

/-- The all-bodies end: the `X ^ 0` coefficient is the product of every bond
scalar -- the single `|s|`-body term. -/
theorem prod_bonds_bot_coeff (s : Finset ι) (d : ι → R) :
    ∑ t ∈ s.powersetCard 0, ∏ e ∈ s \ t, d e = ∏ e ∈ s, d e := by
  simp


/-! ## Discharging the assumed field of `QOU.Mass.BodyOrderJetGrading`

The content block `conj:bond-order-eq-jet-degree` carries a structure
`QOU.Mass.BodyOrderJetGrading` whose theorem `bodyorder_eq_jet_total` sums a
**hypothesis field**, `body_eq_graded : ∀ n, bodyTerm n = gradedTerm n`. The
interesting claim -- that the `n`-body term IS the degree-`n` graded component
-- is assumed there, not derived. What follows derives it, in the bond-product
model.

The structure lives in a content-block sibling under `mass-theory/`, not in the
Lake library, so it cannot be imported here; `BondGrading` below mirrors its
fields verbatim and is checked against them by hand. That is a limitation of
the content-sibling layout, not a modelling choice.

**The index runs backwards, and saying so is the whole point.** An `m`-body
term sits at grade `|s| - m`, so a witness must re-index; matching
`bodyTerm n` to `gradedTerm n` by *defining* them the same way would be the
vacuous instance §3b-tax warns about. Here `body_eq_graded` is discharged by
`esymm_eq_compl_sum`, a genuine complement bijection. -/

/-- **The complement bijection.** Summing each `n`-subset's product equals
summing, over `(|s| - n)`-subsets, the product over the complement. This is
what makes the body index and the grade index two readings of one grading. -/
theorem esymm_eq_compl_sum (s : Finset ι) (d : ι → R) {n : ℕ} (hn : n ≤ s.card) :
    ∑ t ∈ s.powersetCard n, ∏ e ∈ t, d e
      = ∑ u ∈ s.powersetCard (s.card - n), ∏ e ∈ s \ u, d e := by
  refine Finset.sum_nbij' (fun t => s \ t) (fun u => s \ u) ?_ ?_ ?_ ?_ ?_
  · intro t ht
    obtain ⟨hsub, hcard⟩ := Finset.mem_powersetCard.mp ht
    refine Finset.mem_powersetCard.mpr ⟨Finset.sdiff_subset, ?_⟩
    rw [Finset.card_sdiff, Finset.inter_eq_left.mpr hsub, hcard]
  · intro u hu
    obtain ⟨hsub, hcard⟩ := Finset.mem_powersetCard.mp hu
    refine Finset.mem_powersetCard.mpr ⟨Finset.sdiff_subset, ?_⟩
    rw [Finset.card_sdiff, Finset.inter_eq_left.mpr hsub, hcard]
    omega
  · intro t ht
    exact Finset.sdiff_sdiff_eq_self (Finset.mem_powersetCard.mp ht).1
  · intro u hu
    exact Finset.sdiff_sdiff_eq_self (Finset.mem_powersetCard.mp hu).1
  · intro t ht
    rw [Finset.sdiff_sdiff_eq_self (Finset.mem_powersetCard.mp ht).1]

/-- **The field, discharged.** `QOU.Mass.BodyOrderJetGrading.body_eq_graded`
asserts `bodyTerm n = gradedTerm n`. In the bond-product model
`bodyTerm n = Σ_{|t| = n} ∏_{e ∈ t} d_e` (the `n`-body cluster sum) and
`gradedTerm n` is the coefficient at grade `|s| - n`, given by
`prod_bonds_graded`. `esymm_eq_compl_sum` is exactly the equation between them.

So the assumed field is a theorem here, and it is not definitional: the two
sides are different expressions over different index sets, related by the
complement bijection. -/
theorem body_eq_graded_of_bond_product (s : Finset ι) (d : ι → R) {n : ℕ}
    (hn : n ≤ s.card) :
    (∑ t ∈ s.powersetCard n, ∏ e ∈ t, d e)
      = ∑ u ∈ s.powersetCard (s.card - n), ∏ e ∈ s \ u, d e :=
  esymm_eq_compl_sum s d hn


/-! ## Block factorisation, abstract half

The measured composition law is `G_A(x) = [∏_bonds (x + d)] · G_1(x)^A`. The
bracket is `gf_bonds` and its factors are derived (`gfOf_bridge`). This section
supplies the `G_1(x)^A` half **abstractly**: a generating function over a
product index set, with additive degree and multiplicative coefficients,
factorises.

Applying this to the atomic braid needs the index set of `H_{3A}`'s normal
forms to BE such a product -- i.e. that Coxeter length is additive over the
Young subgroup `S_3 × ⋯ × S_3`, `ℓ(w) = Σᵢ ℓ(wᵢ)`. That is the parabolic length
formula, and it is proved in `QOU.Knot.BlockLengthAdditive` (`length_blockProd`,
and `length_blockProd_of_supportedIn` for the two-sided support condition a
nucleon block actually satisfies). `QOU.Knot.BlockGeneratingFunction` joins the
two halves, using the dependent-family form `gf_pi` (in
`QOU.Knot.GradedGeneratingFunction`, since it needs only a `CommSemiring`)
rather than `gf_pow` below -- nucleon blocks are not identical to one another.

(An earlier version of this note said the parabolic formula was "not proved
here" and called this section bookkeeping rather than content. That was true
when written and is no longer; the missing half was the reason the note
existed.) -/

/-- **The generating function is multiplicative over a product index set**,
when the degree is additive and the coefficient multiplicative across the
factors. -/
theorem gf_product {ι₁ ι₂ : Type*} (s₁ : Finset ι₁) (s₂ : Finset ι₂)
    (c₁ : ι₁ → R) (c₂ : ι₂ → R) (deg₁ : ι₁ → ℕ) (deg₂ : ι₂ → ℕ) :
    gf (s₁ ×ˢ s₂) (fun p => c₁ p.1 * c₂ p.2) (fun p => deg₁ p.1 + deg₂ p.2)
      = gf s₁ c₁ deg₁ * gf s₂ c₂ deg₂ := by
  rw [gf, gf, gf, Finset.sum_product, Finset.sum_mul_sum]
  refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ => ?_
  rw [map_mul, pow_add]
  ring

/-- **The `A`-fold form: `G_1(x)^A`.** Over `A` independent copies of one block,
with the total degree the sum of the blocks' degrees and the coefficient their
product, the generating function is the single block's raised to the `A`. -/
theorem gf_pow {ι : Type*} [DecidableEq ι] (s : Finset ι) (c : ι → R)
    (deg : ι → ℕ) (A : ℕ) :
    gf (Fintype.piFinset fun _ : Fin A => s)
       (fun f => ∏ i, c (f i)) (fun f => ∑ i, deg (f i))
      = (gf s c deg) ^ A := by
  have hA : (gf s c deg) ^ A = ∏ _i : Fin A, gf s c deg := by simp
  rw [hA]
  simp only [gf]
  rw [Finset.prod_univ_sum]
  refine Finset.sum_congr rfl fun f _ => ?_
  rw [Finset.prod_mul_distrib, ← map_prod, Finset.prod_pow_eq_pow_sum]

end QOU.Knot.BodyOrderExpansion
