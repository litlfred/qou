import { proof } from "../../schema/builders";

export default proof({
  label: "prf:quantum-observable-universe-exists",
  title: "Proof of existence of quantum observable universes",
  uses: [
    "prop:quantum-observable-universe-exists",
    "lem:qou-exists-axiom-1",
    "lem:qou-exists-axiom-2",
    "lem:qou-exists-axiom-3",
    "lem:qou-exists-axiom-4",
  ],
  cites: [
    "woronowicz1987",
    "woronowicz1988",
    "reshetikhin1991",
    "kassel1995",
    "chari1994guide",
  ],
});
