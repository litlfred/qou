import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-higgs-mechanism",
  lean: { ref: "qou:QOU.BraidsAndKnots.CategoricalHiggsMechanism" },
  title:
    "Categorical Higgs mechanism: Goldstone-eating as topological linking",
  uses: ["prop:weinberg-angle-categorical"],
  tags: [
    "higgs-mechanism",
    "goldstone-eating",
    "linking-number",
    "categorical-physics",
    "broken-symmetry",
    "ew-symmetry-breaking",
    "open-problem",
    "skeleton",
  ],
});
