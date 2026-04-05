import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-motivic-zeta",
  lean: { decl: "QOU.MotivicIntegration.MotivicZeta", validation: "not_checked" },
  title: "$q$-Motivic zeta function",
  uses: [
    "def:qou-motivic-measure",
    "conj:q-gl-kummer-filtration",
  ],
  cites: ["denef2001"],
  tags: ["motivic-integration", "zeta-function", "kummer"],
});
