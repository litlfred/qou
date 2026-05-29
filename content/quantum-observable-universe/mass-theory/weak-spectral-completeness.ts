import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:weak-spectral-completeness",
  lean: { ref: "qou:QOU.BraidKnot.WeakSpectralCompleteness" },
  title:
    "Plancherel completeness for the EW/Higgs $\\{T(2,4), T(2,6), T(2,8)\\}$ idempotent decomposition",
  uses: [
    // broken-ref removed (Phase 7): conj:electroweak-higgs-torus-link-triplet
    // broken-ref removed (Phase 7): conj:force-carrier-knot-vs-link-dichotomy
    // broken-ref removed (Phase 7): conj:electroweak-mass-eigenstate-count
    "thm:em-spectral-completeness",
    // broken-ref removed (Phase 7): prop:gauge-coupling-uniqueness
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
