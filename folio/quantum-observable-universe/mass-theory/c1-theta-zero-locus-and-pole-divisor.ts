import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:c1-theta-zero-locus-and-pole-divisor",
  lean: {
    ref: "qou:QOU.QBeta.C1Poles.qThetaC_eq_zero_iff",
    validation: "validated",
  },
  title:
    "The connection matrix of the ramified binding operator is p-elliptic and " +
    "its poles are theta zeros; the q-theta vanishes exactly on −p^ℤ",
  cites: ["sauloy2000"],
  uses: [
    // conj:qdifference-kernel-prolongation-symbol removed (qou-tm3c): the conjecture consumes this block's theta growth, not the reverse.
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-08",
      body:
        "**Created to stop this arc being invisible to the manifest graph** " +
        "(bean qou-c1wr). The C1 connection work — nine scripts in " +
        "computations/qbeta/c3_w2_c1_*.py and three Lean files under " +
        "QOU/QBeta/ — had no content block at all: no `uses[]` edge reached it, " +
        "so nothing in the corpus recorded that it exists or what it is worth. " +
        "This block is that record. It deliberately claims LESS than the " +
        "computations do; read the scope note below before citing it.\n\n" +
        "**What is Lean-proved, sorry-free, [propext, Classical.choice, " +
        "Quot.sound].** (i) `qTheta_neg_zpow_eq_zero`: θ_p(w) = 0 for every " +
        "w ∈ −p^ℤ, by an involution n ↦ 2k−1−n that fixes the exponent and " +
        "flips the sign — unconditional, no summability needed. (ii) " +
        "`differentiableOn_qThetaC`: θ_P is holomorphic on ℂ*, by Weierstrass " +
        "M-test on annuli plus TendstoLocallyUniformlyOn.differentiableOn " +
        "(Mathlib has no DifferentiableOn.tsum). (iii) the functional equation " +
        "over ℂ, differentiated, and in logarithmic form. (iv) " +
        "`qTheta_winding_step`: ∮_{|z|=pρ} θ'/θ = 2πi + ∮_{|z|=ρ} θ'/θ, via two " +
        "reusable θ-free lemmas — `circleIntegral_scale` (change of variables " +
        "for circleIntegral, absent from Mathlib) and `winding_step`. (v) " +
        "`summable_zeroSideCoeff` / `summable_infSideCoeff`: the 0-side series " +
        "converges on ‖z‖ < 1 and the ∞-side is entire, with both recursions now " +
        "DERIVED from the operator (`zeroCoeffAt_eq_zero_iff`, " +
        "`infCoeffAt_eq_zero_iff`) rather than defined to match the scripts.\n\n" +
        "**What is NOT proved, and this is the important half.** The CONVERSE " +
        "zero locus — that −p^ℤ are the ONLY zeros — is not proved, so the pole " +
        "divisor is ⊇, not =. It needs exactly one missing lemma, the argument " +
        "principle on an annulus, which Mathlib does not have (no argument " +
        "principle, no winding number, no complex residue; name scan at HEAD). " +
        "Everything that lemma would consume IS proved — see (i)–(iv) — so the " +
        "gap is a single named lemma, not a theory build-out. Bean qou-argp " +
        "carries the decomposition. NOT the Jacobi triple product: JTP " +
        "additionally needs Liouville on ℂ*/p^ℤ and is strictly more work; the " +
        "file used to say otherwise and that was over-scoped. Also not proved: " +
        "that Y₀ and Y_∞ are the canonical solutions (normalisation and " +
        "uniqueness, qou-c1ln row 4), the meromorphy of P = Y₀⁻¹Y_∞, divisor " +
        "completeness, and the closed form for the connection invariant χ.\n\n" +
        "**Numerical status, so it is not read for more.** The divisor, the " +
        "residue-theorem completeness check, χ's order 2, α = t₂/T and the " +
        "closed form verified to 5.3e-63 over 12 points are all NUMERICAL " +
        "(witnesses c3-w2-c1-*.witness.json). The zero locus is checked to hold " +
        "at our substrate by contour integration in " +
        "c3_w2_c1_theta_zero_count.py (5/5): one simple zero per fundamental " +
        "annulus at exactly −p^k, and exactly 9 across a 9-annulus sweep.\n\n" +
        "**Consumer status — deliberately explicit.** Per bean qou-c1wr, " +
        "NOTHING in the corpus consumes the pole divisor, χ, the closed form, or " +
        "α = t₂/T. The only C1 outputs with a downstream consumer are the " +
        "theta-growth q^{m²/4} and the isoclinicity obstruction, both cited by " +
        "conj:qdifference-kernel-prolongation-symbol. The dependency runs from " +
        "that conjecture to this block, so this block does not list the " +
        "conjecture in `uses[]` (qou-tm3c, 2026-11-20). It is a record of correct, expensive-to-" +
        "re-derive work, not a load-bearing step.",
      see: "computations/qbeta/c3_w2_c1_theta_zero_count.py",
    },
    {
      kind: "status",
      date: "2026-08-08",
      body:
        "**Voice fix (branch-jargon sweep).** Two defects of my own making, " +
        "caught by the sweep I dispatched: (a) the TITLE still said `C1` after " +
        "I had cleaned the .md body — titles are published and I missed them; " +
        "(b) the .md body carried work narration — `Everything else in this arc " +
        "is numerical`, `Nothing consumes this`, `records correct, " +
        "expensive-to-re-derive work; it is not a load-bearing step` — which is " +
        "this channel's job, not the manuscript's. Both fixed: the title names " +
        "the ramified binding operator, and the body states the computational " +
        "status in scholarly voice without narrating the project.\n\n" +
        "The substance of what was removed, retained here: nothing in the " +
        "corpus consumes the pole divisor, χ, the closed form, or α = t₂/T " +
        "(bean qou-c1wr). The only C1-arc outputs with a consumer are the " +
        "theta growth and the isoclinicity obstruction. This block is a record " +
        "of correct but orphaned work and should not be cited as load-bearing.",
    },
    {
      kind: "status",
      date: "2026-08-08",
      body:
        "**The converse zero locus is proved; this block no longer claims less " +
        "than the mathematics.** `qThetaC_eq_zero_iff` (QOU/QBeta/" +
        "C1ThetaZeroLocus.lean): for w ≠ 0, θ_P(w) = 0 ↔ w ∈ " +
        "−P^{2ℤ}. With `qThetaC_analyticOrderAt_neg_zpow` (every zero " +
        "simple) that is the whole divisor of θ_P on ℂ*, so the three " +
        "pole loci in the .md are exact and reduced rather than containments. " +
        "Sorry-free, [propext, Classical.choice, Quot.sound].\n\n" +
        "**What the note above got wrong, recorded because the error repeated.** " +
        "It said the gap was 'one missing lemma, the argument principle on an " +
        "annulus, which Mathlib does not have'. The name scan behind that was " +
        "real but answered a different question: the corpus already had " +
        "QOU/Mathlib/ArgumentPrinciple.lean (on a disc — inapplicable, " +
        "θ_P has an essential singularity at 0), and Mathlib had the " +
        "factorisation the annulus form needs under " +
        "`MeromorphicOn.extract_zeros_poles`, which is not a name anyone greps " +
        "for when looking for 'argument principle'. Search by what the " +
        "statement says, not by what the theorem is called.\n\n" +
        "**What actually had to be built**, all sorry-free: " +
        "`argumentPrinciple_annulus_filter` (the annulus argument principle with " +
        "factors anywhere off the two contours — the strict-between version " +
        "is undischargeable here, because the factorisation's domain must be " +
        "strictly larger than the contour annulus and its zeros can then sit in " +
        "the collars); `exists_finset_factorisation` strengthened with positive " +
        "multiplicities and S ⊆ V; `analyticOrderAt_eq_of_finset_factorisation`; " +
        "`isPreconnected_openAnnulus` (an annulus is exp of a convex strip — " +
        "the identity theorem wants a connected domain); `qThetaC_ne_zero_outer` " +
        "(the functional equation carries non-vanishing from |z| = ρ out to " +
        "|z| = P²ρ); `qTheta_pos_of_pos` (all terms positive on the " +
        "positive real axis — the cheapest proof that θ is not " +
        "identically zero); and `exists_clean_radius`, which is what turns " +
        "`qTheta_winding_step`'s 'no zero on the contour' hypothesis from a " +
        "restriction into a choice.\n\n" +
        "**Consumer status is unchanged** (bean qou-c1wr): nothing in the corpus " +
        "consumes the pole divisor, χ, the closed form, or α = t₂/T. " +
        "This was worth finishing to close a named gap honestly and for the " +
        "upstreamable lemmas, not because a downstream number moved.",
      see: "folio/quantum-observable-universe/lean/QOU/QBeta/C1ThetaZeroLocus.lean",
    },
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "Lean sibling: archimedean specialisation over $\\mathbb{R}$ " +
        "(AGENTS.md §7c). There is no pre-archimedean statement of this " +
        "result to move to, and the file carries no generic-ring content to " +
        "split off: `C1ThetaZeroLocus.lean` is complex analysis end to end. " +
        "The theorem `qThetaC_eq_zero_iff` is a statement about the zero set " +
        "of a holomorphic function on $\\mathbb{C}^\\times$, and its proof " +
        "runs the argument principle on an annulus — `analyticOrderAt`, " +
        "`circleIntegral`, `MeromorphicOn.extract_zeros_poles`. None of that " +
        "has a `CommRing` form; a divisor computed by contour integration is " +
        "archimedean by construction.\n\n" +
        "Where the real numbers specifically enter, as distinct from the " +
        "complex ones: the modulus $P$ is a *real* parameter constrained by " +
        "the order hypothesis $1 < P$, which is what makes the $q$-theta " +
        "series converge at all — there is no $\\theta_P$ over a ring without " +
        "it; the contour radii $r, R, \\rho, c, d$ are real with $0 < r < R$; " +
        "`isPreconnected_openAnnulus` realises the annulus as " +
        "`Complex.exp` of the strip $\\log r < \\operatorname{re} z < \\log R$, " +
        "using `Real.log` and the $\\mathbb{R}$-linearity of `Complex.re`; and " +
        "`qTheta_pos_of_pos` is a positivity argument on the positive real " +
        "axis. The zero lattice itself, $-P^{2\\mathbb{Z}}$, is indexed by " +
        "$\\mathbb{Z}$ but its points are real powers of $P$ embedded in " +
        "$\\mathbb{C}$.",
      see: "folio/quantum-observable-universe/lean/QOU/QBeta/C1ThetaZeroLocus.lean",
    },
  ],
  tags: [
    "q-difference",
    "theta",
    "connection-matrix",
    "c1",
    "open-problem",
  ],
});
