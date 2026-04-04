import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:yang-mills-mass-gap",
  title: "Yang--Mills Existence and Mass Gap",
  lean: { decl: "QOU.Torsion.YangMillsMassGap", validation: "not_checked" },
  tags: ["yang-mills", "mass-gap", "vacuum", "spectral-gap", "millennium", "kummer", "gm-torsion"],
  uses: [
    "def:quantum-observable-universe",
    "def:mass-identity",
    "def:categorical-connection",
    "def:q-yang-mills-levi",
    "prop:vacuum-state",
    "thm:topological-mass",
    "rem:substrate-gm-torsion",
    "rem:kummer-filtration-obstruction",
    "def:classical-limit-obstruction",
    "thm:qou-obstruction-reduction",
  ],
});
