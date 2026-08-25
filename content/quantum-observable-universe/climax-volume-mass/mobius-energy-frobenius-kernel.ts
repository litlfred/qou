import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:mobius-energy-frobenius-kernel",
  lean: { ref: "qou:QOU.BraidsKnots.mobius_frobenius_kernel",
    validation: "not_checked",
  },
  title: "Classical limit of the Frobenius--Hopf kernel is the repulsive $1/r^2$",
  tags: ["frobenius-pairing", "mobius-energy", "classical-limit", "killing-form"],
  uses: ["def:frobenius-pairing"],
  proofs: ["prf:mobius-energy-frobenius-kernel"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module " +
        "`lean/QOU/BraidsKnots/mobius_frobenius_kernel.lean` uses " +
        "`Filter.Tendsto`. These are real-analytic constructs with no " +
        "generic-`CommRing` counterpart, so the `ℝ` specialisation is " +
        "forced by the statement itself rather than chosen. The block " +
        "therefore sits on the archimedean side of the §7c wall by " +
        "construction.",
    },
  ],
});
