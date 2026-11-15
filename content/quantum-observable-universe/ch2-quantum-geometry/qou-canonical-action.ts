import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:qou-canonical-action",
  title: "Canonical action of a quantum observable universe",
  tags: ["action", "canonical", "dirac", "lagrangian", "decomposition"],
  lean: {
    decl: "QOU.qou_canonical_action",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-action",
    "def:categorical-lagrangian",
    "sec:categorical-action-notation",
    "rem:yekutieli-stokes",
    "def:yekutieli-lifting-condition",
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/qou-canonical-action-0.svg", blockIndex: 0, hash: "3090e65d6a81" },
  ],

});
