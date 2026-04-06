import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-gl-fiber-functor",
  lean: { decl: "QOU.q_gl_fiber_functor", validation: "not_checked" },
  title: "Fibre-functor mediation of the $q$-Langlands correspondence",
  uses: [
    "conj:q-geometric-langlands",
    "rem:fibre-functor-rigidity",
    "def:q-hecke-eigensheaf",
    "def:q-langlands-dual",
  ],
  cites: ["frenkel2007"],
  tags: ["geometric-langlands", "fiber-functor", "tannaka-krein"],
});
