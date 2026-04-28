import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-categorical-q-torsion-leaf",
  lean: { ref: "qou:QOU.CategoricalQTorsionLeaf", validation: "not_checked" },
  title: "Categorical q-torsion leaf",
  tags: ["glossary", "torsion", "q-deformation", "category-theory"],
  uses: ["def:categorical-q-reeb-flow"],
  defines: ["categorical-q-torsion-leaf"],
});
