import { remark } from "../../schema/builders";

/**
 * ⁴He doubly-magic structural identity — magic-shell fingerprint
 * agreement between channel and Wedderburn approaches.
 *
 * The two preceding propositions
 *
 *   prop:he4-two-row-dominance   (Wedderburn-block fingerprint)
 *   prop:he4-channel-active-set  (channel/LP fingerprint)
 *
 * arrive at the same structural picture by independent compute
 * paths:
 *
 *   Channel level (operator-selection LP):
 *     primal-saturating  : T⊕p
 *     highest dual       : D⊕D  (y* = 3.778)
 *     secondary dual     : ³He⊕n (y* = 0.796)
 *
 *   Wedderburn level (canonical Markov trace):
 *     dominant block λ*  : (9, 3)  → 29.0 %
 *     top-5 cumulative   : two-row Λ²(12) at 86.6 %
 *     trivial rep (12)   : only 2.9 %
 *
 * Both fingerprints identify a q-symmetric deuteron-pairing
 * structure as the load-bearing geometry of the doubly-magic
 * binding:
 *
 *   - The channel/LP picture: the LP's primal weight goes to T⊕p
 *     (smallest residual cost), but the dual shadow prices show
 *     D⊕D is the *most receptive* sub-braid to a coupling
 *     perturbation.
 *
 *   - The Wedderburn picture: the trace lives almost entirely in
 *     the two-row stratum Λ²(12), which is the SU(2) Schur-Weyl
 *     image — the q-symmetric spin-pairing sector.
 *
 * These are not two ways of saying the same thing trivially: the
 * channel decomposition is at the categorical-atom level
 * (Δ_cat anchors of D, T, ³He, ⁴He) while the Wedderburn
 * decomposition is at the per-irrep matrix-trace level on the
 * Hecke algebra H_12(q).  The agreement that BOTH identify the
 * deuteron-pairing channel as the structurally-receptive surface
 * is a substrate-derived account of the empirical
 * "doubly-magic" identity of ⁴He.
 *
 * This is consistent with — and extends — the empirical findings
 * of PR #645 (H7a anchor at (2,2) closes to 0.169 %) and the
 * sibling PR #656 (D-2 q-Catalan candidate carries Z/N
 * structure), which respectively pinned the (2,2) anchor
 * empirically and proposed a structural mechanism.  The Wedderburn-
 * block agreement here gives an *algebraic* mechanism rather than
 * a combinatorial one: doubly-magic = q-symmetric two-row
 * stratum dominance.
 *
 * No new logical claim is made beyond what is in the two
 * propositions; this remark is the bridge interpretation.
 *
 * Interprets:
 *   prop:he4-two-row-dominance  (primary)
 *   prop:he4-channel-active-set (secondary; named in body)
 *
 * Used by:
 *   - conj:magic-shell-stabilization (refinement context).
 *
 * Audit:
 *   docs/audits/2026-05-15-three-pr-integration.md §F1 ⁴He
 */
export default remark({
  label: "rem:he4-magic-shell-fingerprint",
  title:
    "Doubly-magic $^4\\mathrm{He}$ structural identity: channel LP and Wedderburn block fingerprints both identify the $q$-symmetric D-pairing stratum",
  interprets: "prop:he4-two-row-dominance",
  uses: [
    "prop:he4-channel-active-set",
    "conj:magic-shell-stabilization",
  ],
  tags: [
    "he4",
    "doubly-magic",
    "magic-shell",
    "two-row",
    "deuteron-pairing",
    "structural-identity",
    "fingerprint-agreement",
    "f1-bridge",
  ],
});
