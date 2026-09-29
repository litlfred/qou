import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:qou-canonical-action",
  label: "rem:canonical-action-obstruction",
  title: "Scalar-ambiguity obstruction of the canonical action",
  tags: ["action", "canonical", "observability", "yekutieli", "obstruction"],
  uses: [
    "prop:qou-canonical-action",
    "def:quantum-observable-universe",
    "def:yekutieli-lifting-condition",
    "rem:yekutieli-stokes",
  ],
});
