import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:yang-mills-mass-gap",
  title: "Yang--Mills Existence and Mass Gap",
  lean: { decl: "QOU.Torsion.YangMillsMassGap", validation: "not_checked" },
  tags: ["yang-mills", "mass-gap", "vacuum", "spectral-gap", "millennium"],
  uses: [
    "def:quantum-observable-universe",
    "def:mass-identity",
    "def:categorical-connection",
    "def:q-yang-mills-levi",
    "prop:vacuum-state",
    "thm:topological-mass",
  ],
});
