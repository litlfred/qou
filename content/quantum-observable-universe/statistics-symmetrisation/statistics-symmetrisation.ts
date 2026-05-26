import { chapter, section } from "../../schema/builders";

/**
 * Chapter 8 — Statistics and Symmetrisation.
 *
 * Categorical derivation of Pauli exclusion, spin–statistics, and the
 * fermion/boson split from the rigid braided structure. Sits between
 * Bring's Surface (Ch 7) and Particles (Ch 9) in the structural-mechanics
 * arc: once the geometric realisation is fixed on Bring's, the rigid-
 * braided structure determines which states are antisymmetric (fermions)
 * vs symmetric (bosons), and forces the exclusion principle on
 * fermionic species.
 *
 * Phase 6 scaffold (2026-05-25): the chapter directory + manifest exist
 * but blocks have not yet been migrated. See
 * docs/chapter-restructure-2026-05-25.md for the migration plan.
 */
export default chapter({
  title: "Statistics and Symmetrisation",
  label: "chap:statistics-symmetrisation",
  sections: [
    section({
      title: "Introduction",
      label: "sec:statistics-symmetrisation-intro",
      blocks: ["intro"],
    }),
    section({
      title: "Reconnected orphan blocks (Phase 7)",
      label: "sec:statistics-symmetrisation-orphan-reconnect",
      blocks: [
        "pontryagin-dual-coxeter-character",
        "spin-from-so3-fiber",
        "type-b-folding-cpt",
        "weinberg-angle-categorical",
        "wigner-su4-from-spin-isospin",
      ],
    }),
  ],
});
