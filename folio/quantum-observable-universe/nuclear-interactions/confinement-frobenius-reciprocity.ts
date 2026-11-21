import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:confinement-frobenius-reciprocity",
  renamedFrom: ["prop:confinement-frobenius-reciprocity"],
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
      kind: "status",
      date: "2026-11-21",
      body:
        "**Demoted from a proposition after an attempt to prove it** (owner: \"Demote both\", then \"Try and prove\", then \"1 2\", thread \"N2 Lean foundations\"). The Lean previously returned six fields of a context record that held the conclusions, the self-assuming projection of AGENTS.md §3b-cond item 5. `QOU.ParticleInteractions.confinement_frobenius_reciprocity` now derives the master formula, the active-set characterisation and nonemptiness, sorry-free, from linearity, symmetry of $G^{-1}$ and stationarity ($x^* = G^{-1}u^*$ on the active set, zero off it). Stationarity is the open hypothesis: it is the optimality condition of a quadratic program, not of the operator-selection LP, whose optimality conditions are feasibility and complementary slackness.",
    },
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
