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
    script: "computations/cl_n_l_value_decomposition.py",
    witness:
      "computations/cl-n-l-value-decomposition.witness.json",
    status: "verified",
  },
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
  // The constructive proof of β(3)=π³/32 invokes Theorem A
  // (prop:jonquiere-cyclotomic-tate-rationality) alongside Theorem G
  // (prop:cyclotomic-dimension-synthesis-all-depths). Both live in mass-theory
  // (an earlier chapter) — genuine backward dependencies, no forward-ref.
  uses: [
    "prop:cyclotomic-dimension-synthesis-all-depths",
    "prop:jonquiere-cyclotomic-tate-rationality",
  ],
});
