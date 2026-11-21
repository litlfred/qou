import { example } from "../../schema/builders";

export default example({
  label: "ex:terminal-resolution-cz",
  title: "Lepton mass ratios in $\\mathbb{C}[z]$",
  lean: { ref: "qou:QOU.Examples.czTerminalResolution", validation: "not_checked" },
  uses: ["def:three-calibration-discipline"],
  tags: ["archimedean", "mass", "polynomial"],
});
