import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:wenzl-bridge-applicability-qou",
  proofs: ["prf:wenzl-bridge-applicability-qou"],
  title:
    "Applicability of the Wenzl-bridge $y_\\lambda$ formula in QOU: Schur--Weyl + 1-dim trace space",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.wenzl_bridge_applicability_qou",
    validation: "not_checked",
  },
  uses: ["prop:y-lambda-closed-form-wenzl-bridge"],
  cites: ["chlouveraki2016", "wenzl1988", "juyumaya2004"],
  tags: [
    "wenzl-bridge",
    "applicability",
    "schur-weyl-duality",
    "tannaka-krein",
    "markov-trace",
    "uniqueness",
    "qou-axioms",
  ],
});
