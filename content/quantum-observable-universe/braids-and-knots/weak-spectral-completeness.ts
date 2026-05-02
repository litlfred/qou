import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:weak-spectral-completeness",
  title:
    "Plancherel completeness for the EW/Higgs $\\{T(2,4), T(2,6), T(2,8)\\}$ idempotent decomposition",
  uses: [
    "conj:electroweak-higgs-torus-link-triplet",
    "conj:force-carrier-knot-vs-link-dichotomy",
    "conj:electroweak-mass-eigenstate-count",
    "thm:em-spectral-completeness",
    "prop:gauge-coupling-uniqueness",
    "rem:hecke-algebra-from-braiding",
  ],
  tags: [
    "electroweak",
    "spectral-completeness",
    "plancherel",
    "weak-coupling",
    "force-carrier",
    "nv-1",
    "open-problem",
  ],
});
