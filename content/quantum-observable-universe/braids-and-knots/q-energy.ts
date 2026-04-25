import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-energy",
  title:
    "$q$-Deformed Energy",
  tags: [
    "energy",
    "q-deformed",
    "categorical-action",
    "momentum",
    "angular-momentum",
    "crossing",
    "mass-energy",
    "kinematic",
  ],
  lean: { ref: "qou:QOU.Descartes.QEnergy",
    validation: "not_checked",
  },
  uses: ["def:q-angular-momentum"],
});
