import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:stable-nucleus",
  label: "rem:knot-atom-diagrams",
  title:
    "Knot diagrams of light atoms ($p \\leq 4$)",
  tags: [
    "knot-diagram",
    "trefoil",
    "hopf-link",
    "electron-shell",
    "sub-link",
    "atom",
  ],
  uses: [
    "conj:electron-shells-hopf",
    "rem:helium-hopf-diagram",
    "def:stable-nucleus",
    "sec:knot-notation-convention",
  ],
});
