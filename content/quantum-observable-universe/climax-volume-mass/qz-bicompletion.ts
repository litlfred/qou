import { definition } from "../../schema/builders";

export default definition({
  label: "def:qz-bicompletion",
  title: "$(q, z)$-bicompletion $\\widehat{\\mathbb{Z}[q^{\\pm 1}, z]}_{q,z}$",
  lean: {
    ref: "qou:QOU.HabiroRing.QZBicompletionElement",
    validation: "not_checked",
  },
  uses: ["def:habiro-ring", "def:z-habiro-ring", "def:algebraic-quantum-volume"],
  tags: [
    "habiro-ring",
    "bicompletion",
    "cyclotomic-completion",
    "brane-tower",
    "colored-jones",
    "open-construction",
  ],
});
