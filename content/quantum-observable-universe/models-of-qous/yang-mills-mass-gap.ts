import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:yang-mills-mass-gap",
  title: "Yang--Mills Existence and Mass Gap",
  lean: { ref: "qou:QOU.Torsion.YangMillsMassGap", validation: "not_checked" },
  tags: ["yang-mills", "mass-gap", "vacuum", "spectral-gap", "millennium", "kummer", "gm-torsion"],
  uses: [
    "prop:vacuum-state",
    "rem:substrate-gm-torsion",
    "rem:kummer-filtration-obstruction",
    "thm:qou-obstruction-reduction",
  ],
});
