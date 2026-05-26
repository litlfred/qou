import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cyclotomic-l-value-decomposition",
  title:
    "Cyclotomic depth-$n$ generators decompose into Dirichlet $L$-values: $\\beta(3) = \\pi^3/32$ as a corollary",
  lean: {
    ref: "qou:QOU.BraidKnot.CyclotomicLValueDecomposition.beta_3_from_jonquiere",
    validation: "not_checked",
  },
  computation: {
    engine: "mpmath",
    script: "folio-assistant/computations/cl_n_l_value_decomposition.py",
    witness:
      "folio-assistant/computations/cl-n-l-value-decomposition.witness.json",
    status: "verified",
  },
  uses: [
    "prop:jonquiere-cyclotomic-tate-rationality",
    "prop:cyclotomic-dimension-synthesis-all-depths",
    "prop:depth-2-identification-bloch-suslin",
    "prop:borel-partial-resolution",
    "rem:k-theory-period-rosetta",
    "rem:transcendental-accounting",
  ],
  cites: ["bloch2000", "zagier1986"],
  tags: [
    "dirichlet-l-value",
    "catalan-beta",
    "gauss-sum",
    "hurwitz-lerch",
    "cyclotomic",
    "polylogarithm",
    "graded-mikusinski",
    "theorem-level",
    "analytic-number-theory-bridge",
  ],
});
