import { example } from "../../schema/builders";

export default example({
  interprets: "def:quantum-universe",
  label: "ex:quantum-universe-su2",
  title: "$\\mathrm{SU}(2)$ as a quantum universe",
  lean: { ref: "qou:QOU.Examples.su2QuantumUniverse", validation: "not_checked" },
  tags: ["su2", "quantum"],
  uses: [
    "def:frobenius-pairing",
    "ex:rigid-monoidal-vect",
  ],
});
