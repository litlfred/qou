import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:q-codifferential-formula",
  label: "rem:q-codifferential-formula",
  title: "Expanded formula for the $q$-codifferential $\\delta_q$",
  uses: ["prop:q-codifferential-formula", "def:categorical-q-ext-deriv", "ex:reeb-decomposition"],
  tags: ["codifferential", "reeb", "adjoint"],
});
