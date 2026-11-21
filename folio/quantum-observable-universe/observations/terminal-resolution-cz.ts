import { example } from "../../schema/builders";

export default example({
  interprets: "prop:terminal-resolution",
  label: "ex:terminal-resolution-cz",
  title: "Lepton mass ratios in $\\mathbb{C}[z]$",
  lean: { ref: "qou:QOU.Examples.czTerminalResolution", validation: "not_checked" },
  uses: ["prop:local-substrate-q", "def:three-calibration-discipline"],
  tags: ["archimedean", "mass", "polynomial"],
});
