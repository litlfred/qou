import { definition } from "../../schema/builders";

export default definition({
  label: "def:z-habiro-ring",
  title: "$z$-Habiro ring $\\widehat{\\mathbb{Z}[q^{\\pm 1}][z]}_z$",
  lean: { ref: "qou:QOU.HabiroRing.ZHabiroElement",
    validation: "not_checked",
  },
  uses: [
    "def:habiro-ring",
    "def:algebraic-quantum-volume",
    "prop:full-pole-structure-mass-trace",
    "cor:habiro-expansion-atomic",
  ],
  tags: [
    "habiro-ring",
    "cyclotomic-completion",
    "quantum-dilogarithm",
    "brane-tower",
    "regularization",
    "open-construction",
  ],
});
