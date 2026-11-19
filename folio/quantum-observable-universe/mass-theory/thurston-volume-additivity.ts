import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:thurston-volume-additivity",
  title:
    "Thurston additivity of hyperbolic volume over ideal tetrahedra",
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: [
      "computations/q-pinning-50-digit.witness.json",
      "computations/all-nuclides-sdp-admissibility.witness.json",
    ],
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
  cites: ["francaviglia2003", "thurston1978"],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
