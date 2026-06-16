import { remark } from "../../schema/builders";

/**
 * Companion to rem:staircase-ew-k3-mpfr-finding (PR #680).  Extends
 * the negative result to k=4 (V_(4,3,2,1), dim 768) at float64,
 * showing the previously-cited 0.14% pairwise match is **comparable
 * to random-coincidence in the dim-768 spectrum** (coincidence factor
 * 3.73× — actual best match is worse than what 147k random pairwise
 * comparisons would produce by chance).
 *
 * Combined with rem:staircase-ew-k3-mpfr-finding, this strengthens
 * the falsification of conj:staircase-ew-residual's literal content
 * (no internal eigenvalue pair has ratio exactly q^(1/(2k−1))) to
 * cover every testable k:
 *  - k=2: untestable (β_EW word collapses to length-0 at n=3)
 *  - k=3: literal pairwise reading off by 6.95% at 50 dps
 *  - k=4: literal pairwise reading off by 0.14% at float64, BUT
 *    coincidence-by-chance baseline is 0.038%, so the 0.14% is
 *    3.7× looser than what random search would produce → no
 *    structural signal
 *
 * The empirical content that survives is the LEADING-ORDER match
 * via the CODATA-residual reading (k=3 only, since k=4 lacks a
 * direct experimental anchor).  The Lean
 * StaircaseEWResidual class instance's sorry should encode this
 * approximate-leading-order status, not an exact closed-form identity.
 *
 * Direct 50-dps verification at k=4 is infeasible (~14 hours for the
 * matrix product alone at naive precision; see audit for the
 * sparse-aware infrastructure that would be required).  The
 * coincidence-by-chance analysis here gives the same conclusion
 * without needing the high-precision upgrade — the random-coincidence
 * floor in the dim-768 spectrum is already comparable to the
 * empirical match, so higher precision cannot rescue the literal
 * conjecture.
 *
 * Bar-pair structure (all 768 eigenvalues form 384 perfect e_+ · e_-
 * = −1 pairs) is independent of the q^(1/7) claim and stands —
 * confirms the conjugate-pairing analysis from
 * prop:beta-ew-bar-pair-recursion.
 */
export default remark({
  label: "rem:staircase-ew-k4-pairwise-readings",
  title:
    "Coincidence-by-chance analysis falsifies the literal staircase EW-residual at $k=4$",
  interprets: "conj:staircase-ew-residual",
  uses: [
    "conj:staircase-ew-residual",
    "rem:staircase-ew-k3-mpfr-finding",
    "def:staircase-partition",
    "lem:staircase-corner-hook",
  ],
  computation: {
    engine: "numpy",
    script:
      "computations/probe_staircase_ew_k4_pairwise_readings.py",
    witness:
      "computations/staircase-ew-k4-pairwise-readings.witness.json",
    status: "verified",
  },
  tags: [
    "empirical-finding",
    "staircase-ew-residual",
    "high-precision-mpmath",
    "negative-result",
    "research-direction",
  ],
});
