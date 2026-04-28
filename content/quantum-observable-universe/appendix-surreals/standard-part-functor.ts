import { definition } from "../../schema/builders";

export default definition({
  label: "def:standard-part-functor",
  lean: {
    ref: "qou:QOU.AppendixSurreals.StandardPart",
    validation: "not_checked",
  },
  title: "Standard-part functor $\\mathrm{st} : \\mathbf{No}_{\\mathrm{fin}} \\to \\mathbb{R}$",
  tags: [
    "surreal-numbers",
    "standard-part",
    "nonstandard-analysis",
    "archimedean",
    "functor",
  ],
  uses: [
    "def:birthday-grading",
  ],
  cites: ["robinson1966", "alling1987"],
});
