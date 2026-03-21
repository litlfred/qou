import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:main-commutative-diagram",
  title: "Main Commutative Diagram",
  lean: { decl: "QOU.main_commutative_diagram", validation: "not_checked" },
  uses: ["ex:c-quantum-observable-universe", "ex:instanton", "def:substrate-parameter", "def:q-yang-mills-levi"],
  hasProof: true,
  tags: ["commutative-diagram", "main-result"],
});
