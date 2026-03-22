import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:yekutieli-lifting",
  title: "Yekutieli Lifting Condition holds in the brane tower",
  tags: ["yekutieli", "lifting", "brane-tower"],
  uses: [
    "def:quantum-observable-universe",
    "def:recursive-brane-tower",
    "def:yekutieli-lifting-condition",
    "def:quantum-characteristic-classes",
    "prop:jet-prolongation",
  ],
  proofs: ["prf:yekutieli-lifting"],
});
