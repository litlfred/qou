import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:per-braid-mass-tower",
  title:
    "Per-braid mass tower",
  tags: [
    "mass-tower",
    "per-braid",
    "sub-braid",
    "markov-trace",
    "schur-weyl",
    "JSJ",
    "phi-q",
    "wedderburn",
  ],
  uses: [
    "prop:pentagon-uv-commutation",
    "rem:markov-moves-brane-tower",
    "prop:pieri-photon-shift",
  ],
  cites: ["jones1985", "wenzl1988", "kassel1995"],
  computation: {
    engine: "python",
    script: "computations/per_braid_tower.py",
    witness: "docs/audits/2026-05-01-per-braid-tower.witness.json",
    status: "verified",
  },
  lean: { ref: "qou:QOU.BraidKnot.perBraidMassTower" },
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** The " +
        "`PerBraidMassTower` class types `trM`, `phiQ`, `mark_z` and `mass` " +
        "over `ℝ`. Two constructs force it and neither has a generic-`CommRing` " +
        "form: the absolute values $|\\mathrm{tr}_M(\\xi)|$ in every summand " +
        "(an order-theoretic operation) and the quantum dilogarithm $\\Phi_q$ " +
        "(transcendental). The tower is a " +
        "statement about evaluated MeV masses, so it sits on the archimedean " +
        "side of the wall by construction.",
    },
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "**Corrected: the third reason was convention C.** This note previously " +
        "listed a *third* construct forcing `ℝ` — the Markov weight " +
        "$z = 1/(q^{1/2} + q^{-1/2})$, \"a real square root\". That is the " +
        "excised convention C. Production is **convention D**, " +
        "$z = q^{3}/(q^{2}+1)$, which is a rational function of $q$ and needs " +
        "no square root: it does not leave $\\mathbb{Q}(q)$, let alone force " +
        "the archimedean side. " +
        "[`markov-trace-frobenius-selection-proof`](#prf:markov-trace-frobenius-selection) " +
        "already made exactly this correction for its own base ring (\"the older " +
        "$\\mathbb{Q}(q^{1/2})$ hypothesis was an artefact of convention C\"); " +
        "this note is the same correction, propagated. " +
        "The conclusion is unchanged — the class still needs `ℝ`, for two " +
        "reasons rather than three — so no Lean signature moves.",
    },
  ],
});
