import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:qou-canonical-action",
  title: "Canonical action of a quantum observable universe",
  tags: ["action", "canonical", "dirac", "lagrangian", "decomposition"],
  lean: { ref: "qou:QOU.qou_canonical_action",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-action",
    "def:categorical-lagrangian",
    "sec:categorical-action-notation",
    "rem:yekutieli-stokes",
    "def:yekutieli-lifting-condition",
  ],
});
