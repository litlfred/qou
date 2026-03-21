import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:descent",
  title: "Descent preserves the quantum observable universe",
  hasProof: true,
  tags: ["descent", "frobenius-hopf", "star-homomorphism"],
  uses: [
    "def:quantum-observable-universe",
    "def:recursive-brane-tower",
    "prop:jet-prolongation",
  ],
});
