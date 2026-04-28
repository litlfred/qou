import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:trefoil-volume-electronic-scale",
  title:
    "Trefoil-Alexander electronic-scale cross-check of $\\lvert q + q^{-1}\\rvert_{\\mathrm{mol}}$",
  tags: [
    "trefoil",
    "alexander-polynomial",
    "electronic-scale",
    "high-precision",
    "cross-check",
    "verification",
  ],
  lean: { ref: "qou:QOU.Organic.trefoilVolumeElectronicScale",
    validation: "not_checked",
  },
  uses: [
    "prop:molecular-crossing-quantum",
    "lem:alexander-T2N-closed-form",
  ],
  cites: [],
});
