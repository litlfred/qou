import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:ns-obstruction-computation",
  lean: { ref: "qou:QOU.FluidDynamics.ns_obstruction_computation", validation: "not_started" },
  title:
    "Computation of the NS obstruction for the Descartes universe",
  uses: [
    "prop:ns-obstruction-tower",
    "conj:levi-degeneracy",
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
