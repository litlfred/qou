import { prose } from "../../schema/builders";

export default prose({
  label: "sec:cp-violation-evidence",
  uses: [
    "conj:complex-chirality-rotation",
    "prop:crossing-energy-decomposition",
    "rem:chirality-trefoil-electron-positron",
    "def:crossing-energy",
  ],
  tags: [
    "cp-violation", "kaon", "b-meson", "CKM",
    "matter-antimatter", "experimental",
  ],
  cites: ["christenson1964", "aubert2001"],
});
