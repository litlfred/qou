import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:r-matrix-braiding-structure",
  title: "Yang--Baxter equation and braid operator from the $R$-matrix",
  tags: ["r-matrix", "yang-baxter", "quantum-group", "braiding"],
  lean: { ref: "qou:QOU.Braiding.r_matrix_braiding_structure",
    validation: "not_checked",
  },
  uses: [
    "def:quantum-su2",
    "def:braid-twist-flip",
  ],
  examples: ["rem:r-matrix-braiding", "rem:skein-crossing-asymmetry"],
});
