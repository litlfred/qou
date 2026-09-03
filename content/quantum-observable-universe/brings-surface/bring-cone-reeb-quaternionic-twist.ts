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
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-09-03",
      body:
        "**Which 3-manifold is the link, and which real form can its Reeb " +
        "triad have.** Bézout gives the complete intersection $(1,2,3)$ in " +
        "$\\mathbb{P}^4$ degree $6$ and adjunction gives $K = \\mathcal{O}(1)$, " +
        "so the embedding is canonical and the link of the affine cone — the " +
        "unit circle bundle of $\\mathcal{O}(-1)|_C = K^{-1} = TC$ — is " +
        "canonically the unit tangent bundle $UT(\\Sigma_4)$, Euler number " +
        "$-6 = \\chi$. A circle bundle over a genus-$4$ surface with non-zero " +
        "Euler number carries $\\widetilde{\\mathrm{SL}}_2$ geometry, so it is not " +
        "a spherical space form and admits no 3-Sasakian structure; its " +
        "natural Reeb triad is the split form $\\mathfrak{sl}_2(\\mathbb{R})$ " +
        "(geodesic, horocyclic, fibre-rotation flows), not $\\mathfrak{su}(2)$. " +
        "The bracket proved here is a true quaternion identity; the question " +
        "is which real form the *degenerate* quaternionic-contact reading " +
        "intends on $UT(\\Sigma_4)$. Every component of the canonical atom " +
        "closure is a $(2,2g+1)$-torus knot whose complement is " +
        "$\\mathrm{PSL}(2,\\mathbb{R})/\\Delta(2,2g+1,\\infty)$, the same kind of " +
        "quotient, so the answer fixes the coordinate frame on those " +
        "complements too. Audit: " +
        "`docs/audits/2026-09-03-bring-cone-link-is-the-unit-tangent-bundle.md` " +
        "(bean `qou-m3sh`).",
    },
    {
      kind: "caveat",
      date: "2026-09-03",
      body:
        "**The \"degenerate\" conciliation works only as the split real form " +
        "(checked).** `def:bring-cone-tetraplectic-structure` supplies a volume " +
        "form, which induces no contact triad; the link is Sasakian with the single " +
        "Reeb field $V$, and a closed aspherical 3-manifold admits no non-trivial " +
        "$\\mathrm{SU}(2)$-action, so three Reeb fields closing into " +
        "$\\mathfrak{su}(2)$ cannot exist on $UT(\\Sigma_4)$. The triad it does " +
        "carry — connection form, Liouville form, its quarter-turn rotation, Reeb " +
        "fields $V, X, X^\\perp$ — closes into $\\mathfrak{sl}_2(\\mathbb{R})$. " +
        "Running this lemma's construction on the split quaternions " +
        "(`lean/QOU/BringConeSplit.lean`, sorry-free) gives $[M_i,M_j]=2M_k$, " +
        "$[M_j,M_k]=-2M_i$, $[M_k,M_i]=2M_j$: one sign flipped, and " +
        "`split_ne_compact` shows it is not the compact bracket. So the identities " +
        "here are true and are those of the real form this link does not carry; " +
        "the $\\mathfrak{su}(2)$ survives as the structure group of the resolvent " +
        "bundle (the gauge reading of `rem:tetraplectic-su2-gauge-reading`), not as " +
        "a Reeb triad. Addendum in the audit cited above.",
    },
  ],
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
