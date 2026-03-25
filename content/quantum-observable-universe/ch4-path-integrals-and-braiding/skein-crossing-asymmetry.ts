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
    "def:r-matrix-braiding",
    "def:substrate-parameter",
    "rem:hadron-operations",
    "prop:terminal-resolution",
  ],
});
