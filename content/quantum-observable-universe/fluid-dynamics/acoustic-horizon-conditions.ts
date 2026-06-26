import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "While the underlying construction of an acoustic metric and its associated Unruh/Hawking temperature is standard in analogue gravity, the mathematical novelty here is instantiating this framework natively over the $q$-deformed categorical substrate. The acoustic horizon conditions, rather than being ad-hoc physical analogies, become exact geometric constraints on the $q$-Navier-Stokes fluid, where the Hawking temperature is rigorously suppressed by the specific cyclotomic factor $\\hbar_q = (q-1)/q$." },
  ],
  label: "prop:acoustic-horizon-conditions",
  lean: { ref: "qou:QOU.FluidDynamics.acoustic_horizon_conditions", validation: "not_checked" },
  title: "Acoustic horizon formation and gravitational emergence",
  uses: ["def:q-navier-stokes"],
  tags: ["acoustic-metric", "horizon", "analogue-gravity", "black-hole", "hawking"],
});
