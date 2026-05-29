import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:poincare-lefschetz-borromean",
  title:
    "Poincaré–Lefschetz duality on Borromean complement — cohomology ↔ homology of manifold-with-cusps",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.PoincareLefschetzBorromean",
    validation: "not_checked",
  },
  uses: [
    "def:borromean-baryon",
    "prop:borromean-bloch-group-element",
    "prop:reeb-bundle-complement-equals-volume",
    "rem:vol-as-motivic-period",
  ],
  cites: [
    "lefschetz1926",
    "neumann-zagier1985",
  ],
  tags: [
    "poincare-lefschetz",
    "duality-d21",
    "borromean-complement",
    "manifold-with-cusps",
    "cohomology-homology",
    "axiom-class",
    "open-problem",
    "non-scholarly-voice-exception",
  ],
});
