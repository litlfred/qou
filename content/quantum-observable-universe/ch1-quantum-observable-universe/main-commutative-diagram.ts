import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:main-commutative-diagram",
  title: "Main Commutative Diagram",
  uses: ["ex:c-quantum-observable-universe", "ex:instanton", "def:substrate-parameter", "def:q-yang-mills-levi"],
  proofs: ["prf:main-commutative-diagram"],
  tags: ["commutative-diagram", "main-result"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/main-commutative-diagram-0.svg", blockIndex: 0, hash: "ac46a8d6ede5" },
  ],

});
