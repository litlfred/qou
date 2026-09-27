import { example } from "../../schema/builders";

export default example({
  interprets: "def:categorical-reeb",
  label: "ex:reeb-su2",
  title: "Reeb derivation for $\\mathrm{SU}(2)$",
  lean: { ref: "qou:QOU.Examples.su2Reeb", validation: "not_checked" },
  uses: ["def:categorical-reeb", "ex:maximal-torus-su2"],
  tags: ["su2", "reeb"],
});
