import { prose } from "../../schema/builders";

export default prose({
  label: "sec:cp-violation-evidence",
  uses: [
    "rem:complex-chirality-rotation",
    "prop:crossing-energy-decomposition",
  ],
  tags: [
    "cp-violation", "kaon", "b-meson", "CKM",
    "matter-antimatter", "experimental",
  ],
  cites: ["christenson1964", "aubert2001"],
});
