import { example } from "../../schema/builders";

export default example({
  interprets: "def:quantum-universe",
  label: "ex:quantum-universe-su2",
  title: "$\\mathrm{SU}(2)$ as a quantum universe",
  lean: { decl: "QOU.Examples.su2QuantumUniverse" },
  tags: ["su2", "quantum"],
  uses: [
    "def:frobenius-pairing",
    "ex:rigid-monoidal-vect",
  ],
});
