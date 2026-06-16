import { remark } from "../../schema/builders";

/**
 * Empirical refinement of the staircase EW-residual conjecture
 * (`conj:staircase-ew-residual`) via 50-dps mpmath spectral analysis
 * at k = 3.
 *
 * The previous float64-precision verification
 * (`close_321_weinberg_gap.py`) found that multiplying the bare
 * V_(3,2,1) eigenvalue ratio `top/2nd` by `q^(1/5)` closes the
 * gap to CODATA cot θ_W with `0.13 %` residual.  Two possible
 * readings:
 *
 *  - **Closed-form**: the 0.13 % residual is a float64 noise artifact
 *    and the conjecture is an exact identity (would give `<1e-12` at
 *    50 dps).
 *  - **Approximate**: the 0.13 % residual is a genuine correction
 *    (would persist at any precision).
 *
 * This finding (`probe_staircase_ew_k3_categorical.py`, witness
 * `staircase-ew-k3-mpfr-spectral.witness.json`) tested both readings
 * at mpmath 50 dps:
 *
 *  - **Reading A** (close_321 residual path): `|Δ_rel| = 1.50e-3`
 *    (≈ 0.150 %) — essentially identical to the float64 baseline.
 *    The 0.13 % residual is NOT float-precision noise.
 *  - **Reading B** (literal conjecture, scan all pairs): best
 *    pairwise ratio match is `1.0921` vs predicted `1.0211`, off
 *    by `6.95 %`.  **No pair of eigenvalues on V_(3,2,1) has ratio
 *    exactly `q^(1/5)` at q_0.**
 *
 * Implications:
 *
 *  1. The conjecture's literal content ("two eigenvalues whose ratio
 *     equals q^(1/(2k−1))") is falsified at 50 dps for k = 3.
 *  2. The "residual factor" reading remains empirically valid but
 *     APPROXIMATE — `q^(1/5)` is the best leading-order match,
 *     accurate to 0.15 %, not exact.
 *  3. Categorical formalisation should target the approximate
 *     status (a leading-order match with controlled correction
 *     series) rather than an exact identity from corner-hook
 *     combinatorics alone.
 *
 * The Lean `StaircaseEWResidual` class instance's `sorry` therefore
 * encodes a CONDITIONAL claim about the next-order correction,
 * not an exact closed-form theorem.  See
 * `docs/audits/2026-05-17-staircase-ew-k3-mpfr-spectral.md` for the
 * full numerical comparison and the recommended conjecture refinement.
 */
export default remark({
  label: "rem:staircase-ew-k3-mpfr-finding",
  title:
    "50-dps spectral analysis falsifies the literal staircase EW-residual at $k=3$",
  interprets: "conj:staircase-ew-residual",
  uses: [
    "conj:staircase-ew-residual",
    "def:staircase-partition",
    "lem:staircase-corner-hook",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/probe_staircase_ew_k3_categorical.py",
    witness:
      "computations/staircase-ew-k3-mpfr-spectral.witness.json",
    status: "verified",
  },
  tags: [
    "empirical-finding",
    "staircase-ew-residual",
    "weinberg-angle",
    "high-precision-mpmath",
    "negative-result",
    "research-direction",
  ],
});
