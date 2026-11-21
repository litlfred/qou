import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cusp-shape-bar-parity",
  title:
    "Cusp-shape bar-parity: the figure-eight modulus splits as $\\mathfrak{V} = \\mathrm{Vol} + i\\,\\mathrm{CS}$",
  lean: { ref: "qou:QOU.Knot.CuspShapeBarParity.cusp_barParity_split" },
  tags: [
    "figure-eight",
    "cusp-shape",
    "complex-volume",
    "chern-simons",
    "bar-parity",
    "cyclotomic",
    "exceptional-divisor",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): It is formalized as `cusp_barParity_split` over a generic `[Field R]` (no archimedean structure)." },
  ],
});
