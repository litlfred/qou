import { definition } from "../../schema/builders";

export default definition({
  label: "def:up-quark",
  title: "Up quark",
  tags: ["quark", "up", "unknot", "borromean", "fermion", "color-tube"],
  lean: { ref: "qou:QOU.Descartes.UpQuark",
    validation: "not_checked",
  },
  uses: ["conj:borromean-quark"],
});
