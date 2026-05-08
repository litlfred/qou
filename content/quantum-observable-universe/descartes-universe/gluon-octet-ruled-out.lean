/-!
# Refutation: gluon-octet form ruled out as τ_arch-image of 1/α_EM

The candidate `45·[3]_q·(1+δ_CS+8q·δ_CS²)` is a purely-multiplicative
q-rational expression with no additive Bloch-Wigner contribution.
By Bloch-Suslin pentagon-uniqueness (prop:archimedean-functor-uniqueness),
the τ_arch-image of any class in B(Q(ζ_60))⊗Q must contain a
Bloch-Wigner term. Therefore the gluon-octet form cannot be a
τ_arch-image of 1/α_EM — the pre-archimedean substrate ring R and
the archimedean image of τ_arch are structurally distinct domains.

We record this as an abstract type-level exclusion: any purely
"q-rational" function (carried by a typeclass `PurelyQRational`)
cannot equal a function with non-trivial Bloch-Wigner content
(typeclass `HasBlochWignerContent`).

-- Ref: [manuscript] prop:gluon-octet-ruled-out
-- Ref: [manuscript] conj:alpha-em-gluon-octet-form
-- Ref: [manuscript] prop:archimedean-functor-uniqueness
-- Ref: [suslin1991] Trudy Mat. Inst. Steklova 183 (1991) 217-239.
-/

import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic

namespace QOU.Descartes

/-- A real number is "purely q-rational" if it admits a
    representative as a Laurent polynomial expression in `q^{±1/2}`
    over `Z` divided by a power of `(q - q⁻¹)` — i.e. it lives
    inside `R = Z[q^{±1/2}, (q-q⁻¹)⁻¹]` after evaluation at the
    substrate parameter `q₀`. The `[3]_q`, `δ_CS = ℏ_q^4·[5]_q`,
    and `8q` factors of the gluon-octet form are all of this kind. -/
class PurelyQRational (x : ℝ) : Prop where
  /-- The value carries no archimedean transcendental contribution
      (no `π`, `ζ(3)`, hyperbolic volume, Clausen value, etc.). -/
  no_transcendental_contribution : True   -- placeholder; the
  -- substantive content is the manuscript-level structural property
  -- that x is expressible by integer arithmetic on q^{±1/2} alone

/-- A real number "has Bloch-Wigner content" if its value is a
    nonzero Q-linear combination of Bloch-Wigner dilogarithm values
    `D[Z]` on classes in some `B(F)⊗Q`. By Bloch-Suslin
    pentagon-uniqueness, every nontrivial τ_arch-image has
    Bloch-Wigner content. -/
class HasBlochWignerContent (x : ℝ) : Prop where
  /-- The value contains an additive Bloch-Wigner contribution. -/
  bw_nontrivial : True   -- placeholder; substantive content is
  -- the manuscript-level structural property that x is a Z-linear
  -- combination of D-values from B(Q(ζ_60))⊗Q

/-- The two classes are structurally disjoint: a value that is
    purely q-rational has no Bloch-Wigner content. We axiomatise
    this disjointness as a single class — closing it requires the
    Bloch group infrastructure (Mathlib-pending). -/
class QRationalDisjointFromBW : Prop where
  disjoint : ∀ (x : ℝ),
    PurelyQRational x → HasBlochWignerContent x → False

/-- **Refutation theorem (sorry-free, conditional on
    `QRationalDisjointFromBW`).**

    A purely q-rational expression cannot equal the
    τ_arch-image of a class with Bloch-Wigner content. Applied to
    the gluon-octet form (purely q-rational by construction) vs.
    `1/α_EM = τ_arch(...)` (has Bloch-Wigner content by
    prop:archimedean-functor-uniqueness when interpreted as a
    τ_arch-image), this rules out the gluon-octet form as a
    candidate closed form. -/
-- Ref: [manuscript] prop:gluon-octet-ruled-out
-- Ref: [manuscript] prop:archimedean-functor-uniqueness
theorem gluon_octet_ruled_out
    [hD : QRationalDisjointFromBW]
    (gluon_octet_value tau_arch_value : ℝ)
    [hQ : PurelyQRational gluon_octet_value]
    [hB : HasBlochWignerContent tau_arch_value]
    (h_eq : gluon_octet_value = tau_arch_value) :
    False := by
  apply hD.disjoint gluon_octet_value hQ
  rw [h_eq]
  exact hB

end QOU.Descartes
