import { example } from "../../schema/builders";

export default example({
  interprets: "prop:terminal-resolution",
  label: "ex:terminal-resolution-cz",
  title: "Terminal resolution in $\\mathbb{C}[z]$",
  lean: { decl: "QOU.Examples.czTerminalResolution" },
  uses: [
    "prop:terminal-resolution",
    "ex:c-quantum-observable-universe",
    "prop:topological-mass-formula",
    "def:substrate-parameter",
    "def:quantum-planck-constant",
    "prop:local-substrate-q",
  ],
  tags: ["archimedean", "mass", "polynomial"],
});
