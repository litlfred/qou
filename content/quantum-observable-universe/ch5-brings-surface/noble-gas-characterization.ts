import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:noble-gas-characterization",
  title:
    "Noble gas characterization: full shell as full curls",
  tags: [
    "noble-gas",
    "electron-shell",
    "hopf-link",
    "sub-link",
    "trefoil",
    "closed-shell",
    "curl",
    "helium",
    "neon",
    "argon",
  ],
  uses: [
    "conj:electron-shells-hopf",
    "rem:helium-hopf-diagram",
    "def:electron-knot",
    "def:stable-nucleus",
    "def:crossing-energy",
    "prop:torus-hopf-stability",
  ],
});
