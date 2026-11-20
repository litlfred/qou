import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:topological-mass-transient-localisation",
  lean: { ref: "qou:QOU.LiftingDescent.tm_transient_localisation",
    validation: "not_checked",
  },
  title: "Transient terms are bounded by exceptional-divisor contributions",
  tags: ["transient", "exceptional-divisor", "blow-up", "central-extension"],
  uses: [
    "def:brane-boundary",
    "lem:topological-mass-eigenspace-decomp",
  ],
  proofs: ["prf:topological-mass-transient-localisation"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The equality is recorded as the open conjecture `TransientLocalisationNormEquality` in the Lean formalisation." },
    {
      kind: "refined-framing",
      date: "2026-10-10",
      body:
        "**Restated as an inequality (owner ruling 2026-10-10, bean `tmvac`).** The block " +
        "previously stated `‖MI∫_Σ‖ = Σ_i ‖MI∫_{E_i}‖`. The Lean module " +
        "`lean/QOU/LiftingDescent/tm_transient_localisation.lean` derives only the " +
        "inequality `≤` from the disc split and support hypotheses (triangle inequality of " +
        "a group seminorm), and `norm_additivity_not_forced` gives data in `Multiplicative ℝ` " +
        "satisfying both hypotheses with strict inequality. The statement now matches what " +
        "is derived. The equality is open and recorded as the conjecture class " +
        "`TransientLocalisationNormEquality`, with no instance. The label is unchanged.",
    },
  ],

});
