import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:frakD-energy-decomposition",
  title:
    "Bar-parity energy decomposition: retained ($\\cosh$) $\\oplus$ emitted ($\\sinh$, the $\\mathfrak{D}$ channel)",
  lean: { ref: "qou:QOU.MassTheory.FrakD.even_add_odd" },
  uses: ["prop:deuteron-fusion-frame"],
  cites: ["neumann-zagier1985", "jones1987"],
  computation: {
    engine: "python",
    script: "computations/mass_binding_dashboard.py",
    status: "verified",
  },
  tags: [
    "bar-parity",
    "decay-width",
    "complex-volume",
    "binding",
    "retained-emitted",
    "involution-projection",
  ],
});
