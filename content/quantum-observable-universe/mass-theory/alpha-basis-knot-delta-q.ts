import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:alpha-basis-knot-delta-q",
  title: "q-dimension decoration of the basis knots: $\\delta_q(T_{2,k}) = h\\,[k]_q$",
  lean: {
    ref: "qou:QOU.AlphaBasisKnot.deltaQ_eq_h_qbracket",
    validation: "not_checked",
  },
  computation: {
    engine: "python",
    status: "verified",
    script: "computations/delta_q_h_bracket_identity.py",
    witness: [
      "computations/delta-q-h-bracket-identity.witness.json",
    ],
  },
  uses: [
    "prop:alpha-em-categorical-trace-ratio",
  ],
  tags: [
    "alpha-basis-knot",
    "q-dimension",
    "quantum-integer",
    "pre-archimedean",
    "fine-structure-constant",
    "hecke",
  ],
});
