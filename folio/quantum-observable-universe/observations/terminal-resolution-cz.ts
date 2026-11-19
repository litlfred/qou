import { example } from "../../schema/builders";

export default example({
  interprets: "prop:terminal-resolution",
  label: "ex:terminal-resolution-cz",
  title: "Terminal resolution in $\\mathbb{C}[z]$",
  lean: { ref: "qou:QOU.Examples.czTerminalResolution", validation: "not_checked" },
  uses: ["prop:local-substrate-q"],
  tags: ["archimedean", "mass", "polynomial"],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
});
