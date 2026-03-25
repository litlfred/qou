import { definition } from "../../schema/builders";

export default definition({
  label: "def:division-algorithm",
  title: "Division algorithm",
  lean: {
    decl: "Fred2005.DivisionAlgorithm",
    validation: "not_checked",
  },
  tags: ["groebner-basis", "division", "algorithm"],
  uses: ["def:admissible-system", "def:remainder-module"],
});
