import { definition } from "../../schema/builders";

export default definition({
  label: "def:down-quark",
  title: "Down quark",
  tags: ["quark", "down", "unknot", "borromean", "fermion", "color-tube"],
  lean: { ref: "qou:QOU.Descartes.DownQuark",
    validation: "not_checked",
  },
  uses: ["def:up-quark"],
});
