import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:c1-theta-zero-locus-and-pole-divisor",
  lean: {
    ref: "qou:QOU.QBeta.C1Poles.qTheta_neg_zpow_eq_zero",
    validation: "validated",
  },
  title:
    "The connection matrix of the ramified binding operator is p-elliptic and " +
    "its poles are theta zeros; the q-theta vanishes on −p^ℤ",
  uses: [
    "conj:qdifference-kernel-prolongation-symbol",
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
        "conj:qdifference-kernel-prolongation-symbol. This block therefore " +
        "`uses[]` that conjecture — the arc's actual context — and does not " +
        "pretend to feed anything else. It is a record of correct, expensive-to-" +
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
  ],
  tags: [
    "q-difference",
    "theta",
    "connection-matrix",
    "c1",
    "open-problem",
  ],
});
