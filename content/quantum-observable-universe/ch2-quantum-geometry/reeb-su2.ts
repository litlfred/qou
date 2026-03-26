import { example } from "../../schema/builders";

export default example({
  label: "ex:reeb-su2",
  title: "Reeb derivation for $\\mathrm{SU}(2)$",
  lean: { decl: "QOU.Examples.su2Reeb" },
  uses: ["def:categorical-reeb", "ex:maximal-torus-su2"],
  tags: ["su2", "reeb"],
});
