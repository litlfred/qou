import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:interface-knot-markov-z",
  title:
    "Interface-knot contribution to canonical-atom Markov trace equals the Markov parameter z exactly",
  lean: {
    ref: "qou:QOU.BraidKnot.interface_knot_markov_z",
    validation: "not_checked",
  },
  uses: [
    // broken-ref removed (Phase 7): def:ew-interface-knot
    "thm:jones-markov-trace",
  ],
  cites: ["jones1987", "markov1936"],
  computation: {
    engine: "python",
    script:
      "computations/delta_lambda_fr_identity_phase5c.py",
    witness:
      "computations/delta-lambda-fr-identity-phase5c.witness.json",
    status: "verified",
  },
  tags: [
    "markov-trace",
    "markov-axiom",
    "interface-knot",
    "atomic-braid",
    "canonical-derivation",
    "z-parameter",
  ],
});
