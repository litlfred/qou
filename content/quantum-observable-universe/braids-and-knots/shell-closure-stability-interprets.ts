import { remark } from "../../schema/builders";

export default remark({
  label: "rem:shell-closure-stability-interprets",
  title:
    "Physical interpretation of shell-closure stability: periodicity, inertness, ionisation peaks",
  tags: [
    "noble-gas",
    "periodic-table",
    "ionisation-energy",
    "chemical-inertness",
    "valence",
    "magic-numbers",
  ],
  uses: [
    "prop:shell-closure-stability",
    "def:dressed-particle",
    "def:electron-shell",
  ],
  interprets: "prop:shell-closure-stability",
});
