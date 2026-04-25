import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:pawlowski-leitner-inner-product",
  title: "Inner product on intertwiner spaces",
  lean: { ref: "qou:QOU.PawLeiInnerProduct",
    validation: "not_checked",
  },
  uses: [
    "prop:pawlowski-leitner-basis",
    "rem:adjoint-trace",
  ],
  tags: ["inner-product", "intertwiner", "orthogonality", "pawlowski-leitner"],
});
