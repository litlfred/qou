import { proposition } from "../../schema/builders";

/**
 * Two-row stratum dominance in the ⁴He canonical Markov trace.
 *
 * Let β_{⁴He} = canonical atomic braid word for ⁴He (Z=2, N=2) on
 * H_12(q), 47 crossings with 3 operator-valued interfaces (pp at
 * gen 2, pn at gen 5, nn at gen 8), per
 *
 *   mass_at_3A_proper.atom_braid_word_3A(2, 2).
 *
 * Define the per-partition contribution
 *
 *   c_λ(q_0) := y_λ(q_0) · χ^λ_q(β_{⁴He})
 *
 * (Wenzl Markov weight × Hoefsmit per-irrep character at the
 * substrate parameter q_0).  Numerical evaluation at 50 dps via
 * the per-irrep numeric Hoefsmit path
 * (`wedderburn_jones_markov.global_wedderburn_sum_q_hecke_seminormal`
 * machinery) gives, across all 77 partitions of 12:
 *
 *   Σ_λ c_λ(q_0) = tr_M(β_{⁴He})(q_0) = 0.011237417660.
 *
 * **Proposition.** The two-row stratum (def:two-row-stratum)
 * carries the trace at ≥ 80 %:
 *
 *   |Σ_{λ ∈ Λ²(12)} c_λ| / |tr_M(β_{⁴He})| ≥ 0.80.
 *
 * Empirically (witness): the ratio is **exactly 1** — all 70
 * partitions of 12 with more than two rows contribute 0, so the
 * seven partitions of Λ²(12) carry the whole trace.  Blocks by
 * |c_λ| (all in Λ²(12); two enter with the opposite sign):
 *
 *   [12]      +85.398 %
 *   [9, 3]    +64.406 %
 *   [11, 1]   -40.890 %
 *   [8, 4]    -31.659 %
 *   [10, 2]   +11.461 %
 *   [6, 6]     +8.652 %
 *   [7, 5]     +2.633 %
 *
 * The sign rep [1¹²] is 0 at 50 dps.  The leading NON-TRIVIAL
 * block is [9, 3]; the trivial rep [12] leads overall only
 * because its character cannot move under a reordering of the
 * braid word while every other block fell past it, and it leads
 * in each of p, n, D, T, ³He and ⁴He alike.
 *
 * SUPERSEDED FIGURES, kept so a reader meeting them elsewhere can
 * date them: `0.05534835` / ratio 86.6 % / [9,3] 29.0 % are the
 * pre-2026-08-23 generation (wrong y_λ family, see authorNotes);
 * `0.160974145442` / [9,3] 29.617 % are the 2026-08-23 correction,
 * computed under the SUPERSEDED grouped intra-nucleon ordering.
 *
 * Independent of (and confirming)
 * delta_lambda_2row_stratum_analysis.py — which established the
 * same pattern empirically across {D, T, ³He, ⁴He}: the dominant
 * Wedderburn block is always two-row.
 *
 * **Conditional on:** the empirical witness file
 * `he4-canonical-tr-m-block-fingerprint.witness.json` for the
 * within-stratum per-block ranking (`HasHe4DominantBlock`), while
 * the two-row stratum support (`ratio = 1`) holds unconditionally
 * under convention D (`z_D = q^3/(q^2+1)`, Wenzl level `r = 2`) by
 * `QOU.MassTheory.TwoRowCap.twoRow_share_eq_one_of_wenzl`
 * (specialized in the Lean sibling as
 * `he4_twoRow_share_eq_one_of_wenzl`; `bean qou-58w3`).  The class
 * `HasHe4TwoRowDominance` carries `ratio := 1` (`ratio_eq_one :
 * ratio = 1`) together with the implied `4/5 <= ratio <= 1` bounds,
 * retiring the superseded convention-C `866/1000` numeral.  The
 * companion `HasHe4DominantBlock` pins `[9, 3]` as the leading
 * non-trivial block alongside `[12]` as the largest block overall.
 *
 * Used by:
 *   - rem:he4-magic-shell-fingerprint — physical interpretation
 *     (q-symmetric pairing magic shell).
 *
 * Witness:
 *   computations/he4-canonical-tr-m-block-fingerprint.witness.json
 * Probe:
 *   computations/probe_he4_canonical_tr_m_fingerprint.py
 * Audit:
 *   docs/audits/2026-05-15-three-pr-integration.md §F1 ⁴He
 */
