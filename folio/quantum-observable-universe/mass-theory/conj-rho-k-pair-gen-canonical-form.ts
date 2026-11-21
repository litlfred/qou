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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): | Refuted | `rho-k-pair-gen-extension.witness.json` |\n\n## Lean formalization\n\n```lean\nnamespace QOU.BraidKnot.RhoKPairGenCanonicalForm\n\n/-- The quantum dilogarithm `Li₂^q` as a concrete real function — the\n    Faddeev–Kashaev series, evaluated over `ℝ`. -/\nnoncomputable def qDilog (q x : ℝ) : ℝ :=\n  ∑' n : ℕ, x ^ (n + 1) / ((n + 1 : ℝ) * (1 - q ^ (n + 1)))\n\n/-- Markov datum for one atomic braid: the Wedderburn-traced\n    per-generator volumes `|V̂_i|`. -/\nstructure AtomicBraid where\n  vols : List ℝ\n\n/-- The measured (CODATA) pair-gen contribution — an external empirical\n    datum, hence an opaque *function* of the braid's Markov data. -/\naxiom physMass : AtomicBraid → ℝ\n\n/-- Pairwise sum `Σ_{i<j} f (vᵢ) (vⱼ)`. -/\ndef pairSum (f : ℝ → ℝ → ℝ) : List ℝ → ℝ\n  | [] => 0\n  | v :: vs => (vs.map (f v)).sum + pairSum f vs\n\n/-- The six-term theorem's `T₃` Kashaev-limit functional\n    `f(x, y) = -z² · Li₂^q(-|x·y|)`. -/\ndef kashaevT3 (Li2q : ℝ → ℝ) (z x y : ℝ) : ℝ :=\n  -z ^ 2 * Li2q (-(|x * y|))\n\n/-- Conjecture axiomatisation (§3b class, content-bearing). One concrete\n    `T₃` functional recovers every atomic braid's measured pair-gen mass\n    to sub-percent accuracy, uniformly in the braid. **No instance is\n    provided** — that is the open Kashaev-limit derivation. -/\nclass PairGenCanonical : Prop where\n  content :\n    ∃ (q z : ℝ), 1 < q ∧\n      ∀ K : AtomicBraid, 0 < physMass K →\n        |pairSum (kashaevT3 (qDilog q) z) K.vols - physMass K| ≤ physMass K / 100\n\nend QOU.BraidKnot.RhoKPairGenCanonicalForm\n```\n\n\n" },
    {
      kind: "refined-framing",
      date: "2026-08-30",
      body:
        "**Lean block re-synced to the sibling `.lean`.** The narrative Lean block " +
        "previously showed `pair_gen_functional ... := sorry` together with a carrier " +
        "field $\\forall M \\ge 0,\\ \\exists M_{\\mathrm{rec}},\\ |M_{\\mathrm{rec}} - M| \\le M/100$. " +
        "That field is trivially inhabited (take $M_{\\mathrm{rec}} := M$), so it asserted " +
        "nothing and a downstream `[PairGenCanonical]` hypothesis would have constrained " +
        "nothing. The sibling `.lean` had already been corrected to the content-bearing " +
        "form — one concrete $T_3$ quantum-dilogarithm functional recovering `physMass` " +
        "uniformly over atomic braids, with no instance provided — but this narrative " +
        "block had not been re-synced. It now matches the `.lean`.",
    },
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
