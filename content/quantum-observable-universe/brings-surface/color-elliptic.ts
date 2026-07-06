import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:color-elliptic",
  lean: { ref: "qou:QOU.Brings.color_elliptic",
    validation: "not_checked",
  },
  title: "Color fibre as an elliptic curve",
  uses: ["rem:braid-group-action", "rem:holonomy-trefoil"],
  proofs: ["prf:color-elliptic"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/color-elliptic-0.svg", blockIndex: 0, hash: "3b18553affcb" },
  ],

});
