import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:q-gl-fiber-functor",
  lean: { decl: "QOU.q_gl_fiber_functor", validation: "not_checked" },
  title: "Fibre-functor mediation of the $q$-Langlands correspondence",
  uses: [
    "conj:q-geometric-langlands",
    "prop:fibre-functor-rigidity",
    "def:q-hecke-eigensheaf",
    "def:q-langlands-dual",
  ],
  proofs: ["prf:q-gl-fiber-functor"],
  tags: ["geometric-langlands", "fiber-functor", "tannaka-krein"],
});
