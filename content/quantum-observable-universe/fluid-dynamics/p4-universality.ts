import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:universality",
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
});
