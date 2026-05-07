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
  ],
  computation: {
    engine: "python",
    script: "folio-assistant/computations/probe_phiq_uniform_k.py",
    witness: "folio-assistant/computations/probe-phiq-uniform-k.witness.json",
    status: "experimental",
  },
});
