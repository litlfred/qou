import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:skein-coulomb-enhancement",
  proofs: ["prf:skein-coulomb-enhancement"],
  title:
    "Coulomb enhancement from electron-proton Skein crossings",
  tags: [
    "coulomb",
    "fermi-function",
    "sommerfeld",
    "skein",
    "beta-decay",
    "half-life",
    "electron",
    "crossing",
  ],
  lean: { ref: "qou:QOU.Archimedean.skein_coulomb_enhancement",
    validation: "not_checked",
  },
});
