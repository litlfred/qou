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
    "prop:mass-endomorphism-tower",
    "rem:mass-endomorphism-jet-tower",
    "prop:graded-trace-residue-split",
    "prop:wedderburn-weight-canonical",
    "prop:schur-weyl-mass-decomposition",
    "prop:jet-tower-convergence",
    "prop:pentagon-uv-commutation",
    "lem:vhat-pair-commutation-trace",
    "prop:descent-eigenspaces",
    "prop:descended-level-zero",
    "thm:jones-markov-trace",
    "thm:markov-trace-factorization",
    "rem:markov-moves-brane-tower",
    "prop:pieri-photon-shift",
    "conj:archimedean-remainder-exponential-decay",
  ],
  cites: ["jones1985", "wenzl1988", "kassel1995"],
  lean: { ref: "qou:QOU.BraidKnot.perBraidMassTower" },
});
