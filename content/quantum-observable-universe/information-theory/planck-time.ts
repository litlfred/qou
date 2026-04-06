import { definition } from "../../schema/builders";

export default definition({
  label: "def:planck-time",
  title: "Planck Time",
  tags: ["planck-time", "discrete-time", "reeb-flow", "information-theory"],
  lean: {
    decl: "QOU.planckTime",
    validation: "leanok",
  },
  uses: ["rem:julia-set-reeb"],
});
