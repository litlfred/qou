import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-self-duality",
  lean: { ref: "qou:QOU.categorical_self_duality",
    validation: "not_checked",
  },
  title: "Categorical self-duality",
  tags: ["self-duality", "yang-mills"],
  uses: ["def:categorical-instanton"],
  proofs: ["prf:categorical-self-duality"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-self-duality-0.svg", blockIndex: 0, hash: "c997dc218a1d" },
  ],

});
