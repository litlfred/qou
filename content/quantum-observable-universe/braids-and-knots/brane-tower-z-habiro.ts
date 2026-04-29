import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:brane-tower-z-habiro",
  title: "Brane tower lives in the $z$-Habiro ring",
  uses: [
    "def:z-habiro-ring",
    "def:habiro-ring",
    "def:algebraic-quantum-volume",
    "cor:quantum-dilogarithm",
    "prop:atom-knot-mass-derivation",
    "thm:topological-mass",
  ],
  tags: [
    "brane-tower",
    "habiro-ring",
    "cyclotomic-completion",
    "regularization",
    "quantum-dilogarithm",
    "open-problem",
  ],
});
