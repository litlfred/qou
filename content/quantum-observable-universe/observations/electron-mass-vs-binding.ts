import { remark } from "../../schema/builders";

export default remark({
  label: "rem:electron-mass-vs-binding",
  title:
    "Electrons enter atomic mass via $Z m_e$ linearly; not as strands in $B(Z,N)$",
  interprets: "prop:tower-binding-energy",
  uses: [
    "prop:tower-binding-energy",
    "def:electron-knot",
  ],
  tags: [
    "electron",
    "binding-energy",
    "mass-formula",
    "framework-clarification",
  ],
});
