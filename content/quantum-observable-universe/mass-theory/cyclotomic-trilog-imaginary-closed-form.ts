import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cyclotomic-trilog-imaginary-closed-form",
  title:
    "Trilogarithm imaginary part at $\\zeta_n$: closed form $(n - 1)(n - 2)\\pi^3 / (3 n^3)$ for every root of unity",
  lean: {
    ref: "qou:QOU.BraidKnot.CyclotomicTrilogImaginary.closed_form_holds",
    validation: "not_checked",
  },
  computation: {
    engine: "mpmath",
    script: "computations/cyclotomic_trilog_imaginary.py",
    witness:
      "computations/cyclotomic-trilog-imaginary.witness.json",
    status: "verified",
  },
  uses: ["prop:bring-trilog-imaginary-tate-rational"],
  cites: ["bloch2000", "zagier1986"],
  tags: [
    "kummer-reflection",
    "trilogarithm",
    "cyclotomic",
    "tate-rational",
    "closed-form",
    "depth-3",
    "graded-mikusinski",
    "theorem-level",
  ],
});
