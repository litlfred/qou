import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:coral-elliptic",
  lean: {
    decl: "QOU.Brings.coral_elliptic",
    validation: "not_checked",
  },
  title: "Coral fibre as an elliptic curve",
  uses: ["rem:braid-group-action", "rem:holonomy-trefoil"],
  proofs: ["prf:coral-elliptic"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/coral-elliptic-0.svg", blockIndex: 0, hash: "8d6bf4a5074b" },
  ],

});
