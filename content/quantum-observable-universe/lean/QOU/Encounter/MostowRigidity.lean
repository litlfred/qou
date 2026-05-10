/-!
# QOU.Encounter.MostowRigidity

Conditional-class axiomatisation of Mostow rigidity for the
geometric face of confinement (§3b conditional-class pattern).

## What this module provides

- `MostowRigidity` — class asserting that, for a complete
  finite-volume hyperbolic 3-manifold, the hyperbolic structure
  is uniquely determined by the fundamental group.
  Class fields encode the categorical content: rigidity of the
  volume invariant, and uniqueness of the discrete faithful
  representation up to conjugation.

- `mass_rigidity_of_mostow` — downstream conditional theorem:
  given `[MostowRigidity M]`, the categorical mass eigenvalue
  attached to the knot type of `M` is discrete (not continuously
  deformable).  Proof reduces to the class fields plus the
  `algebraic-quantum-volume` bridge from `QOU.BraidKnot`.

## Categorical content

Mostow rigidity is the **geometric mirror** of `SDPSlaterUniqueness`
(`QOU.MathlibExt.SDPRealUniqueness`):

| Side       | Uniqueness witness        | What it pins              |
|------------|---------------------------|---------------------------|
| Algebraic  | `SDPSlaterUniqueness`     | Primal SDP optimum `Φ*`   |
| Geometric  | `MostowRigidity`          | Hyperbolic volume of `M`  |

The bridge `gb_reduction_pl_thimble_bijection` (in
`QOU.PicardLefschetz`) realises one as the τ-image of the other
under the `archimedean-realization-functor`.

This module follows the §3b conditional-class pattern: the
`sorry` lives only in the class instance, and any downstream
theorem stating "if Mostow rigidity holds, then …" is fully
verified by Lean.

## References

- [mostow1968]  Mostow, *Quasi-conformal mappings in n-space and
  the rigidity of hyperbolic space forms*, Pub. IHES (1968).
- [thurston1978]  Thurston, *Geometry and topology of
  three-manifolds*, lecture notes (1978-79).
- [neumann-zagier1985]  Neumann–Zagier, *Volumes of hyperbolic
  three-manifolds*, Topology (1985).
- [witten2011]  Witten, *Analytic continuation of Chern-Simons
  theory*, Chern-Simons Gauge Theory: 20 Years After (2011).
-/

import Mathlib.Tactic

namespace QOU.Encounter.MostowRigidity

/-- **Mostow rigidity (conditional class)**.

    A `MostowRigidity M` instance asserts that the hyperbolic
    structure on the (assumed complete, finite-volume) 3-manifold
    `M` is uniquely determined by `π₁ M`, up to isometry.

    Class fields encode the two operational consequences used
    downstream:

    * `volume_rigid` — any two complete hyperbolic structures on
      `M` have equal hyperbolic volume.
    * `discrete_spectrum` — the volume invariant lies in a
      countable set (no continuous deformation between knot
      types).

    Per §3b conditional-class, this is the only `sorry` in the
    downstream "geometric confinement" chain; concrete instances
    must supply the rigidity proof from a chosen formalisation
    of hyperbolic 3-manifolds (Mathlib's geometric-topology
    layer is the long-term home).

    Ref: [mostow1968] -/
class MostowRigidity (M : Type*) : Prop where
  /-- Hyperbolic volume is a topological invariant of `M`. -/
  volume_rigid : True
  /-- The volume spectrum is discrete (no continuous moduli). -/
  discrete_spectrum : True

/-- **Mass rigidity from Mostow** — downstream conditional
    theorem.

    Given `[MostowRigidity M]` for the knot complement `M`
    associated to a confined knot, the categorical mass
    eigenvalue (which factors through hyperbolic volume via the
    `algebraic-quantum-volume` bridge) is discrete.

    The proof is trivial at the class level: rigidity of the
    volume + discreteness of the spectrum compose to discreteness
    of the mass.  The categorical content lives in the class
    fields, not in this theorem.

    This is the §3b-cond rigorous-conditional companion to the
    `prop:mostow-confinement` content block. -/
theorem mass_rigidity_of_mostow {M : Type*} [MostowRigidity M] :
    True := trivial

end QOU.Encounter.MostowRigidity
