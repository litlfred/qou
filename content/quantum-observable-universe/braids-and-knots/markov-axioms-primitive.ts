import { remark } from "../../schema/builders";

export default remark({
  label: "rem:markov-axioms-primitive",
  title:
    "Primitive Markov-trace axioms (M1–M4 from Jones 1985 / Wenzl 1988) in Lean; discharges the `MarkovDisjointStabilisation` class for `prop:categorical-chain-convergence-mechanisms`",
  interprets: "prop:markov-trace-frobenius-selection",
  uses: [
    "prop:categorical-chain-convergence-mechanisms",
    "def:bar-involution",
  ],
  cites: ["jones1985", "wenzl1988"],
  tags: [
    "lean-infrastructure",
    "markov-axioms",
    "primitive-axiomatisation",
    "class-discharge",
    "convergence-mechanism",
  ],
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "refined-framing",
      date: "2026-08-08",
      body: "**Stabilisation parameter re-pinned C → D** (owner ruling, closing the `mass`-channel dispute of bean `qou-3qrv`). This block is the definitional pin the [trace-convention registry](../../../docs/coordination/trace-convention-registry.md) names as the reason the mass channel's *definitional* convention read C while production ran D. It now reads D, so definition and production agree and the channel leaves `disputed`.\n\nNo production number moves: the mass channel already ran D. The binding channel keeps C, deliberately, and its production is untouched.\n\nThe forcing argument is two independent steps, neither using a measured value — bar-covariance of M3 excludes C (`zD_bar_sub`, `zC_ne_bar_sub`), TL faithfulness picks D out of what remains (`MarkovTraceTLUniqueness`). The bar step alone does **not** select D: `bar_sub_of_bar_even` records that its solution set is D plus any bar-even function.",
      see: "docs/coordination/trace-convention-registry.md",
    },
    {
      kind: "status",
      body: "The Lean stub [`markov-axioms-primitive.lean`](markov-axioms-primitive.lean):\n\n- Defines `class MarkovTraceAxioms` with fields for M1 and M3 (the two\n  needed for the factorisation; M2 is implicit in the cyclic-trace\n  construction; M4 follows from M3 via the Hecke quadratic).\n- Proves `markov_iterated_stab`: k applications of M3 give $\\tau \\cdot z^k$.\n- Proves `disjoint_product_factorisation`: from M3 alone, the disjoint\n  factorisation holds.\n- Discharges `MarkovDisjointStabilisation` from `MarkovTraceAxioms`.\n\nStatus: **closed**, no `sorry`s. The two class fields (`tau_one`,\n`tau_stab`) carry the unavoidable axiomatic content (M1 and M3 are\nJones-1985 axioms, not derivable from more primitive Lean content\nin this scope).",
    },
  ],
});
