import { definition } from "../../schema/builders";

export default definition({
  label: "def:hadron",
  title: "Hadron (stable knot composite)",
  tags: ["hadron", "knot", "composite", "stable", "crossing-energy"],
  lean: {
    decl: "QOU.Hadron",
    validation: "not_checked",
  },
  uses: ["def:coulomb-charge"],
});
