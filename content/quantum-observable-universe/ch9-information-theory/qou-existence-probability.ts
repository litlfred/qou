import { definition } from "../../schema/builders";

export default definition({
  label: "def:qou-existence-probability",
  lean: { decl: "QOU.MotivicIntegration.ExistenceProbability", validation: "not_checked" },
  title: "Categorical probability of QOU existence",
  uses: [
    "def:qou-motivic-measure",
    "prop:qou-motivic-euler",
    "def:qo-moduli",
  ],
  cites: ["denef2001"],
  tags: ["motivic-integration", "probability", "existence"],
});
