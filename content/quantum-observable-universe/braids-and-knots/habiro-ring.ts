import { definition } from "../../schema/builders";

export default definition({
  label: "def:habiro-ring",
  title: "Habiro ring $\\widehat{\\mathbb{Z}[q]}$",
  lean: {
    decl: "QOU.HabiroRing.HabiroElement",
    validation: "not_checked",
  },
  uses: [
    "rem:hecke-algebra-from-braiding",
    "def:algebraic-quantum-volume",
  ],
});
