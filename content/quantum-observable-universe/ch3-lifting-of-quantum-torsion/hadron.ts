import { definition } from "../../schema/builders";

export default definition({
  label: "def:hadron",
  title: "Hadron (composite localized knot)",
  tags: ["hadron", "knot", "composite", "categorical", "mass"],
  lean: {
    decl: "QOU.Hadron",
    validation: "not_checked",
  },
  status: "has_sorry",
  uses: [
    "def:localized-knot",
    "def:projective-line-object",
  ],
});
