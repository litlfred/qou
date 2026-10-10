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
  authorNotes: [
    {
      kind: "note",
      date: "2026-09-03",
      body:
        "**A named probe that was never written.** This block carried two " +
        "top-level fields no schema declares — `probe: \"audit/" +
        "positron-correction-probe\"` and `consumers: []` — so zod stripped " +
        "both and the parse succeeded; nothing downstream ever saw them, and " +
        "nothing in the corpus reads either name. Checked before removing: " +
        "`audit/positron-correction-probe` does not exist anywhere in the " +
        "tree, and the only positron compute is the deprecated " +
        "`computations/_deprecated/positron_lifted_sdp.py`. So the field " +
        "could not be promoted to `computation.script`, which the pipeline " +
        "resolves against a real file — it recorded an intended probe, not " +
        "an existing one. Recorded here so the intent survives the removal. " +
        "`consumers: []` was empty and is dropped without replacement.",
    },
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
