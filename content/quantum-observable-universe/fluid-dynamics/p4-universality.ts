import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:universality",
  lean: {
    decl: "QOU.FluidDynamics.universality",
    validation: "not_checked",
  },
  title:
    "Universality of the critical exponent: dependence on $\\chi(A)$ alone",
  uses: [
    "prop:critical-exponent",
    "prop:blowup-yekutieli",
    "prop:euler-char-stability",
    "def:recursive-brane-tower",
    "conj:regularity-breakdown",
  ],
  tags: [
    "universality",
    "critical-exponent",
    "euler-characteristic",
    "phase-transition",
    "renormalization",
  ],
});
