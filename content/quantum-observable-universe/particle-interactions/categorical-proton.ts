import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-proton",
  title: "Proton (categorical)",
  tags: ["proton", "hadron", "baryon", "color-tube", "knot", "categorical"],
  lean: { ref: "qou:QOU.Torsion.CategoricalProton",
    validation: "not_checked",
  },
  uses: ["def:down-quark"],
  cites: ["manuscript"],
  computation: {
    engine: "python",
    script: "folio-assistant/computations/codata_masses.py",
    witness: "folio-assistant/computations/codata-masses.witness.json",
    status: "verified",
  },
});
