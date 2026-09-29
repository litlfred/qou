import { remark } from "../../schema/builders";

export default remark({
  label: "rem:chirality-trefoil-electron-positron",
  title:
    "Left and right trefoils: electron and positron",
  interprets: "prop:antiparticle-crossing-reversal",
  tags: [
    "trefoil",
    "chirality",
    "electron",
    "positron",
    "antiparticle",
    "time-reversal",
    "exceptional-divisor",
  ],
  uses: ["prop:antiparticle-crossing-reversal"],
});
