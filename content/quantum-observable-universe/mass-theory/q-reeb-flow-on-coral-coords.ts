import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-reeb-flow-on-coral-coords",
  lean: {
    ref: "qou:QOU.CategoricalReeb.QReebFlowOnCoralCoords",
    validation: "not_checked",
  },
  title: "The $q$-Reeb flow in coral-sector coordinates",
  tags: [
    "reeb-flow",
    "coral-sectors",
    "exceptional-divisor",
    "substrate-parameter",
  ],
  uses: [
    "def:coral-sector-coords",
    "def:reeb-bundle",
    "ex:q-reeb-flow",
    "def:substrate-parameter",
  ],
});
