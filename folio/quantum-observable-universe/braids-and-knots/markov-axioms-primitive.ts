import { remark } from "../../schema/builders";

export default remark({
  label: "rem:markov-axioms-primitive",
  title:
    "Primitive Markov-trace axioms (M1–M4 from Jones 1985 / Wenzl 1988) and the disjoint-stabilisation factorisation",
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
      date: "2026-10-10",
      body:
        "**Lean status corrected (bean `qou-ekga`, owner decisions A+B+C).** This " +
        "note previously said the Lean defined a class `MarkovTraceAxioms` carrying " +
        "M1 and M3, proved `markov_iterated_stab` and `disjoint_product_factorisation`, " +
        "and discharged `MarkovDisjointStabilisation`. None of that held: the class " +
        "(`QOU.BraidKnot.MarkovTraceAxioms`) had no trace in it — two scalars, each " +
        "pinned by its own equation, so trivially inhabited — and the theorems had " +
        "the shape `∃ x, x = e`. The class is now the deprecated " +
        "`QOU.BraidKnot.MarkovScalarPins`; the six existentials and the unwired " +
        "\"discharge\" are withdrawn.\n\n" +
        "The honest statements are proved against the single content-bearing class " +
        "`QOU.Hecke.MarkovTraceAxioms` (`lean/QOU/Hecke/MarkovTraceProduct.lean`, " +
        "a real `trace : List GeneratorChain → R_q`): `markov_trace_stabilise` " +
        "(appending k bare generators multiplies the trace by $z^k$) and " +
        "`markov_trace_disjoint_stabilise` (trace of $K_1$ then $K_2$ then k bare " +
        "generators is $\\mathrm{tr}(K_1)\\,\\mathrm{tr}(K_2)\\,z^k$), sorry-free, " +
        "no extra hypothesis. Both are statements about the chain-list model, whose " +
        "class has exactly one inhabitant (`trace = chainProduct z`); the bridge from " +
        "the Hecke-algebra trace of a braid to that model is not formalised, and " +
        "`MarkovDisjointStabilisation` remains an axiomatic class — it is not " +
        "discharged.",
    },
  ],
});
