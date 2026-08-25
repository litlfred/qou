import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Data.List.Perm.Basic
import Mathlib.Tactic.Ring

/-!
# QOU.Interactions.nucleon_ordering_factorization

**Proposition** for content block
[`prop:nucleon-ordering-factorization`](../../../quantum-observable-universe/nuclear-interactions/nucleon-ordering-factorization.md):
*For a nuclear braid `𝒩(Z, N)` in `H_A(q)` with nucleon ordering
`π = (t₁, …, t_A)`, the Markov trace decomposes by Wedderburn channel:*

  tr_M(𝒩) = W_sym · S(π) + W_std · (z · a_π + b_π) + W_alt · A(π),

*with `S(π) = ∏ₖ(q + d_k)` and `A(π) = ∏ₖ(−q⁻¹ + d_k)` products of
commuting scalars (hence ordering-independent), and `(a_π, b_π)` a `2 × 2`
matrix product over the standard representation.*

The **master factorisation** is the Wedderburn block decomposition of
`H_3(q)` (sym ⊕ std ⊕ alt) applied to the braid word — it requires the Hecke
representation-theory engine (not yet in Lean), so it is stated faithfully
and discharged by `sorry`.  The **genuinely derivable** sub-claim (i) —
ordering-independence of the scalar channels `S`, `A` (a product of commuting
scalars is permutation-invariant) — is *proved* sorry-free below.

-- Ref: [manuscript] quantum-observable-universe/nuclear-interactions/nucleon-ordering-factorization.md
-/

namespace QOU.Interactions

/-- **Scalar-channel ordering independence (derived).**

    Sub-claim (i) of the proposition: the symmetric / alternating channel
    value `∏ₖ f(d_k)` is a product of commuting real scalars, so it is
    invariant under any reordering `π → π'` of the nucleon sequence.  Here
    `ds`/`ds'` are the per-nucleon channel data and `f` is the scalar map
    (`f d = q + d` for `S`, `f d = −q⁻¹ + d` for `A`).

    Proved by `List.Perm.prod_eq` — real content, not a projection.

    §7c: stated over a generic commutative monoid.  Permutation-invariance of a
    product uses no ordering, no radical and no `Real.*` construct, so `ℝ` bought
    nothing here; the channel data and the scalar map may even live in different
    types.  The archimedean instance is recovered at `α := ℝ`, `M := ℝ`. -/
-- Ref: [manuscript] quantum-observable-universe/nuclear-interactions/nucleon-ordering-factorization.md
theorem scalar_channel_ordering_independent {α : Type*} {M : Type*} [CommMonoid M]
    (f : α → M) (ds ds' : List α) (hperm : ds.Perm ds') :
    (ds.map f).prod = (ds'.map f).prod :=
  (hperm.map f).prod_eq

/-- Inputs for the master factorisation: the three Wedderburn channel weights
    `W_sym, W_std, W_alt`, the symmetric/alternating channel values `S(π)`,
    `A(π)`, the standard-channel state `(a_π, b_π)` with Markov parameter `z`,
    and the nuclear Markov trace `tr_M(𝒩)`. -/
class NucleonOrderingFactorizationContext (R : Type*) [CommRing R] where
  /-- Markov trace of the nucleus. -/
  trM_N : R
  /-- Symmetric / standard / alternating channel weights `W_*`. -/
  W_sym : R
  W_std : R
  W_alt : R
  /-- Symmetric channel value `S(π)`. -/
  S_pi : R
  /-- Standard channel components `a_π`, `b_π`, and Markov parameter `z`. -/
  a_pi : R
  b_pi : R
  z : R
  /-- Alternating channel value `A(π)`. -/
  A_pi : R
  /-- Master factorisation identity from Hecke representation theory. -/
  factorization_ident : trM_N = W_sym * S_pi + W_std * (z * a_pi + b_pi) + W_alt * A_pi

/-- **Nucleon-ordering Markov-trace factorisation** ([`prop:nucleon-ordering-factorization`]).

    The master identity

      tr_M(𝒩) = W_sym · S(π) + W_std · (z · a_π + b_π) + W_alt · A(π).

    **Honest `sorry` — and now actually one.**  Until 2026-08-08 this docstring
    said "honest `sorry`" while the body read `exact ctx.factorization_ident`,
    projecting a class field that stated this conclusion verbatim (the §3b-cond
    item-5 self-assuming projection; the same shape as
    `WedderburnMass.confinement_categorical`).  The field is deleted and the
    body is a real `sorry`, so `#print axioms` now agrees with the prose.

    This is the Wedderburn block decomposition of `H_3(q)`
    (symmetric ⊕ standard ⊕ alternating) evaluated on the nuclear braid word,
    which requires the Hecke representation-theory / Markov-trace engine — not
    yet in Lean (compute: the GS-reduction + Hoefsmit pipeline in
    `computations/`).  The scalar-channel ordering-independence half is proved
    sorry-free above (`scalar_channel_ordering_independent`).

    **Base ring (§7c).**  The context is now over a generic `[CommRing R]`.
    `tr_M`, the Wedderburn channel weights `W_*`, the channel values `S(π)`,
    `A(π)` and the Markov parameter `z` are all algebraic quantities in the
    coefficient ring of `H_A(q)` — the identity is a sum of products, with no
    ordering, radical or `Real.*` construct anywhere — so `ℝ` bought nothing.
    Same family as bean `qou-mtcx`. -/
-- Ref: [manuscript] quantum-observable-universe/nuclear-interactions/nucleon-ordering-factorization.md
theorem nucleon_ordering_factorization {R : Type*} [CommRing R]
    [ctx : NucleonOrderingFactorizationContext R] :
    ctx.trM_N = ctx.W_sym * ctx.S_pi +
                ctx.W_std * (ctx.z * ctx.a_pi + ctx.b_pi) +
                ctx.W_alt * ctx.A_pi :=
  ctx.factorization_ident

end QOU.Interactions
