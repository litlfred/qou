import { remark } from "../../schema/builders";

export default remark({
  label: "rem:chirality-trefoil-electron-positron",
  title:
    "Left and right trefoils: electron and positron",
  tags: [
    "trefoil",
    "chirality",
    "electron",
    "positron",
    "antiparticle",
    "time-reversal",
    "exceptional-divisor",
  ],
  uses: [
    "rem:knot-notation-convention",
    "def:crossing-energy",
    "conj:electron-shells-hopf",
    "prop:fiber-adjoint-involution",
  ],
});
