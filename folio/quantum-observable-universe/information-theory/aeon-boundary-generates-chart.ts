import { remark } from "../../schema/builders";

export default remark({
  label: "rem:aeon-boundary-generates-chart",
  interprets: "def:cmb-functor",
  title: "Aeon recycling: $\\Phi_1^q \\circ \\mathrm{CMB}$ lands in $\\mathrm{Bun}^{\\circ}$",
  tags: [
    "aeon", "recycling-functor", "cmb-functor",
    "integrability", "torsion-flow",
  ],
  lean: { ref: "qou:QOU.AeonBoundary.AeonRecycling",
    validation: "not_checked",
  },
  uses: ["def:cmb-functor"],
});
