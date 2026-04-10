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
    "def:quantum-characteristic-classes",
    "prop:topological-mass-formula",
  ],
  lean: {
    decl: "QOU.Descartes.VolumeTowerDecomposition",
    file: "QOU/Descartes/HyperbolicVolumeTranscendence.lean",
    validation: "not_checked",
  },
});
