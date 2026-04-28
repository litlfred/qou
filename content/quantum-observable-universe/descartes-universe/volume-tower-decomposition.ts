import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:volume-tower-decomposition",
  title:
    "Tower-level decomposition of hyperbolic volume",
  tags: [
    "hyperbolic-volume",
    "cosimplicial",
    "brane-tower",
    "quantum-dilogarithm",
    "spectral-sequence",
  ],
  uses: [
    "prop:cosimplicial-crossed-groupoid",
    "prop:topological-mass-formula",
  ],
  lean: { ref: "qou:QOU.Descartes.VolumeTowerDecomposition",
    validation: "not_checked",
  },
});
