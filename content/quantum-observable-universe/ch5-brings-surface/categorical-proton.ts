import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-proton",
  title: "Proton (categorical)",
  tags: ["proton", "hadron", "baryon", "color-tube", "knot", "categorical"],
  lean: {
    decl: "QOU.Torsion.CategoricalProton",
    validation: "not_checked",
  },
  uses: [
    "def:hadron",
    "def:up-quark",
    "def:down-quark",
    "def:knot-particle-generation",
    "def:color-tube-coordinates",
  ],
});