export default proposition({
  label: "prop:he4-two-row-dominance",
  title:
    "Two-row stratum carries $\\ge 80\\%$ of $\\mathrm{tr}_M(\\beta_{^4\\mathrm{He}})$ at $q_0$ (exactly $1$ empirically)",
  uses: ["def:two-row-stratum"],
  computation: {
    engine: "scipy",
    script: "computations/probe_he4_canonical_tr_m_fingerprint.py",
    witness: "computations/he4-canonical-tr-m-block-fingerprint.witness.json",
    status: "verified",
    requires: ["numpy", "scipy", "sympy", "mpmath"],
  },
  lean: { ref: "qou:QOU.BraidKnot.He4TwoRowDominance.HasHe4TwoRowDominance" },
  tags: [
    "he4",
    "doubly-magic",
    "wedderburn-decomposition",
    "two-row",
    "magic-shell",
    "su2-schur-weyl",
    "f1-fingerprint",
    "verified-empirically",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Proposition (conditional on [`he4-canonical-tr-m-block-fingerprint.witness.json`](../../../computations/he4-canonical-tr-m-block-fingerprint.witness.json)).**" },
    {
      kind: "caveat",
      date: "2026-09-06",
      body:
        "**Every number in the table moved again, and the ordering changed (bean `qou-85wn`).** `atom_braid_word_3A`'s per-nucleon confinement core went from GROUPED to alternating (`intra_order: \"borromean\"`) on the 2026-09-05 owner ruling (bean `qou-hu1f`), and the `chi-helium-4-h12-at-q0-50dps` cache was regenerated under the follow-up ruling `qou-92u9` on 2026-09-06. The trace falls `0.160974145442` \u2192 `0.011237417660`, exactly the \u2074He factor `R_quark = 14.3248`. **What is untouched:** the `y_\u03bb` column (a function of the partition and `q` alone), the stratum ratio (still exactly 1, 7 nonzero blocks of 77), the braid word's shape (47 crossings, interfaces at generators 2/5/8 \u2014 the grouped and borromean words are the same multiset reordered), and therefore the Proposition itself. **What changed:** two blocks now enter with the opposite sign, `[11,1]` at \u221240.890 % and `[8,4]` at \u221231.659 %, so the trace is a partial cancellation within the stratum (positives 172.549 %, negatives \u221272.549 %); and the ranking is now `[12]`, `[9,3]`, `[11,1]`, `[8,4]`, `[10,2]`, `[6,6]`, `[7,5]`. The independent \u0394_\u03bb empirical-tabulation route, regenerated the same day, reports the same leading three \u2014 so the two routes still agree, through a change that moved every number.",
    },
    {
      kind: "note",
      date: "2026-09-06",
      body:
        "**RESOLVED 2026-09-07 (owner disposition): the class now carries BOTH.** Under the regenerated data the largest `|c_\u03bb|` is the TRIVIAL representation `[12]` at 85.398 %, ahead of `[9,3]` at 64.406 %. That is not a \u2074He fingerprint: the trivial rep leads in **six of eight** atoms in the \u0394_\u03bb witness \u2014 p, n, \u00b2H, \u00b3H, \u00b3He, \u2074He \u2014 and those six are exactly the ones whose chi caches were regenerated (\u2075Li and \u2076Li, not regenerated, still lead with `[12,3]` and `[14,4]`). The trivial rep's character is invariant under any reordering of the braid word, so it did not move; it leads because everything else fell. The block's prose and the Lean instance both keep `[9,3]` as the leading NON-TRIVIAL block, which is the reading under which the magic-shell interpretation has content. **Nothing is broken either way** \u2014 `dominant_eq : dominant_partition = [9, 3]` sits in the class signature and every downstream theorem is a structural consequence of `4/5 \u2264 ratio \u2264 1`, so no proof depends on the choice. If the author wants `[12]`, the change is the class field, its instance, and `dominant_eq_nine_three_in_stratum`'s name and statement; `IsTwoRow` is `length \u2264 2`, so `[12]` is in \u039b\u00b2(12) and `by decide` still discharges. \u2014 **Done.** The class gained `largest_partition := [12]` with its own two-row and sums-to-12 proofs, and a field `leading_ne_largest : dominant_partition \u2260 largest_partition` that ASSERTS the distinction rather than merely recording two values. Two derived results follow from it: `largest_in_two_row_stratum` and `dominant_ne_trivial_rep`. `dominant_partition` is unchanged at `[9,3]`, so every existing downstream theorem is untouched. Verified `lean`-direct with `-DautoImplicit=false -s 65536`: **exit 0**, and `#print axioms` on all three new/affected declarations reports **`[propext]`** only \u2014 no `sorryAx`. The point of carrying both: before the ruling the two notions picked out the same block, so one field expressed both and nothing recorded which was meant.",
    },
    {
      kind: "caveat",
      date: "2026-08-23",
      body:
        "**The empirical table was wrong and is corrected (bean `qou-bm4i`).** It gave `tr_M(\u03b2_\u2074He)(q\u2080) = 0.05534835` and a two-row ratio of 86.6 %; the canonical producer computes **0.160974145442** and a ratio of **exactly 1** \u2014 all 70 partitions with more than two rows contribute 0. Diagnosed, not assumed: re-running `probe_he4_canonical_tr_m_fingerprint.py` reproduces the committed witness byte-for-byte, the Hoefsmit characters \u03c7^\u03bb AGREE with the old table to 3+ digits, and only `y_\u03bb` differed \u2014 by a NON-uniform factor (2.66\u20134.04), so a different weight formula rather than a normalisation. AGENTS.md records that `y_\u03bb` / `w_\u03bb` / `w\u0303_\u03bb` are distinct at q \u2260 1 and must not be conflated; the old table appears to have used another family under the `y_\u03bb` label. The proposition itself is unaffected and in fact strengthened \u2014 the \u2265 80 % bound holds at 100 % and the top block \u03bb* = (9,3) is unchanged. The producer's CITED_* constants track the block's prose, so they were corrected with it and the cross-check stays live.",
    },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "status",
      body: "The proposition is verified at 50-dps numerical precision in the\ncompanion witness. The Lean formalisation follows the conditional-\nclass pattern (AGENTS.md §3b-cond): the stratum-share figure is\nencoded as a class\n`HasHe4TwoRowDominance` whose only `sorry` is the empirical\ninstance, and downstream propositions such as\n`rem:he4-magic-shell-fingerprint`\ntake this class as a `[HasHe4TwoRowDominance]` typeclass\nhypothesis.",
    },
  ],
});
