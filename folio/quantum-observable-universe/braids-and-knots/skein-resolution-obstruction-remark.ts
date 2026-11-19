import { remark } from "../../schema/builders";

export default remark({
  label: "rem:skein-resolution-obstruction-remark",
  title: "The Skein resolution obstruction among the evaluations of the universal class",
  interprets: "def:skein-resolution-obstruction",
  tags: ["obstruction", "skein"],
  uses: [
    "def:skein-resolution-obstruction",
    "conj:wigner-axiom",
    "thm:qou-obstruction-reduction",
    "rem:kummer-filtration-obstruction",
    "prop:ns-obstruction-tower",
  ],
});
