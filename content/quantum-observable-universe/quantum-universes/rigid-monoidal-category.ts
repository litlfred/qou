import { definition } from "../../schema/builders";

export default definition({
  label: "def:rigid-monoidal-category",
  title: "Rigid monoidal category",
  tags: ["category-theory", "monoidal"],
  lean: {
    decl: "QOU.RigidMonoidalCategory",
    validation: "not_checked",
  },
  uses: ["def:snake-identity", "def:no-quasi-zeros"],
  examples: ["ex:rigid-monoidal-vect"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/rigid-monoidal-category-0.svg", blockIndex: 0, hash: "dcde857fc6e5" },
  ],

});
