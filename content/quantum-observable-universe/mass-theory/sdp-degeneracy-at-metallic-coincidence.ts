import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:operator-selection-lp",
  label: "rem:sdp-degeneracy-at-metallic-coincidence",
  title:
    "SDP degeneracy at cost-coincidence detects the metallic-ratio ladder",
  tags: [
    "metallic-ratio",
    "lp-degeneracy",
    "sdp-strict-complementarity",
    "active-set",
    "color-flavor-locking",
    "cfl-transition",
    "lean-proved",
  ],
  uses: [
    "prop:operator-selection-lp",
    "prop:confinement-sdp",
    "conj:color-superconductivity-borromean",
  ],
  cites: [],
  authorNotes: [
    {
      kind: "note",
      date: "2026-06-09",
      body:
        "Surfaced by the metallic-q probe series on PR #2047.  Lean " +
        "proof of the silver case is sorry-free in " +
        "`QOU.AlgebraicSubstrate.MetallicLPIdentities.silver_lp_coincidence`. " +
        "The §3b-cond classes `SDPDegeneracyDetectsMetallic` and " +
        "`CSCSilverIsCFLTransition` make the higher-n generalisation " +
        "and the physical CFL identification explicit.",
    },
    {
      kind: "refined-framing",
      date: "2026-06-09",
      body:
        "Exact-Gram re-run (PR #2081, " +
        "`metallic_q_s4_exact_lp_sweep.py`): S(3) = S(4) = " +
        "{δ_silver} EXACT at the cost-coincidence level (γ vs σ₁, " +
        "mpfr residual < 1e-37), but the n≥3 LP active-set flip of " +
        "the approximate probe was a Gram-approximation artifact — " +
        "only the n=2 active-set transition stands.  Coincidences " +
        "are q-Plancherel-convention-anchored (absent under " +
        "canonical Markov weights).",
      see: "docs/audits/2026-06-09-metallic-qrho-calibration-nova-cascade.md",
    },
  ],
});
