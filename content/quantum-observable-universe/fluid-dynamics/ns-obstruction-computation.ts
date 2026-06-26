import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "While calculating local Euler classes via excision ($H^2_{\\{p\\}}$) and asserting Biot-Savart jet divergence are standard in differential topology and fluid mechanics respectively, the mathematical novelty is explicitly combining them to show that analytic and topological terms live in complementary subgroups of the Yekutieli obstruction tower. This proves that classical divergence bounds cannot be \"cancelled out\" by topological adjustments in the background manifold, guaranteeing the persistence of the obstruction across all jet levels." },
  ],
  label: "prop:ns-obstruction-computation",
  lean: { ref: "qou:QOU.FluidDynamics.ns_obstruction_computation", validation: "not_checked" },
  title:
    "Computation of the NS obstruction for the Descartes universe",
  uses: [
    "prop:ns-obstruction-tower",
    // conj:levi-degeneracy removed (2026-06-08 §3b): the Euler-class / jet-divergence
    // computation is unconditional; Levi-degeneracy is the scenario it illustrates.
    "rem:body-asymptotics-catalog",
  ],
  tags: [
    "computation",
    "obstruction",
    "descartes",
    "euler-characteristic",
    "brings-surface",
  ],
});
