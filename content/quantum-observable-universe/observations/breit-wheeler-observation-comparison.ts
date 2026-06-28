import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:pair-creation-energy",
  label: "rem:breit-wheeler-observation-comparison",
  title: "Breit--Wheeler process: comparison with STAR and ATLAS observation",
  uses: [
    "rem:pair-creation-energy",
    "rem:breit-wheeler-observation",
  ],
  tags: [
    "breit-wheeler", "pair-creation", "STAR", "ATLAS",
    "cos2phi", "azimuthal-asymmetry", "observation",
  ],
  cites: ["star2021bw", "atlas2021bw"],
});
