import { definition } from "../../schema/builders";

export default definition({
  label: "def:commutative-qou",
  lean: { ref: "qou:QOU.CommutativeQOU", validation: "not_checked" },
  title: "Commutative specialisation of a QOU",
  tags: ["commutative-limit", "classical-limit", "frobenius-hopf"],
  uses: ["rem:hopf-non-cocommutativity"],
});
