import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hook-weight-derivation",
  proofs: ["prf:hook-weight-derivation"],
  title:
    "Hook weight $\\beta_4 = -\\tfrac{1}{2} w_{[2,2]}(4)$ from baryon Wedderburn-Artin decomposition",
  lean: { ref: "qou:QOU.BaryonWeight.beta4_hook",
    validation: "not_checked",
  },
  uses: [
    "prop:degree-two-baryon-weight",
    "conj:shell-transition-knot",
  ],
});
