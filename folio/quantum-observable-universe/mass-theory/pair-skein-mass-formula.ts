import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:pair-skein-mass-formula",
  lean: { ref: "qou:QOU.MassTheory.pair_skein_mass_formula",
    validation: "not_checked",
  },
  title: "Pair Skein mass and crossing-by-crossing recursion",
  tags: ["skein-relation", "pair-skein-mass", "borromean", "recursion"],
  uses: ["lem:nucleon-borromean-topology", "prop:trm-hopf-sigma1-sq-closed-form"],
  proofs: ["prf:pair-skein-mass-formula"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-28",
      body:
        "**Re-derived under convention D (owner ruling 2026-11-27).** The " +
        "pair Skein mass is now the Markov trace at $z = q^3/(q^2+1)$ of the " +
        "weighted crossing element $\\mu_a\\sigma + \\mu_b\\sigma^{-1}$ in " +
        "$H_2(q)$, derived sorry-free in " +
        "`QOU.MassTheory.PairSkeinD.pairMassD_closed`. The convention-C form " +
        "$(q\\mu_a + q^{-1}\\mu_b)/(q^{1/2}+q^{-1/2})$, whose denominator was " +
        "never derived, is retired together with its square-root variable and " +
        "its archimedean Lean companion. The Lean sibling is over a generic " +
        "field (§7c).",
    },
  ],
});
