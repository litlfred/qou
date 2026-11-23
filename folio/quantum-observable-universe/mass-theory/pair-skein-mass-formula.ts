import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:pair-skein-mass-formula",
  lean: { ref: "qou:QOU.HadronicMass.pair_skein_mass_formula",
    validation: "not_checked",
  },
  title: "Pair Skein mass and crossing-by-crossing recursion",
  tags: ["skein-relation", "pair-skein-mass", "borromean", "recursion"],
  uses: ["lem:nucleon-borromean-topology"],
  proofs: ["prf:pair-skein-mass-formula"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module " +
        "`lean/QOU/HadronicMass/pair_skein_mass_formula.lean` uses " +
        "`Real.sqrt`. These are real-analytic constructs with no " +
        "generic-`CommRing` counterpart, so the `ℝ` specialisation is " +
        "forced by the statement itself rather than chosen. The block " +
        "therefore sits on the archimedean side of the §7c wall by " +
        "construction.",
    },
  ],
});
