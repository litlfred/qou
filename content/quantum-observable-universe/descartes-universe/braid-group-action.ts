import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:braid-group",
  label: "rem:braid-group-action",
  title: "Braid-group action on the resolvents",
  uses: [
    "rem:brings-curve",
    "rem:lagrange-resolvents",
    "def:braid-group",
    "def:so3-generators",
    "def:braid-twist-flip",
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/braid-group-action-0.svg", blockIndex: 0, hash: "6ed88e108444" },
    { mime: "image/svg+xml", url: "rendered/braid-group-action-1.svg", blockIndex: 1, hash: "a286057dd3b8" },
  ],

});
