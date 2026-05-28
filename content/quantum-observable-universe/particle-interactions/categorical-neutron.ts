import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-neutron",
  title: "Neutron (categorical)",
  tags: ["neutron", "hadron", "baryon", "color-tube", "knot", "categorical"],
  lean: { ref: "qou:QOU.Torsion.CategoricalNeutron",
    validation: "not_checked",
  },
  uses: ["def:categorical-proton"],
});
