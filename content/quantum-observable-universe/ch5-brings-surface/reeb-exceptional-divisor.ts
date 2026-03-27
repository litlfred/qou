import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:substrate-parameter",
  label: "rem:reeb-exceptional-divisor",
  title: "Reeb vector field on the exceptional divisor",
  uses: [
    "ex:q-reeb-vector-field",
    "def:substrate-parameter",
    "ex:q-reeb-flow",
    "rem:brings-smoothness",
    "rem:heisenberg-commutator",
  ],
});
