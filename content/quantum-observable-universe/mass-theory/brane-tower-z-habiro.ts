import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:brane-tower-z-habiro",
  lean: { ref: "qou:QOU.BraidKnot.BraneTowerZHabiro" },
  title: "Brane tower lives in the $z$-Habiro ring",
  uses: [
    "def:z-habiro-ring",
    "def:habiro-ring",
    "cor:quantum-dilogarithm",
    "prop:atom-knot-mass-derivation",
    "prop:habiro-residue-sum-equivalence",
  ],
  tags: [
    "brane-tower",
    "habiro-ring",
    "cyclotomic-completion",
    "regularization",
    "quantum-dilogarithm",
    "open-problem",
    "scalar-nstar-refuted",
    "closure-2026-05-11",
  ],
});
