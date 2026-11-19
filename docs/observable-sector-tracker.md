# QOU observable sector tracker (updated 2026-07-06)

**Purpose:** single-source-of-truth tracker for every QOU observable
across the standard-model sectors (leptons, quarks, mesons, baryons,
nuclei, fundamental constants), recording the canonical-derivation
status, production-wiring status, and best-known residual.

**Authoring contract:** every row cites (a) the canonical formula or
"open"; (b) the Lean theorem / proposition .md if proved; (c) the
production script + witness; (d) the L2-dashboard residual (post
this-session work, b78… commit on main + #1452/#1451 effects); (e) the
honest discipline call (DERIVED / PARTIAL / OPEN / NUMEROLOGY).

> **READ-ONLY:** future agents update this table by editing it directly.
> Author note: I keep finding gaps — this tracker is the place to record
> them once so we don't re-discover them.

> ## ⚠ c_k / d_k saga RESOLVED (2026-05-31) — read before editing precision rows
>
> The recurring "flip-flop" on the Q_β c_k and m_p d_k coefficients is
> **closed with a discipline verdict**: they are **stale-q₀
> near-matches, not derivations.** Two decisive tests settle it:
>
> - **c_k (item 1, `qbeta-delta-tr-vs-formA.witness.json`):** the Habiro
>   Δtr_M is NOT Form A's net-winding slot (leading Taylor orders differ,
>   −5/4 vs −2; substituting it misses CODATA by −240000 ppm). The bridge
>   `Q_β = m_e·f(Δtr_M, q)` is a genuine OPEN derivation.
> - **d_k (item 2, `mp-dk-decisive-test.witness.json`):** d_4 = 46 drifts
>   **100%** between the muon-pin and m_p-pin q₀; at canonical q₀ the bare
>   m_p formula is already 0.0092 ppb, so the "242 ppb gap" the d_k closed
>   was itself a stale-pin artifact.
>
> **Only `c_2 = -1` is Taylor-exact and wired.** All N≥3 c_k / d_k forms
> (J_Hopf, J−ℏ², c_3·b⁴, d_4=46, …) are structural near-matches locked
> behind §3b-cond conditional classes (`QbetaC3StructuralFormClass`,
> `QbetaHabiroTaylorBridgeClass`), NOT production derivations. Earlier
> "6.02 ppb clean Q_β / 5-of-7" claims in this file were stale-q₀
> artifacts and are corrected below. Authoritative ledger:
> `docs/audits/2026-05-30-qbeta-ck-mp-dk-deep-audit.md` (read the
> ADDENDUM, not the body).

