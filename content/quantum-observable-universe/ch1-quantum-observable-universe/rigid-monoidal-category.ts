import { definition } from "../../schema/builders";

export default definition({
  label: "def:rigid-monoidal-category",
  title: "Rigid monoidal category",
  tags: ["category-theory", "monoidal"],
  lean: {
    decl: "QOU.RigidMonoidalCategory",
    file: "QOU/Category/Rigid.lean",
    validation: "not_checked",
  },
  status: "not_started",
  uses: [],
  examples: ["ex:rigid-monoidal-vect"],
});
