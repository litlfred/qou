import { remark } from "../../schema/builders";

export default remark({
  label: "rem:mu-p-residual-two-readings",
  title:
    "The $\\mu$–$p$ residual: two readings of a two-pin discrepancy, and what decides between them",
  interprets: "def:three-calibration-discipline",
  uses: [
    "rem:epistemic-status-of-calibrations",
    "prop:self-dual-higgs-real-volume",
  ],
  tags: [
    "calibration",
    "epistemology",
    "audit",
    "no-fitting",
    "open-derivation",
    "substrate-parameter",
    "falsifiability",
  ],
  computation: {
    engine: "python",
    script: "computations/mu_substrate_tension_audit_100dps.py",
    witness: [
      "computations/mu-substrate-tension-audit-100dps.witness.json",
      "computations/per-observable-100x-status.witness.json",
      "computations/q-pinning-50-digit.witness.json",
      "computations/probes/keystone-wlambda-vs-ylambda-projected-shift.witness.json",
      "computations/deuteron-from-scratch-ledger.witness.json",
      "computations/m-tau-volume-target.witness.json",
      "computations/mu-p-cyclotomic-ladder-magnitude.witness.json",
      "computations/brng-two-row-dominant-block-a6.witness.json",
    ],
    status: "verified",
  },
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-03",
      body:
        "**Provenance.** Numbers: `computations/mu-substrate-tension-audit-100dps.witness.json` " +
        "(pin separation `data.delta_q0_canonical_minus_mu_anchored.delta_q0_ppb = -11.61`; muon-side " +
        "residual `data.residual_ppb_at_canonical_q0 = 211.16`; inversion-floor ratio " +
        "`data.leg_separation.tension_over_residual = 5157`; the assertion " +
        "`h1_propagated_shift_reproduces_observed_residual` is the statement that the residual is the " +
        "pin separation propagated through the lepton relation); " +
        "`computations/per-observable-100x-status.witness.json` (`m_mu`: `err_ppb 211.2`, " +
        "`target_100x_ppb 0.2177`, `miss_factor 970.2` — the sibling `sm-params-lepton-masses` block " +
        "still quotes the pre-CODATA-2022 963.6x); the order-window probe " +
        "`docs/audits/scripts/mu_p_carrier_order_window_probe.py`, which emits no witness (re-run " +
        /* <!-- literal-source: mu_p_carrier_order_window_probe.py audit script output (no witness file emitted, noted above) --> */
        "2026-09-03 at the CODATA-2018 ratio it hard-codes: `t = 2.0975e-7`, 9.534 sigma, " +
        "`sigma_exp/t = 10.49 %`, `c_6 = 0.2217`, `c_7 = 2.2375`, `t/w^3 = 0.1621`, `t/w^4 = 14.877`, " +
        "window 20.98 %; re-measured at the package-layer CODATA-2022 ratio: `t = 2.1121e-7`, " +
        /* <!-- literal-source: mu_p_carrier_order_window_probe.py audit script output at CODATA-2022 ratio (no witness file) --> */
        "9.49 sigma, 10.53 %, `c_6 = 0.2232`, `c_7 = 2.2529`, `t/w^3 = 0.1632`, `t/w^4 = 14.98`, " +
        "window 21.07 % — the prose quotes the CODATA-2022 values; the 2018 run differs in the third " +
        "significant figure of c_7 and t/w^3); and " +
        "`computations/probes/keystone-wlambda-vs-ylambda-projected-shift.witness.json` " +
        "(`data.over_210ppb_factor = 3.35e6`, `data.bar_parity = even`: the projector-weight-shift " +
        "exclusion is on magnitude alone — its earlier bar-mixed leg was withdrawn 2026-08-30, bean " +
        "`qou-j3u0`, so the prose does not repeat it). The proton-side residual is witnessed in " +
        "`computations/deuteron-from-scratch-ledger.witness.json` (`muon_anchor.err_m_p_ppb = -243.86`, " +
        "both anchors live); its sigma count (about 1.4e4 sigma) uses the CODATA-2022 `m_p/m_e` " +
        "uncertainty 0.017 ppb from `qou_substrate.constants`; the 'roughly 4000 sigma' in the sibling " +
        "epistemic-status remark is the CODATA-2018 (0.06 ppb) figure. The `hbar_q` literal 0.0991 in " +
        "the prose is the proton-pin value (0.09908171604, order-window probe); the registry's `hbar_q` " +
        "entry is the muon-pin witness value and was deliberately not used, to keep the block on one " +
        "pin. Beans: `qou-6au4` (convention-independence: the tension is already the convention-D " +
        "number), `qou-6gf9` (the three prunes: order window, bar parity, entropy), `qou-8t3k` " +
        "(attack-option roast: a direct re-fit of the residual is foreclosed). Audits: " +
        "`docs/audits/2026-08-24-mu-p-tension-is-already-convention-d.md`, " +
        "`docs/audits/2026-08-01-mu-p-tension-attack-recon-floor-verdict.md`, " +
        "`docs/audits/2026-08-08-mu-p-residual-carrier-order-and-bar-parity-prune.md`. Lean cited in " +
        "the prose: `QOU.BraidKnot.MuPCarrierOrderWindow.order_window`, " +
        "`QOU.BraidKnot.MuPCarrier.hbarGen_bar`, `hbarGen_monomial_bar_even`, " +
        "`hbarGen_six_bar_even_dressing` (all sorry-free per the files' own verification notes). " +
        "The w-tower exclusion the prose cites as measured is now also Lean-proved, sorry-free: " +
        "`QOU.BraidKnot.MuPCorrectionAdmissibility` (`bar_even_monomial_iff`, the converse half of the " +
        "selection rule; `no_small_height_w_monomial`; `no_bar_even_small_height_monomial`; " +
        "`GapA4CorrectionAdmissible` with `monomial_not_admissible`) — cited in the prose.",
    },
  ],
});
