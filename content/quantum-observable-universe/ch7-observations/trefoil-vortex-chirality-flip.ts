import { remark } from "../../schema/builders";

export default remark({
  label: "rem:trefoil-vortex-chirality-flip",
  title: "Can the chirality of a stable trefoil vortex flip?",
  uses: [
    "rem:chirality-trefoil-electron-positron",
    "rem:vortex-intensity-modes",
    "def:crossing-energy",
    "prop:fiber-adjoint-involution",
    "def:substrate-parameter",
    "rem:complex-substrate-interpretation",
    "conj:complex-chirality-rotation",
    "def:exceptional-divisor",
  ],
  tags: [
    "vortex", "chirality", "reconnection", "trefoil",
    "fluid-dynamics", "stability", "exceptional-divisor",
  ],
  cites: ["kleckner2013", "scheeler2014"],
});
