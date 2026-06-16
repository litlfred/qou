import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confinement-frobenius-reciprocity",
  lean: { ref: "qou:QOU.ParticleInteractions.confinement_frobenius_reciprocity", validation: "not_checked" },
  title:
    "Confinement Frobenius reciprocity: bound-state observables as $G^{-1}$-weighted dual pairings",
  tags: [
    "frobenius-pairing",
    "frobenius-dual",
    "gram-matrix",
    "lp-duality",
    "shadow-price",
    "operator-selection",
    "bound-state",
    "reciprocity",
    "categorical-binding",
  ],
  cites: ["yekutieli2015", "kassel1995"],
  computation: {
    engine: "numpy",
    script: "computations/borromean-axial-coupling.py",
    witness: "computations/borromean-axial-coupling.witness.json",
    status: "verified",
  },
});
