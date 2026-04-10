import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-proton",
  title: "Proton (categorical)",
  tags: ["proton", "hadron", "baryon", "color-tube", "knot", "categorical"],
  lean: {
    decl: "QOU.Torsion.CategoricalProton",
    validation: "not_checked",
  },
  uses: ["def:up-quark", "def:down-quark", "conj:borromean-quark", "def:color-tube-coordinates"],
});
