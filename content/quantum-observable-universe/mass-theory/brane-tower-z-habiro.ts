import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:brane-tower-z-habiro",
  title: "Brane tower lives in the $z$-Habiro ring",
  uses: [
    "def:z-habiro-ring",
    "def:habiro-ring",
    "def:algebraic-quantum-volume",
    "cor:quantum-dilogarithm",
    "prop:atom-knot-mass-derivation",
    "thm:topological-mass",
    "cor:habiro-expansion-atomic",
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
