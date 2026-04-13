import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:knot-operator-basis-table",
  label: "rem:polarization-writhe-tracking",
  title:
    "Polarization, writhe, and the Hecke relation as writhe reduction",
  tags: [
    "photon",
    "writhe",
    "polarization",
    "hecke-algebra",
    "reidemeister",
    "normal-form",
  ],
  uses: [
    "rem:knot-operator-basis-table",
    "rem:trivial-knot-photon-interpretation",
    "prop:reidemeister-mass-invariance",
  ],
});
