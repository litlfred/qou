import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:recursive-brane-tower",
  label: "rem:vacuum-polarization-virtual-pairs",
  title: "Virtual pairs, vacuum polarisation, and Skein resolution",
  tags: [
    "virtual-particles",
    "vacuum-polarisation",
    "pair-creation",
    "skein-resolution",
    "interpretation",
  ],
  uses: [
    "rem:virtual-particles-exceptional-divisor",
    "rem:pair-creation-energy",
    "prop:reidemeister-mass-invariance",
  ],
});
