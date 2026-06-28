import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:em-coupling-projection",
  label: "rem:em-coupling-projection-discussion",
  title: "Spectral characterisation, the Chern--Simons correction, and the open bare residual",
  uses: [
    "prop:em-coupling-projection",
    "thm:em-spectral-completeness",
    "prop:force-carrier-bring-uniqueness",
    "conj:em-coupling-chern-simons",
    "rem:alpha-em-derivation-open-problems",
    "prop:em-coupling-bring-zero-mode",
  ],
});
