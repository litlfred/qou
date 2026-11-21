import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:pair-skein-mass-formula",
  lean: { ref: "qou:QOU.MassTheory.PairSkeinNucleon.pairSkeinD_eq",
    validation: "not_checked",
  },
  title: "Pair Skein mass and crossing-by-crossing recursion",
  tags: ["skein-relation", "pair-skein-mass", "borromean", "recursion"],
  uses: ["lem:nucleon-borromean-topology"],
  proofs: ["prf:pair-skein-mass-formula"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-21",
      body:
        "**Moved to convention D (issue #8923).** The formula read " +
        "$(q\\mu_a + q^{-1}\\mu_b)/(q^{1/2}+q^{-1/2})$, a convention-C " +
        "normaliser. It is now $(q - z)(q^2\\mu_a + q^{-2}\\mu_b)$ at " +
        "$z = q^3/(q^2+1)$. The normaliser $q - z = 1/[2]_q$ and the skein " +
        "weights $q^{\\pm 2}$ are derived in Lean " +
        "(`QOU.MassTheory.PairSkeinNucleon`: `trE_conventionD`, " +
        "`writheFactor_eq`); the assignment of masses to a crossing pair is " +
        "still a reading. The Lean ref moved from the convention-C, `ℝ`-valued " +
        "`QOU.HadronicMass.pair_skein_mass_formula`, which is unchanged and " +
        "now superseded for this block. The §7c note below describes that old " +
        "module only.",
    },
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
