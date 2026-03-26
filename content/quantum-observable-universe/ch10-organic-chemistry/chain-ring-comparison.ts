import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:chain-ring-comparison",
  title:
    "Predicted vs.\\ observed $\\mathrm{C}_6$ ring-closure barrier",
  tags: [
    "comparison",
    "experimental",
    "theoretical",
    "activation-energy",
    "benzene",
    "carbyne",
    "ring-closure",
    "substrate-parameter",
  ],
  uses: [
    "prop:ring-closure-barrier",
    "ex:carbon-chain-c6",
    "ex:benzene-ring",
    "rem:chain-ring-energy",
    "def:substrate-parameter",
    "def:crossing-energy",
  ],
});
