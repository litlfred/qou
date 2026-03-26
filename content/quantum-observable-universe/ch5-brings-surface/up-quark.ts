import { definition } from "../../schema/builders";

export default definition({
  label: "def:up-quark",
  title: "Up quark",
  tags: ["quark", "up", "trefoil", "fermion", "generation-1"],
  lean: {
    decl: "QOU.Descartes.UpQuark",
    validation: "not_checked",
  },
  uses: [
    "prop:torus-knot-generators",
    "rem:knot-notation-convention",
  ],
});
