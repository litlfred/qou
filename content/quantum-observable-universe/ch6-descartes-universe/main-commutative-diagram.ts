import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:main-commutative-diagram",
  lean: {
    decl: "QOU.main_commutative_diagram",
    validation: "not_checked",
  },
  title: "Main Commutative Diagram",
  uses: ["def:q-yang-mills-levi"],
  proofs: ["prf:main-commutative-diagram"],
  tags: ["commutative-diagram", "main-result"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/main-commutative-diagram-0.svg", blockIndex: 0, hash: "3d1c55010082" },
  ],

});
