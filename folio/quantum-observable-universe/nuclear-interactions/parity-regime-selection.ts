import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:parity-regime-selection",
  title:
    "Parity regime selection for Q-values",
  tags: [
    "parity",
    "regime-selection",
    "sign",
    "odd-even",
    "q-value",
    "mass-number",
  ],
  lean: { ref: "qou:QOU.ParticleInteractions.parity_regime_selection",
    validation: "not_checked",
  },
  uses: [
    "prop:branching-qvalue-factorization",
    "prop:confinement-lp",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Q-value regimes in `parity_regime_selection.lean` are stated in " +
        "**MeV against measured masses**: the context carries `m_e : ℝ` " +
        "(electron rest mass, MeV) and `Q_value : ℝ` (the decay Q-value, " +
        "MeV), and each regime is an equation `Q = … · m_e`. A measured mass " +
        "is the §7c \"experimental value → `ℝ`\" row, so the `ℝ` is forced by " +
        "the statement rather than chosen.",
    },
  ],
});
