import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:stable-nucleus",
  label: "rem:knot-atom-diagrams",
  title:
    "Knot diagrams of light atoms ($Z \\leq 4$)",
  tags: [
    "knot-diagram",
    "trefoil",
    "hopf-link",
    "electron-shell",
    "sub-link",
    "atom",
    "transfer-matrix",
    "antineutrino",
    "borromean",
  ],
  uses: ["prop:shell-structure-eigenvalues"],
});
