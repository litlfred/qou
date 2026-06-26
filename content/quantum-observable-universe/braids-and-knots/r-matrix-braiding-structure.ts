import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "The underlying R-matrix, Yang-Baxter, and braid-representation content is standard quantum-group theory. However, the specific identification of the eigenvalues $q, -q^{-1}$ (Hecke channels) provides the essential framework tie-in, connecting standard representation theory to the physical observable structures in this universe." },
  ],
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
