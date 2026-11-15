import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:pawlowski-leitner-inner-product",
  title: "Inner product on intertwiner spaces",
  lean: {
    decl: "QOU.PawLeiInnerProduct",
    validation: "not_checked",
  },
  uses: [
    "prop:pawlowski-leitner-basis",
    "rem:adjoint-trace",
  ],
  tags: ["inner-product", "intertwiner", "orthogonality", "pawlowski-leitner"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/pawlowski-leitner-inner-product-0.svg", blockIndex: 0, hash: "2fdca79bb8e5" },
  ],

});
