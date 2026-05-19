import { remark } from "../../schema/builders";

export default remark({
  label: "rem:picard-lefschetz-thimble",
  title: "Picard--Lefschetz thimbles: archimedean shadow of the algebraic residue",
  interprets: "prop:sw-period-thimble-equivalence",
  lean: {
    ref: "qou:QOU.Descartes.ThimbleData",
    validation: "not_checked",
  },
  tags: [
    "picard-lefschetz",
    "thimble",
    "archimedean-shadow",
    "exposition",
    "color-tube",
    "seiberg-witten",
  ],
  uses: [
    "rem:lepton-mass-integrals",
    "prop:descartes-elliptic-curve",
    "prop:sw-period-thimble-equivalence",
  ],
  cites: ["pham1965", "seidel2008", "witten2011"],
  computation: {
    engine: "scipy",
    script: "folio-assistant/computations/picard_lefschetz_thimble.py",
    witness: "folio-assistant/computations/picard-lefschetz-thimble.witness.json",
    status: "verified",
    requires: ["numpy", "scipy"],
  },
});
