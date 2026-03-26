import { remark } from "../../schema/builders";

export default remark({
  label: "rem:cp-violation-evidence",
  title: "CP violation: experimental evidence and QOU interpretation",
  uses: [
    "conj:complex-chirality-rotation",
    "rem:crossing-energy-decomposition",
    "rem:chirality-trefoil-electron-positron",
    "def:crossing-energy",
  ],
  tags: [
    "cp-violation", "kaon", "b-meson", "CKM",
    "matter-antimatter", "experimental",
  ],
  cites: ["christenson1964", "aubert2001"],
});
