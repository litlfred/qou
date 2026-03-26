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
  lean: {
    decl: "QOU.Organic.benzene_weights",
    validation: "not_checked",
  },
  uses: [
    "prop:ring-closure-barrier",
    "def:threading-link",
    "ex:carbon-chain-c6",
    "ex:benzene-ring",
    "rem:chain-ring-energy",
    "def:substrate-parameter",
    "def:crossing-energy",
    "def:topological-mass-formula",
  ],
});
