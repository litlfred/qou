import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confinement-frobenius-reciprocity",
  lean: { ref: "qou:QOU.ParticleInteractions.confinement_frobenius_reciprocity", validation: "not_started" },
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
  uses: [
    "prop:frobenius-gram-matrix",
    "prop:operator-selection-lp",
    "prop:mass-coefficient-shadow-price",
    "prop:confinement-operator-selection",
    "conj:knot-factor-frobenius-pairing",
  ],
  cites: ["yekutieli2015", "kassel1995"],
  computation: {
    engine: "numpy",
    script: "folio-assistant/computations/borromean-axial-coupling.py",
    witness: "folio-assistant/computations/borromean-axial-coupling.witness.json",
    status: "verified",
  },
});
