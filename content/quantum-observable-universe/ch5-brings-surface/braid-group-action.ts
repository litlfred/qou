import { remark } from "../../schema/builders";

export default remark({
  label: "rem:braid-group-action",
  title: "Braid-group action on the resolvents",
  uses: [
    "rem:brings-curve",
    "rem:lagrange-resolvents",
    "def:braid-group",
    "def:su2-generators",
    "def:so3-generators",
    "def:braid-twist-flip",
    "rem:chirality-trefoil",
  ],
});
