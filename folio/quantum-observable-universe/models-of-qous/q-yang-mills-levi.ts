import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-yang-mills-levi",
  title: "$q$-Weighted curvature--Levi functional",
  lean: { ref: "qou:QOU.QYangMillsLevi", validation: "not_checked" },
  uses: [
    "ex:c-quantum-observable-universe",
    "ex:instanton",
  ],
  tags: ["curvature", "levi-form", "functional"],
});
