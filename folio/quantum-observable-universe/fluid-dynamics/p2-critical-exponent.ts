import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:critical-exponent",
  lean: { ref: "qou:QOU.FluidDynamics.CriticalExponent" },
  title: "Critical exponent of the enstrophy divergence at $q = 1$",
  uses: [
    "prop:q-ns-nonlinear-uniqueness",
    "conj:regularity-breakdown",
  ],
  tags: ["critical-exponent", "enstrophy", "phase-transition", "scaling"],
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
  ],
});
