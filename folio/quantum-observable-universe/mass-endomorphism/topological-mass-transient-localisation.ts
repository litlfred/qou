import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:topological-mass-transient-localisation",
  lean: { ref: "qou:QOU.LiftingDescent.tm_transient_localisation",
    validation: "not_checked",
  },
  title: "Transient terms localise to exceptional divisors",
  tags: ["transient", "exceptional-divisor", "blow-up", "central-extension"],
  uses: [
    "def:brane-boundary",
    "lem:topological-mass-eigenspace-decomp",
  ],
  proofs: ["prf:topological-mass-transient-localisation"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-10-10",
      body:
        "**The displayed equality is not established (bean `tmvac`).** The Lean module " +
        "`lean/QOU/LiftingDescent/tm_transient_localisation.lean` derives only the " +
        "inequality `‖MI∫_Σ‖ ≤ Σ_i ‖MI∫_{E_i}‖` from the disc split and support hypotheses " +
        "(triangle inequality of a group seminorm). The proof block's step that the norm " +
        "of the product equals the sum of the norms does not follow from those hypotheses: " +
        "`norm_additivity_not_forced` gives data in `Multiplicative ℝ` satisfying both with " +
        "strict inequality. The equality is recorded as the conjecture class " +
        "`TransientLocalisationNormEquality`, with no instance. Whether this block should be " +
        "restated as an inequality or demoted to a conjecture is open.",
    },
  ],

});
