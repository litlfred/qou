import { proof } from "../../schema/builders";

export default proof({
  label: "prf:mobius-energy",
  title: "Proof of Categorical recovery of Möbius energy",
  uses: ["prop:mobius-energy", "def:frobenius-pairing"],
  lean: {
    decl: "QOU.MobiusEnergy",
    validation: "not_checked",
  },
});
