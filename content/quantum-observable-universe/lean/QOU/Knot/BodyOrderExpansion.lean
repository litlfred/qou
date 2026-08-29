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

end QOU.Knot.BodyOrderExpansion
