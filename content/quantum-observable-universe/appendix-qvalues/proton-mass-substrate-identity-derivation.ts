import { remark } from "../../schema/builders";

export default remark({
  label: "rem:proton-mass-substrate-identity-derivation",
  title:
    "Proton-mass substrate identity — numerical verification, $h$-expansion, and precision frontier",
  interprets: "prop:proton-mass-substrate-identity",
  uses: [
    "prop:proton-mass-substrate-identity",
    "def:f-bor-borromean-observable",
    "prop:flavor-split-substrate",
  ],
  tags: [
    "proton-mass",
    "substrate-identity",
    "numerical-verification",
    "h-expansion",
    "precision-frontier",
    "appendix",
  ],
});
