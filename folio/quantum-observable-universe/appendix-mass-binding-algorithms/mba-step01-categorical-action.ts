import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:categorical-action",
  title: "Braid-to-Hecke categorical representation $\\rho_n\\colon B_n \\to H_n(q)^\\times$",
  uses: [
    "def:categorical-action",
    "prop:categorical-action-exists",
    "prop:categorical-action-unique",
  ],
  tags: [
    "mba",
    "step-1",
    "categorical-action",
    "braid-group",
    "canonical-chain",
  ],
});
