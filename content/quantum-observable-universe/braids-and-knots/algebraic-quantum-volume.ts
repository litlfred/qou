import { definition } from "../../schema/builders";

export default definition({
  label: "def:algebraic-quantum-volume",
  title: "Algebraic quantum volume $\\mathrm{Vol}_q(K)$",
  lean: {
    decl: "QOU.BraidKnot.AlgebraicQuantumVolume",
    validation: "not_checked",
  },
  uses: [
    "thm:markov-trace-product",
    "def:vertex-operator",
    "thm:wedderburn-mass-formula",
  ],
});
