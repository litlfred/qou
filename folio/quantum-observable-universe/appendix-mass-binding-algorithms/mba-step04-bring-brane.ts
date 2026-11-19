import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:bring-brane",
  title: "Genus-4 Bring curve $\\Sigma_4 \\subset \\mathbb{P}^4$: topological and Hodge invariants",
  uses: [
    "def:brings-surface",
    "lem:brings-euler-characteristic",
    "prop:force-carrier-bring-uniqueness",
  ],
  tags: [
    "mba",
    "step-4",
    "bring-surface",
    "hodge-invariants",
    "canonical-chain",
  ],
});
