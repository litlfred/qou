import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:chiral-elliptic",
  title: "Chiral fibre as an elliptic curve",
  hasProof: true,
  uses: ["rem:braid-group-action", "rem:holonomy-trefoil"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/chiral-elliptic-0.svg", blockIndex: 0, hash: "3b18553affcb" },
  ],

});
