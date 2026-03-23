import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-codifferential-formula",
  title: "Expanded formula for the $q$-codifferential $\\delta_q$",
  uses: ["def:categorical-q-ext-deriv", "def:reeb-decomposition"],
  tags: ["codifferential", "reeb", "adjoint"],
});
