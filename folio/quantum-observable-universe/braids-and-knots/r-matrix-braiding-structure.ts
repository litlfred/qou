import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:r-matrix-braiding-structure",
  title: "Yang--Baxter equation and braid operator from the $R$-matrix",
  tags: ["r-matrix", "yang-baxter", "quantum-group", "braiding"],
  lean: { ref: "qou:BraidKnotOctonion.r_matrix_braiding_structure",
    validation: "not_checked",
  },
  uses: [
    "def:quantum-su2",
    "def:braid-twist-flip",
  ],
  examples: ["rem:r-matrix-braiding", "rem:skein-crossing-asymmetry"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`, `qou-z9ws`): `2026-08-30-context-classes-are-inhabited-by-zero.lean` records that any commutative multiplication satisfies the abstract Yang–Baxter equation (motivating retirement of `RMatrixBraidingContext` in favour of `YangBaxterHolds`).",
      see: "docs/audits/2026-08-30-context-classes-are-inhabited-by-zero.lean",
    },
  ],
});
