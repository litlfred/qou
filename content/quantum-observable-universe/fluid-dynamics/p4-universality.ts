import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:universality",
  title:
    "Universality of the critical exponent: dependence on $\\chi(A)$ alone",
  uses: [
    "conj:critical-exponent",
    "conj:blowup-yekutieli",
  ],
  tags: [
    "universality",
    "critical-exponent",
    "euler-characteristic",
    "phase-transition",
    "renormalization",
  ],
});
