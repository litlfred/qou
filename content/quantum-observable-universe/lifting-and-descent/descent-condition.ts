import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:descent-condition",
  lean: { ref: "qou:QOU.Torsion.descent_condition",
    validation: "not_checked",
  },
  title: "Descent condition --- twisted $2$-cocycle",
  tags: ["descent", "cocycle", "twisted", "yekutieli"],
  uses: [
    "def:yekutieli-triple",
    "rem:distributional-connection",
    "prop:yekutieli-lifting",
  ],
  proofs: ["prf:descent-condition"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/descent-condition-0.svg", blockIndex: 0, hash: "2cc87fe2ebcd" },
  ],

});
