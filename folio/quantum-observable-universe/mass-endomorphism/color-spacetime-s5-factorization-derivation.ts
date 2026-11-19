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
    {
      kind: "note",
      body: "Formalized in `color-spacetime-s5-factorization.lean` (`QOU.MassEndomorphism`) via `spacetime_color_card`, `colorSpacetimeEmbed_injective`, `color_fixes_spacetime`, `spacetime_fixes_color`, and `winding_hom_to_finite_trivial`.",
    },
  ],
});
