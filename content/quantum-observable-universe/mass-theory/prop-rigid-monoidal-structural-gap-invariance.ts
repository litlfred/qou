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
  ],
  computation: {
    engine: "python",
    script: "folio-assistant/computations/lp-duality-check.py",
    witness: "folio-assistant/computations/lp-duality-check.witness.json",
    status: "verified",
  },
  tags: [
    "rigid-monoidal",
    "type-b-folding",
    "kashiwara-crystal",
    "structural-gap",
    "convention-invariance",
    "categorical-unification",
  ],
});
