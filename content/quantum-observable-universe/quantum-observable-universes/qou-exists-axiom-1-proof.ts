import { proof } from "../../schema/builders";

export default proof({
  label: "prf:qou-exists-axiom-1",
  title: "Proof of axiom 1 (Frobenius pairing) for QOU existence",
  uses: ["lem:qou-exists-axiom-1"],
  cites: ["woronowicz1987"],
});
