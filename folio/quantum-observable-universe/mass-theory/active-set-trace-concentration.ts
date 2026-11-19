import { conjecture } from "../../schema/builders";

/**
 * Fusion bound on the trace-active set.
 *
 * Conjectures that the canonical atom braid of mass number A factors
 * through (H_3)^{⊗A} with each nucleon in the symmetric ground state
 * [3], so the Markov-trace-active Wedderburn blocks are contained in
 * the Littlewood-Richardson / induction support of [3]^{⊗A} — i.e.
 * partitions λ ⊢ 3A with at most A rows, multiplicity the Kostka
 * number K_{λ,(3^A)}. Blocks with more than A rows carry zero trace
 * for a ground-state nucleus.
 *
 * The A = 4 support (34 of 77 partitions of 12) and the per-block
 * empirical shares quoted in the .md are pinned to the committed
 * He-4 fingerprint witness; the two-row *dominance* itself is the
 * separately verified prop:he4-two-row-dominance and is compatible
 * with, but not implied by, this support bound.
 */
export default conjecture({
  label: "conj:active-set-trace-concentration",
  title:
    "Trace concentration via Littlewood--Richardson fusion of nucleon ground states",
  uses: [
    "prop:he4-two-row-dominance",
    "def:two-row-stratum",
    "def:atomic-braid",
  ],
  lean: {
    ref: "qou:QOU.BraidKnot.ActiveSetTraceConcentration",
    validation: "leanok",
  },
  computation: {
    engine: "python",
    script: "computations/active_set_lr_profile.py",
    witness: "computations/active-set-lr-scaling-profile.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-07-12",
      body:
        "The original orphan draft displayed an 8-term decomposition of " +
        "$[3]^{\\otimes 4}$ (two-row terms plus $(4,4,4)$ only, with " +
        "coefficient 3 at $(6,6)$) and claimed the other 69 partitions " +
        "vanish. Direct Kostka enumeration ($K_{\\lambda,(3,3,3,3)}$) " +
        "corrects this: the support is exactly the 34 partitions of 12 " +
        "with at most 4 rows, $(6,6)$ has multiplicity 4, and three-row " +
        "components such as $(8,3,1)$ (multiplicity 15, $\\approx 4\\%$ " +
        "of the observed trace) are inside the support. The block-share " +
        "percentages were re-pinned to " +
        "`computations/he4-canonical-tr-m-block-fingerprint.witness.json` " +
        "((9,3) 28.99%, (8,4) 23.56%, two-row stratum 92.66%) in place " +
        "of the draft's unwitnessed 32%/26%/95% figures.",
    },
    {
      kind: "note",
      date: "2026-07-12",
      body:
        "Integrated from an orphan `.md` (no manifest) per the 2026-07-12 " +
        "exposition-drain ledger §5.",
    },
  ],
  tags: [
    "active-set",
    "trace-concentration",
    "littlewood-richardson",
    "kostka",
    "wedderburn",
    "he4",
    "open-conjecture",
  ],
});
