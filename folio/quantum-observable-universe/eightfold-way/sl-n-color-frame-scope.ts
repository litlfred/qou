import { remark } from "../../schema/builders";

/**
 * Scope of the SU(N) frame: color observables only.
 *
 * Records the owner ruling G5 = (a) (2026-11-15, relayed by the qou-qs0e
 * coordinator): color observables are read with q^{-1/N} sigma; the Markov
 * parameter z, convention D and the writhe-normalised tr_M stay as ruled.
 * Also re-scopes the level-3 probe's "det T = -1" attribution and records
 * that the sl_2 frame gives the nuclear channel ratio 3, not 33.7.
 */
export default remark({
  label: "rem:sl-n-color-frame-scope",
  title: "Scope of the $\\mathrm{SU}(N)$ frame",
  interprets: "prop:sl-n-color-framing",
  uses: ["prop:sl-n-color-framing"],
});
