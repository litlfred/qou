import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:skein-coulomb-enhancement",
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
  lean: {
    decl: "QOU.Descartes.skein_coulomb_enhancement",
    validation: "not_checked",
  },
  uses: [
    "prop:hadron-half-life",
    "def:skein-binding-lagrangian",
    "rem:skein-crossing-asymmetry",
    "def:hadron",
    "def:substrate-parameter",
    "def:electron-knot",
  ],
});
