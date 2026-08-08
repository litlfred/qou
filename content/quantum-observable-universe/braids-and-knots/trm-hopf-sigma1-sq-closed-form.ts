import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:trm-hopf-sigma1-sq-closed-form",
  lean: {
    ref: "qou:QOU.Braiding.TrMHopfSigma1SqClosedForm",
    validation: "not_checked",
  },
  title: "Closed form for the canonical Markov trace of σ_1² (Hopf+ braid)",
  tags: ["hecke-algebra", "markov-trace", "closed-form", "hopf-braid", "binomial-series"],
  uses: ["thm:jones-markov-trace"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module " +
        "`lean/QOU/Braiding/TrMHopfSigma1SqClosedForm.lean` uses " +
        "`Real.sqrt`. These are real-analytic constructs with no " +
        "generic-`CommRing` counterpart, so the `ℝ` specialisation is " +
        "forced by the statement itself rather than chosen. The block " +
        "therefore sits on the archimedean side of the §7c wall by " +
        "construction.",
    },
  ],
});
