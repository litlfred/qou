import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:graded-baer-star-Hq",
  title:
    "Graded Baer-* on $\\mathcal{H}_q$ across the depth filtration",
  lean: { ref: "qou:QOU.BraidKnot.GradedBaerStarHq", validation: "stub" },
  cites: ["bloch2000", "kontsevich1995"],
  tags: [
    "tier:S",
    "graded-baer-star",
    "graded-mikusinski",
    "depth-filtration",
    "explicit-witnesses",
    "bar-involution",
    "open-problem",
  ],
});
