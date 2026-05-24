import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:categorical-higgs-idempotent",
  title:
    "Categorical Higgs idempotent $e_H \\colon A \\to A$ projecting onto unbroken $\\mathrm{U}(1)_{em}$",
  lean: { ref: "qou:QOU.QuantumObservableUniverses.CategoricalHiggsIdempotent", validation: "stub" },
  uses: [
    "def:frobenius-hopf-substrate",
    "def:categorical-action",
    "thm:em-spectral-completeness",
  ],
  tags: [
    "higgs-mechanism",
    "categorical-idempotent",
    "ew-symmetry-breaking",
    "u1-em",
    "unbroken-direction",
    "n-sym",
    "open-problem",
  ],
});
