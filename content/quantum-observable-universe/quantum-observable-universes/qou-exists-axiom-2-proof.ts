import { proof } from "../../schema/builders";

export default proof({
  label: "prf:qou-exists-axiom-2",
  title: "Proof of axiom 2 (observability) for QOU existence",
  uses: ["lem:qou-exists-axiom-2"],
  cites: ["woronowicz1988"],
});
