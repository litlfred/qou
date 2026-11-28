import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bounded-width-trace-cost",
  title: "A fixed-width trace costs linear time, not $3^c$",
  lean: { ref: "qou:QOU.Information.WordEval.traceCost_fst" },
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-28",
      body:
        "Lean: `QOU/InformationTheory/WordEvalCost.lean` — `evalCost`, `evalCost_fst` (result is `l.prod *ᵥ v`), `evalCost_snd` (count `c·d²`), `traceCost_fst` (result is `trace l.prod`), `traceCost_snd` (count `d·c·d²`), `traceCost_not_superPoly` (for fixed `d` the count is not `SuperPolynomial`, the predicate of `PhysicalIntractability`). The second paragraph's application to `H_n` uses the regular representation and is not itself formalised.",
    },
  ],
  tags: ["transfer-matrix", "computational-horizon", "matrix-trace"],
  uses: ["def:computational-horizon", "prop:skein-polynomial-transfer-matrix"],
});
