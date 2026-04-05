import { definition } from "../../schema/builders";

export default definition({
  label: "def:qou-motivic-measure",
  lean: { decl: "QOU.MotivicIntegration.MotivicMeasure", validation: "not_checked" },
  title: "$q$-Motivic measure on quantum observables",
  uses: [
    "def:qo-moduli",
    "def:qou-locus",
  ],
  cites: ["denef2001", "cluckers2008"],
  tags: ["motivic-integration", "measure", "grothendieck-ring"],
});
