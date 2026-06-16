import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:jonquiere-cyclotomic-tate-rationality",
  title:
    "General Jonquière Tate-rationality: wrong-parity part of $\\mathrm{Li}_n(\\zeta_K)$ has closed form $-(2\\pi i)^n / n! \\cdot B_n(1/K)$ at every depth",
  lean: {
    ref: "qou:QOU.BraidKnot.JonquiereCyclotomicTateRationality.jonquiere_tate_rationality",
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
    "jonquiere-inversion",
    "bernoulli-polynomial",
    "tate-rational",
    "cyclotomic",
    "polylogarithm",
    "all-depths",
    "general-form",
    "graded-mikusinski",
    "theorem-level",
  ],
});
