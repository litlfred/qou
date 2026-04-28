import { definition } from "../../schema/builders";

export default definition({
  label: "def:motivic-mass-measure",
  title: "Motivic mass measure $\\mu$ on the brane arc space",
  tags: ["motivic", "mass", "lefschetz", "grobner-shirshov", "arc-space"],
  uses: [
    "def:arc-space",
    "thm:wedderburn-mass-formula",
  ],
  cites: ["kontsevich1995", "denef-loeser2001"],
  lean: {
    ref: "qou:QOU.BraidsKnots.MotivicMassMeasure",
    validation: "not_checked",
  },
});
