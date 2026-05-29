import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:graded-baer-star-Hq",
  title:
    "Graded Baer-* on $\\mathcal{H}_q$ across the depth filtration",
  lean: { ref: "qou:QOU.BraidKnot.GradedBaerStarHq", validation: "stub" },
  uses: [
    "def:frobenius-hopf-substrate",
    "prop:gb-depth-period-correspondence",
    "prop:hecke-baer-star-generic",
    "prop:explicit-central-idempotent",
    "rem:chirality-period-pairing",
    "prop:bring-trilog-depth-3-witness",
  ],
  cites: ["bloch2000", "kontsevich1995"],
  tags: [
    "graded-baer-star",
    "graded-mikusinski",
    "depth-filtration",
    "explicit-witnesses",
    "bar-involution",
    "open-problem",
  ],
});
