import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-neutron",
  title: "Neutron (categorical)",
  tags: ["neutron", "hadron", "baryon", "color-tube", "knot", "categorical"],
  lean: { ref: "qou:QOU.Torsion.CategoricalNeutron",
    validation: "not_checked",
  },
  uses: ["def:categorical-proton"],
  computation: {
    engine: "python",
    script: "computations/codata_masses.py",
    witness: "computations/codata-masses.witness.json",
    status: "verified",
  },
});
