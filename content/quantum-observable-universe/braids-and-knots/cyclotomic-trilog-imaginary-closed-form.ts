import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cyclotomic-trilog-imaginary-closed-form",
  title:
    "General closed form: Im Li$_3$($\\zeta_n$) = $(n - 1)(n - 2)\\pi^3 / (3 n^3)$ for every root of unity",
  computation: {
    engine: "mpmath",
    script: "folio-assistant/computations/cyclotomic_trilog_imaginary.py",
    witness:
      "folio-assistant/computations/cyclotomic-trilog-imaginary.witness.json",
    status: "verified",
  },
  uses: [
    "prop:bring-trilog-imaginary-tate-rational",
    "prop:borel-partial-resolution",
    "rem:transcendental-accounting",
    "conj:cl3-zeta5-geometric-realization",
  ],
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
