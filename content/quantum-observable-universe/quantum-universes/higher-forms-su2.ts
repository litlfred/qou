import { example } from "../../schema/builders";

export default example({
  interprets: "def:higher-forms",
  label: "ex:higher-forms-su2",
  title: "Higher forms on $\\mathcal{O}(\\mathrm{SU}(2))$",
  lean: { ref: "qou:QOU.Examples.su2FormDims", validation: "not_checked" },
  tags: ["su2", "differential-forms"],
  uses: ["def:higher-forms", "ex:quantum-universe-su2"],
});
