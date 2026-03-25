import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:chiral-elliptic",
  lean: {
    decl: "QOU.Brings.chiral_elliptic",
    validation: "not_checked",
  },
  title: "Chiral fibre as an elliptic curve",
  uses: ["rem:braid-group-action", "rem:holonomy-trefoil"],
  proofs: ["prf:chiral-elliptic"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/chiral-elliptic-0.svg", blockIndex: 0, hash: "3b18553affcb" },
  ],

});
