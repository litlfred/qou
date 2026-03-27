import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:categorical-q-ext-deriv",
  label: "rem:q-codifferential-formula",
  title: "Expanded formula for the $q$-codifferential $\\delta_q$",
  uses: ["def:categorical-q-ext-deriv", "ex:reeb-decomposition"],
  tags: ["codifferential", "reeb", "adjoint"],
});
