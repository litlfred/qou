import { remark } from "../../schema/builders";

export default remark({
  label: "rem:jones-faithfulness-crossing-8",
  title:
    "Bring-embeddable Jones-faithfulness: theorem at crossing $\\leq 10$, falsified for Conway-KT at crossing 11",
  interprets: "rem:knot-exhaustiveness",
  uses: [
    "rem:knot-exhaustiveness",
    "rem:bring-embeddable-knots",
    "rem:conway-kt-vol-injectivity-test",
    "rem:transcendental-accounting",
  ],
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
});
