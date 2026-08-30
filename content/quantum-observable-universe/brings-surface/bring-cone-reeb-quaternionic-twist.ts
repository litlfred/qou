import { lemma } from "../../schema/builders";

/**
 * The 3-Sasakian boundary of the Bring cone and its Reeb triad.
 *
 * The 4-dimensional cone has a 3-dimensional link. Where the bulk carries an
 * invariant volume form, that link carries a 3-Sasakian (degenerate
 * quaternionic-contact) structure: not one Reeb vector field but an SU(2)
 * triad of contact forms and dual Reeb fields.
 *
 * Modelling the triad as right-multiplication by the quaternionic units gives
 * the bracket [M_i, M_j] = 2 M_k and cyclic — the su(2) commutation relations
 * with structure constant +2. This is the one formalized piece of the
 * tetraplectic layer: sorry-free in `lean/QOU/BringCone.lean`, over a generic
 * `CommRing` rather than ℝ, since nothing archimedean enters.
 */
export default lemma({
  label: "lem:bring-cone-reeb-quaternionic-twist",
  title:
    "Reeb quaternionic twist on the Bring-cone link: $[M_i, M_j] = 2M_k$ and cyclic",
  lean: {
    ref: "qou:QOU.Tetraplectic.reeb_twist_ij",
    sorryFree: true,
    validation: "not_checked",
  },
  uses: ["def:bring-cone-tetraplectic-structure"],
  cites: ["fothleitner2003"],
  tags: [
    "tetraplectic",
    "bring-cone",
    "reeb-triad",
    "3-sasakian",
    "quaternionic-contact",
    "su2",
    "lean-formalised",
  ],
});
