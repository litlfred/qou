import { example } from "../../schema/builders";

export default example({
  interprets: "def:categorical-hodge-star",
  label: "ex:hodge-su2",
  title: "Hodge star on $\\mathcal{O}(\\mathrm{SU}(2))$",
  lean: { ref: "qou:QOU.Examples.su2Hodge", validation: "not_checked" },
  uses: ["def:categorical-hodge-star", "ex:higher-forms-su2"],
  tags: ["su2", "hodge-star"],
});
