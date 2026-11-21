import QOU.Basic

/-!
# QOU.FlavorDressing.FlavorDressingFunctor

The categorical assignment of a dressed-mass scale to each quark
flavor, formalised as a typeclass on a concrete `Flavor` enum.

LaTeX: `\label{def:flavor-dressing-functor}`
-/

namespace QOU.FlavorDressing

/-- The discrete category of quark flavors.  Initial scope: u, d.
    Heavy flavors (s, c, b, t) included in the enum for forward
    compatibility; their individual `μ` values are open and live as
    opt-in instances in follow-up files. -/
inductive Flavor where
  | up      : Flavor
  | down    : Flavor
  | strange : Flavor
  | charm   : Flavor
  | bottom  : Flavor
  | top     : Flavor
  deriving Repr, DecidableEq

/-- **Flavor dressing functor.** Assigns a dressed-mass scale `μ q ∈ ℝ`
    to each quark flavor with the positivity hypothesis `0 < μ q`.

    The discrete-category framing makes the assignment compatible
    with the chapter's other categorical constructions (Markov
    trace, Hoefsmit functor, Wedderburn block decomposition):
    flavor-sums in hadronic mass formulas are then intended to read
    as natural transformations rather than ad-hoc weighted sums.

    **Naming note (functor vs. object-map).** A functor out of a
    *discrete* category is exactly an object-map (every morphism is an
    identity), so calling `μ` a "functor" is defensible — but note this
    class encodes **only** the object-map `μ : Flavor → ℝ` (+ positivity);
    it is not a `CategoryTheory.Functor`, and no natural transformation is
    formalised here. The "natural transformations" remark above is the
    intended categorical reading, not encoded structure.

    Instances at specific substrate parameter values (e.g. `q = q₀`)
    live in sibling files; this class carries only the structural
    signature + positivity. -/
-- Ref: [leitner2026] braids-and-knots/flavor-dressing-functor
class FlavorDressingFunctor where
  /-- Dressed-mass scale at each flavor, in physical units (MeV). -/
  μ : Flavor → ℝ
  /-- Positivity: every dressed quark mass is strictly positive. -/
  μ_pos : ∀ q : Flavor, 0 < μ q

namespace FlavorDressingFunctor

/-- Convenience accessor for the up-quark dressed mass. -/
def μ_u [F : FlavorDressingFunctor] : ℝ := F.μ Flavor.up

/-- Convenience accessor for the down-quark dressed mass. -/
def μ_d [F : FlavorDressingFunctor] : ℝ := F.μ Flavor.down

/-- The u-d splitting `μ_d − μ_u` (commonly used in hadronic mass
    formulas; signed so that the neutron–proton splitting is
    proportional to this quantity). -/
def μ_ud_split [F : FlavorDressingFunctor] : ℝ :=
  F.μ Flavor.down - F.μ Flavor.up

/-- Positivity of the up-quark dressed mass (specialisation). -/
theorem μ_u_pos [F : FlavorDressingFunctor] : 0 < (μ_u : ℝ) :=
  F.μ_pos Flavor.up

/-- Positivity of the down-quark dressed mass (specialisation). -/
theorem μ_d_pos [F : FlavorDressingFunctor] : 0 < (μ_d : ℝ) :=
  F.μ_pos Flavor.down

end FlavorDressingFunctor

end QOU.FlavorDressing
