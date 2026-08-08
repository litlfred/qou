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
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "caveat",
      date: "2026-08-08",
      body: "**Naming corrected, value deliberately not.** The block previously concluded that axioms 1–3 force the *Jones*-Markov trace while axiom 3 stipulates $z = 1/(q^{1/2}+q^{-1/2})$, which is convention **C** (full-Hecke Ocneanu / Wenzl $z$-trace) in the [trace-convention registry](../../../docs/coordination/trace-convention-registry.md) — not the trace whose closure is the Jones polynomial (convention **D**, $z = q^3/(q^2+1)$). The name was corrected. The **value of $z$ was left at C**: moving it to D would decide the reserved `mass`-channel owner decision (bean `qou-3qrv`) from the definitional side, and would falsify at least eight other corpus sites that stipulate or derive from the C value — including `thm:jones-markov-trace`, which this block cites, and `rem:bar-involution-c5-algebraic-identities`, whose bar-invariance claim holds for C and fails for D.",
      see: "docs/audits/2026-08-08-markov-axioms-naming-vs-z-value.md",
    },
    {
      kind: "status",
      body: "The Lean stub [`markov-axioms-primitive.lean`](markov-axioms-primitive.lean):\n\n- Defines `class MarkovTraceAxioms` with fields for M1 and M3 (the two\n  needed for the factorisation; M2 is implicit in the cyclic-trace\n  construction; M4 follows from M3 via the Hecke quadratic).\n- Proves `markov_iterated_stab`: k applications of M3 give $\\tau \\cdot z^k$.\n- Proves `disjoint_product_factorisation`: from M3 alone, the disjoint\n  factorisation holds.\n- Discharges `MarkovDisjointStabilisation` from `MarkovTraceAxioms`.\n\nStatus: **closed**, no `sorry`s. The two class fields (`tau_one`,\n`tau_stab`) carry the unavoidable axiomatic content (M1 and M3 are\nJones-1985 axioms, not derivable from more primitive Lean content\nin this scope).",
    },
  ],
});
