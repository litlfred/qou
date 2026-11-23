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
  // (prop:jonquiere-cyclotomic-tate-rationality) only. The edge to the
  // dimension count (now conj:cyclotomic-dimension-synthesis-all-depths) was
  // cut 2026-11-21: the proof never uses it, and keeping it would make this
  // proposition downstream of a conjecture.
  uses: [
    "prop:jonquiere-cyclotomic-tate-rationality",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module " +
        "`lean/QOU/BraidKnot/CyclotomicLValueDecomposition.lean` uses " +
        "`Real.pi`. These are real-analytic constructs with no " +
        "generic-`CommRing` counterpart, so the `ℝ` specialisation is " +
        "forced by the statement itself rather than chosen. The block " +
        "therefore sits on the archimedean side of the §7c wall by " +
        "construction.",
    },
  ],
});
