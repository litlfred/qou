import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:degree-two-baryon-weight",
  title: "Degree-2 weight $\\beta_2 = -2[3]_q$ from baryon quantum number",
  uses: [
    "thm:wedderburn-mass-formula",
    "prop:three-parameters-wedderburn",
    "def:color-tube-coordinates",
  ],
});
