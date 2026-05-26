import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:pachner-pentagon-borromean",
  title:
    "Pachner $2$–$3$ move = Pentagon identity at Borromean ideal-tetrahedron decomposition",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.PachnerPentagonBorromean",
    validation: "not_checked",
  },
  uses: [
    "prop:pentagon-uv-commutation",
    "prop:q-rogers-pentagon-archimedean",
    "prop:quantum-dilogarithm-stratified",
    "def:quantum-dilogarithm-disambiguation",
    "def:borromean-baryon",
    "prop:exterior-square-borromean",
    "prop:atom-knot-exists",
    "prop:reeb-bundle-complement-equals-volume",
  ],
  cites: [
    "pachner1991",
    "faddeev1996",
    "kashaev1997",
    "turaev-viro1992",
    "neumann-zagier1985",
  ],
  tags: [
    "pachner",
    "pentagon",
    "duality-d15",
    "borromean",
    "ideal-tetrahedron",
    "tv-rt-state-sum",
    "h4-closure-route",
    "axiom-class",
    "open-problem",
    "conditional-on-class",
    "non-scholarly-voice-exception",
    "quantum-dilogarithm",
  ],
});
