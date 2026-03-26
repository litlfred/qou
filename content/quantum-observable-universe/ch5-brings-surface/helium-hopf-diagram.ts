import { remark } from "../../schema/builders";

export default remark({
  label: "rem:helium-hopf-diagram",
  title:
    "Helium: two trefoils forming a closed Hopf link",
  tags: [
    "helium",
    "hopf-link",
    "trefoil",
    "electron-shell",
    "diagram",
  ],
  uses: [
    "conj:electron-shells-hopf",
    "def:stable-nucleus",
    "rem:knot-notation-convention",
  ],
});
