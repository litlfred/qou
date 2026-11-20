import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:torus-knot-delta-q-writhe",
  title:
    "Writhe exponent of the torus-knot $\\delta_q$ decoration: $\\delta^{\\mathrm{top}}_q(T_{m,p}) = h\\,[(m-1)p]_q$",
  lean: {
    ref: "qou:QOU.TorusKnotDeltaQ.torus_deltaQ_eq_h_qbracket",
    validation: "not_checked",
  },
  computation: {
    engine: "python",
    status: "verified",
    script: "computations/rosso_jones_three_strand_delta_q.py",
    witness: [
      "computations/rosso-jones-three-strand-delta-q.witness.json",
    ],
  },
  uses: [
    "def:torus-knot-top-channel-decoration",
    "prop:alpha-basis-knot-delta-q",
    "prop:alpha-em-categorical-trace-ratio",
  ],
  tags: [
    "alpha-basis-knot",
    "q-dimension",
    "quantum-integer",
    "torus-knot",
    "rosso-jones",
    "writhe",
    "pre-archimedean",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): the level-pair invariant of `QOU/StandardModel/WritheLevelParity.lean` —" },
  ],
});
