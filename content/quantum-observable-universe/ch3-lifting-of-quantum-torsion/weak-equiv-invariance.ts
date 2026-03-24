import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:weak-equiv-invariance",
  lean: {
    decl: "QOU.Torsion.weak_equiv_invariance",
    validation: "not_checked",
  },
  title: "Weak equivalence invariance of physical states",
  tags: ["weak-equivalence", "vacuum-state", "physical-states"],
  uses: [
    "def:quantum-observable-universe",
    "def:recursive-brane-tower",
    "def:direct-limit-algebra",
    "def:descent-involution",
    "prop:cosimplicial-crossed-groupoid",
    "prop:vacuum-state",
    "prop:descent-eigenspaces",
    "lem:descent",
  ],
  proofs: ["prf:weak-equiv-invariance"],
});
