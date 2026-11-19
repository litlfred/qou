import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:standard-part-functor",
  label: "rem:standard-part-functor-remark",
  title: "Formulas and properties of the standard-part map and functor",
  uses: ["def:standard-part-functor", "conj:classical-limit-stpart", "def:birthday-grading"],
  cites: ["robinson1966", "alling1987"],
});
