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
    "scalar-nstar-refuted",
    "closure-2026-05-11",
  ],
  computation: {
    engine: "python",
    script: "folio-assistant/computations/probe_phiq_uniform_k.py",
    witness: [
      "folio-assistant/computations/probe-phiq-uniform-k.witness.json",
      "folio-assistant/computations/probe-phiq-n-star-rule.witness.json",
      "folio-assistant/computations/probe-phiq-operator-valued.witness.json",
      "folio-assistant/computations/probe-phiq-multiplicity-refined.witness.json",
      "folio-assistant/computations/probe-phiq-avg-chi-over-classical-dim.witness.json",
    ],
    status: "verified",
  },
});
