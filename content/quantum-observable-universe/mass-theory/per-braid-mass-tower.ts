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
});
