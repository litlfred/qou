import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:categorical-higgs-mechanism",
  lean: { ref: "qou:QOU.BraidsAndKnots.CategoricalHiggsMechanism" },
  title:
    "Categorical Higgs mechanism: Goldstone-eating as topological linking",
  uses: ["conj:weinberg-angle-categorical"],
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
