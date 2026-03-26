import { definition } from "../../schema/builders";

export default definition({
  label: "def:down-quark",
  title: "Down quark",
  tags: ["quark", "down", "trefoil", "mirror", "fermion", "generation-1"],
  lean: {
    decl: "QOU.Descartes.DownQuark",
    validation: "not_checked",
  },
  uses: [
    "def:up-quark",
    "rem:knot-notation-convention",
  ],
});
