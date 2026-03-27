import { remark } from "../../schema/builders";

export default remark({
  label: "rem:electron-immortality",
  title: "Electrons are immortal: no beta decay for elementary trefoils",
  interprets: "prop:antiparticle-crossing-reversal",
  uses: [
    "rem:time-reversal-energy-barrier",
    "rem:cosmological-chirality-flip",
    "rem:reidemeister-mass-invariance",
    "rem:chirality-trefoil-electron-positron",
    "rem:cmb-q-torsion",
    "def:borromean-baryon",
  ],
  tags: [
    "electron", "stability", "immortality", "beta-decay",
    "radiation", "CMB", "aeon", "trefoil",
  ],
});
