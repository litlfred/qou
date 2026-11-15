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
});
