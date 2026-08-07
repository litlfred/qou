import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:nsi-q-deformed-kernel",
  lean: { ref: "qou:QOU.BraidsKnots.nsi_q_deformed_kernel",
    validation: "not_checked",
  },
  title: "$q$-deformed commutator replaces $1/r^2$ with a hard kernel at $r = \\hbar_q$",
  tags: ["q-deformation", "r-matrix", "q-hodge-star", "quantum-exclusion"],
  uses: ["def:q-hodge-star"],
  proofs: ["prf:nsi-q-deformed-kernel"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module " +
        "`lean/QOU/BraidsKnots/nsi_q_deformed_kernel.lean` uses " +
        "`Filter.Tendsto`. These are real-analytic constructs with no " +
        "generic-`CommRing` counterpart, so the `ℝ` specialisation is " +
        "forced by the statement itself rather than chosen. The block " +
        "therefore sits on the archimedean side of the §7c wall by " +
        "construction.",
    },
  ],
});
