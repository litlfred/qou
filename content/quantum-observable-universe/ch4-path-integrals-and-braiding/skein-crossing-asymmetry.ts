import { remark } from "../../schema/builders";

export default remark({
  label: "rem:skein-crossing-asymmetry",
  title: "Crossing asymmetry and emergent Coulomb repulsion",
  tags: [
    "skein",
    "crossing",
    "coulomb",
    "repulsion",
    "braiding",
    "r-matrix",
    "nucleus",
    "binding",
  ],
  uses: [
    "rem:r-matrix-braiding",
    "def:substrate-parameter",
    "def:crossing-energy",
    "def:coulomb-charge",
  ],
});
