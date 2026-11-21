import { theorem } from "../../schema/builders";

export default theorem({
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Edge `conj:hook-weight-derivation` removed from `uses`. That block's open content is the identification of β₄ = −½ w_{[2,2]} with the Φ₄ coefficient; this theorem uses neither β₄ nor Φ₄ (its Lean sibling imports only Mathlib and takes dim_q as block data), so the edge was spurious and made a proved statement look conjecture-dependent. On H_{n+1}(q) itself, `QOU.MassTheory.CoCasimirHecke` (CoCasimirHeckeBridge.lean) proves the surviving-block version for every Markov trace at z_D: `cHecke_central`, `markov_radical_iff` (radical = elements acting by zero on all partitions with at most two rows), `tr_cHecke` (τ(C°) = Σ_{ℓ(λ) ≤ 2} 1/dim_q(λ)) and `tr_of_agree_on_surviving`. This composes `AnyChar.heckeWedderburnF` and `SeminormalRep.eq_wtrace_of_markov`, so the Wedderburn model and the trace weights are no longer assumed. Production Term 4 is unchanged (owner option B stands; issue #8109)." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): over a generic field, Lean proves that |  (`QOU.MassTheory.CoCasimirSurviving.mem_traceRadical_iff`, `tr_of_lift`, `no_full_coCasimir`). Under convention D the surviving sum runs over the partitions with at most two rows (`tr_coCasimirSurv_conventionD`)." },
    { kind: "caveat", date: "2026-11-15", body: "Under convention D, τ(p_λ) = 0 for every λ with three or more rows, so C_dim_q is undefined on H_n for n ≥ 3; the statement now carries the hypothesis τ(p_λ) ≠ 0 and a scope paragraph. The uniqueness claim was false (dim Z(A) = p(n) ≥ 2) and is withdrawn. The production Term 4 (paper_six_term_isotope_sweep.term4_frobenius_codim) still sums over all λ; that is flagged, not changed." },
    { kind: "status", date: "2026-11-16", body: "Owner ruling (option B): the production Term 4 keeps its number and is relabelled as the formal sum Σ_{λ ⊢ 3A} 1/dim_q(λ) over all partitions. It is not τ(C_dim_q) under convention D. Whether Term 4 should instead be τ(C°_dim_q) over the surviving blocks, or an object on the radical quotient, stays open." },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "thm:frobenius-codim-universal",
  title:
    "Universal Frobenius co-dimension trace: $\\tau(C_{\\dim_q}) = \\sum_\\lambda 1/\\dim_q(\\lambda)$",
  lean: {
    ref: "qou:QOU.BraidKnot.frobenius_codim_universal",
    validation: "not_checked",
  },
  uses: [],
  cites: ["kassel1995"],
  tags: [
    "frobenius",
    "co-casimir",
    "self-dual",
    "quantum-dimension",
    "universal",
    "tqft",
    "theorem",
  ],
});
