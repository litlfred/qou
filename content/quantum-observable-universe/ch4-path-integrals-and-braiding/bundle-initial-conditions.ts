import { definition } from "../../schema/builders";

export default definition({
  label: "def:bundle-initial-conditions",
  title: "Bundle initial conditions (big bang state)",
  tags: ["bundle", "initial-conditions", "knot", "categorical", "big-bang"],
  lean: {
    decl: "QOU.BundleInitialConditions",
    validation: "not_checked",
  },
  uses: [
    "def:localized-knot",
    "def:hadron",
  ],
});
