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
  uses: [
    "prop:a2-from-three-strands",
    "rem:flavor-charge-assignments",
  ],
  // Lean backs the DIMENSION shadow the block states — "(9 = 8 + 1)":
  // meson_octet_at_three proves sorry-free that the fundamental ⊗ anti-
  // fundamental (dim N² = 9) splits as adjoint (octet, dim N²−1 = 8) ⊕ singlet
  // (1), i.e. 9 = 8 + 1 at N = 3. It does NOT formalise the rep-level Clebsch-
  // Gordan 𝟑⊗𝟑̄ = 𝟖⊕𝟏 nor the weight/quantum-number assignments (SU(3) content,
  // a Mathlib gap — as on the baryon side, RowCapObstruction); this backs the
  // dimension arithmetic only.
  lean: { ref: "qou:QOU.Eightfold.MesonOctet.meson_octet_at_three" },
});
