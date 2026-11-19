import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:ns-counterexample",
  lean: { ref: "qou:QOU.FluidDynamics.NSCounterexample" },
  title:
    "Counter-example to Navier--Stokes regularity via $q \\to 1$ degeneration",
  uses: [
    "prop:universality",
    "prop:acoustic-horizon-conditions",
  ],
  tags: [
    "counter-example",
    "millennium-problem",
    "navier-stokes",
    "blowup",
    "yekutieli",
    "homological",
    "vortex-collision",
  ],
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
  ],
});
