import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-beta-cos-resummation",
  lean: {
    ref: "qou:QOU.Interactions.q_beta_cos_resummation",
    validation: "not_checked",
  },
  title:
    "$\\mathfrak{Q}_\\beta$ cos-resummation in convention D: $\\mathfrak{Q}_\\beta^{\\cos} = \\mathfrak{Q}_\\beta^{\\mathrm{base}} \\cdot \\cos((z_D-1)h/2)$ (conditional on the transfer-matrix eigenphase identification)",
  uses: [
    "prop:q-beta-spectral-bridge",
    // NOTE: the Φ_q/AJ hub (prop:phi-q-aj-machinery-identification) is
    // linked narratively in the .md only — a uses[] edge would pull the
    // hub's conj:quantum-langlands-dual cone into this proposition's
    // transitive uses[] without a matching §3b-cond class hypothesis in
    // its Lean (which axiomatises only the eigenphase identification).
  ],
  cites: [
    "jones1985",
    "wenzl1988",
  ],
  tags: [
    "q-beta",
    "cos-resummation",
    "eigenphase-average",
    "markov-cyclicity",
    "classical-decategorification",
    "1ppb-roadmap",
    "prediction",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/qbeta/qbeta_cos_resummation_d_probe.py",
    witness: [
      "computations/qbeta/qbeta-cos-resummation-d.witness.json"
    ],
    status: "experimental",
  },
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-10-10",
      body: "*Until 2026-10-10 this block was stated in convention C, $z = 1/(\\sqrt q + 1/\\sqrt q) \\approx 0.4993203342$, with Form A as the base, and claimed a tightening of the CODATA residual from $+1677.5$ ppm to $+305.7$ ppm ($5.49\\times$; recomputed at the current proton pin, $+306.05$ ppm). It also stated that the classical cosine beats the $q$-deformed cosine by $\\approx 7$ ppm; that figure is convention-C and has not been re-measured under D.*",
    },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "status",
      body: "Per [`audit_delta_S_chain.py`](../../computations/audit_delta_S_chain.py),\nthe n-p mass-split residual $\\varepsilon_{\\Delta S}$ inherits\n$\\mathfrak{Q}_\\beta$'s residual through the algebraic chain identity\n\n$$\n  \\varepsilon_{\\Delta S}\n  \\;=\\;\n  \\frac{\\mathfrak{Q}_\\beta}{\\mathfrak{Q}_\\beta + m_e} \\cdot \\varepsilon_Q\n  \\;\\approx\\;\n  0.605\\,\\varepsilon_Q .\n$$\n\nUnder the cos resummation **in convention C on the retired Form A base (superseded 2026-10-10; C-measured, historical)**:\n$\\varepsilon_Q$ drops $1678 \\to 306$ ppm, and consequently\n$\\varepsilon_{\\Delta S}$ drops $1015 \\to 185$ ppm.  **Recomputed in convention D** (mpmath, proton pin, [`qbeta_cos_resummation_d_probe.py`](../../computations/qbeta/qbeta_cos_resummation_d_probe.py)): on the retired Form A base $\\varepsilon_{\\Delta S}$ goes $+1014.8 \\to +518.2$ ppm; on the **ruled** $z_D$ base it goes $-261056.6 \\to -261338.4$ ppm, i.e. away from zero.  Neither base is selected by residual.  This is one\nrung of the precision ladder toward the $1$ ppb target\n($\\varepsilon_Q \\approx 0.0017$ ppm).  The remaining $305$ ppm\ngap calls for the **3-irrep** extension: $V_{(3)}$ and\n$V_{(1,1,1)}$ contribute at $O(h^2)$ to $\\mathrm{tr}_M$ but are not yet\nincluded in the single-eigenphase resummation above.",
    },
    {
      kind: "status",
      body: "This proposition is **conditional** on\n[`prop:beta-decay-transfer-matrix`](#prop:beta-decay-transfer-matrix)'s\nidentification of $\\alpha = (z-1)h/2$ as the single-wrap eigenphase\non $V_{(2,1)}$.  The Lean class\n[`QOU.Interactions.QBetaCosResummation`](q-beta-cos-resummation.lean)\ncarries that identification as class hypotheses (trace and determinant\nof the $2\times 2$ restriction to $V_{(2,1)}$); the cos-resummation\ntheorem derives from them by rewriting the trace condition, with the\nconvention-C $5.49\\times$ tightening (superseded 2026-10-10; historical, in the\n[`q-beta-tightening-landscape`](../../computations/q-beta-tightening-landscape.witness.json)\nwitness) and the convention-D numbers in\n[`qbeta-cos-resummation-d`](../../computations/qbeta/qbeta-cos-resummation-d.witness.json).",
    },
    {
      kind: "status",
      date: "2026-09-03",
      body:
        "**Lean carrier restated (bean `qou-eixt`).**  The class previously carried two fields that hold for *every* real ($-2 \\le 2\\cos x \\le 2$ and $\\cos x = \\cos(-x)$), so it asserted nothing and every conditional result under it was unconditional; separately, the theorem's proof never mentioned the instance at all.  Both are fixed: the class now pins $\\operatorname{tr} M = 2\\cos\\alpha$ and $\\det M = 1$ on the $2 \\times 2$ restriction to $V_{(2,1)}$, and the theorem derives from that --- negative control: drop the hypothesis and the goal is unprovable.\n\n**This does not close the gap.**  Per [`EigenphaseCarrierVacuity`](../lean/QOU/QBeta/EigenphaseCarrierVacuity.lean) the obligation is a trichotomy: $M$ in the braid image is *excluded* (characters lie in $\\mathbb{Z}[q,q^{-1}]$, while $2\\cos((z-1)h/2)$ is transcendental over $\\mathbb{Q}(q,z)$); $M$ arbitrary is *circular* (the rotation $\\exp(\\alpha J)$ satisfies both fields, built from $\\alpha$ itself); and the Kohno--Drinfeld / KZ form of the third is **excluded too** --- [`HolonomySpectrumSignObstruction`](../lean/QOU/QBeta/HolonomySpectrumSignObstruction.lean) (2026-08-31, sorry-free) rules out every holonomy whose generator has real spectrum: such a character is $\\cosh a \\ge 1$ for every real $a$, while the required factor is $0.998399 < 1$, and Kohno--Drinfeld's own $\\hbar = 2\\ln q$ is hyperbolic at real $q_0$ ($\\det A = -(\\ln q_0)^2 < 0$).  What survives is narrower: a generator that is **elliptic** at real $q$ ($\\det A > 0$, $\\pm i\\theta$, $\\theta = 0.0565947$), tracked as condition D0 on beans `qou-pdix` / `qou-cds1`.  The present encoding is the second branch --- a real carrier rather than an empty one, but not evidence about the substrate.  **This note previously named branch 3 as the contentful one; that was written from a sibling file whose \u00a73 predates the obstruction, and is corrected here.**",
    },
    {
      kind: "status",
      date: "2026-10-10",
      body:
        "**Restated in convention D (bean `qou-zuva`).**  The block previously used $z_C = 1/(\\sqrt q + 1/\\sqrt q) \\approx 0.4993203342$ (excised) and Form A as base.  Recomputed at the proton pin, mpmath 50 dps, with $z_D = q^3/(q^2+1) \\approx 0.6126880371$: $\\alpha \\approx -0.0404857773$, $\\cos\\alpha \\approx 0.9991805629$.  On the **ruled** $z_D$ base ($0.4447004085$ MeV, $-431571.8$ ppm) the cos factor gives $0.4443360045$ MeV, $-432037.5$ ppm --- it moves the residual *away* from zero, as it must: $F_{\\mathrm{required}} > 1$ there while $\\cos\\alpha \\le 1$ (docs/audits/2026-09-13-formb-probe-adjudication-and-cds1-state.md \\S5.1).  On the **retired** Form A base the D-phase gives $+1677.6 \\to +856.8$ ppm ($1.96\\times$), against the convention-C $+1677.5 \\to +305.7$ ppm ($5.49\\times$; $+306.05$ at the current pin).  Neither base is selected by residual.  The downstream $\\varepsilon_{\\Delta S}$ figures ($1015 \\to 185$ ppm) above are convention-C; the convention-D recomputation is recorded beside them.  The Markov-cyclicity evenness argument relied on $z(1/q) = z(q)$, which fails for $z_D$, so evenness is no longer derived.",
    },
    {
      kind: "status",
      date: "2026-10-10",
      body:
        "**Lean sibling restated in convention D and producer replaced (bean `qou-zuva`).**  `eigenphase` now uses `markovZD q = q^3/(q^2+1)`, and the class `TransferMatrixEigenphase` and theorem `q_beta_cos_resummation` are stated with it.  The convention-C declarations are kept and labelled C-historical (`markovZC`, `eigenphaseC`, `eigenphaseC_bar_involution`, plus a deprecated legacy alias `eigenphase_bar_involution`).  New sorry-free D facts: `markovZD_bar_ne` ($z_D(q^{-1}) \\neq z_D(q)$ for $q > 0$, $q \\neq 1$), `eigenphase_bar_even_sum` ($\\alpha_D(q^{-1}) + \\alpha_D(q) = (q^2-1)^2/(2q^2)$), `eigenphase_not_bar_odd`.  The computation now points at the mpmath producer `computations/qbeta/qbeta_cos_resummation_d_probe.py`, which reproduces every number in the block and its table (max deviation $4.7 \\times 10^{-11}$ on values, $0.05$ ppm on residuals); the former producer `probe_q_beta_tightening_landscape.py` is convention C.",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The resummation lives in the real-$q$ (archimedean) regime of the framework's dilogarithm context-sorting, fixed once by the [$\\Phi_q$/AJ machinery identification](#prop:phi-q-aj-machinery-identification)." },
  ],
});
