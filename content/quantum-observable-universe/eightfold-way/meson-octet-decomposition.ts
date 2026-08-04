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
  md: "meson-octet-decomposition.md",
  uses: [
    "prop:a2-from-three-strands",
    "rem:flavor-charge-assignments",
  ],
});
