import { definition } from "../../schema/builders";

export default definition({
  label: "def:bundle-initial-conditions",
  title: "Bundle initial conditions",
  tags: ["bundle", "initial-conditions", "knot", "categorical", "configuration-space"],
  lean: { ref: "qou:QOU.BundleInitialConditions",
    validation: "not_checked",
  },
  uses: ["def:hadron"],
});
