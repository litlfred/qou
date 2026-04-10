import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:composite-crossing-parity",
  title: "Crossing parity of composite nuclear knots",
  tags: [
    "crossing-number",
    "parity",
    "nuclear-knot",
    "transfer-matrix",
    "phase-transition",
    "sublimation",
  ],
  lean: {
    decl: "QOU.Information.compositeCrossingParity",
    validation: "not_checked",
  },
  uses: [
    "prop:skein-polynomial-transfer-matrix",
    "def:stable-nucleus",
    "prop:phase-transition-boundary",
  ],
});
