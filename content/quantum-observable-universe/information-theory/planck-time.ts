import { definition } from "../../schema/builders";

export default definition({
  label: "def:planck-time",
  title: "Planck Time",
  tags: ["planck-time", "discrete-time", "reeb-flow", "information-theory"],
  lean: { ref: "qou:QOU.planckTime",
    validation: "leanok",
  },
  uses: ["def:substrate-parameter", "def:quantum-planck-constant"],
});
