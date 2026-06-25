import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:rho-k-pair-gen-canonical-form",
  lean: {
    ref: "qou:QOU.BraidKnot.RhoKPairGenCanonicalForm.PairGenCanonical",
    validation: "not_checked",
  },
  title:
    "Conjectural canonical form of the pair-gen piece $\\rho_K^{\\text{pair-gen}}$ in the graded $\\rho_K$ expansion: there exists a closed-form Wedderburn-coupled functional form $f_2(q, \\hat V_i, \\hat V_j)$ such that $\\rho_K^{\\text{pair-gen}} = \\sum_{i<j} f_2(q, \\hat V_i^{\\text{full}}, \\hat V_j^{\\text{full}})$ recovering the six-term theorem's Kashaev limit at sub-percent accuracy.",
  uses: [
    "prop:rho-k-graded-expansion",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-05-25",
      body:
        "**Open conjecture (PR #1127).** Promotes the 'pair-gen piece (open)' " +
        "section of [`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md) " +
        "to an explicit conjecture block per AGENTS.md §3b conjectural-propagation " +
        "discipline. Per the existing audit: " +
        "(a) the naive log-additive form $\\alpha z^2 \\sum \\ln|\\hat V_i \\hat V_j|$ " +
        "DEGRADES accuracy across $Z = 1..20$ in `rho-k-pair-gen-extension.witness.json`, " +
        "(b) the correct functional form is the six-term theorem's pair piece " +
        "$T_3 = -z^2 \\sum \\text{Li}_2^q(-|V_i V_j|)$, " +
        "(c) the Kashaev-limit derivation that gives $\\alpha \\sum \\ln|V_i|$ for the " +
        "single-gen piece needs a PARALLEL derivation for the pair-gen piece. " +
        "**Status**: OPEN analytical work; multi-day effort.",
    },
    {
      kind: "refined-framing",
      date: "2026-05-25",
      body:
        "**Wedderburn-coupling structure** (per `prop:rho-k-graded-expansion` §pair-gen): " +
        "the pair-gen factor `|V_i V_j|_Wedderburn` decomposes as " +
        "`w_sym λ_i^sym λ_j^sym + w_std [z(M_iM_j)_{12} + (M_iM_j)_{22}] + w_alt λ_i^alt λ_j^alt`, " +
        "with $M_i$ the per-generator 2×2 standard-rep transfer matrix. " +
        "The OPEN piece is the Kashaev-limit functional form that converts " +
        "this Wedderburn-coupled product to the correct $T_3$-matching prefactor. " +
        "Empirical witness: `rho-k-pair-gen-extension.witness.json`.",
    },
  ],
  tags: [
    "tier:S",
    "rho_k",
    "graded-expansion",
    "pair-gen",
    "open-conjecture",
    "kashaev-limit",
    "wedderburn-coupling",
    "phase-3",
  ],
  cites: [
    "wenzl1988",
    "kashaev1995",
  ],
});
