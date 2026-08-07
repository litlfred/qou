import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:per-braid-mass-tower",
  title:
    "Per-braid mass tower: $\\mathfrak{m} = |\\mathrm{tr}_M(W)| + \\sum_{\\xi \\in \\mathcal{S}_1}\\Phi_q(|\\mathrm{tr}_M(\\xi)|) + z^2 \\sum_{(\\xi,\\xi') \\in \\mathcal{S}_2}\\Phi_q(|\\mathrm{tr}_M(\\xi\\xi')|)$",
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
        "over `ℝ`. Three constructs force it and none has a generic-`CommRing` " +
        "form: the absolute values $|\\mathrm{tr}_M(\\xi)|$ in every summand " +
        "(an order-theoretic operation), the quantum dilogarithm $\\Phi_q$ " +
        "(transcendental), and the Markov weight " +
        "$z = 1/(q^{1/2} + q^{-1/2})$ (a real square root). The tower is a " +
        "statement about evaluated MeV masses, so it sits on the archimedean " +
        "side of the wall by construction.",
    },
  ],
});
