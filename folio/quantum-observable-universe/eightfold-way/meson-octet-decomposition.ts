import { proposition } from "../../schema/builders";

/**
 * Meson octet from tensor decomposition 3 ⊗ 3̄ = 8 ⊕ 1.
 *
 * Derives the meson multiplet structure from the ⊗_K product of
 * flavor triplet and antitriplet. The 8 mesons sit at the vertices
 * and edges of the hexagonal weight lattice; the singlet η′ sits
 * at the origin.
 *
 * ANTI-FITTING: Pure representation theory of SU(3) / A₂.
 * The physics identification (π, K, η, η′) is stated as a
 * dictionary entry, not as an input to the derivation.
 */
export default proposition({
  label: "prop:meson-octet-decomposition",
  title: "The meson octet via $\\mathbf{3} \\otimes \\bar{\\mathbf{3}}$",
  // rem:flavor-charge-assignments dropped from uses[] 2026-11-20 (owner choice, bean qou-tm3c):
  // not cited in the statement or proof. A remark carries no premise; the edge only put this block
  // downstream of a conjecture.
  uses: ["prop:a2-from-three-strands"],
  // Lean backs the DIMENSION shadow the block states — "(9 = 8 + 1)":
  // meson_octet_at_three proves sorry-free that the fundamental ⊗ anti-
  // fundamental (dim N² = 9) splits as adjoint (octet, dim N²−1 = 8) ⊕ singlet
  // (1), i.e. 9 = 8 + 1 at N = 3. It does NOT formalise the rep-level Clebsch-
  // Gordan 𝟑⊗𝟑̄ = 𝟖⊕𝟏 nor the weight/quantum-number assignments (SU(3) content,
  // a Mathlib gap — as on the baryon side, RowCapObstruction); this backs the
  // dimension arithmetic only.
  lean: { ref: "qou:QOU.Eightfold.MesonOctet.meson_octet_at_three" },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The idempotent algebra is formalised for any $k$-linear category:\n\nThe Lean does not\nprove that the octet is irreducible, and it does not construct" },
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body: "The QOU realization paragraph previously called 3⊗3̄ a Clebsch–Gordan decomposition of H₃(q) Specht modules. H₃(q) is not a Hopf algebra, so its modules carry no tensor product, and its Specht modules have dimensions 1, 2, 1; it acts on V^{⊗3} (the baryon side), not on V⊗V*. The paragraph now uses the rigid-category trace splitting in Rep U_q(sl₃): singlet = image of coevaluation, octet = kernel of evaluation, projector coev∘ev/[3]_q. The idempotent algebra is proved sorry-free for any k-linear category in `QOU.Eightfold.TraceSplitting` (proj_idem, coproj_idem, proj_add_coproj, coev_comp_coproj, coproj_comp_ev, qint_three_ne_zero). That file does not construct U_q(sl₃), does not supply the pivotal structure, and does not prove the octet irreducible.",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): As noted in\n[the Schur--Weyl proposition](#prop:schur-weyl-eightfold), the $N = 3$ question is" },
  ],
});
