import { remark } from "../../schema/builders";

export default remark({
  label: "rem:epistemic-status-of-calibrations",
  title:
    "Epistemic status of CAL-1, CAL-2, CAL-3 — what is genuinely derived vs what is pinned",
  interprets: "def:three-calibration-discipline",
  uses: [
    "prop:three-calibration-inputs",
    "def:three-calibration-discipline",
    "prop:self-dual-higgs-real-volume",
    "rem:qstar-decay-sector-q0",
  ],
  tags: [
    "calibration",
    "epistemology",
    "audit",
    "no-fitting",
    "cohomology",
    "open-derivation",
    "substrate-parameter",
  ],
  computation: {
    engine: "python",
    script: "computations/mu_substrate_tension_audit_100dps.py",
    witness: [
      "computations/q-pinning-50-digit.witness.json",
      "computations/mu-substrate-tension-audit-100dps.witness.json",
      "computations/per-observable-100x-status.witness.json",
      "computations/deuteron-from-scratch-ledger.witness.json",
      "computations/qbeta/qbeta-coherent-collapse-sinh-cosh.witness.json",
    ],
    status: "verified",
  },
  authorNotes: [
    {
      kind: "refined-framing",
      body: "An earlier version of the muon-anchor paragraph asserted that the neutron-decay observable supplies an independent third determination of q₀ and that the μ–p tension is a three-way test.",
    },
    {
      kind: "note",
      date: "2026-11-15",
      body: "**Excised (owner, 2026-11-15, D-W2).** The description of $\\mathfrak{Q}_\\beta$ as the bar-odd $\\sinh$ partner of the bar-even $\\cosh$ meson scale $m_\\pi$ was removed. No $\\mathfrak{Q}_\\beta$ functional on record has a definite bar parity under $q \\mapsto q^{-1}$: not Form A, not the $z = 1$ trace, and not the ruled $z_D$ trace. The two traces carry only an overall factor $h = q - q^{-1}$. No number, Lean declaration or producer depended on the label. Whether a bar-odd projection of the ruled trace carries such a role is bean `qou-hlx8`. Measurement: `docs/audits/2026-11-15-one-sided-weak-vertex.md` §4.",
      see: "https://github.com/litlfred/qou/blob/main/docs/audits/2026-11-15-one-sided-weak-vertex.md",
    },
    {
      kind: "status",
      date: "2026-09-04",
      body:
        "**Figure currency (supersedes the `~964×` in the 2026-06-16 note below, and the pre-CODATA-2022 literals this block carried until today).** " +
        "Every numeral in the prose is now either a `:val[…]` directive or traced to a live witness field:\n\n" +
        "- The muon-pin $q_0$ in the two-layer table and the $q_0 \\approx 1.10998$ in §CAL-2 are `:val[q_0]`, which reads " +
        "`derived_50_digit.q` of `computations/q-pinning-50-digit.witness.json` — the anchor-DEFINING witness that " +
        "`qou_substrate.witness._q0_value_for_anchor(\"muon\")` resolves. The literal previously written there, " +
        "`1.1099785955573347…`, is the pin **retired** by `fca08de7d2` (2026-08-22, owner ruling \"CODATA 2022 for muon\"); " +
        "the live value is `1.1099785956427390466817…`. Recorded on bean `qou-silm`.\n" +
        "- The CAL-2 ratio is `:val[m_mu_over_e]` ← `calibration_inputs.m_mu_over_e_str` = `206.7682827` (CODATA 2022). " +
        "The prose said `206.7682830`, which is CODATA 2018.\n" +
        "- $\\mu$–$p$ tension `11.5 → 11.6` ppb ← `data.leg_separation.substrate_tension_ppb = -11.6118085259` of " +
        "`mu-substrate-tension-audit-100dps.witness.json` (sign is proton-pin minus muon-pin; the prose quotes the magnitude).\n" +
        "- $\\sigma(m_p/m_e)$ `0.06 → 0.017` ppb ← `qou_substrate.constants.MASS_RATIO_P_E_ERR = 3.2e-8` on `1836.152673426`, " +
        "i.e. `1.743e-11`; the witness states it as prose in `calibration_inputs.m_p_over_e_source` (\"CODATA 2022 (0.017 ppb)\"). " +
        "`0.06 ppb` is the CODATA-2018 figure.\n" +
        "- Muon-anchored proton miss `roughly 4000σ → ≈ 1.4e4 σ` ← `deuteron-from-scratch-ledger.witness.json` " +
        /* <!-- literal-source: CODATA 2022 relative uncertainty on m_p/m_e = 3.2e-8 / 1836.152673426 = 0.01743 ppb --> */
        "`data.S2_nucleons.muon_anchor.err_m_p_ppb = -243.863` over that same `0.01743` ppb.\n" +
        "- The muon ratio's `22` ppb is unchanged and correct (`MASS_RATIO_MU_E_ERR = 4.6e-6` on `206.7682827` = `2.225e-8`), " +
        "as is the `9.5σ` (`211.16 / 22.25`). Note the L2 dashboard's `sigma_exp_ppb = 21.77` is the σ on the **mass** " +
        "$m_\\mu$, which gives `9.70σ`; the ratio σ is the right denominator for a residual on the ratio relation. " +
        "Different denominators, not a stale figure — do not \"reconcile\" them.\n\n" +
        "The `:val[…]` pinning is the durable half: the two figures that now read from the anchor witness cannot go stale " +
        "again. The ppb figures remain literals because no purpose-named scalar field carries them " +
        "(`substrate_tension_ppb` is signed; the `0.017 ppb` and the miss factor exist only as prose or as an " +
        "array-indexed dashboard row). Producer-side fix filed as bean `qou-m4au`.",
      see: "https://github.com/litlfred/qou/blob/claude/tender-keller-nvldp3/folio/quantum-observable-universe/observations/mu-p-residual-two-readings.md",
    },
    {
      kind: "status",
      date: "2026-06-16",
      body: "**Two-layer convention (owner-clarified 2026-06-16).** Canonical math triple = `(m_e, m_μ/m_e → q₀, m_π)`; **CAL-3 = `m_π`**, and **`$\\mathfrak{Q}$_β` is derived** (the CAL-2 proxy; `m_π` is the CAL-3 proxy). The §\"CAL-3\" section below discusses the *derived* `$\\mathfrak{Q}$_β`/`E₀` hadronic observable — its epistemic status is unchanged, but it is **not** a calibration; the third calibration is `m_π`. CAL-2 stays the canonical lepton ratio `m_μ/m_e` (it dimensionalises to `Vol(4₁)`); the **Physical-Observations** layer may numerically anchor `q₀` on the more-precise proton ratio `m_p/m_e` (re-pin 2026-05-28, `01c18125`), making `m_μ/m_e` a 9.5σ cross-check prediction — a precision substitution, not a change to CAL-2. (m_μ L2 status convention note: ratio-anchored meets 100× to noise; bare-categorical `4₁` Geom misses ~964×, PR #1556.) Live compute: `tools/qou-substrate/python/qou_substrate/constants.py`.",
      see: "https://github.com/litlfred/qou/blob/claude/gracious-lovelace-uzuovl/docs/audits/2026-06-16-q-anchor-drift-and-local-q-routes.md",
    },
    {
      kind: "refined-framing",
      date: "2026-06-26",
      body: "**Supersedes the 2026-06-16 note above (owner ruling 2026-06-26, PR #2866).** Canonical mathematical triple is the weak-sector bar-parity channels `(m_e, P_skew^β, P_avg^π)`, NOT three masses. CAL-3 = `P_avg^π` (proxy `m_π`); CAL-2 = `P_skew^β` (proxy `m_μ/m_e`). `$\\mathfrak{Q}$_β = ℏ/P_skew^β` is the **CAL-2 proxy**, not 'derived, not a calibration' — the §\"CAL-3\" section's epistemic assessment (can q₀ reproduce `$\\mathfrak{Q}$_β`?) stands, but the label is corrected.",
      see: "https://github.com/litlfred/qou/pull/2866",
    },
  ],
});