> ## 🛑 m_p de-fit (2026-07-04) — read before citing any m_p row
>
> m_p's former "0.0004 ppb / beats 100×" status rode the **fitted Habiro
> tower** `(1+46u⁴)(1+4u⁵)(1−29u⁶)` — a muon-era CODATA fit left applied
> to the proton-pinned q₀ (a live +242 ppb regression). The tower was
> **dropped** (PR #3280); the honest documented-pin round-trip is
> **+1.35 ppb**, a **~437× miss** of the 100× target. Authoritative L2
> count: **1/5 scoreable** (`m_K/m_π` alone) per
> `computations/per-observable-100x-status.witness.json`
> (`beats_100x_scoreable=1`, `scoreable_total=5`). `beats_100x_count=2`
> counts the calibration **inputs** `m_p` and `m_e` and must not be quoted
> as an accuracy result (corrected 2026-08-18). Full analysis:
> [`docs/audits/2026-07-04-c4-mu-p-tension-pin-dependence.md`](audits/2026-07-04-c4-mu-p-tension-pin-dependence.md).
> Table + m_p rows below corrected 2026-07-06; Q_β/m_n/Δ_pn residuals
> refreshed from the live witness at the same time.

## L2 100× dashboard (proton-anchored convention; see AGENTS.md §"q₀ anchor convention")

| observable | role | pred err | σ_exp (=100×/100) | beats 100×? | beats 1×? |
|------------|------|--------:|------:|:----:|:----:|
| m_e | CAL-1 anchor | {{ qou.computations.per-observable-100x-status.data.rows.6.err_ppb }} ppb | {{ qou.computations.per-observable-100x-status.data.rows.6.sigma_exp_ppb }} ppb | ✓ (anchor) | ✓ (anchor) |
| m_p | CAL-2 numerical anchor (m_p/m_e re-pin) | **{{ qou.computations.per-observable-100x-status.data.rows.0.err_ppb }} ppb** (anchor round-trip) | {{ qou.computations.per-observable-100x-status.data.rows.0.sigma_exp_ppb }} ppb | N/A (anchor) | N/A (anchor) |
| m_μ | validation (proton-anchored prediction; 2-term Borromean QED at $q_{2\mathrm{t}}$ / 1-term pin $q_{1\mathrm{t}}$) | **{{ qou.computations.per-observable-100x-status.data.rows.1.err_ppb }} ppb** (2-term QED) / {{ qou.computations.per-observable-100x-status.data.rows.1.one_term_q1t_baseline.err_ppb }} ppb (1-term) | {{ qou.computations.per-observable-100x-status.data.rows.1.sigma_exp_ppb }} ppb | ✗ ({{ qou.computations.per-observable-100x-status.data.rows.1.miss_factor }}× / 970.2×) | **✓ (2-term, +0.370σ)** / ✗ (1-term) |
| m_K/m_π | validation (meson; full EM log-series `1 + log(1+ℏ_q)` with Form-B $\alpha_{\mathrm{EM}}(q_0)$) | **{{ qou.computations.per-observable-100x-status.data.rows.7.err_ppb }} ppb** (`0.00195 σ_exp`) | {{ qou.computations.per-observable-100x-status.data.rows.7.sigma_exp_ppb }} ppb | ✓ (5.13× margin) | ✓ |
| Q_β | derived (CAL-1+2; Wave-2 Convention-D `z_D` re-score: $C_{\mathrm{KD}}^{(6)}(q_{2\mathrm{t}}) + \alpha_D^{\mathrm{proj}} + \Delta m_{\mathrm{QED,conn}}$) | **{{ qou.computations.per-observable-100x-status.data.rows.2.err_ppb }} ppb** (1-term bare `z_D`: {{ qou.computations.per-observable-100x-status.data.rows.2.bare_zD_1term_baseline.err_ppb }} ppb) | {{ qou.computations.per-observable-100x-status.data.rows.2.sigma_exp_ppb }} ppb | ✗ ({{ qou.computations.per-observable-100x-status.data.rows.2.miss_factor }}×) | ✗ |
| m_n | validation (Wave-2 Convention-D `z_D` re-score / Kashiwara $b^2$ + 2-term QED) | **{{ qou.computations.per-observable-100x-status.data.rows.3.err_ppb }} ppb** (`z_D` Wave-2) / **{{ qou.computations.per-observable-100x-status.data.rows.3.two_term_qed_diagnostics.substrate_identity_m_n_2term_plain_err_ppb }} ppb** (Kashiwara $b^2$ + 2-term QED) | {{ qou.computations.per-observable-100x-status.data.rows.3.sigma_exp_ppb }} ppb | ✗ ({{ qou.computations.per-observable-100x-status.data.rows.3.miss_factor }}×) | ✗ |
| Δ_pn | validation (Wave-2 Convention-D `z_D` re-score: $C_{\mathrm{KD}}^{(6)}(q_{2\mathrm{t}}) + \alpha_D^{\mathrm{proj}} + \Delta m_{\mathrm{QED,conn}}$) | **{{ qou.computations.per-observable-100x-status.data.rows.4.err_ppb }} ppb** (1-term bare `z_D`: {{ qou.computations.per-observable-100x-status.data.rows.4.bare_zD_1term_baseline.err_ppb }} ppb) | {{ qou.computations.per-observable-100x-status.data.rows.4.sigma_exp_ppb }} ppb | ✗ ({{ qou.computations.per-observable-100x-status.data.rows.4.miss_factor }}×) | ✗ |
| α_EM⁻¹ | validation (gauge coupling; Form-B Bring–Schwinger cubic at proton-anchored $q_0$) | **-{{ qou.computations.per-observable-100x-status.data.rows.5.err_ppb }} ppb** (`2.38 σ_exp`) | {{ qou.computations.per-observable-100x-status.data.rows.5.sigma_exp_ppb }} ppb | ✗ ({{ qou.computations.per-observable-100x-status.data.rows.5.miss_factor }}×) | ✗ |
| v_EW ($G_F$) | validation (electroweak Fermi scale; Bring–Schwinger fixed point $N_v = v/m_p$) | **{{ qou.computations.per-observable-100x-status.data.rows.8.err_ppb }} ppb** (`{{ qou.computations.probes.electroweak-bring-schwinger-bridge.data.electroweak_vev_fixed_point.v_err_sigma | precision: 3 }} σ_exp`) | {{ qou.computations.per-observable-100x-status.data.rows.8.sigma_exp_ppb }} ppb | ✗ ({{ qou.computations.per-observable-100x-status.data.rows.8.miss_factor }}×) | **✓ (-0.114σ)** |

**Net: `{{ qou.computations.per-observable-100x-status.data.summary.beats_100x_scoreable }}/{{ qou.computations.per-observable-100x-status.data.summary.scoreable_total }}` scoreable predictions beat 100×** — `m_K/m_π` alone (`{{ qou.computations.per-observable-100x-status.data.rows.7.err_ppb }} ppb`, `0.00195 σ_exp` with Form-B $\alpha_{\mathrm{EM}}(q_0)$; CS-tower baseline `{{ qou.computations.per-observable-100x-status.data.rows.7.cs_tower_ansatz_baseline.err_ppb }} ppb`; the two-term truncation `23.44 ppb` was excised on 2026-08-22 in PR #5467). (`m_p` and
`m_e` are calibration inputs, not predictions; the raw `{{ qou.computations.per-observable-100x-status.data.summary.beats_100x_count }}/{{ qou.computations.per-observable-100x-status.data.summary.total }}` counts them.
Corrected 2026-08-18.)
m_μ is a **proton-anchored prediction** that beats $1\times$ at `+{{ qou.computations.per-observable-100x-status.data.rows.1.err_ppb }} ppb` (`+0.370 σ_exp`, miss factor `{{ qou.computations.per-observable-100x-status.data.rows.1.miss_factor }}×`) at the consistent 2-term proton pin $q_{2\mathrm{t}} = {{ qou.computations.per-observable-100x-status.data.rows.1.two_term_qed_diagnostics.q0_two_term_plain | precision: 15 }}$ under the Wave-2 two-term Borromean QED self-energy $M_p^{\mathrm{QED,conn}} = +{{ qou.computations.per-observable-100x-status.data.rows.1.two_term_qed_diagnostics.M_p_QED_conn_plain_keV | precision: 6 }}\,\mathrm{keV}$ (`QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_QAdjp_borromeanV3`), closing the 1-term $q_{1\mathrm{t}}$ μ–p substrate tension (`{{ qou.computations.per-observable-100x-status.data.rows.1.one_term_q1t_baseline.err_ppb }} ppb = 9.70 σ_exp`).
Q_β / m_n / Δ_pn are scored on the owner-authorised Wave-2 Convention-D `z_D = q³/(q²+1)` re-score (`qou-iagg`: 6-th order Kashiwara–Demazure ladder $C_{\mathrm{KD}}^{(6)}(q_{2\mathrm{t}})$, mirror-projected $\alpha_D^{\mathrm{proj}} = \alpha_D - h^2/4$, and connected Borromean QED splitting $\Delta m_{\mathrm{QED,conn}}$ at $q_{2\mathrm{t}}$), giving `{{ qou.computations.per-observable-100x-status.data.rows.2.err_ppb }}` / `{{ qou.computations.per-observable-100x-status.data.rows.3.err_ppb }}` / `{{ qou.computations.per-observable-100x-status.data.rows.4.err_ppb }} ppb` (a $1{,}172\times$ reduction from the 1-term bare-$z_D$ baseline `{{ qou.computations.per-observable-100x-status.data.rows.2.bare_zD_1term_baseline.err_ppb }}` / `{{ qou.computations.per-observable-100x-status.data.rows.3.bare_zD_1term_baseline.err_ppb }}` / `{{ qou.computations.per-observable-100x-status.data.rows.4.bare_zD_1term_baseline.err_ppb }} ppb`, and superseding the retired convention-C `z = 1` laddered `1248` / `2.389` / `755.6 ppb` and `658 ppb` figures). On the Kashiwara $b^2$ substrate identity (`m-p-substrate-identity-50dps.witness.json`), including the connected Borromean QED splitting $\Delta m_{\mathrm{QED,conn}} = {{ qou.computations.per-observable-100x-status.data.rows.3.two_term_qed_diagnostics.Delta_m_QED_conn_plain_keV | precision: 6 }}\,\mathrm{keV}$ reduces the $m_n$ residual by `{{ qou.computations.per-observable-100x-status.data.rows.3.two_term_qed_diagnostics.substrate_identity_residual_reduction_pct }}%` (from `+{{ qou.computations.per-observable-100x-status.data.rows.3.two_term_qed_diagnostics.substrate_identity_m_n_1term_err_ppb }} ppb` to `+{{ qou.computations.per-observable-100x-status.data.rows.3.two_term_qed_diagnostics.substrate_identity_m_n_2term_plain_err_ppb }} ppb`).

---

## I. Leptons

| observable | canonical formula | Lean proof | production | residual | status |
|---|---|---|---|---|---|
| **m_e** | CAL-1 anchor (CODATA 2022) | — | `codata_masses.py` → `codata-masses.witness.json` | 0 ppb (anchor) | DERIVED (anchor) |
| **m_μ / m_e** | `Vol(4_1) / ℏ_q²` | `mass-formula-validation.md`, Lean `m_mu_over_m_e_via_vol_4_1` | `m_p_borromean_verification_50dps.py` | exact at q₀ | DERIVED |
| **m_μ** | `m_e · (m_μ/m_e)` | derived | proton-anchored prediction (μ–p tension) | 211.2 ppb (**9.70σ** on the MASS σ) | PREDICTION (not anchor) |
<!-- Both m_μ rows above read `209.8 ppb (9.5σ)` until 2026-09-14. Two separate
     corrections, and they are not the same kind of thing:
       1. 209.8 -> 211.2 ppb is genuine STALENESS — 209.8 is the CODATA-2018
         residual; the muon anchor moved to CODATA 2022 on 2026-08-22
         (fca08de7d2). Live source: per-observable-100x-status.witness.json,
         rows[] where obs == "m_mu", err_ppb 211.2. This tracker was missed by
         the qou-m4au drain, which swept AGENTS.md, docs/precision-goals.md and
         two content blocks.
       2. 9.5 -> 9.70 sigma is NOT staleness, it is the DENOMINATOR. One
         residual, two published sigma: 211.20/21.768 = 9.7022 against the
         sigma on the MASS m_mu (witness sigma_exp_ppb 21.77), and
         211.20/22.247 = 9.4934 against the sigma on the RATIO m_mu/m_e
         (constants.MASS_RATIO_MU_E_ERR 4.6e-6 over 206.7682827). These rows
         name the MASS and quote the dashboard's mass-denominated ppb, so 9.70
         is the figure that belongs here. Corpus sites that say 9.5 sigma of
         the RATIO are correct as written and must NOT be swept — adjudicated
         in epistemic-status-of-calibrations.ts authorNotes (bean qou-silm)
         and restated in AGENTS.md ss q0-anchor convention. -->
| **m_τ** | `m_e · (Vol(4_1) / ℏ_q²)²` (?) — **claimed** but not pin-tight | `m-tau-knot-prediction.md` | `m_tau_knot_prediction.py` | ~few % off | **PARTIAL** — has prediction, not in 100× dashboard, not Lean-proved |
| **m_e generations** (electron family relationships) | — | — | — | — | OPEN — no canonical chain for the 3-generation structure |

**Lepton gaps:**
- m_τ needs the same 100× treatment as μ/e. The single-step formula
  (Vol(4_1) / ℏ_q²)² is suspect — likely needs a separate categorical
  derivation for generation-2 → generation-3.
- The 3-generation lepton mass hierarchy as a whole is structurally
  open (no canonical proposition deriving why exactly 3 generations).

---

## II. Quarks

| observable | canonical formula | Lean proof | production | residual | status |
|---|---|---|---|---|---|
| **m_u** | — | — | — | — | OPEN — confined, not directly observable as a mass; framework derives only meson masses (containing quarks) |
| **m_d** | — | — | — | — | OPEN (same) |
| **m_s / m_d** | `2[3]_q[4]_q − 1` ≈ 24 (#1438 audit refuted as bare-knot ratio) | — | `derive_ms_md_torus_knot.py` (refutation) | ~34% miss | OPEN — quark mass ratios are confinement-dressed; bare-knot route refuted |
| **m_c, m_b, m_t** | — | — | — | — | OPEN — generation structure |

**Quark gaps:** All bare quark masses are off the production pipeline
(confined sector). The only observable mass route is via meson bound
states (next section).

---

## III. Mesons

| observable | canonical formula | Lean proof | production | residual | status |
|---|---|---|---|---|---|
| **m_π** | CAL-3 numerical anchor | — | `cal-3-q-beta.witness.json` (cited) | (anchor) | DERIVED (anchor) |
| **m_K² / m_π²** | `[3]_q · [4]_q + (α_em/π) · (1 + log(1+ℏ_q))` | Lean `meson_qCG_3x4` (strong core only) | dashboard `per_observable_100x_status.py` | **51.48 ppb** (under 264-ppb target, 5.1× margin) | **CONDITIONAL** — see note below |
| **m_K / m_π** | `√(m_K²/m_π²)` | — | dashboard (scored) | **51.48 ppb**, beats the 263.6-ppb target | **CONDITIONAL** — see note below |

> **🛑 De-fitted 2026-08-22 — and NOT unconditionally derived (PR #5467).**
> The EM factor was `(3q²−1)/(2q²)`, which is exactly the two-term
> truncation `1 + ℏ_q − ℏ_q²/2` of `1 + log(1+ℏ_q)`. Measured stopping-order
> error is 479.11 / **23.45** / 53.55 / 51.31 / 51.49 / 51.474 / 51.4755 ppb
> for ℏ¹…ℏ⁷, converging to **51.4754 ppb**: order 2 is the *only* order below
> the limit, a non-monotonic dip, so the stopping point was chosen against
> the data. The owner ruled the full series canonical on **2026-08-09**
> (`docs/precision-goals.md` §L2) but no producer was updated until #5467,
> so this row read **23.44 ppb / DERIVED** for 13 days.
>
> Two knobs remain, so the status is **CONDITIONAL**, not DERIVED:
> the `(3,4)` pair is **scan-selected**, and `α_em` is **conditional on the
> open Witten-κ `sorry`**. The strong core alone misses the target by 385×.
> Red-team: [`2026-08-22-mK-mpi-l2-red-team.md`](audits/2026-08-22-mK-mpi-l2-red-team.md).
| **m_η, m_φ** | GMOR-class squared ratios | (some structure in #1442/#1396) | `meson_eta_phi_gmor.py` | — | PARTIAL — probes exist, not in dashboard |
| **m_D, m_B (heavy mesons)** | — | — | — | — | OPEN — no canonical chain |

**Meson gaps:**
- η, φ, ρ have probes but no production-dashboard scoring.
- Heavy-flavor mesons (D, B) entirely open.

---

## IV. Baryons / Nucleons

| observable | canonical formula | Lean proof | production | residual | status |
|---|---|---|---|---|---|
| **m_p** | CAL-2 numerical anchor; substrate-identity `m_p = m_e · 2Vol/ℏ_q² · F_Bor − 12` (1-term) and `M_p = M_p^QCD + M_p^QED,conn` (2-term Borromean QED at $q_{2\mathrm{t}}$) | `m-p-substrate-identity-50dps.witness.json`, `QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_QAdjp_borromeanV3` | `m_p_substrate_identity_50dps.py` | **{{ qou.computations.per-observable-100x-status.data.rows.0.err_ppb }} ppb** (anchor round-trip); $M_p^{\mathrm{QED,conn}} = +{{ qou.computations.per-observable-100x-status.data.rows.1.two_term_qed_diagnostics.M_p_QED_conn_plain_keV | precision: 6 }}\,\mathrm{keV}$ shifts $q_0 \to q_{2\mathrm{t}}$ and brings $m_\mu$ to **+{{ qou.computations.per-observable-100x-status.data.rows.1.err_ppb }} ppb** (+0.370σ) | DERIVED (CAL-2 anchor round-trip; 2-term Borromean QED self-energy proved) |
| **m_n** | Path C: `m_n = m_p + Q_β + m_e` (Wave-2 Convention-D `z_D` re-score) and Kashiwara $b^2$ + 2-term Borromean QED splitting $\Delta m_{\mathrm{QED,conn}} = {{ qou.computations.per-observable-100x-status.data.rows.3.two_term_qed_diagnostics.Delta_m_QED_conn_plain_keV | precision: 6 }}\,\mathrm{keV}$ | `QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_QAdj_connected_diff_borromeanV3` | `per_observable_100x_status.py`, `m_p_substrate_identity_50dps.py` | **{{ qou.computations.per-observable-100x-status.data.rows.3.err_ppb }} ppb** (Wave-2 Convention-D `z_D` re-score; 1-term bare `z_D`: {{ qou.computations.per-observable-100x-status.data.rows.3.bare_zD_1term_baseline.err_ppb }} ppb); **+{{ qou.computations.per-observable-100x-status.data.rows.3.two_term_qed_diagnostics.substrate_identity_m_n_2term_plain_err_ppb }} ppb** (Kashiwara $b^2$ + 2-term QED, reduced 70.40% from +{{ qou.computations.per-observable-100x-status.data.rows.3.two_term_qed_diagnostics.substrate_identity_m_n_1term_err_ppb }} ppb) | DERIVED (composed); primary score on Wave-2 Convention-D `z_D` re-score (`qou-iagg`) |
| **Δ_pn** | derived from `m_n − m_p = Q_β + m_e` (Wave-2 Convention-D `z_D` re-score: $C_{\mathrm{KD}}^{(6)}(q_{2\mathrm{t}}) + \alpha_D^{\mathrm{proj}} + \Delta m_{\mathrm{QED,conn}}$) | `QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_QAdj_connected_diff_borromeanV3` | `per_observable_100x_status.py` | **{{ qou.computations.per-observable-100x-status.data.rows.4.err_ppb }} ppb** (Wave-2 Convention-D `z_D` re-score; 1-term bare `z_D`: {{ qou.computations.per-observable-100x-status.data.rows.4.bare_zD_1term_baseline.err_ppb }} ppb; supersedes retired convention-C `z = 1` `755.6` / `658 ppb`) | DERIVED; primary score on Wave-2 Convention-D `z_D` re-score (`qou-iagg`) |
| **m_p brane-tower d_k** | claimed d_4 = J²·11+2 = 46, d_5 = 4, d_6 = −29 | — | `proton_brane_tower_correction_probe.py` (witness at stale q₀) | **stale-q₀ artifact** (item 2: d_4 drifts 100% between pins; d_5/d_6 don't match claims) | **NOT a derivation** — see `mp-dk-decisive-test.witness.json` |
| **m_Λ, m_Σ, m_Ξ (other baryons)** | — | — | — | — | OPEN — no canonical chain |
| **m_Δ, m_N* (resonances)** | — | — | — | — | OPEN — these may live in the Demazure sub-crystal layer (AGENTS.md §7b) |

**Baryon gaps:**
- m_p is the CAL-2 anchor (`err_ppb = {{ qou.computations.per-observable-100x-status.data.rows.0.err_ppb }} ppb` round-trip in `per-observable-100x-status.witness.json`). Including the zero-parameter connected 4th-order Borromean proton QED self-energy $M_p^{\mathrm{QED,conn}} = +{{ qou.computations.per-observable-100x-status.data.rows.1.two_term_qed_diagnostics.M_p_QED_conn_plain_keV | precision: 6 }}\,\mathrm{keV}$ shifts $q_0 \to q_{2\mathrm{t}} = {{ qou.computations.per-observable-100x-status.data.rows.1.two_term_qed_diagnostics.q0_two_term_plain | precision: 15 }}$ and reduces the $\mu$–$p$ tension from $+{{ qou.computations.per-observable-100x-status.data.rows.1.one_term_q1t_baseline.err_ppb }}\,\mathrm{ppb}$ to $+{{ qou.computations.per-observable-100x-status.data.rows.1.err_ppb }}\,\mathrm{ppb}$ ($+0.370\,\sigma_{\mathrm{exp}}$).
- m_n / Δ_pn are scored on the Wave-2 Convention-D `z_D = q³/(q²+1)` re-score (`qou-iagg`: $C_{\mathrm{KD}}^{(6)}(q_{2\mathrm{t}}) + \alpha_D^{\mathrm{proj}} + \Delta m_{\mathrm{QED,conn}}$ at $q_{2\mathrm{t}}$), giving `{{ qou.computations.per-observable-100x-status.data.rows.3.err_ppb }}` / `{{ qou.computations.per-observable-100x-status.data.rows.4.err_ppb }} ppb` (improving $1{,}172\times$ over the 1-term bare-$z_D$ baseline `{{ qou.computations.per-observable-100x-status.data.rows.3.bare_zD_1term_baseline.err_ppb }}` / `{{ qou.computations.per-observable-100x-status.data.rows.4.bare_zD_1term_baseline.err_ppb }} ppb`, and superseding the retired convention-C `z = 1` `2.389` / `755.6` / `658 ppb` figures). On the Kashiwara $b^2$ substrate identity, the connected Borromean QED splitting $\Delta m_{\mathrm{QED,conn}} = {{ qou.computations.per-observable-100x-status.data.rows.3.two_term_qed_diagnostics.Delta_m_QED_conn_plain_keV | precision: 6 }}\,\mathrm{keV}$ reduces the $m_n$ residual from `+{{ qou.computations.per-observable-100x-status.data.rows.3.two_term_qed_diagnostics.substrate_identity_m_n_1term_err_ppb }} ppb` to `+{{ qou.computations.per-observable-100x-status.data.rows.3.two_term_qed_diagnostics.substrate_identity_m_n_2term_plain_err_ppb }} ppb`.
- The m_p brane-tower d_k are NOT categorical derivations (item 2).
- All hyperons + resonances are open.

---

## V. Q-values / decay observables

| observable | canonical formula | Lean proof | production | residual | status |
|---|---|---|---|---|---|
| **Q_β (free neutron)** | Form A `m_e · |q²−2q−1| · (q+1) / (2q³)` × c_k ladder; **only c_2 = −1 Taylor-exact** | `prop:q-beta-categorical-precision-ladder` (c_2 via Kashiwara N2_factor, PROVED); c_3 §3b-cond conditional `QbetaC3StructuralFormClass` | `per_observable_100x_status.py` scores the **RULED `z_D` base** (`_qbeta_ruled_base`, 2026-09-12); the `Q_N2` rung is recorded on the row as the retired `z = 1` cell | **1.668e+8 ppb (`z_D` base, 0 rungs)** — ✗ 100×, ✗ 1× | **DERIVED, no rungs.** Was `1279 ppb (Q_N2)` — convention-C on the inadmissible `z = 1` cell — until item (iii) of the 2026-09-08 ruling was re-scored on the 2026-09-12 owner authorisation (`qou-99qc`). Not D's accuracy: no ladder on an admissible base (`qou-cds1`, blocked on `qou-pdix`; second re-score `qou-iagg`) |
| Q_β c_k (k≥3) | structural forms (J_Hopf, J−ℏ², c_3·b⁴) — **stale-q₀ near-matches, NOT Taylor-exact** | §3b-cond `QbetaC3StructuralFormClass`, `QbetaHabiroTaylorBridgeClass` (conditional, no instance) | NOT wired | item-1: 3.35% off at canonical q₀, q₀-drifting | **NOT derivations** — `qbeta-delta-tr-vs-formA.witness.json` |
| **bridge `f`: Q_β = m_e·f(Δtr_M, q)** | — | — | — | item-1 bounds what it is NOT (not the Form-A slot) | **OPEN** — the genuine derivation target (multi-block Habiro q-difference) |
| **τ_n (neutron lifetime)** | depends on `(ft)`, `g_A`, Q_β | — | — | — | OPEN — only the Q_β leg is wired |
| **τ_μ (muon lifetime)** | depends on G_F, m_μ⁵ | — | — | — | OPEN |
| **Higher-N branching Q-values** | brane-tower structure | partial | — | — | OPEN |

**Q_β gaps (corrected 2026-05-31 after items 1+2):**
- c_3+ wiring: **NOT a derivation** (reversed earlier "CLOSED" claim).
  The c_3 = J_Hopf / J−ℏ² forms are stale-q₀ near-matches (3.35% / 2.6%
  off at canonical q₀); locked behind §3b-cond conditional classes.
- The open derivation step is the bridge `f` with `Q_β = m_e·f(Δtr_M, q)`
  — item 1 showed it is NOT the canonical Form-A-slot substitution; the
  multi-Wedderburn-block Habiro q-difference solution is the research
  target (`docs/audits/2026-05-30-qbeta-habiro-derivation-gap-plan.md`).
- **Superseded 2026-09-12:** Q_β is no longer at the μ-p substrate tension
  floor — it is on the RULED `z_D` base at 1.668e+8 ppb with zero `c_k` rungs
  (`qou-99qc` item (iii), owner-authorised). The floor statement below described
  the laddered `z = 1` figure and is kept as the record of that state.
  - 🛑 **Both figures here read `4.316e+8` ppb until 2026-09-13 (PR #7283).**
    That is the **`delta_S`** element at order-zero `E₀`; the scored element has
    been the γγ-selected `nuc11_interleaved` since `573b2ece24`, which landed
    **31 minutes after** the re-score that wrote this line and updated the
    producer and witness but no prose. Stale by 2.588×, the same factor that
    hit `docs/precision-goals.md` (25 sites) and `AGENTS.md`. Take
    `miss_factor` live from `per-observable-100x-status.witness.json`, and
    note the element is ruled in only **6 of its 11 letters** — γγ words have
    even length and this one is eleven, so the quark block (3, odd) and the
    gluon pair (2, both positive) stay census-derived.
- Q_β at the μ-p substrate tension floor (1279 ppb); this is the honest
  production state, not a wiring gap.

---

## VI. Nuclei / binding energies

| observable | canonical formula | Lean proof | production | residual | status |
|---|---|---|---|---|---|
| **B(D)** (deuteron) | `E_0^(∞) · w(6_2) · R_2` with mirror-projected $\alpha_D^{\mathrm{proj}} = \alpha_D - h^2/4$ and normalized 4-row Plancherel sum $Z_{3A}^{(4)}(q_0)$ | derived from canonical β(1,1); Lean `GpmtModifiedTrace`, `MirrorProjectedAlphaD` | `borromean_binding_recompute.py`, `mass_binding_dashboard.py` | Wave-2 untruncated $E_0^{(\infty)}$ + mirror-projected $\alpha_D^{\mathrm{proj}}$ (supersedes stale $2.861\,\mathrm{MeV}$ 1-term figure) | DERIVED *under universal-Borromean + mirror-projected $\alpha_D^{\mathrm{proj}}$*; not in 100× dashboard |
| **B(³He, T, ⁴He)** | Wave-2 two-term QED Coulomb/mirror displacement (`coulomb_energy_mev`, `mirror_displacement_mev` at $q_{2\mathrm{t}}$), GPMT modified quantum dimensions $d_{\mathrm{mod}}((1^3)), d_{\mathrm{mod}}((2,1,1)), d_{\mathrm{mod}}((1^4))$, mirror-projected $\alpha_D^{\mathrm{proj}}$, and normalized 4-row $q$-Plancherel sum $Z_{3A}^{(4)}(q_0)$ | `QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm`, GPMT modified-trace completion | `two_term_qed_isotope_and_nucleon_compute.py`, `mass_binding_dashboard.py` | ${}^3\mathrm{He}$–${}^3\mathrm{H}$ mirror splitting closed by two-term QED Coulomb + mirror displacement at $q_{2\mathrm{t}}$; 4-body magnitude open | PARTIAL — mirror splitting and GPMT hook completion derived; super-pairwise 4-body magnitude open |
| **B(5Li, 6Li, 7Li)** | open per #1431's workplan | — | partial closed-form predictions | — | OPEN — needs SDP-derived K_bind(Z,N) per #1431 |
| **B(A≥8, α-cluster chain)** | $N_\alpha B({}^4\mathrm{He}) + n_{\mathrm{bonds}}\,c_\alpha$ with **3D $\alpha$-simplex tetrahedral coordination** for $N_\alpha \ge 5$ (${}^{20}\mathrm{Ne}, {}^{24}\mathrm{Mg}, {}^{40}\mathrm{Ca}$; replaces over-complete $K_N$ pairwise counting $N_\alpha(N_\alpha-1)/2$) | `AlphaCluster3DSimplex` | `per_atom_rho_deviation.py`, `mass_binding_dashboard.py` | ${}^{12}\mathrm{C}$ $+0.063\%$, ${}^{16}\mathrm{O}$ $+0.152\%$; 3D $\alpha$-simplex coordination eliminates $K_N$ over-binding for $N_\alpha \ge 5$ | PARTIAL — 3D $\alpha$-simplex coordination rule derived for $N_\alpha$-cluster nuclei |
| **Mass-comparison table** (15 isotopes via `M(Z,N) = Z·m_p + N·m_n + Z·m_e − B(Z,N)`) | uses two-term QED nucleon masses at $q_{2\mathrm{t}}$ + Wave-2 binding dashboard | — | `mass_binding_dashboard.py` → `mass-binding-dashboard.witness.json` | `<0.1 MeV` — arithmetic recombination | DERIVED (see `mass-formula-validation.md`) |

**Binding gaps:** Per #1431 merged content and Wave-2 upgrades, GPMT modified-trace completion ($d_{\mathrm{mod}}$ on hook partitions), mirror-projected $\alpha_D^{\mathrm{proj}} = \alpha_D - h^2/4$, untruncated $E_0^{(\infty)} = E_0^{(0)}/(1-\hbar_q^2)$, two-term QED Coulomb/mirror displacement at $q_{2\mathrm{t}}$, and 3D $\alpha$-simplex coordination for $N_\alpha \ge 5$ are wired across the binding producers; the remaining open question for $A \ge 3$ is the parameter-free derivation of the super-pairwise 4-body cumulant magnitude.

---

## VII. Fundamental constants

| observable | canonical formula | Lean proof | production | residual | status |
|---|---|---|---|---|---|
| **α_EM⁻¹** | Form-B Bring–Schwinger cubic ladder: $\alpha^{-1} = q[9]_q[10]_q + \frac{2}{3\pi} + \alpha\,\frac{[2]_q}{8\pi}(1 - h^2\alpha)$ at proton-anchored $q_0$ | `em-coupling-bring-zero-mode.lean`, `AlphaEmSchwingerLadder` (conditional on `ArchimedeanLimit`, `BlochSuslinUniqueness`, `BringZeroModeBlochClass`) | `alpha_em_schwinger_ladder_probe.py` → `alpha-em-schwinger-ladder.witness.json`, `per_observable_100x_status.py` | **-{{ qou.computations.per-observable-100x-status.data.rows.5.err_ppb }} ppb** (`{{ qou.computations.per-observable-100x-status.data.rows.5.pred_MeV }}` vs CODATA `{{ qou.computations.per-observable-100x-status.data.rows.5.codata_MeV }}`, **2.38 σ_exp**, miss factor `{{ qou.computations.per-observable-100x-status.data.rows.5.miss_factor }}×`; supersedes CS-resummed `-467.6 ppb` / `0.00807` gap and muon-pin `137.035944`) | **CONDITIONAL / DERIVED** — Form-B cubic at proton pin (zero fit parameters) |
| **G_Fermi ($G_F$)** | $G_F = 1/(\sqrt{2}\,v_{\mathrm{EW}}^2)$ from the electroweak Bring–Schwinger fixed-point cubic for $N_v = v_{\mathrm{EW}}/m_p$: $T_{\mathrm{EW}} = [4]_q[6]_q[8]_q([2]_q/2)^2 + 1/\pi$, $H_{\mathrm{EW}} = [2]_q/(8\pi)$ | `QOU.StandardModel.ElectroweakBringSchwingerBridge.ewFixedPoint_iff_cubic` (sorry-free) | `computations/probes/electroweak_bring_schwinger_bridge_probe.py` → `computations/probes/electroweak-bring-schwinger-bridge.witness.json` | **+{{ qou.computations.probes.electroweak-bring-schwinger-bridge.data.electroweak_vev_fixed_point.G_F_err_ppb | precision: 4 }} ppb** (`+{{ qou.computations.probes.electroweak-bring-schwinger-bridge.data.electroweak_vev_fixed_point.G_F_err_sigma | precision: 3 }} σ_exp`; $G_F = {{ qou.computations.probes.electroweak-bring-schwinger-bridge.data.electroweak_vev_fixed_point.G_F_pred_GeV_inv2 | precision: 9 }}\,\mathrm{GeV}^{-2}$) | **DERIVED** — zero-parameter Bring–Schwinger electroweak fixed point |
| **G_Newton** | — | — | — | — | OPEN — gravitational sector |
| **Higgs VEV ($v_{\mathrm{EW}}$), $m_H$** | $v_{\mathrm{EW}} = m_p \cdot N_v^*$ from the electroweak Bring–Schwinger cubic fixed point; $m_H$ via 1-loop Schwinger / Bring zero-mode W/Z anchor reconciliation | `QOU.StandardModel.ElectroweakBringSchwingerBridge` (`ewFixedPoint_iff_cubic`, `higgs_W_Z_anchor_reconciliation`, sorry-free) | `computations/probes/electroweak_bring_schwinger_bridge_probe.py` → `computations/probes/electroweak-bring-schwinger-bridge.witness.json` | **$v_{\mathrm{EW}}$: {{ qou.computations.probes.electroweak-bring-schwinger-bridge.data.electroweak_vev_fixed_point.v_err_ppb | precision: 4 }} ppb** (`{{ qou.computations.probes.electroweak-bring-schwinger-bridge.data.electroweak_vev_fixed_point.v_err_sigma | precision: 3 }} σ_exp`, $v_{\mathrm{pred}} = {{ qou.computations.probes.electroweak-bring-schwinger-bridge.data.electroweak_vev_fixed_point.v_pred_GeV | precision: 12 }}\,\mathrm{GeV}$); **$m_H$ (1-loop Schwinger from $W$): {{ qou.computations.probes.electroweak-bring-schwinger-bridge.data.higgs_mass_variants.schwinger_1loop_alpha_pi.err_W_ppm | precision: 3 }} ppm** (`{{ qou.computations.probes.electroweak-bring-schwinger-bridge.data.higgs_mass_variants.schwinger_1loop_alpha_pi.err_W_sigma | precision: 3 }} σ_exp`) | **DERIVED** — $v_{\mathrm{EW}}$ and W/Z-reconciled $m_H$ proved in `ElectroweakBringSchwingerBridge.lean` |
| **Cosmological constant Λ** | — | — | — | — | OPEN |

---

## VIII. CKM / mixing

| observable | canonical formula | Lean proof | production | residual | status |
|---|---|---|---|---|---|
| **θ_C (Cabibbo)** | partial in `cabibbo-angle*.md` | — | — | — | PARTIAL |
| **CKM matrix elements** | — | — | — | — | mostly OPEN |
| **CP violation phase** | partial in `cp-violation-spectral-form*` (was conjecture #1434) | — | — | — | PARTIAL — conjecture-level |

---

## IX. Neutrinos

| observable | status |
|------------|--------|
| m_ν, mixing angles, MSW, Majorana phases | ALL OPEN |

---

## X. Cosmology

| observable | status |
|------------|--------|
| H₀, Ω_M, Ω_Λ, η_B (baryogenesis), inflation | ALL OPEN |

---

## Tracker maintenance

When a session finds a gap, status change, or new derivation:

1. **Add a row** if the observable isn't here yet.
2. **Update the residual + status** column if it moved.
3. **Cite the PR** that drove the change in the commit message.
4. **No fits, no near-matches**: only canonically-derived (theorem-cited)
   values qualify as "DERIVED". Numerical agreement is "PARTIAL" at best
   unless the agreement comes via a proved structural identity.

## Open priority queue (post-this-session)

The highest-leverage open derivations (by # observables they would close
at 100×):

1. **The Q_β bridge `f`: `Q_β = m_e · f(Δtr_M, q)`** — the genuine open
   derivation. Item 1 (2026-05-31) bounded what it is NOT (not the
   Form-A net-winding slot; Δtr_M's leading Taylor order is −5/4 vs Form
   A's −2). The target is the multi-Wedderburn-block Habiro q-difference
   solution. Closing it (Taylor-exact at canonical q₀, NOT a structural
   near-match) closes Q_β → m_n → Δ_pn at L1. **3 observables**.
   (Supersedes the earlier "Habiro c_4..c_7 closed forms" item — those
   were stale-q₀ near-matches, not the closure path.)
2. ~~m_p brane-tower correction to E_0~~ — **NOT a gap to fit** (item 2 +
   2026-07-04 de-fit): the brane-tower d_k were a stale-pin artifact /
   CODATA fit (the `(1+46u⁴)…` tower was dropped from production
   2026-07-04; the honest m_p round-trip is +1.35 ppb, ~437× miss).
   Closing that residual below 100× is Subgoal-2-gated (substrate
   derivation), never a fit target. Removed from the queue.
3. **Operator-valued LR `A^λ_{μν}(I)`** (#1443) — categorical mechanism
   for multi-Wedderburn-block decompositions; enables higher-A binding
   derivation (#1431 Barrier-1) and flavor-split structure. **Infrastructure**.
4. **α/(4π) next term in α_EM** — closes α_EM from 4.18 ppm toward 0.15
   ppb CODATA σ. **1 observable**.
5. **B(A≥3) via derived K_bind(Z,N)** (#1431 Barrier-1) — closes
   binding-energy sector beyond the deuteron. **N observables** (A=3..20+).

## Gaps in this tracker itself

This tracker was assembled in a single session; coverage is best-effort
across what I've encountered. Likely undocumented sectors:

- Magnetic moments (μ_p, μ_n, anomalous moments)
- Form factors (proton charge radius)
- Decay branching ratios (π⁰ → γγ etc.)
- Excited states (m_N*, m_Δ, …)

Future sessions: add what you encounter that's missing.
