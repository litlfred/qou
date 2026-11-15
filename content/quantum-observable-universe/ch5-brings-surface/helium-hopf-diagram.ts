import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:stable-nucleus",
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
  uses: ["conj:electron-shells-hopf"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/helium-hopf-diagram-0.svg", blockIndex: 0, hash: "a270d88da756" },
    { mime: "image/svg+xml", url: "rendered/helium-hopf-diagram-1.svg", blockIndex: 1, hash: "a91ebcaaed3f" },
  ],

});
