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
});
