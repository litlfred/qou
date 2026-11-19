import { definition } from "../../schema/builders";

export default definition({
  label: "def:adelic-substrate",
  title: "Adelic aether $\\mathbb{A}$",
  tags: ["adeles", "macroscopic-limit", "global", "non-archimedean"],
  uses: [],
  cites: ["tate1967"],
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.AdelicSubstrate",
    validation: "not_checked",
  },
});
