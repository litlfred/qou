import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:aeon-recycling",
  title:
    "Aeon recycling: $\\Phi_1^q \\circ \\mathrm{CMB}$ lands in $\\mathrm{Bun}^{\\circ}$",
  lean: {
    ref: "qou:QOU.AeonBoundary.AeonRecycling",
    validation: "not_checked",
  },
  uses: ["def:cmb-functor"],
  tags: [
    "aeon",
    "recycling-functor",
    "cmb-functor",
    "integrability",
    "torsion-flow",
  ],
});
