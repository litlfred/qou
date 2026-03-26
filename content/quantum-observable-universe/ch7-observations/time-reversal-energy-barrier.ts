import { remark } from "../../schema/builders";

export default remark({
  label: "rem:time-reversal-energy-barrier",
  title: "Time reversal requires infinite energy in the observable sector",
  uses: [
    "rem:pair-creation-energy",
    "rem:trefoil-vortex-chirality-flip",
    "rem:chirality-trefoil-electron-positron",
    "def:crossing-energy",
    "def:substrate-parameter",
    "rem:positron-knot",
    "def:borromean-baryon",
    "prop:torus-hopf-stability",
  ],
  tags: [
    "time-reversal", "energy-barrier", "topological-protection",
    "electron", "proton", "neutron", "feynman-stueckelberg",
  ],
});
