import { example } from "../../schema/builders";

export default example({
  label: "ex:terminal-resolution-cz",
  title: "Terminal resolution in $\\mathbb{C}[z]$",
  lean: { decl: "QOU.Examples.czTerminalResolution" },
  uses: [
    "rem:terminal-resolution",
    "ex:c-quantum-observable-universe",
    "conj:topological-mass-formula",
    "def:substrate-parameter",
    "def:quantum-planck-constant",
  ],
  tags: ["archimedean", "mass", "polynomial"],
});
