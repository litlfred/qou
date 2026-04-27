import { remark } from "../../schema/builders";

export default remark({
  label: "rem:breit-wheeler-observation",
  title: "Breit--Wheeler process: first direct observation and QOU prediction",
  interprets: "rem:pair-creation-energy",
  uses: [
    "rem:breit-wheeler-vertex",
    "rem:pair-creation-energy",
    "prop:crossing-energy-decomposition",
  ],
  tags: [
    "breit-wheeler", "pair-creation", "polarisation",
    "STAR", "ATLAS", "testable", "first-testable",
    "cos2phi", "azimuthal-asymmetry",
  ],
  cites: ["star2021bw", "atlas2021bw"],
});
