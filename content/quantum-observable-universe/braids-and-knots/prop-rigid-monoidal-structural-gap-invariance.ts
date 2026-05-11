import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:rigid-monoidal-structural-gap-invariance",
  title:
    "Convention-independence of the structural gap: the brane-tower factors through the rigid monoidal Markov trace on the Type-B-folded Hecke category",
  lean: {
    ref: "qou:QOU.BraidKnot.RigidMonoidalStructuralGapInvariance",
    validation: "not_checked",
  },
  uses: [
    "prop:spin-involution-lp-dual-invariance",
    "conj:brane-tower-z-habiro",
    "conj:magic-shell-stabilization",
    "def:rigid-monoidal-category",
    "prop:operator-selection-lp",
  ],
  tags: [
    "rigid-monoidal",
    "type-b-folding",
    "kashiwara-crystal",
    "structural-gap",
    "convention-invariance",
    "categorical-unification",
  ],
});
