import { definition } from "../../schema/builders";

export default definition({
  label: "def:hadron",
  title: "Hadron (abstract composite knot)",
  tags: ["hadron", "knot", "composite", "categorical", "mass"],
  lean: {
    decl: "QOU.Hadron",
    validation: "not_checked",
  },
  status: "has_sorry",
  uses: [],
});
