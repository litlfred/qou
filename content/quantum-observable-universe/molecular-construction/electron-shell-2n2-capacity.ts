import { remark } from "../../schema/builders";

/**
 * Historical note on the 2n² shell capacity.
 *
 * This block was formerly `conj:electron-shell-2n2-capacity`, asserting that
 * 2n² = 2·Σ(2ℓ+1) required an SO(4)-type accidental degeneracy. Both halves of
 * that are superseded:
 *
 *   - the count is DERIVED (prop:shell-capacity-self-square, sorry-free Lean at
 *     q = 1), so it is no longer an open problem; and
 *   - the SO(4)/Runge–Lenz mechanism is retracted by the owner ruling of
 *     2026-06-20 ("no second *compact* SU(2)"), which replaces it with the
 *     self-fusion V⊗V of one angular object.
 *
 * Demoted to a remark interpreting the proposition rather than deleted: the
 * retraction is worth keeping in the corpus, since the SO(4) framing was
 * adopted once already (2026-06-16) and re-derived from scratch is exactly the
 * failure mode this record prevents.
 *
 * The surviving open step is conj:shell-space-is-self-square.
 */
export default remark({
  interprets: "prop:shell-capacity-self-square",
  label: "rem:electron-shell-2n2-capacity",
  title: "The $2n^2$ capacity needs no second compact $\\mathrm{SU}(2)$",
  uses: [
    "prop:shell-capacity-self-square",
    "conj:shell-space-is-self-square",
  ],
  tags: [
    "shell-capacity",
    "2n2",
    "self-square",
    "no-second-su2",
    "retraction",
  ],
});
