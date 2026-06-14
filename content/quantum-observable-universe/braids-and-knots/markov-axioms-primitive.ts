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
    {
      kind: "status",
      body: "The Lean stub [`markov-axioms-primitive.lean`](markov-axioms-primitive.lean):\n\n- Defines `class MarkovTraceAxioms` with fields for M1 and M3 (the two\n  needed for the factorisation; M2 is implicit in the cyclic-trace\n  construction; M4 follows from M3 via the Hecke quadratic).\n- Proves `markov_iterated_stab`: k applications of M3 give $\\tau \\cdot z^k$.\n- Proves `disjoint_product_factorisation`: from M3 alone, the disjoint\n  factorisation holds.\n- Discharges `MarkovDisjointStabilisation` from `MarkovTraceAxioms`.\n\nStatus: **closed**, no `sorry`s. The two class fields (`tau_one`,\n`tau_stab`) carry the unavoidable axiomatic content (M1 and M3 are\nJones-1985 axioms, not derivable from more primitive Lean content\nin this scope).",
    },
  ],
});
