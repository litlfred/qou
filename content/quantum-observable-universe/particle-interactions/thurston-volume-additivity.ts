import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:thurston-volume-additivity",
  title:
    "Thurston additivity of hyperbolic volume over ideal tetrahedra",
  tags: [
    "thurston",
    "hyperbolic-volume",
    "ideal-tetrahedron",
    "bloch-wigner",
    "dilogarithm",
    "crossing",
  ],
  lean: {
    decl: "QOU.ParticleInteractions.thurstonVolumeAdditivity",
    validation: "not_checked",
  },
  uses: [
    "def:atomic-braid",
    "prop:wedderburn-mass-formula",
    "prop:local-substrate-q",
  ],
  cites: ["thurston1978"],
});
