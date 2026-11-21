import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:mass-endomorphism",
  title: "Mass endomorphism conjecture",
  lean: {
    ref: "qou:QOU.MassEndomorphism.MassEndomorphism",
    validation: "not_checked",
  },
  // conj:hecke-mass-trace and conj:brane-tower-z-habiro removed from
  // uses[] (2026-06-01 detangler Bucket-A): the conjecture only
  // *mentions* them narratively ("its Markov trace gives the mass
  // (…)"; "the [brane-tower] conjecture has two independent claims") —
  // it does not build its claim ON them. Prose links retained in the
  // .md. Reclassifies two cross-chapter logical forward-refs to
  // storytelling. See docs/coordination/forward-ref-defect-triage-2026-06-01.md.
  uses: [
    "def:qz-bicompletion",
    "def:motivic-substrate",
    "def:archimedean-realization-functor",
  ],
  tags: [
    "tier:keystone",
    "mass",
    "endomorphism",
    "quantum-dilogarithm",
    "volume-conjecture",
    "higgs",
    "brane-tower",
    "habiro-ring",
    "open-problem",
  ],
  cites: [
    "kashaev1997",
    "murakami-murakami2001",
  ],
  authorNotes: [
    { kind: "caveat", date: "2026-11-21", body: "The descended-vs-transient table row read \"e⁻ (trefoil)\". Under the owner ruling the electron is σ₀σ₁σ₀ ∈ B₃ with Hopf-link closure, and the trefoil σ₀³ ∈ B₂ is only a backup. The producer of this table is not in the tree (no witness carries 0.551 / 111.86), so it is not known which word was used. The values are kept as recorded and the row now says the word is not recorded; re-measure on σ₀σ₁σ₀ before quoting. Candidate (a) previously said 4₁ \"acts as the identity on the trefoil\"; it now states only what its equation shows, tr_M(e⁻·4₁) = tr_M(e⁻) with e⁻ = σ₀σ₁σ₀." },
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): This limit object is the motive of the mass: it carries the combinatorial data mapping to $\\mathrm{Vol}(K)/\\hbar_q^2$ only when the archimedean realization [$\\rho_\\infty$](#def:archimedean-realization-functor) of the [motivic substrate](#def:motivic-substrate) is applied at $q_0 \\in \\mathbb{R}$." },
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): ([Habiro ring](#def:habiro-ring))" },
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): ([algebraic quantum volume](#def:algebraic-quantum-volume))" },
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): ([Habiro ring](#def:habiro-ring))" },
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): **Step 2 (Tower sum $\\to$ Vol, archimedean).** Then $\\mathfrak{m}(\\varrho)|_{\\text{full tower}} = \\mathrm{Vol}(K)/\\hbar_q^2$. This is the [archimedean mass formula](#conj:topological-mass-formula). The descended trace gives $\\mathrm{Vol}(K)$, each transient trace gives $\\Phi_q(z_i)$, and their sum is $\\mathrm{Vol}(K)/\\hbar_q^2$." },
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): **Step 1 (Categorical $\\to$ Markov, proved).** One has $\\mathfrak{m}(\\varrho)|_{\\text{single level}} = |\\mathrm{tr}_M(\\rho(\\beta))|$. This is [categorical mass as Markov trace](#prop:categorical-mass-markov). The Nakayama automorphism is $S^2 = \\mathrm{id}$, so the mass reduces to the Markov trace of the braid word." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): In the unified six-term formula ([unified knot mass](#thm:knot-mass-formula-unified)), $|\\mathrm{tr}_M(\\rho(\\beta))|$ forms **Term 1** ($E_\\infty^{0,*}$, vortex-specific). The brane tower $\\sum \\Phi_q(z_i)$ supplies **Terms 2–3** ($E_\\infty^{1,*}$ and $E_\\infty^{2,*}$). In the archimedean realisation, these three terms together evaluate to $\\mathrm{Vol}(K)/\\hbar_q^2$ ([topological decomposition](#conj:topological-mass)). Terms 4–6 (Frobenius co-Casimir, chirality, jet prefix) form separate structural pieces handled elsewhere. This conjecture concerns only the tower piece." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Hecke mass element](#def:hecke-mass-element))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): Its Markov trace gives the full categorical mass ([mass via Markov trace](#conj:hecke-mass-trace))." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Hecke mass element](#def:hecke-mass-element))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Hecke mass element](#def:hecke-mass-element))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): 1. *The [$z$-Habiro completion](#def:z-habiro-ring)—analogous to the $q$-Habiro completion but in the $z$-variable. The cyclotomic denominator structure in $z$, parallel to $(q; q)_n$ in $q$, is*\n\n  $$\n      P_n(q, z) \\;=\\; \\prod_{k=1}^{n} \\bigl(1 - q^{-k} z\\bigr)\n      \\;=\\; (z q^{-1};\\, q^{-1})_n,\n  $$\n\n  *whose zero locus is exactly the first $n$ poles of $\\Phi_q$. The completion $\\widehat{\\mathbb{Z}[q^{\\pm 1}][z]}_z = \\varprojlim_n \\mathbb{Z}[q^{\\pm 1}][z] / (P_n(q, z))$ has cyclotomic projections $\\pi_n^{(z)}$ acting as structural truncations at depth $n$, replacing Yekutieli's ad-hoc cutoff with a quotient by a structural ideal. The [conjecture that the brane tower lives in this ring](#conj:brane-tower-z-habiro) has two independent claims: (a) the algebraic Cauchy-limit (the partial sums converge in the $z$-Habiro topology), and (b) the existence of a canonical level-selection rule $n_\\star(\\mathfrak{H})$ derivable from substrate data.*" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): **(c) Spectral decomposition via RJ weights.** The Rosso--Jones inner product ([RJ canonical inner product](#prop:rj-canonical-inner-product)) decomposes the Markov trace over irreps: $\\mathrm{tr}_M = \\sum_\\lambda d_\\lambda(q) \\cdot \\mathrm{tr}_\\lambda$. A mass endomorphism could reweight the irreps: $\\Phi_{\\mathrm{mass}} = \\sum_\\lambda w_\\lambda(q) \\cdot e_\\lambda$, where $w_\\lambda$ encodes the volume information. The Volume Conjecture then states that the weights $w_\\lambda$ grow exponentially with $\\lambda$, recovering $\\mathrm{Vol}(K)$ in the limit." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ## Relation to knot operator selection\n\nThe multi-channel decomposition ([knot operator selection](#prop:knot-operator-selection)) showed that interactions decompose over irreps of $H_n(R, q)$ weighted by quantum dimensions. The mass endomorphism conjecture asserts that mass is a specific reweighting of the same decomposition—using weights that produce $\\mathrm{Vol}(K)$ instead of $J(K; q)$.\n\nIf the conjecture holds:\n- The operator selection framework (Frobenius dual, Gram matrix, demand/supply) applies to mass, with $\\Phi_{\\mathrm{mass}}$ replacing the identity.\n- The Higgs field provides the dominant contribution to $\\Phi_{\\mathrm{mass}}$ for leptons (it supplies the volume that the trefoil lacks).\n- The graviton is the residual of $\\Phi_{\\mathrm{mass}}$ after subtracting the Higgs contribution." },
  ],
});
