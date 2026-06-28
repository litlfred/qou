import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:habiro-residue-sum-equivalence",
  label: "rem:habiro-residue-sum-equivalence-interpretation",
  title: "Constructive vs analytic handles on the same Habiro object",
  uses: [
    "prop:habiro-residue-sum-equivalence",
    "cor:habiro-expansion-atomic",
  ],
});
