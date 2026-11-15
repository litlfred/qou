import { example } from "../../schema/builders";

export default example({
  interprets: "prop:terminal-resolution",
  label: "ex:terminal-resolution-cz",
  title: "Terminal resolution in $\\mathbb{C}[z]$",
  lean: { ref: "qou:QOU.Examples.czTerminalResolution", validation: "not_checked" },
  uses: ["prop:local-substrate-q"],
  tags: ["archimedean", "mass", "polynomial"],
});
