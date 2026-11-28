import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:universality",
  lean: { ref: "qou:QOU.FluidDynamics.p4_universality", validation: "not_checked" },
  title:
    "Universality of the critical exponent: dependence on $\\chi(A)$ alone",
  uses: [
    "conj:critical-exponent",
    "prop:blowup-yekutieli",
  ],
  tags: [
    "universality",
    "critical-exponent",
    "euler-characteristic",
    "phase-transition",
    "renormalization",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-28",
      body:
        "Relabelled from proposition to conjecture (owner Lean ruling 2026-11-28: only Lean with a human semantic equivalent counts as proved). The Lean derives the conclusion from a class field asserting it (alpha factors through the invariants), so nothing is proved. Content kept as a documented open item; label renamed from prop: to conj:.",
    },
  ],
});
