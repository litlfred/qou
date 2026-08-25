import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:positron-correction",
  title:
    "Parity-dependent Q-value offset",
  tags: [
    "positron",
    "correction",
    "pair-production",
    "action-difference",
    "parity",
  ],
  lean: { ref: "qou:QOU.ParticleInteractions.positron_correction",
    validation: "not_checked",
  },
  uses: ["thm:parity-regime-selection"],
  probe: "audit/positron-correction-probe",
  consumers: [],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module `lean/QOU/ParticleInteractions/positron_correction.lean` " +
        "carries the electron mass `m_e`, the charge `Q` and the character sum `Σ_char` as physical quantities. " +
        "The `ℝ` is therefore forced by the statement itself rather than " +
        "chosen, so the block sits on the archimedean side of the §7c wall " +
        "by construction.",
    },
  ],

});
