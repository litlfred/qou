import { definition } from "../../schema/builders";

export default definition({
  label: "def:three-calibration-discipline",
  title:
    "Three-calibration discipline ($m_e$, $m_\\mu/m_e$, $m_\\pi$) and the calibrated substrate parameter $q_0$",
  tags: [
    "calibration",
    "dimensional-analysis",
    "substrate-parameter",
    "mass",
    "binding-energy",
    "beta-decay",
    "cohomology",
    "audit",
  ],
  // Pure definition since 2026-11-20 (owner choice, bean qou-tm3c). The
  // factorisation claim that used to live here is
  // conj:three-calibration-inputs; the H^1(Bring) alignment is
  // conj:calibration-cohomology-alignment. Neither is used by the definition.
  uses: [
    "def:substrate-parameter",
    "def:quantum-planck-constant",
    "prop:meson-scale-independence",
  ],
  cites: [
    "jones1985",
    "kock2004",
    "wenzl1988",
  ],
  lean: { ref: "qou:QOU.Observations.CalibrationTriple" },
  // Moved here from conj:three-calibration-inputs 2026-11-20 (bean qou-tm3c):
  // the producers compute the calibration inputs themselves.
  computation: {
    engine: "python",
    script: "computations/codata_masses.py",
    // Second witness produced by computations/build_cal_3_q_beta_witness.py
    // (CAL-3 Q_beta(n) source-of-truth JSON).
    witness: [
      "computations/codata-masses.witness.json",
      "computations/cal-3-q-beta.witness.json",
    ],
    consumers: [
      "computations/sweeps/paper_six_term_isotope_sweep.py",
    ],
    status: "verified",
  },
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-20",
      body: "**Split into a definition and two conjectures (owner choice, 2026-11-20; bean qou-tm3c).** This block used to be a `definition` that also asserted that every hadronic mass factors as $m_e^{a} m_\\pi^{c} Q_X(q_0)$. That assertion is a universal claim, not a definition. Its Lean was a class whose headline theorem returned the assumed field `mass_factorisation`. The claim is now [conj:three-calibration-inputs](#conj:three-calibration-inputs), and the $H^1(\\mathrm{Bring})$ alignment is [conj:calibration-cohomology-alignment](#conj:calibration-cohomology-alignment). What remains here is definitional: the three inputs, and $q_0$ as the unique root $q > 1$ of the CAL-2 equation. Existence and uniqueness of that root are proved sorry-free in `QOU.Observations.CalibrationTriple.q0_spec` and `q0_unique`. The older notes below describe the block before the split.",
    },
    {
      kind: "note",
      date: "2026-11-15",
      body: "**Excised (owner, 2026-11-15, D-W2).** The description of $\\mathfrak{Q}_\\beta$ as the bar-odd $\\sinh$ partner of the bar-even $\\cosh$ meson scale $m_\\pi$ was removed. No $\\mathfrak{Q}_\\beta$ functional on record has a definite bar parity under $q \\mapsto q^{-1}$: not Form A, not the $z = 1$ trace, and not the ruled $z_D$ trace. The two traces carry only an overall factor $h = q - q^{-1}$. No number, Lean declaration or producer depended on the label. Whether a bar-odd projection of the ruled trace carries such a role is bean `qou-hlx8`. Measurement: `docs/audits/2026-11-15-one-sided-weak-vertex.md` §4.",
      see: "https://github.com/litlfred/qou/blob/main/docs/audits/2026-11-15-one-sided-weak-vertex.md",
    },
    {
      kind: "caveat",
      date: "2026-05-25",
      body: "**The cohomological mapping is structural; the calibration *choice* is independent.** The proposition maps $m_e \\leftrightarrow$ the $W$-plane scale, $q_0 \\leftrightarrow$ the $W$-plane modulus (anchored by the lepton ratio $m_\\mu/m_e$), and $m_\\pi \\leftrightarrow$ the orthogonal $\\mathrm{Vol}(\\mathrm{Hopf})=0$ meson class — the three real degrees of freedom of $H^1 = 2W$ (see [`conj:calibration-cohomology-alignment`](../mass-theory/calibration-cohomology-alignment.md)). These are categorically forced. That they are pinned by CODATA/PDG values *rather than derived structurally* is an independent stance. Open derivation work in flight: PR #1127 (CAL-3 net-ansatz finding), PR #1246 (CAL-2 self-referential critique), and the substrate-$q_0$ workplan (re-opened 2026-05-25). See [`rem:epistemic-status-of-calibrations`](epistemic-status-of-calibrations.md) for the unified accounting per-CAL.",
      see: "https://github.com/litlfred/qou/pull/1246",
    },
    {
      kind: "refined-framing",
      date: "2026-06-16",
      body: "**Two-layer calibration convention (owner-clarified 2026-06-16).** The **canonical mathematical** calibration triple is `(m_e, m_μ/m_e → q₀, m_π)` with `$\\mathfrak{Q}$_β` **derived** (the CAL-2 proxy; `m_π` is the CAL-3 proxy). In the **Physical-Observations** layer one may substitute a *derived* quantity of smaller experimental error for a calibration — concretely `q₀` is numerically anchored on the proton ratio `m_p/m_e` (0.06 ppb vs the muon ratio's 22 ppb; live solver `tools/qou-substrate/python/qou_substrate/constants.py::q_at`, re-pin 2026-05-28), making `m_μ/m_e` a `9.5σ` cross-check prediction (the μ–p substrate tension). This is a precision substitution, **not** a change to the canonical CAL-2. CAL-3 = `m_π` is forced because `m_π` is provably independent of `(m_e, q₀)` (`Vol(Hopf)=0`) whereas `$\\mathfrak{Q}$_β = m_e·|q₀²−2q₀−1|(q₀+1)/(2q₀³)` is a function of CAL-1+CAL-2. **Remaining ripple:** `conj:three-calibration-inputs` still carries the older neutron-width (`P_skew^β`, h²) framing for CAL-2 — reconciled in the same PR to the canonical lepton-ratio framing.",
      see: "https://github.com/litlfred/qou/blob/claude/gracious-lovelace-uzuovl/docs/audits/2026-06-16-q-anchor-drift-and-local-q-routes.md",
    },
    {
      kind: "refined-framing",
      date: "2026-06-26",
      body: "**Supersedes the 2026-06-16 note above (owner ruling 2026-06-26, PR #2866).** The ideal *mathematical* canonical calibration triple is the weak-sector bar-parity channel observables `(m_e, P_skew^β, P_avg^π)`, NOT three masses. CAL-2 = `P_skew^β` (neutron β-sector bar-skew channel, h²); CAL-3 = `P_avg^π` (pion-sector bar-even channel, h³). The masses `(m_e, m_μ/m_e, m_π)` and `$\\mathfrak{Q}$_β = ℏ/P_skew^β` are the numerical *proxies*; `$\\mathfrak{Q}$_β` is the **CAL-2 proxy**, not 'derived, not a calibration'. The modulus is overdetermined and pinned most precisely by `m_μ/m_e`, so `$\\mathfrak{Q}$_β` reproduced from q₀ is a 0.17% cross-check. The 2026-06-16 'reconciliation to the lepton-ratio framing' is reversed: the `P_skew^β` framing is canonical.",
      see: "https://github.com/litlfred/qou/pull/2866",
    },
  ],
});
