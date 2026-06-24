import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:degree-two-baryon-weight",
  title: "Degree-2 weight $\\beta_2 = -2[3]_q$ from baryon quantum number",
  lean: { ref: "qou:QOU.BaryonWeight.beta2_approx",
    validation: "not_checked",
  },
  uses: ["thm:wedderburn-mass-formula"],
  proofs: ["prf:degree-two-baryon-weight"],
});
