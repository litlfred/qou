import { remark } from "../../schema/builders";

export default remark({
  label: "rem:commutative-qou-remark",
  title: "The strictly commutative case as the classical limit",
  interprets: "def:commutative-qou",
  uses: ["def:commutative-qou"],
  tags: ["commutative-limit", "classical-limit", "frobenius-hopf"],
});
