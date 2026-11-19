import { remark } from "../../schema/builders";

export default remark({
  label: "rem:poisson-object-remark",
  title: "The Poisson bracket via pullback, and its anti-symmetry",
  interprets: "def:poisson-object",
  uses: ["def:poisson-object", "def:frobenius-pairing", "def:higher-forms"],
  tags: ["poisson", "bivector", "pullback", "differential-calculus"],
});
