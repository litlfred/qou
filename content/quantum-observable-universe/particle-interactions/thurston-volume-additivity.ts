import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:thurston-volume-additivity",
  title:
    "Thurston additivity of hyperbolic volume over ideal tetrahedra",
  computation: {
    engine: "mpmath",
    script: "folio-assistant/computations/q_pinning_50_digit.py",
    witness: "folio-assistant/computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
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
  uses: ["thm:wedderburn-mass-formula"],
  cites: ["thurston1978"],
});
