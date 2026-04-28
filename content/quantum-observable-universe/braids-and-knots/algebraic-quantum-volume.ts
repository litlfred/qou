import { definition } from "../../schema/builders";

export default definition({
  label: "def:algebraic-quantum-volume",
  title: "Algebraic quantum volume $\\mathrm{Vol}_q(K)$",
  lean: {
    ref: "qou:QOU.BraidKnot.AlgebraicQuantumVolume",
    validation: "not_checked",
  },
  uses: ["thm:wedderburn-mass-formula"],
});
