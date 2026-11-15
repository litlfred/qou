import { proposition } from "../../schema/builders";

export default proposition({
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
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "Re-scoped 2026-11-15 (owner decision, PR #7747, bean qou-lx8f): the previous text read: \"(governed by the perpetual obstruction mechanism, [QU-to-QOU](#thm:qu-to-qou) item 3).\"",
    },
  ],
});
