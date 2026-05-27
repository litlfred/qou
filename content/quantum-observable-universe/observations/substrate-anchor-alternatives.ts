import { remark } from "../../schema/builders";

export default remark({
  label: "rem:substrate-anchor-alternatives",
  title:
    "Multiple experimental routes to the substrate parameter $q_0$",
  interprets: "prop:proton-mass-substrate-identity",
  uses: [
    "prop:proton-mass-substrate-identity",
    "prop:flavor-split-substrate",
  ],
  tags: [
    "calibration",
    "substrate",
    "anchor-flip",
    "experimental-precision",
  ],
});
