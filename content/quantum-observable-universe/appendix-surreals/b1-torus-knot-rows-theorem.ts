import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:b1-torus-knot-rows-theorem",
  title:
    "The depth correspondence is theorem-level at the torus-knot rows (Bloch--Suslin + Garoufalidis--Lê)",
  lean: {
    ref: "qou:QOU.AppendixSurreals.B1TorusKnotRowsTheorem.b1_torus_knot_rows",
    validation: "not_checked",
  },
  uses: ["prop:b1-figure-8-row-theorem"],
  cites: ["bloch2000", "suslin1991"],
  tags: [
    "B1-discharge",
    "torus-knots",
    "garoufalidis-le",
    "chern-simons-rational",
    "tate-twist",
    "theorem-level",
    "graded-mikusinski",
  ],
});
