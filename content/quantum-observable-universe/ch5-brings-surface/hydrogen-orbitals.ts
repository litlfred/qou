import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:hydrogen-shell-writhe",
  label: "rem:hydrogen-orbitals",
  title:
    "Hydrogen orbitals: the spinning trefoil around the Borromean anchor",
  tags: [
    "hydrogen",
    "orbital",
    "shell",
    "subshell",
    "trefoil",
    "writhe",
    "borromean",
    "electron-cloud",
  ],
  uses: [
    "ex:hydrogen-knot-structure",
    "prop:hydrogen-shell-writhe",
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/hydrogen-orbitals-0.svg", blockIndex: 0, hash: "83220f72f696" },
  ],

});
