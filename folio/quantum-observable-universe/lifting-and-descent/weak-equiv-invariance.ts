import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:weak-equiv-invariance",
  lean: { ref: "qou:QOU.Torsion.weak_equiv_invariance",
    validation: "not_checked",
  },
  title: "Weak equivalence invariance of physical states",
  tags: ["weak-equivalence", "vacuum-state", "physical-states"],
  uses: [
    "prop:cosimplicial-crossed-groupoid",
    "prop:vacuum-state",
    "prop:descent-eigenspaces",
  ],
  proofs: ["prf:weak-equiv-invariance"],
});
