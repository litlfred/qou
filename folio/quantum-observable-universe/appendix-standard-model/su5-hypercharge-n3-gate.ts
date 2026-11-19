import { remark } from "../../schema/builders";

export default remark({
  label: "rem:su5-hypercharge-n3-gate",
  title: "$\\mathrm{SU}(5)$ is rung five of the level tower the fibre stands on",
  interprets: "conj:sm-gauge-truncation",
  uses: ["conj:sm-gauge-truncation", "conj:sm-hypercharge-invariant"],
  cites: ["baez-huerta2010"],
  tags: [
    "appendix",
    "standard-model",
    "hypercharge",
    "grand-unification",
    "open-problem",
    "level-tower",
    "scope",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-08-25",
      body:
        "**CORRECTION, same day, on the owner's one-word question 'SU(5) " +
        "derived?'** The first merged version of this block opened *'SU(5) " +
        "is not an import into this framework. It is already present, as " +
        "level r=5 of the Wenzl tower.'* That over-claims, and in exactly " +
        "the way AGENTS.md \u00a7'Conditional-proved \u2260 " +
        "premise-established' names. What is present at r=5 is a VALUE OF A " +
        "RATIONAL FUNCTION; ocneanu_param_eq_of_fibre_qdim is an " +
        "IMPLICATION whose antecedent (a fibre of quantum dimension [5]_q, " +
        "or [3]_q) no construction in this framework supplies. 'Already " +
        "present' restated that hypothesis as fact. The block now opens by " +
        "saying plainly that SU(5) is NOT derived, and the conditional is " +
        "marked as one.",
    },

    {
      kind: "note",
      date: "2026-08-25",
      body:
        "**Scope observation, not a derivation (bean `qou-r3sw`).** Prompted " +
        "by the owner's note that GUT SU(5) is near-absent from the corpus " +
        "(measured: 3 hits, all bibliographic), then by the owner's sharper " +
        "question — *where does SU(5) come from categorically?* The first " +
        "draft of this block answered by importing Lambda C^5, which was the " +
        "wrong move: SU(5) is ALREADY in the corpus, as level r=5 of the " +
        "Wenzl tower z_r = q^r/[r]_q whose r=2 member is the framework's own " +
        "canonical trace parameter. The block was rewritten around that. " +
        "Supporting results, both already in the corpus and NOT re-derived " +
        "here: QOU.BraidsAndKnots.FibreDimensionForcesTL." +
        "ocneanu_param_eq_of_fibre_qdim (proved GENERAL IN N — a fibre of " +
        "quantum dimension [N]_q forces z[N]_q = q^N, so the rung fixes the " +
        "parameter with no fit), and docs/audits/" +
        "2026-08-16-su-r-level-tower-gap-map.md for the tower itself plus " +
        "the fibre-dimension = Wenzl-level identification (reached " +
        "independently there and by sibling PR #5229 [N1]).",
    },
    {
      kind: "caveat",
      date: "2026-08-25",
      body:
        "**The two fives are not known to be the same five.** The tower's " +
        "level-5 fibre is 5-dimensional; Lambda C^5's C^5 splits as " +
        "C^2 + C^3 (isospin + colour). That the former splits as the latter " +
        "is NOT a consequence of the tower — the tower fixes a row cap and a " +
        "trace parameter, nothing about a flavour-colour decomposition. " +
        "Identifying them is the open question, and the block says so. " +
        "Flagged explicitly because 'both are 5' is exactly the coincidence " +
        "the anti-laundering discipline exists to catch, and because the " +
        "SU(5) row in docs/audits/2026-08-16-su-r-level-tower-gap-map.md " +
        "will be the first thing a future grep lands on.",
    },
  ],
  computation: {
    engine: "python",
    script: "computations/markov_z_fibre_rank_bar_covariance_probe.py",
    witness: "computations/markov-z-fibre-rank-bar-covariance.witness.json",
    status: "verified",
  },
});
