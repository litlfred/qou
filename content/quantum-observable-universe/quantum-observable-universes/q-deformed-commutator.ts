import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-deformed-commutator",
  title: "$q$-deformed commutator $[\\hat{X}, \\hat{P}]_q$",
  tags: ["heisenberg", "uncertainty", "commutator", "reeb", "fibre-coordinate"],
  uses: ["def:quantum-planck-constant", "def:substrate-parameter"],
  lean: {
    ref: "qou:QOU.ArchimedeanUniverse.qDeformedCommutator",
    validation: "not_checked",
  },
});
