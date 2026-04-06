import { definition } from "../../schema/builders";

export default definition({
  label: "def:localized-hadron",
  title: "Localized hadron",
  tags: ["hadron", "knot", "localized", "categorical"],
  lean: {
    decl: "QOU.LocalizedHadron",
    validation: "not_checked",
  },
  uses: [
    "def:hadron",
    "def:categorical-point",
    "def:projective-line-object",
  ],
});
