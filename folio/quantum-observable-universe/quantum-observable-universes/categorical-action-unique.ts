import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-action-unique",
  title: "Uniqueness of the categorical action (given $\\Phi$)",
  lean: { ref: "qou:QOU.CategoricalAction.unique",
    validation: "not_checked",
  },
  uses: ["prop:categorical-action-exists"],
  proofs: ["prf:categorical-action-unique"],
  tags: ["uniqueness", "categorical-action", "right-dual"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-22",
      body:
        "**Restated as independence of the choice of right dual (owner card, 2026-11-22).** " +
        "The old statement, any two morphisms equal to tr(Phi) are equal, holds by transitivity of equality; its Lean was `rw [h1, h2]`. " +
        "The new Lean `QOU.CategoricalAction.unique` is sorry-free (lean -DautoImplicit=false exit 0; axioms propext, Classical.choice, Quot.sound). " +
        "Issue #9004, PR #9005, bean qou-jy1r.",
    },
  ],
});
