import { definition } from "../../schema/builders";

export default definition({
  label: "def:rigid-monoidal-category",
  title: "Rigid monoidal category",
  tags: ["category-theory", "monoidal"],
  lean: { ref: "qou:QOU.RigidMonoidalCategory",
    validation: "not_checked",
  },
  uses: ["def:snake-identity"],
  examples: ["ex:rigid-monoidal-vect"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/rigid-monoidal-category-1.svg", blockIndex: 1, hash: "9b5f1dfb5af4" },
  ],

});
