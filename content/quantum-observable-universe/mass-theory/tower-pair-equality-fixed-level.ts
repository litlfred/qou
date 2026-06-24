import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:tower-pair-equality-fixed-level",
  proofs: ["prf:tower-pair-equality-fixed-level"],
  title:
    "Pair-contribution equality at a fixed jet level: $z^2 \\sum_{(i,j) \\in \\mathcal{P}_n} \\Phi_q(|\\hat V_i^{(n)} \\hat V_j^{(n)}|)$ is an exact identity",
  lean: {
    ref: "qou:QOU.BraidKnot.TowerPairEqualityFixedLevel",
    validation: "not_checked",
  },
  uses: ["lem:vhat-pair-commutation-trace"],
  cites: [
    "kassel1995",
    "geckpfeiffer2000",
  ],
  tags: [
    "pair-contribution",
    "markov-trace",
    "jet-tower",
    "sharpness",
    "equality",
    "narrative-replacement",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "**Status: provable** — the lemma's content is `prop:markov-pair-z2`\nplus pair commutativity\n([`lem:vhat-pair-commutation-trace`](#lem\\:vhat-pair-commutation-trace))\nplus Markov-trace factorization\n([`thm:markov-trace-factorization`](#thm\\:markov-trace-factorization)),\nall of which are themselves provable. The corresponding Lean stub\n[qou:QOU.BraidKnot.TowerPairEqualityFixedLevel](tower-pair-equality-fixed-level.lean)\nstates the lemma in the abstract form `tr_M(prod over P_n) = z^2 * (sum\nof dilogs)` and reduces to those upstream lemmas.\n\nThis block closes audit GAP 17b\n([line 114 of `derivation-audit-.md`](../../../docs/audits/derivation-audit-.md))\nand the corresponding \":refterm[Descent]{#descent} involution on pairs / pentagon\nsharpness\" subconjecture: the level-$n$ pair formula is an exact\nequality. The empirical residual to CODATA at light atoms reflects\nincomplete tower truncation (level $\\ge 1$ contributions), not a\nsharpness gap in the level-$n$ formula.\n\nThe remaining open piece is the uniform $\\Delta_{\\max}$ bound for\nthe truncation-error formula\n([`prop:jet-tower-convergence`](#prop\\:jet-tower-convergence)),\ntracked as workplan task **P3.4**.",
    },
  ],
});
