import { remark } from "../../schema/builders";

export default remark({
  label: "rem:alpha-em-derivation-exploration-options",
  title:
    "Exploration map: GB/spectral-sequence/Hopf infrastructure for closing $1/\\alpha_{EM}$ derivation",
  interprets: "conj:em-coupling-bring-zero-mode",
  uses: [
    "conj:em-coupling-bring-zero-mode",
    "prop:reeb-bundle",
    "prop:q-chromaticity",
    "prop:spectral-sequence-collapse",
    "prop:gb-spectral-sequence",
    "prop:curvature-rank-gb-stratification",
    "prop:unified-curvature-rank-mass-formula",
    "prop:y-lambda-closed-form-wenzl-bridge",
    "prop:force-carrier-bring-uniqueness",
    "def:exceptional-divisor",
    "def:confinement-level",
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
