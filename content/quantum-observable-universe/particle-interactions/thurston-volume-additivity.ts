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
  lean: { ref: "qou:QOU.ParticleInteractions.thurstonVolumeAdditivity",
    validation: "not_checked",
  },
  uses: ["prop:wedderburn-mass-formula"],
  cites: ["thurston1978"],
});
