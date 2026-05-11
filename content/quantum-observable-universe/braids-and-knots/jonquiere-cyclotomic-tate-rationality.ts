import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:jonquiere-cyclotomic-tate-rationality",
  title:
    "General Jonquière Tate-rationality: wrong-parity part of $\\mathrm{Li}_n(\\zeta_K)$ has closed form $-(2\\pi i)^n / n! \\cdot B_n(1/K)$ at every depth",
  computation: {
    engine: "mpmath",
    script: "folio-assistant/computations/jonquiere_cyclotomic_general.py",
    witness:
      "folio-assistant/computations/jonquiere-cyclotomic-general.witness.json",
    status: "verified",
  },
  uses: [
    "prop:cyclotomic-trilog-imaginary-closed-form",
    "prop:bring-trilog-imaginary-tate-rational",
    "prop:cyclotomic-orbit-sum-all-depths",
    "prop:cyclotomic-dimension-synthesis-all-depths",
    "rem:transcendental-accounting",
  ],
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
