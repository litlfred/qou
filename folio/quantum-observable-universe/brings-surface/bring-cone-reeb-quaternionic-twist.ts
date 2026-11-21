import { lemma } from "../../schema/builders";

/**
 * The Bring-cone link, and the Reeb triad of its quaternionic model.
 *
 * The 4-dimensional cone has a 3-dimensional link, and that link is the unit
 * tangent bundle UT(Sigma_4) with Seifert Euler number -6: it has SL~2
 * geometry, infinite pi_1, and the triad of flows it supports closes into the
 * SPLIT real form sl_2(R).
 *
 * Modelling the triad as right-multiplication by the quaternionic units gives
 * the bracket [M_i, M_j] = 2 M_k and cyclic — the COMPACT su(2) commutation
 * relations with structure constant +2. That is a statement about H = C^2, the
 * smooth local model of the cone (own link: the Hopf fibration S^3, Euler
 * number -1), and is a local/frame statement rather than a structure on the
 * link. It is the one formalized piece of the tetraplectic layer: sorry-free in
 * `lean/QOU/BringCone.lean`, over a generic `CommRing` rather than ℝ, since
 * nothing archimedean enters; `lean/QOU/BringConeSplit.lean` (also sorry-free)
 * runs the same construction on the split quaternions and `split_ne_compact`
 * shows the two brackets are distinct.
 *
 * The su(2) survives in this layer as the structure group of the quaternionic
 * resolvent bundle — `rem:tetraplectic-su2-gauge-reading` — not as a Reeb triad.
 */
export default lemma({
  label: "lem:bring-cone-reeb-quaternionic-twist",
  title:
    "Reeb quaternionic twist on the Bring-cone model: $[M_i, M_j] = 2M_k$ and cyclic",
  lean: {
    ref: "qou:QOU.Tetraplectic.reeb_twist_ij",
    sorryFree: true,
    validation: "not_checked",
  },
  uses: ["def:bring-cone-tetraplectic-structure"],
  cites: ["fothleitner2003"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-10-10",
      body:
        "**The two caveats below are now IN the statement (owner decision, bean `qou-rydq`).** The prose asserted a 3-Sasakian (degenerate quaternionic-contact) structure on the link while these notes recorded, from 2026-09-03, that the link is $UT(\\Sigma_4)$ at Euler number $-6$ with $\\widetilde{\\mathrm{SL}}_2$ geometry and a split $\\mathfrak{sl}_2(\\mathbb{R})$ triad. A caveat is for author tracking (AGENTS.md \u00a74d), not for carrying the correction to a false claim, so the statement now leads with the link's identity and scopes the compact $\\mathfrak{su}(2)$ bracket to the model $\\mathbb{H} = \\mathbb{C}^2$. Added as a third independent argument (bean `qou-xlw1`): a NON-DEGENERATE quaternionic-contact structure needs $\\dim = 4n+3$ with $n \\geq 1$, i.e. $\\dim \\geq 7$, and the link has dimension 3. **Do not read that as a dimensional refutation of 3-Sasakian** — $4n+3$ allows $n = 0$ and $S^3$ is 3-Sasakian; it is the infinite $\\pi_1$ / asphericity argument that excludes that reading. **No Lean changed**: `reeb_twist_ij/jk/ki` are quaternion identities and the restatement makes the prose MORE faithful to them, not less.",
    },
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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): *The $\\mathfrak{su}(2)$ does survive in this layer, as the structure group of\nthe quaternionic resolvent bundle rather than as a Reeb triad — see*\n[the gauge reading](#rem:tetraplectic-su2-gauge-reading)." },
  ],
  tags: [
    "tetraplectic",
    "bring-cone",
    "reeb-triad",
    "3-sasakian-retired",
    "quaternionic-contact",
    "su2",
    "lean-formalised",
  ],
});
