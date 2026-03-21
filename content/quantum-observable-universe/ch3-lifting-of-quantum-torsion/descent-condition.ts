import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:descent-condition",
  title: "Descent condition --- twisted $2$-cocycle",
  hasProof: true,
  tags: ["descent", "cocycle", "twisted", "yekutieli"],
  uses: [
    "def:quantum-observable-universe",
    "def:recursive-brane-tower",
    "def:yekutieli-triple",
    "def:quantum-characteristic-classes",
    "rem:distributional-connection",
    "prop:yekutieli-lifting",
  ],
});
