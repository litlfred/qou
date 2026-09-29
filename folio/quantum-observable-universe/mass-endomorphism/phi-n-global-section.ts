import { remark } from "../../schema/builders";

export default remark({
  label: "rem:phi-n-global-section",
  title:
    "$\\Phi_n$ as the global section of the categorical mass functor",
  interprets: "conj:mass-endomorphism",
  uses: ["prop:categorical-neutrality-saturated-shells"],
  tags: [
    "categorical-mass",
    "global-section",
    "ribbon-flux",
    "framing",
    "interpretation",
  ],
});
