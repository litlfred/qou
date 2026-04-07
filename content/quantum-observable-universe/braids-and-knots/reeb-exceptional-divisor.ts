import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:exceptional-divisor",
  label: "rem:reeb-exceptional-divisor",
  title: "Reeb vector field on the exceptional divisor",
  uses: [
    "ex:q-reeb-flow",
    "rem:brings-smoothness",
    "rem:heisenberg-commutator",
    "prop:vertex-is-exceptional-divisor",
  ],
});
