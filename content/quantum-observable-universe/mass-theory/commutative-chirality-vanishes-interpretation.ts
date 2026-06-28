import { remark } from "../../schema/builders";

export default remark({
  interprets: "cor:commutative-chirality-vanishes",
  label: "rem:commutative-chirality-vanishes-interpretation",
  title: "Significance: chirality is the unique S-odd channel, trivial in the commutative limit",
  uses: ["cor:commutative-chirality-vanishes", "prop:frobenius-s-classification"],
});
