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
      body: "**Superseded 2026-11-20 (bean `qou-ltwg`, owner options 2 + 3).** The library file `QOU/BraidKnot/MarkovAxiomsPrimitive.lean` used to define `class MarkovTraceAxioms` with two scalar fields pinned to `1` and `markovZax u`, plus theorems of the form `∃ τ', τ' = τ·z^k := ⟨_, rfl⟩`. The class mentioned no trace and could be inhabited in one line. The theorems were tautologies, so the claimed discharge of `MarkovDisjointStabilisation` was empty.\n\nThe class and the tautologies are removed. M1–M4 are now the fields of the genuine `QOU.MathlibExt.OcneanuTrace.MarkovTrace` (a trace on a tower of algebras). Iterated stabilisation is `tr_mul_genWord`, disjoint-block multiplicativity on a braided tower is `BraidedBlockShiftTrace.tr_blockProd`, and ascending-word chain factorisation is `tr_chainWord`. All three are proved for every genuine trace. A genuine instance of that structure at `q ≠ 1` on the full Hecke tower is still missing (epic `qou-dxbw` M4).",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Jones–Markov trace](#thm:jones-markov-trace))" },
  ],
});
