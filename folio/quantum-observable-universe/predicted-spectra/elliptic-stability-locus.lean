/-!
# Elliptic stability locus (conjectural)

Class-axiomatized stub for `rem:elliptic-stability-locus`: the
nuclear degeneracy locus (valley of stability in (Z, N) integer
lattice) is the integer-point set of an elliptic curve over
Bring's surface. The Coulomb and pairing terms in the
liquid-drop ansatz reduce to a Weierstrass elliptic curve whose
integer points trace the valley.

-- Ref: [manuscript]
Per `AGENTS.md §3b-cond`, opaque Props + class fields + sorry
instance per claim. Algebraic tier only — the numerical match
to the observed stable-isotope set belongs to a future
Archimedean tier (per gemini review on #721).

## References

- `[manuscript]` `rem:elliptic-stability-locus`
- `[manuscript]` `prop:integer-stability`
- `[manuscript]` `def:color-tube-fibers`
-/

namespace QOU.EllipticStabilityLocus

/-- **Algebraic claim (Weierstrass form)**: the (Coulomb +
    pairing) part of the nuclear binding ansatz, after rescaling
    by m_e, reduces to a Weierstrass elliptic curve over the
    color-tube fibration of Bring's surface (`def:color-tube-fibers`). -/
opaque WeierstrassFormHolds : Prop

/-- **Algebraic claim (integer-point identification)**: the
    valley of stability in `(Z, N)` integer lattice coincides
    with the integer points of the Weierstrass curve above. -/
opaque IntegerPointIdentificationHolds : Prop

/-- **Elliptic-stability-locus conjecture** (class-axiomatized per §3b-cond). -/
class EllipticStabilityLocus : Prop where
  weierstrass_form : WeierstrassFormHolds
  integer_point_identification : IntegerPointIdentificationHolds

-- **No instance is provided — that is the honest open state** (AGENTS.md
-- §3b-tax).  An instance would have to supply the field(s) below, which is
-- exactly the open conjecture; supplying one asserts the conjecture.
--
-- History: this file previously carried
--     instance elliptic_stability_locus_conjecture : EllipticStabilityLocus where
--     axiom elliptic_stability_locus_weierstrass_form : WeierstrassFormHolds
--     axiom elliptic_stability_locus_integer_point_identification : IntegerPointIdentificationHolds
-- i.e. the conjecture was discharged by `axiom` and installed as a global
-- instance, so every downstream `[EllipticStabilityLocus]` resolved for free and the
-- assumption was invisible outside `#print axioms`.  Removed, not completed.
-- Downstream results must take `[EllipticStabilityLocus]` as an explicit hypothesis.

end QOU.EllipticStabilityLocus
