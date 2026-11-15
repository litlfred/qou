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
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The reciprocity statement carries ordering hypotheses on the " +
        "confinement gap (`0 < …`) over `ℝ`. The Frobenius pairing itself " +
        "is algebraic, but the positivity that makes it a *confinement* " +
        "statement is an archimedean condition and is stated post-wall.",
    },
  ],
});
