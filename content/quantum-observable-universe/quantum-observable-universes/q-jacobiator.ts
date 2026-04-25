import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-jacobiator",
  lean: { ref: "qou:QOU.q_jacobiator",
    validation: "not_checked",
  },
  title: "Jacobiator of the q-Lie bracket",
  tags: ["q-deformation", "lie-bracket", "leibniz-algebra"],
  uses: ["def:categorical-q-lie-bracket"],
  proofs: ["prf:q-jacobiator"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/q-jacobiator-0.svg", blockIndex: 0, hash: "1aac21e2c547" },
  ],

});
