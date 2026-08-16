import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:quantum-observable-universe-exists",
  title: "Existence of quantum observable universes",
  lean: { ref: "qou:QOU.QuantumObservableUniverse.exists_instance",
    validation: "not_checked",
  },
  uses: [
    "ex:qou-su2",
    "ex:c-quantum-observable-universe",
  ],
  proofs: ["prf:quantum-observable-universe-exists"],
  tags: [
    "existence",
    "quantum-observable-universe",
    "chern-class",
    "reshetikhin-turaev",
    "woronowicz",
  ],
  cites: [
    "woronowicz1987",
    "woronowicz1988",
    "reshetikhin1991",
    "kassel1995",
    "chari1994guide",
  ],
});
