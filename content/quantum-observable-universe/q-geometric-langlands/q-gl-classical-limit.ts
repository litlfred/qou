import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-gl-classical-limit",
  lean: { ref: "qou:QOU.q_gl_classical_limit", validation: "not_checked" },
  title: "Classical limit of the $q$-Geometric Langlands correspondence",
  uses: ["conj:q-geometric-langlands"],
  cites: ["frenkel2007"],
  tags: ["geometric-langlands", "classical-limit"],
});
