import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-reeb-flow-on-color-coords",
  lean: {
    ref: "qou:QOU.CategoricalReeb.QReebFlowOnColorCoords",
    validation: "not_checked",
  },
  title: "The $q$-Reeb flow in color-sector coordinates",
  tags: [
    "reeb-flow",
    "color-sectors",
    "exceptional-divisor",
    "substrate-parameter",
  ],
  uses: [
    "def:color-sector-coords",
    "def:reeb-bundle",
    "ex:q-reeb-flow",
  ],
});
