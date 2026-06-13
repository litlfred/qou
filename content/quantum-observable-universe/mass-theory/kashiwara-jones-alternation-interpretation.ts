import { remark } from "../../schema/builders";

export default remark({
  label: "rem:kashiwara-jones-alternation-interpretation",
  title:
    "Alternation of $Q_\\beta$ precision-ladder coefficients $c_k$ between Kashiwara matrix elements (intra-block) and Jones invariants (inter-block): interpretation via two moduli spaces meeting at Markov closure, twisted by GB jet order",
  interprets: "prop:q-beta-categorical-precision-ladder",
  uses: [
    "prop:q-beta-categorical-precision-ladder",
    "prop:markov-trace-frobenius-selection",
    "rem:borromean-baryon-interpretation",
  ],
  cites: [
    "kashiwara1990",
    "jones1985",
  ],
  tags: [
    "interpretation",
    "kashiwara-crystal",
    "jones-polynomial",
    "GB-filtration",
    "jet-order",
    "moduli-space",
    "hyperbolic-torus",
    "1ppb-roadmap",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "This is a **structural interpretation remark**, not a new theorem. It\ncaptures the rep-theoretic picture motivating the empirical alternation\nobserved in [`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder).\nThe remark interprets but does not introduce new logical content.",
    },
  ],
});
