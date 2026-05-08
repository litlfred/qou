import { definition } from "../../schema/builders";

export default definition({
  label: "def:bundle-isotopy-equivalence",
  title: "Isotopy equivalence of bundle initial conditions",
  tags: ["bundle", "isotopy", "equivalence"],
  lean: { ref: "qou:QOU.BundleIsotopyEquiv",
    validation: "not_checked",
  },
  uses: ["def:bundle-initial-conditions"],
});
