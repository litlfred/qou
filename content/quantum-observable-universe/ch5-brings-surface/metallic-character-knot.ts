import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:metallic-character-knot",
  title:
    "Metallic character from incomplete sub-Hopf links",
  tags: [
    "metal",
    "metallic-bonding",
    "electron-shell",
    "hopf-link",
    "sub-link",
    "trefoil",
    "delocalization",
    "conductivity",
    "incomplete-shell",
  ],
  uses: [
    "conj:electron-shells-hopf",
    "prop:noble-gas-characterization",
    "def:electron-knot",
    "def:crossing-energy",
    "def:stable-nucleus",
    "prop:torus-hopf-stability",
  ],
});
