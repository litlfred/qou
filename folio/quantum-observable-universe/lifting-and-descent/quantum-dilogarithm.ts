import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:quantum-dilogarithm",
  lean: { ref: "qou:QOU.Torsion.quantum_dilogarithm",
    validation: "not_checked",
  },
  title: "Quantum Dilogarithm as Localized Torsion Volume",
  proofs: ["prf:quantum-dilogarithm"],
  tags: ["quantum-dilogarithm", "torsion-volume", "reeb-flow", "archimedean"],
  uses: ["conj:topological-mass", "def:briggs-klein-chart"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/quantum-dilogarithm-0.svg", blockIndex: 0, hash: "9dfe6018a432" },
  ],

});
