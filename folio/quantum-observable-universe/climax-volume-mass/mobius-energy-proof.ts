import { proof } from "../../schema/builders";

export default proof({
  label: "prf:mobius-energy",
  title: "Proof of Categorical recovery of Möbius energy",
  uses: [
    "prop:mobius-energy",
    "lem:mobius-energy-frobenius-kernel",
  ],
  lean: { ref: "qou:QOU.MassTheory.MobiusEnergy",
    validation: "not_checked",
  },
});
