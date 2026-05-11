import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:b1-torus-knot-rows-theorem",
  title:
    "B1 keystone is theorem-level at the torus-knot rows (Bloch--Suslin + Garoufalidis--Lê)",
  lean: {
    ref: "qou:QOU.AppendixSurreals.B1TorusKnotRowsTheorem.b1_torus_knot_rows",
    validation: "not_checked",
  },
  uses: [
    "conj:gb-depth-period-correspondence",
    "prop:depth-2-identification-bloch-suslin",
    "prop:borel-partial-resolution",
    "rem:bring-embeddable-knots",
    "prop:b1-figure-8-row-theorem",
    "prop:b1-soft-sharpness-theorem",
    "rem:transcendental-accounting",
  ],
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
