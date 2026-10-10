import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:color-spacetime-s5-factorization",
  title:
    "Color and spacetime are orthogonal $S_2\\times S_3$ factors of the Bring Galois group $S_5$",
  lean: {
    ref: "qou:QOU.MassEndomorphism.colorSpacetimeEmbed_injective",
    validation: "validated",
  },
  uses: [
    "prop:cohomological-embedding",
    "rem:chirality-trefoil",
  ],
  tags: [
    "color",
    "spacetime",
    "bring",
    "galois",
    "symmetric-group",
    "electromagnetism",
    "complex-volume",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module " +
        "`mass-endomorphism/color-spacetime-s5-factorization.lean` uses " +
        "`Real.pi`, `Complex.*`. These are real-analytic constructs with " +
        "no generic-`CommRing` counterpart, so the `ℝ` specialisation is " +
        "forced by the statement itself rather than chosen. The block " +
        "therefore sits on the archimedean side of the §7c wall by " +
        "construction.",
    },
  ],
});
