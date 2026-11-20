import { remark } from "../../schema/builders";

export default remark({
  label: "rem:markov-axioms-primitive",
  title:
    "Primitive Markov-trace axioms (M1–M4 from Jones 1985 / Wenzl 1988) in Lean; discharges the `MarkovDisjointStabilisation` class for `prop:categorical-chain-convergence-mechanisms`",
  interprets: "prop:markov-trace-frobenius-selection",
  uses: ["prop:categorical-chain-convergence-mechanisms"],
  cites: ["jones1985", "wenzl1988"],
  tags: [
    "lean-infrastructure",
    "markov-axioms",
    "primitive-axiomatisation",
    "class-discharge",
    "convergence-mechanism",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): - `lem:feynman-eigenbasis-decomposition` already writes the row cap\n\n- Given $y_{(1^3)} = 0$, `markovWeights_eq_jones_of_threeRow_eq_zero`\n  ([`MarkovTraceTLUniqueness.lean`](../lean/QOU/BraidsAndKnots/MarkovTraceTLUniqueness.lean))\n  shows the faithful" },
    {
      kind: "refined-framing",
      date: "2026-08-09",
      body:
        "**Convention C excised; the loop value went from stipulated to " +
        "forced.** This remark previously fixed $z = 1/(q^{1/2}+q^{-1/2})$ " +
        "and described it as \"a stipulation of this definition, not a " +
        "consequence of it\" — convention C of the trace-convention " +
        "registry. Under the owner ruling that excised C, the selection is " +
        "derived instead: the two-row cap already in the mass channel's own " +
        "decomposition gives $y_{(1^3)} = 0$, and " +
        "`markovWeights_eq_jones_of_threeRow_eq_zero` then makes the " +
        "faithful normalised Markov trace unique at $z = q^3/(q^2+1)$. The " +
        "prose above states the forcing; that an earlier version stipulated " +
        "is recorded here rather than in the paper, per §4d.",
    },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "status",
      body: "The Lean stub [`markov-axioms-primitive.lean`](markov-axioms-primitive.lean):\n\n- Defines `class MarkovTraceAxioms` with fields for M1 and M3 (the two\n  needed for the factorisation; M2 is implicit in the cyclic-trace\n  construction; M4 follows from M3 via the Hecke quadratic).\n- Proves `markov_iterated_stab`: k applications of M3 give $\\tau \\cdot z^k$.\n- Proves `disjoint_product_factorisation`: from M3 alone, the disjoint\n  factorisation holds.\n- Discharges `MarkovDisjointStabilisation` from `MarkovTraceAxioms`.\n\nStatus: **closed**, no `sorry`s. The two class fields (`tau_one`,\n`tau_stab`) carry the unavoidable axiomatic content (M1 and M3 are\nJones-1985 axioms, not derivable from more primitive Lean content\nin this scope).",
    },
  ],
});
