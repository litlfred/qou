import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:descent",
  lean: { decl: "QOU.DescentLemma" },
  title: "Descent preserves the quantum observable universe",
  tags: ["descent", "frobenius-hopf", "star-homomorphism"],
  uses: [
    "def:quantum-observable-universe",
    "def:recursive-brane-tower",
    "prop:jet-prolongation",
  ],
  proofs: ["prf:descent"],
});
