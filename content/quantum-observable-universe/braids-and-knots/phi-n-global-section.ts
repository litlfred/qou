import { remark } from "../../schema/builders";

export default remark({
  label: "rem:phi-n-global-section",
  title:
    "$\\Phi_n$ as a global section of the categorical mass endomorphism (locality dropped)",
  interprets: "conj:mass-endomorphism",
  uses: [
    "conj:mass-endomorphism",
    "conj:categorical-neutrality-saturated-shells",
  ],
  tags: [
    "global-section",
    "locality",
    "rigid-monoidal",
    "ribbon-operator",
    "topological-flux",
  ],
});
