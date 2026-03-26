import { example } from "../../schema/builders";

export default example({
  label: "ex:nitrogen-14-threading",
  title: "Nitrogen-14: $\\mathcal{N}(7,7)$ vs $\\mathcal{N}(6,8)$ via threading",
  tags: [
    "nitrogen-14",
    "carbon-14",
    "threading-link",
    "braid-shortcut",
    "beta-stability",
    "crossing-asymmetry",
  ],
  uses: [
    "def:nuclear-threading-link",
    "def:stable-nucleus",
    "def:crossing-energy",
    "rem:skein-crossing-asymmetry",
    "def:skein-binding-lagrangian",
    "conj:skein-shell-correction",
  ],
});
