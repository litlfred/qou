import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:three-calibration-inputs",
  title:
    "Exactly three calibration inputs: every observable factors through $m_e$, $m_\\pi$ and $q_0$",
  lean: {
    ref: "qou:QOU.BraidKnot.ThreeCalibrationFactorisation",
    validation: "not_checked",
  },
  cites: ["codata2022"],
  tags: [
    "calibration",
    "three-parameters",
    "mass-scale",
    "energy-scale",
    "substrate-parameter",
    "wedderburn",
    "cohomology",
    "no-fitting",
    "predictive-content",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): of the\n[three-calibration discipline](#def:three-calibration-discipline)" },
    {
      kind: "status",
      date: "2026-11-20",
      body: "**Demoted from `prop:three-calibration-inputs` (owner choice, 2026-11-20; bean qou-tm3c).** The statement is a universal claim about every canonical observable, and it is realised only case by case. Its former Lean, `three_calibration_inputs`, was `∃ f, obs = f q₀ m_e Q_β`, which every `obs` satisfies by taking `f` constant; it also listed $\\mathfrak{Q}_\\beta$ instead of $m_\\pi$. The carrier is now the class `QOU.BraidKnot.ThreeCalibrationFactorisation`, with the claim as its one open field and no instance. The definitional part (the three inputs, $q_0$ as a root) is [def:three-calibration-discipline](#def:three-calibration-discipline), which now also carries the CODATA calibration witnesses that used to hang on this block. The two older notes below describe the block before the change.",
    },
    {
      kind: "caveat",
      date: "2026-05-25",
      body: "**Structural-vs-empirical conflation.** The proposition correctly identifies the 3 cohomological degrees of freedom of $H_3(R, q)$ surviving the on-shell + gauge + observability quotient. The step from *\"3 cohomological degrees\"* to *\"3 external calibration inputs\"* is an independent choice, not forced by the categorical structure. Three stances are math-consistent: **(a)** 3 calibrations + 0 derivations [current paper position], **(b)** 1 unit choice + 2 cohomological derivations [research path], **(c)** 0 calibrations + 3 derivations [the ideal — requires substrate-$q_0$ derivation declined 2026-05-08, **reopened 2026-05-25**, plus the cohomological $\\mathrm{Vol}(4_1)/\\hbar_q^2$ identity for CAL-2 and Khovanov-Rozansky closure for CAL-3]. The forbidden-4th-CAL clause is preserved; this caveat does NOT propose a 4th input — it clarifies the epistemic status of the existing three. See [`rem:epistemic-status-of-calibrations`](../observations/epistemic-status-of-calibrations.md) + [`2026-05-25-cal-2-cohomological-vs-calibration-critique.md`](../../../docs/audits/2026-05-25-cal-2-cohomological-vs-calibration-critique.md).",
      see: "https://github.com/litlfred/qou/pull/1246",
    },
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "Lean sibling: archimedean specialisation over $\\mathbb{R}$ " +
        "(AGENTS.md §7c). This block *is* the archimedean interface, so the " +
        "$\\mathbb{R}$ is essential rather than incidental: the three fields " +
        "of `ThreeCalibrationInputs` are CODATA-measured **dimensional** " +
        "quantities ($m_e$ and $\\mathfrak{Q}_\\beta(n)$ in MeV, plus the " +
        "dimensionless ratio $m_\\mu/m_e$), which is the §7c table's " +
        "*CODATA / experimental value* row; the `m_e_pos` / " +
        "`m_mu_ratio_pos` / `Q_beta_n_pos` fields are order on measured " +
        "magnitudes; and `three_calibration_inputs` quantifies over " +
        "numerical observables `obs`. The pre-archimedean content the " +
        "narrative names — the $\\mathbb{Q}(q_0)$-element " +
        "$\\hat{\\mathcal{O}}(q_0) \\in \\mathbb{Z}[q_0^{\\pm 1/2}]$ that " +
        "every observable factors through, and the Wedderburn channel count " +
        "$3 = \\dim H^1(\\mathrm{Bring})$ — lives upstream in the Hecke / " +
        "cohomology layer, not here; only the two dimensional bridges to MeV " +
        "are archimedean. De-specialising to an abstract ordered field was " +
        "considered and rejected: it would type the CODATA anchors as " +
        "elements of an arbitrary field and obscure exactly the wall this " +
        "block marks.",
    },
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "**§7c base-ring-minimal adjudication (`q_zero⁻¹`, " +
        "`ThreeCalibrationInputs.lean:46`).** The advisory flags the ring " +
        "inverse in $\\hbar_q = 1 - q_0^{-1}$ as a candidate for a " +
        "division-free restatement over $\\mathbb{Z}[q^{\\pm 1}]$. Adjudged " +
        "**no change**: at the substrate layer $q_0^{-1}$ genuinely is a " +
        "Laurent monomial (a unit of $\\mathbb{Z}[q^{\\pm 1}]$, not a field " +
        "division), so there is nothing to restate — but this structure " +
        "records the *evaluation* of that Laurent datum at the archimedean " +
        "anchor, where the faithful reading is a real inverse. A " +
        "`Units`-coerced form here would assert invertibility of a measured " +
        "quantity, which is weaker information than the positivity already " +
        "carried.",
    },
  ],
});
