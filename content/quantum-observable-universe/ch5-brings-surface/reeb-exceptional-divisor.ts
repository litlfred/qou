import { remark } from "../../schema/builders";

export default remark({
  label: "rem:reeb-exceptional-divisor",
  title: "Reeb vector field on the exceptional divisor",
  uses: [
    "def:q-reeb-vector-field",
    "def:substrate-parameter",
    "def:q-reeb-flow",
    "rem:brings-smoothness",
    "rem:heisenberg-commutator",
  ],
});
