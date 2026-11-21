import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:composite-crossing-parity",
  label: "rem:crossing-parity-test",
  title: "Observational test of the $Z$-parity sublimation rule",
  tags: [
    "crossing-parity",
    "sublimation",
    "observational-test",
    "metallic-bonding",
    "condensed-matter",
  ],
  uses: [
    "conj:composite-crossing-parity",
    "prop:phase-transition-boundary",
  ],
});
