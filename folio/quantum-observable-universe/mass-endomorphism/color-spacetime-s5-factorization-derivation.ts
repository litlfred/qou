import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:color-spacetime-s5-factorization",
  label: "rem:color-spacetime-s5-factorization-derivation",
  title:
    "Single trace object, discreteness of the winding phase, and the Lean formalisation",
  tags: [
    "bring-fivefold",
    "color-grading",
    "spacetime",
    "s5-galois",
    "derivation-chain",
  ],
  uses: ["prop:color-spacetime-s5-factorization"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ## Lean formalism\n\nThese claims are formalized without `sorry` in [`QOU.MassEndomorphism`](color-spacetime-s5-factorization.lean) via `spacetime_color_card`, `colorSpacetimeEmbed_injective`, `color_fixes_spacetime`, `spacetime_fixes_color`, and `winding_hom_to_finite_trivial`. The construction is generic. The embedding and divisibility arguments rely strictly on combinatorial data, requiring no archimedean input." },
  ],
});
