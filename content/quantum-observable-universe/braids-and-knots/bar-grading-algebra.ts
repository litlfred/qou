import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bar-grading-algebra",
  title: "Bar-grading algebra of $\\mathcal{H}_q$",
  lean: {
    ref: "qou:QOU.BraidKnot.BarInvolutionDef.decompose",
    validation: "not_checked",
  },
  uses: [
    "def:bar-involution",
  ],
  tags: [
    "lean-infrastructure",
    "bar-invariance",
    "categorical-action",
    "classification",
  ],
});
