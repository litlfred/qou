import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:quantum-dilogarithm",
  title: "Quantum Dilogarithm as Localized Torsion Volume",
  hasProof: false,
  tags: ["quantum-dilogarithm", "torsion-volume", "reeb-flow"],
  uses: ["thm:topological-mass"],
});
