import { definition } from "../../schema/builders";

export default definition({
  label: "def:standard-part-functor",
  lean: {
    ref: "qou:QOU.AppendixSurreals.standardPart",
    validation: "not_checked",
  },
  title: "standard-part map $\\mathrm{st} : \\mathbf{No}_{\\mathrm{fin}} \\to \\mathbb{R}$",
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
