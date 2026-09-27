import { definition } from "../../schema/builders";

export default definition({
  label: "def:unit-root-f-crystal",
  title: "Unit-root F-crystal",
  lean: { ref: "fred2005:Fred2005.UnitRootFCrystal",
    validation: "not_checked",
  },
  tags: ["f-crystal", "unit-root", "frobenius"],
  uses: ["def:commutative-formal-group"],
  cites: ["hazewinkel1978", "zink2002"],
});
