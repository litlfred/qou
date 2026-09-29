import { remark } from "../../schema/builders";

export default remark({
  label: "rem:categorical-coordinate-ring-dedup",
  title:
    "$R[i,q^{\\pm1}]$ as the ambient deformation ring: " +
    "deduplicating four complexifications",
  interprets: "def:crossing-energy",
  tags: [
    "categorical-coordinate",
    "deformation-ring",
    "complexification",
    "wick-rotation",
    "dedup",
  ],
  uses: [
    "def:crossing-energy",
    "rem:commutative-crossing-energy",
    "prop:categorical-coordinate-ring",
    "rem:laplace-fourier-wick-rotation",
    "rem:complex-substrate-interpretation",
    "rem:i-as-braiding-orientation",
    "def:hyperelliptic-quintic",
    "prop:descartes-elliptic-curve",
    "rem:u1-phase-tube",
  ],
});
