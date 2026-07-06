import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cyclotomic-orbit-sum-all-depths",
  title:
    "General orbit-sum at every depth: $\\sum_k \\mathrm{Cl}_n(2\\pi k/N) = (N^{1-n} - 1)\\zeta(n)$ for $n$ odd, $0$ for $n$ even",
  lean: {
    ref: "qou:QOU.BraidKnot.CyclotomicOrbitSumAllDepths.orbit_sum_all_depths",
    validation: "not_checked",
  },
  computation: {
    engine: "mpmath",
    script: "computations/jonquiere_cyclotomic_general.py",
    witness:
      "computations/jonquiere-cyclotomic-general.witness.json",
    status: "verified",
  },
  cites: ["bloch2000", "zagier1986"],
  tags: [
    "multiplication-formula",
    "orbit-sum",
    "all-depths",
    "general-form",
    "polylogarithm",
    "cyclotomic",
    "graded-mikusinski",
    "theorem-level",
  ],
});
