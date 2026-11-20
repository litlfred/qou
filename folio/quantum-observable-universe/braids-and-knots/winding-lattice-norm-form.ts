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
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): All statements are formalized in `QOU.QBeta.WindingLatticeNormForm` — the ring identity over a generic `CommRing` (no ordering, no $\\mathbb{R}$, $s$ entering only through $s^2 = 3$), the two norm recursions over $\\mathbb{Z}$, and the induction giving $N(\\varphi^n) = (-1)^n$." },
  ],
});
