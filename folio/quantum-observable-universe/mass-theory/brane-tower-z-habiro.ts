import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:brane-tower-z-habiro",
  lean: { ref: "qou:QOU.BraidKnot.BraneTowerZHabiro" },
  title: "Brane tower lives in the $z$-Habiro ring",
  uses: [
    "def:z-habiro-ring",
    "def:habiro-ring",
    "cor:quantum-dilogarithm",
  ],
  tags: [
    "tier:S",
    "brane-tower",
    "habiro-ring",
    "cyclotomic-completion",
    "regularization",
    "quantum-dilogarithm",
    "open-problem",
    "partial-refutation-six-families",
    "closure-2026-05-11",
    "phase-3-leverage-15-users",
    "algebraic-cauchy-limit-half-open",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
    {
      kind: "status",
      date: "2026-06-07",
      body:
        "**Split status (half-open): algebraic Cauchy-limit claim survives; " +
        "n⋆ level-selection refuted.** Two independent claims live in this " +
        "block. (1) The algebraic claim — that the brane tower " +
        "Φ_mass^trans(β) = Σ Φ_q(z_i) has a Cauchy limit in the z-Habiro " +
        "topology — remains OPEN (untouched). (2) The companion claim that a " +
        "level-selection rule n⋆($\\mathfrak{h}$) picks the physical truncation depth was " +
        "REFUTED across six probed families (scalar, operator-valued, " +
        "multiplicity-refined, pair-knot product, pair-knot Markov-trace, and " +
        "the regularization sweep): no uniform n⋆ closes the AME gap — see the " +
        "Yekutieli-truncation failure (D: ~22%, T: ~17000%) recorded in the " +
        "block body and the linked `conj:mass-endomorphism` §'Two distinct " +
        "convergence problems'. Report the two claims separately; do not cite " +
        "the refuted n⋆ rule as live. (Conjecture-triage 2026-06-07.)",
      see: "docs/audits/2026-06-07-conjecture-triage.md",
    },
  ],
  computation: {
    engine: "python",
    script: "computations/two_term_qed_isotope_and_nucleon_compute.py",
    witness: [
      "computations/two-term-qed-isotope-and-nucleon-compute.witness.json",
      "computations/delta-q-decoration.witness.json",
      "computations/borromean-binding-recompute.witness.json",
    ],
    status: "verified",
  },
});
