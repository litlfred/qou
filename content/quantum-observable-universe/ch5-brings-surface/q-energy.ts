import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-energy",
  title:
    "$q$-Energy: sum of $q$-angular momentum, $q$-momentum, and categorical action",
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
  lean: {
    decl: "QOU.Descartes.QEnergy",
    validation: "not_checked",
  },
  uses: [
    "def:q-momentum",
    "def:q-angular-momentum",
    "def:substrate-parameter",
    "def:crossing-energy",
    "prop:topological-mass-formula",
    "prop:local-substrate-q",
  ],
});
