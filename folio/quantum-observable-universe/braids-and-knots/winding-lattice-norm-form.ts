import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:winding-lattice-norm-form",
  title:
    "The winding lattice of a braid-word geodesic: $\\mathrm{Im}\\,\\mathfrak{V}_{4_1}$ is the norm form of $\\mathbb{Z}[\\sqrt3]$",
  lean: { ref: "qou:QOU.QBeta.WindingLatticeNormForm.winding_lorentz_form" },
  uses: ["prop:cusp-shape-bar-parity", "prop:meridian-holonomy-boost"],
  tags: [
    "cusp-torus",
    "geodesic",
    "winding-lattice",
    "norm-form",
    "pell",
    "bar-parity",
    "complex-volume",
    "golden-ratio",
    "brings-surface",
  ],
});
