import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:pawlowski-leitner-inner-product",
  title: "Inner product on intertwiner spaces",
  lean: {
    decl: "QOU.PawlowskiLeitnerInnerProduct",
    validation: "not_checked",
  },
  uses: [
    "prop:pawlowski-leitner-basis",
    "rem:adjoint-trace",
    "def:frobenius-pairing",
  ],
  tags: ["inner-product", "intertwiner", "orthogonality", "pawlowski-leitner"],
});
