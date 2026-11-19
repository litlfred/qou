import { remark } from "../../schema/builders";

/**
 * The other half of Călugăreanu, measured on the torus-knot components: total
 * torsion and writhe move freely along an isotopy, Wr + Tw_F stays an integer
 * — and even that integer is a property of the curve, not the knot type,
 * because the family crosses q simultaneous inflections at r = 4/(q²+4) and
 * the Frenet self-linking jumps by q there. The inflection algebra is in
 * `lean/QOU/Mass/TorusInflection.lean` (sorry-free); the measurement is
 * `the_torsion_half_is_not_an_invariant_probe.py`.
 */
export default remark({
  interprets: "prop:canonical-closure-torus-chain",
  label: "rem:frenet-framing-is-not-an-invariant",
  title:
    "The torsion half is not an invariant: the Frenet self-linking of $T(2,q)$ jumps by $q$ at $r = 4/(q^2+4)$",
  lean: {
    ref: "qou:QOU.Mass.TorusInflection.inflection_iff",
    sorryFree: true,
    validation: "not_checked",
  },
  uses: [
    "prop:canonical-closure-torus-chain",
  ],
  cites: ["milnor1950", "lickorish1997"],
  computation: {
    engine: "mpmath",
    script: "computations/probes/the_torsion_half_is_not_an_invariant_probe.py",
    witness: ["computations/probes/the_torsion_half_is_not_an_invariant_probe.witness.json"],
    status: "verified",
  },
  tags: [
    "mass-theory",
    "torus-knots",
    "total-curvature",
    "torsion",
    "framing",
    "lean-formalised",
    "draft",
  ],
});
