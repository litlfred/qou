import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:schur-weyl-mass-decomposition",
  title:
    "Schur–Weyl decomposition of the atomic mass trace",
  lean: {
    ref: "qou:QOU.BraidKnot.schur_weyl_mass_decomposition",
    validation: "not_checked",
  },
  uses: [
    "prop:markov-pair-z2",
    "prop:shell-schur-weyl-self-duality",
  ],
  tags: [
    "schur-weyl",
    "wedderburn",
    "mass",
    "hook-product",
    "partition",
    "hecke-algebra",
  ],
  computation: {
    engine: "python",
    script: "computations/atom_level_wedderburn_tower.py",
    witness:
      "computations/atom-level-wedderburn-tower.witness.json",
    status: "verified",
    requires: ["mpmath", "numpy", "scipy"],
  },
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
    {
      kind: "caveat",
      date: "2026-09-06",
      body:
        "**Two false axioms deleted from the sibling `.lean`.** " +
        "`a_eq_one_three_channels_axiom` (partitions of 3 number 3) and " +
        "`additive_wedderburn_missing_partitions_axiom` both quantified " +
        "over every `SchurWeylMassDecomposition` as though its " +
        "`partitions` field were the complete partition list. It is free " +
        "data: the only field relating it to anything, `decomposition`, is " +
        "satisfiable for any list by choosing `markovTrace` to match, so " +
        "the list can be empty. Refuted by " +
        "`not_a_eq_one_three_channels` and " +
        "`not_additive_wedderburn_missing_partitions`. The cited " +
        "combinatorics is not in dispute -- 3 is the number of partitions " +
        "of 3 -- but neither Lean statement said that. A statement that " +
        "did would quantify over `Nat.Partition 3`, or the structure would " +
        "carry a completeness field; that refactor is not guessed at here.",
      see: "docs/audits/2026-09-06-q-analysis-uniqueness-axioms-are-false.md",
    },
  ],
});
