import { definition } from "../../schema/builders";

export default definition({
  label: "def:habiro-ring",
  title: "Habiro ring $\\widehat{\\mathbb{Z}[q]}$",
  lean: { ref: "qou:QOU.HabiroRing.HabiroElement",
    validation: "not_checked",
  },
  uses: ["def:algebraic-quantum-volume"],
});
