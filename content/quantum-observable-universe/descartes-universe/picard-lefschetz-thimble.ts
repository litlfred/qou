import { definition } from "../../schema/builders";

export default definition({
  label: "def:picard-lefschetz-thimble",
  title: "Picard--Lefschetz thimble decomposition of the color-tube cubic",
  lean: {
    ref: "qou:QOU.Descartes.ThimbleData",
    validation: "not_checked",
  },
  tags: [
    "picard-lefschetz",
    "thimble",
    "steepest-descent",
    "color-tube",
    "discriminant",
    "seiberg-witten",
    "baryon-mass",
  ],
  uses: [
    "rem:lepton-mass-integrals",
    "prop:descartes-elliptic-curve",
  ],
});
