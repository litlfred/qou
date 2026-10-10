import { remark } from "../../schema/builders";

export default remark({
  label: "rem:alpha-em-derivation-exploration-options",
  title:
    "Exploration map: GB/spectral-sequence/Hopf infrastructure for closing $1/\\alpha_{EM}$ derivation",
  interprets: "prop:em-coupling-bring-zero-mode",
  uses: [
    "prop:em-coupling-bring-zero-mode",
    "prop:y-lambda-closed-form-wenzl-bridge",
  ],
  tags: [
    "alpha-em",
    "fine-structure",
    "exploration",
    "open-problem",
    "derivation-roadmap",
    "spectral-sequence",
    "gb-filtration",
    "hopf-fibration",
  ],
});
