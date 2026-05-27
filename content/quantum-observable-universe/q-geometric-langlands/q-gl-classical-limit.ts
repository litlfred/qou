import { conjecture } from "../../schema/builders";

export default proposition({
  label: "prop:q-gl-classical-limit",
  lean: { ref: "qou:QOU.QGeometricLanglands.q_gl_classical_limit", validation: "not_checked" },
  title: "Classical limit of the $q$-Geometric Langlands correspondence",
  uses: ["prop:q-geometric-langlands"],
  cites: ["frenkel2007"],
  tags: ["geometric-langlands", "classical-limit"],
});
