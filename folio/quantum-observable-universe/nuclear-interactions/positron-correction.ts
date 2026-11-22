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
      kind: "caveat",
      date: "2026-11-21",
      body:
        "**The offset is a per-case choice, not derived.** δ_A = 1 for A = 1 and even A, 0 for odd A ≥ 3, is chosen so the character sum matches observed Q-values. " +
        "Under AGENTS.md §NO FITTING a formula that branches on A with a different term per branch is a fit. " +
        "It is also not on the ruled β-decay route: Q_β is derived from γγ pair production (owner ruling 2026-11-20), " +
        "and all β-decay routes use the two-term Lagrangian trace (2026-11-21), `docs/coordination/owner-rulings.md`. " +
        "The statement records the offset as used; it is not evidence for the framework.",
    },
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
        "`fsh-guts/deprecated/computations/positron_lifted_sdp.py`. So the field " +
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
