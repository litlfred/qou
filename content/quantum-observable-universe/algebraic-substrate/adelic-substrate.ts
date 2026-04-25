import { definition } from "../../schema/builders";

export default definition({
  label: "def:adelic-substrate",
  title: "Adelic substrate $\\mathbb{A}$",
  tags: ["adeles", "macroscopic-limit", "global", "non-archimedean"],
  uses: [
    "def:classical-limit-functor",
    "def:archimedean-realization-functor",
    "def:algebraic-quantum-volume",
    "def:classical-riemann-zeta",
  ],
  cites: ["tate1967"],
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.AdelicSubstrate",
    validation: "not_checked",
  },
});
