import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:quantum-dilogarithm",
  lean: { ref: "qou:QOU.Torsion.quantum_dilogarithm",
    validation: "not_checked",
  },
  title: "Quantum Dilogarithm as Localized Torsion Volume",
  proofs: ["prf:quantum-dilogarithm"],
  tags: ["quantum-dilogarithm", "torsion-volume", "reeb-flow", "archimedean"],
  // The statement identifies one term, the transient trace tr_trans(ϱ, p_i),
  // and needs only its definition. That definition is stated in
  // prop:topological-mass-upper-bound. The open equality
  // conj:topological-mass (mass = sum of the term norms) is not used:
  // the proof evaluates a single term and never sums the terms.
  uses: ["prop:topological-mass-upper-bound", "def:briggs-klein-chart"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/quantum-dilogarithm-0.svg", blockIndex: 0, hash: "9dfe6018a432" },
  ],

});
