import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-gl-classical-limit",
  lean: { decl: "QOU.q_gl_classical_limit", validation: "not_checked" },
  title: "Classical limit of the $q$-Geometric Langlands correspondence",
  uses: [
    "conj:q-geometric-langlands",
    "def:q-local-system",
    "def:q-hecke-operator",
  ],
  proofs: ["prf:q-gl-classical-limit"],
  cites: ["frenkel2007"],
  tags: ["geometric-langlands", "classical-limit"],
});
