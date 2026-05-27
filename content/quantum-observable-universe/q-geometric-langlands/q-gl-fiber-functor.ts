import { conjecture } from "../../schema/builders";

export default proposition({
  label: "prop:q-gl-fiber-functor",
  lean: { ref: "qou:QOU.QGeometricLanglands.q_gl_fiber_functor", validation: "not_checked" },
  title: "Fibre-functor mediation of the $q$-Langlands correspondence",
  uses: [
    "prop:q-geometric-langlands",
    "rem:fibre-functor-rigidity",
  ],
  cites: ["frenkel2007"],
  tags: ["geometric-langlands", "fiber-functor", "tannaka-krein"],
});
