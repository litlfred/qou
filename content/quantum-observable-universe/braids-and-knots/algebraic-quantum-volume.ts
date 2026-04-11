import { definition } from "../../schema/builders";

export default definition({
  label: "def:algebraic-quantum-volume",
  title: "Algebraic quantum volume $\\mathrm{Vol}_q(K)$",
  uses: [
    "thm:markov-trace-product",
    "def:vertex-operator",
    "thm:wedderburn-mass-formula",
  ],
});
