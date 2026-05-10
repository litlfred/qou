import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mostow-confinement",
  title: "Mostow confinement: hyperbolic rigidity locks the mass eigenvalue",
  lean: {
    ref: "qou:QOU.Encounter.MostowRigidity.mass_rigidity_of_mostow",
    validation: "not_checked",
  },
  uses: [
    "conj:algebraic-geometric-dilog-equivalence",
    "conj:gb-reduction-pl-thimble-bijection",
    "def:archimedean-realization-functor",
    "prop:confinement-sdp",
  ],
  cites: ["mostow1968", "thurston1978", "neumann-zagier1985", "witten2011"],
  tags: [
    "mostow-rigidity",
    "geometric-confinement",
    "conditional-class",
    "hyperbolic-volume",
    "mass-quantization",
    "encounter",
  ],
});
