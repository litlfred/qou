import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:meson-qcg-fusion-identity",
  title:
    "q-Clebsch–Gordan fusion identity $[3]_q\\cdot[4]_q = [2]_q + [4]_q + [6]_q$",
  lean: {
    ref: "qou:QOU.BraidKnot.meson_qCG_3x4",
  },
  uses: [],
  cites: [
    "kassel1995",
    "jones1987",
  ],
  tags: [
    "hecke-algebra",
    "clebsch-gordan",
    "meson",
    "fusion-product",
    "categorical-derivation",
  ],
});
