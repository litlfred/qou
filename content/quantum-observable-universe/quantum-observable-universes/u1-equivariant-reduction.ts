import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:u1-equivariant-reduction",
  proofs: ["prf:u1-equivariant-reduction"],
  lean: { ref: "qou:QOU.CommutativeQOU.u1EquivariantReduction", validation: "not_checked" },
  title: "$\\mathrm{U}(1)$-equivariant reduction of the exceptional divisor",
  tags: ["exceptional-divisor", "u1", "equivariant", "commutative-limit"],
  uses: [
    "def:exceptional-divisor",
    "def:commutative-qou",
  ],
});
