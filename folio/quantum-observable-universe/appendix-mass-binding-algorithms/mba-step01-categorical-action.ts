import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:categorical-action",
  title: "Categorical action $\\rho_n\\colon B_n \\to \\mathrm{Aut}_{\\mathbf{C}}(V^{\\otimes n})$",
  uses: [
    "def:categorical-action",
    "prop:categorical-action-exists",
    "prop:categorical-action-unique",
  ],
  computation: {
    engine: "rust",
    script: "tools/hecke-engine/src/lib.rs",
    status: "verified",
  },
  tags: [
    "mba",
    "step-1",
    "categorical-action",
    "braid-group",
    "canonical-chain",
  ],
});
