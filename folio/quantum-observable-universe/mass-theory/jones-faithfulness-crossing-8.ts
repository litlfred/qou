import { remark } from "../../schema/builders";

export default remark({
  label: "rem:jones-faithfulness-crossing-8",
  title:
    "Bring-embeddable Jones-faithfulness: theorem at crossing $\\leq 10$, falsified for Conway-KT at crossing 11",
  interprets: "rem:knot-exhaustiveness",
  uses: ["rem:conway-kt-vol-injectivity-test"],
  cites: ["thurston1978"],
  tags: [
    "jones-faithfulness",
    "crossing-number",
    "hoste-thistlethwaite-weeks",
    "conway-knot",
    "mutant-pair",
    "tightening",
    "graded-mikusinski",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "**Theorem-level at crossing $\\leq 10$. Conway-KT mutant pair (crossing\n11) is the unique known Jones-coincident pair satisfying Vol-equality\nvia Ruberman. Crossing $\\geq 12$ open.**",
    },
  ],
});
