import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cyclotomic-cl3-orbit-sum-general",
  title:
    "General orbit-sum identity: $\\sum_k \\mathrm{Cl}_3(2\\pi k/N) = -(N^2-1)/N^2 \\cdot \\zeta(3)$ at every $N \\geq 2$",
  computation: {
    engine: "mpmath",
    script: "folio-assistant/computations/cyclotomic_trilog_imaginary.py",
    witness:
      "folio-assistant/computations/cyclotomic-trilog-imaginary.witness.json",
    status: "verified",
  },
  uses: [
    "prop:cl3-zeta5-orbit-sum-identity",
    "prop:cyclotomic-trilog-imaginary-closed-form",
    "prop:borel-partial-resolution",
    "rem:transcendental-accounting",
    "prop:cl3-zeta5-pslq-independence",
  ],
  cites: ["bloch2000", "zagier1986"],
  tags: [
    "multiplication-formula",
    "orbit-sum",
    "trilogarithm",
    "cyclotomic",
    "zeta-3",
    "closed-form",
    "depth-3",
    "graded-mikusinski",
    "theorem-level",
  ],
});
