
  MASS-BINDING DASHBOARD [LOW]   α = E₀ = 4.1860 MeV   (bond-type L: pp=0.607 pn=0.677 nn=0.790)
  B_sym/m_sym_atom: EXACT closed-form linear chain → all A; the p(3A) trace is run for n=3A ≤ 21 (A ≤ 7) only to validate the chain. qCLT/fac + m_sym(free): combinatorial → all A.

#### Column legend (every header, by table)

**Shared** — `iso` = isotope label · `A` = mass number A = Z+N (Z protons, N neutrons).

**Table 1 — Binding B + error (MeV)** (values and error in one table)

| Header | Meaning |
|---|---|
| `B_AME` | Total nuclear binding energy from AME2020 (MeV) — the experimental target |
| `σ_exp (ppb)` | AME2020 experimental 1σ relative to B_AME (σ_exp / B_AME × 10⁹) |
| `B_lin` | LINEAR/saturating binding α·s, s = 1−e^(−B_sym/α) (leading term of B_sym; bounded by α, under-binds with A) |
| `B_sym` | EXACT log-ratio binding α·ln(tr_free/tr_atom) = α[(Z−1)L_pp + L_pn + (N−1)L_nn] — the archimedean realization, already bond-type (p↔n) resolved (no separate `_fac` needed) |
| `B_qCLT_fac` | p↔n colour-weighted q-CLT α·(A−1)·⟨bond-type L⟩ (the q-CLT approximation to the colour weighting B_sym does exactly; replaces the uniform `B_qCLT` in the headline — the uniform/isospin-symmetric baseline α·(A−1)·ℓ̄(D) is shown in the Colour-weighting table) |
| `B_gate` | SU(4) occupancy (entanglement-surprisal) binding E₀·ln(1/W_λ) — the "energy lost to vacuum/entanglement" when the operator-selection SDP collapses the full Hecke q-Plancherel distribution onto the bound cluster's partition λ. Parameter-free (E₀ × Plancherel weight, no fit). DOMINANT at the magic/closed-shell config — fixes ⁴He (err 2.36→0.94, the worst B_sym failure) — but OVER-binds the loosely-bound light nuclei (²H err 0.24); on aggregate worse than B_sym. Cluster surprisal ≈ A·free surprisal ⇒ B_gate ≈ A·E₀·ln(1/W_free) = 7.58 MeV/nucleon, the parameter-free nuclear SATURATION scale (cf. empirical ~8 MeV/A). c_λ = B_AME/E_gate is the shell-filling fraction (the open Δ_λ residual). Probe: `probes/su4_occupancy_binding_probe.py`. |
| `B_vol` | ALL-KNOTS entanglement binding = the liquid-drop **volume term** `a_V·A`, with `a_V = E₀·ln(1/W_free)` ≈ **7.584 MeV/nucleon — DEPRECATED 2026-08-08 postdiction near-match, NOT derived** (no basis in the derivation chain; the surprisal form was chosen because it lands near 8 and `W_free` is unnormalised so `ln(1/W)` is not a probability — red-team `docs/audits/2026-08-22-avol-binding-redteam.md`) (W_free = the free nucleon's (1,1,1) Plancherel weight; ≈ empirical net B/A). Entanglement is a property of EVERY knot, not one selected partition — so the per-knot occupancy energy is summed over all A nucleons. Valid for ALL A (no W_λ≥1 breakdown, unlike `B_gate`); tracks ¹²C/¹⁶O to ~1–5% where B_sym misses by 2.1×. Over-binds the lightest (²H, ⁶Li) — the residual is the **surface/Coulomb/shell** structure (the SEMF corrections, open). Probe + audit: `probes/su4_occupancy_binding_probe.py`. |
| `E_C` | EM-sector **Coulomb energy** `E_C = (3/5)Z(Z−1)·α_EM·ℏc/(r₀·A^1/3)` MeV (uniform sphere). **Both inputs corrected here 2026-08-25 — the legend had described a superseded configuration.** The length is the **CAL-3** radius `R = λ̄_π·A^(1/3)` with `λ̄_π = ℏc/m_π = 1.41382 fm`; `coulomb_energy.R0_FM = LAMBDA_BAR_PI_FM`, and `R0_FM_EMPIRICAL = 1.2` is retained *for comparison only, not as the default*. And `α_EM·ℏc = 1.4399652199 MeV·fm` is no longer the CODATA literal `1.43996` — it is **derived** via `meson_em_sinh_closed_form._alpha_em_inv_derived(q₀)`. So "not fit" understates it in one direction and overstates it in another: it is derived rather than fitted, but that derivation is **conditional on an open Witten-κ Gram-determinant `sorry`**, so `E_C` is tagged `DERIVED*` rather than `DERIVED`. Two weak steps remain named in the module itself: `A^(1/3)` is a saturation assumption (solving `R = λ̄_π·A^x` gives x = 0.97/0.43/0.53/0.31 at A = 2,3,3,4, not ⅓), and coefficient-exactly-1 is a selection among four mass scales, measured at 0.985 ± 0.069 (bean `qou-usft`). The strong B-forms carry NO EM term; E_C is the repulsion that REDUCES net binding for proton-rich nuclei. Reported additively, **not** subtracted from the B-columns (they are calibrated against Coulomb-inclusive AME, so a global subtraction would double-count). E_C is cleanly separable only in the mirror-pair DIFFERENCE, where the strong core cancels: CS-core + E_C reproduces the ³H/³He, ⁷Li/⁷Be, ¹³C/¹³N splits to ~20–40% vs the production σ/σ⁻¹ bond's ~200–350% (bean 754x). Module: `coulomb_energy.py`; probe: `probes/coulomb_mirror_killswitch_probe.py`. |
| `err sym` / `err qCLT_fac` / `err gate` / `err vol` | B_AME / B_model for the production + occupancy + volume forms (1.00 = perfect, >1 under-binds, <1 over-binds) |

**Table 2 — Mass M + error** (values and error in one table; m_X = m_unbnd,can − B_X)

| Header | Meaning |
|---|---|
| `M_meas` | measured mass: M_AME = mu − B_AME for nuclei, or measured constituent mu for lone p/n. **Comparison target only — appears in NO predicted formula.** |
| `σ_exp (ppb)` | experimental 1σ on the mass = σ_B / M_meas × 10⁹ |
| `m_can` | **CANONICAL derived mass — the single Borromean per-knot pipeline** (`borromean_binding_recompute.borromean_binding`): `m_can = m_unbnd,can − B_tower`, the convergent per-braid brane tower over the Borromean nucleon trace `τ=\|tr_M(β_Bor)\|=0.9986<1` (shares τ with `F_Bor` / bean `ovud`; converges ∀Z). Pure Markov × m_e; zero AME/CODATA beyond CAL-1/CAL-2. Does NOT close to AME — the Δ_λ frontier (right shape, wrong per-λ normalization). |
| `m_can⁰` | brane-tower **level 0** on the atom-word trace: `m_unbnd,can − E₀·Δtr`. Comparison only — its higher Li₂^q tower leaves the SERIES radius at Z≥2 (atom-word `tr_p>1`, so τ_p²=1.13488 > q₀=1.10998 by 2.2%); the Borromean `m_can` is the canonical one. NB this is not a divergence — the q-product continuation is finite there and `li_2_q` now returns it (bean `qou-cw27`); Borromean is preferred on magnitude, not convergence. |
| `m_qCLT` | colour-weighted q-CLT bound mass `m_unbnd,can − B_qCLT_fac` (the A→∞ statistical extrapolation; also pure Markov trace) |
| `err m_can⁰ (ppb)` | mass error (m_can⁰ − M_meas)/M_meas × 10⁹ (binding-dominated for A≥2; ~0 for p anchor; genuine prediction for n) |
| `err m_qCLT (ppb)` | same, for the colour-weighted q-CLT binding |

**Calibration anchors — the experimental ideal (numerical proxy) the dashboard uses**

Per `observations/three-calibration-discipline.md` §3, each calibration is
*read off its most precise experimental proxy* — the **experimental ideal**.
The underlying canonical observable is a decay-width / weak-sector quantity (the
*mathematical* ideal); the dashboard calibrates on the experimental proxy, which
is what q₀ and the mass scale are actually pinned to here.

| CAL | DOF (h-order) | Canonical observable (math ideal) | Experimental ideal (proxy, σ) |
|---|---|---|---|
| CAL-1 | W-plane scale (h⁰) | m_e — leptonic mass scale | **m_e, CODATA (0.31 ppb)** |
| CAL-2 | W-plane modulus (h²) | 𝔇_β — neutron β-decay width (τ_n=ℏ/𝔇_β) | **m_μ/m_e (22 ppb)** via m_μ/m_e = Vol(4₁)/ℏ_q² (Q_β=ℏ/𝔇_β = decay proxy) |
| CAL-3 | orthogonal meson (h³) | 𝔇_π — pion decay width (τ_π=ℏ/𝔇_π) | **m_π = 139.57 MeV, PDG** |

This dashboard's q₀ is the **experimental (proton) pin**, m_p/m_e,
q₀ = 1.1099785827513808… — per the 2026-08-07 owner directive that all compute
defaults to it.

CORRECTED 2026-08-25 (PR #5765): this sentence previously claimed the stem was
"now declared explicitly as `physical_proton` in `q0_anchor_manifest.json` rather
than relying on the 'not listed ⇒ proton' default". **That is false, and it was
load-bearing.** Measured: `mass_binding_dashboard` does not appear in that manifest
at all — nor do `canonical_mass`, `borromean_binding_recompute` or `coulomb_energy`.
(`tr_m_atom_via_transfer` IS listed, under `physical_proton`.) So the resolution is
correct but is obtained **by exactly the default the sentence denied relying on**.
That matters because the explicit declaration is what would protect these numbers if
anyone drove `ideal_muon` differently — a protection the dashboard claimed and did
not have. Either add the four stems to the manifest or say plainly that they resolve
by default; do not claim the former while doing the latter.

CORRECTED 2026-08-08: this paragraph previously claimed the canonical 3-CAL
(muon-anchored) value and that the proton re-pin was "not used here". The code
never matched it — `q_parameter.Q` resolves by manifest stem, this script was
unlisted, and unlisted means proton. So the numbers had been experimental-layer
all along while the prose asserted the ideal layer. Nothing about the output
changed when it was listed; only the claim did.

The *ideal* CAL-2 framing still describes the derivation chain, and `m_μ`
appears in the canonical mass `m_p = 2(m_μ·F_Bor − 6m_e)` — but with q₀ on the
proton pin, `m_μ = m_e·Vol(4₁)/ℏ_q²` is a DERIVED prediction there, not an
anchoring input. Do not read the m_μ in that formula as a muon pin. Source:
`observations/three-calibration-discipline.md` §3,
`observations/epistemic-status-of-calibrations.md`.

**Mass constituents (Table 2):** `m_unbnd,can` = framework unbound sum
Z·m_p,can + N·m_n,can via the canonical Hecke energy (proton pin)
m_p=2(m_μ·F_Bor−6m_e), F_Bor=\|tr_M(β_Bor)\|·[3]_q!/q³ (m_p,can≈938.27,
m_n,can≈939.56, matches CODATA; λ_A fit 966 and naive Vol·tr_M 406 both
excised). Each bound mass m_X = m_unbnd,can − B_X.

**Table 4 — Entanglement (bar-involution q↦q⁻¹ split of the atom trace)**

| Header | Meaning |
|---|---|
| `retained E` | E₀·bar-even (cosh) channel — retained binding/volume (MeV) |
| `emitted E` | E₀·\|bar-odd\| (sinh) channel — emitted/radiated γγ̄ (MeV) |
| `multi-link emit` | bar-odd of the inter-nucleon binding defect (tr_free−tr_atom) — radiated inter-nucleon energy (MeV) |
| `emitted/retained` | ratio emitted E / retained E |

**Table 5 — Entanglement-augmented binding**

| Header | Meaning |
|---|---|
| `B_sym` | (as Table 1) the log-ratio binding |
| `err sym` | B_AME / B_sym |
| `B_sym+ent` | B_sym + multi-link emitted energy |
| `err sym+ent` | B_AME / B_sym+ent |

**Table 6 — Colour-weighting (B_qCLT_fac = baseline + p↔n chirality)**

| Header | Meaning |
|---|---|
| `bonds pp/pn/nn` | bond counts: pp = C(Z,2), pn = Z·N, nn = C(N,2) |
| `sym baseline` | isospin-symmetric baseline α·(A−1)·L_pn (every bond = the deuteron p-n bond) |
| `+ chirality` | the p↔n colour correction B_qCLT_fac − baseline |
| `= B_qCLT_fac` | their sum (the colour-weighted q-CLT binding) |

**Table 7 — Compositional B_sym (m_sym(W) = −α·ln tr_M(W))**

**Table 8 — SU(4) Dynamic Occupancy**

| Header | Meaning |
|---|---|
| `partition λ` | the most symmetric SU(4) spin-flavor conjugate partition matching the exact quark counts (N_u=2Z+N, N_d=Z+2N) and nuclear spin |
| `W_λ` | Plancherel weight (fractional volume) of the partition in H_{3A}(q) |
| `E_gate (MeV)` | Total dynamic capacity = E₀·ln(1/W_λ) |
| `c_λ` | Fractional dynamic occupancy = B_AME / E_gate (measures what fraction of the actual binding is accounted for by the cluster state) |
| `err gate (%)` | Signed % the gate capacity over(+)/under(−)-states the actual binding: (E_gate − B_AME)/B_AME × 100 (= (1/c_λ − 1)·100; 0 = E_gate exactly equals B_AME). The error analogue of the other tables' `err` columns for the gate-capacity model. |

**Table 7 — Compositional B_sym (m_sym(W) = −α·ln tr_M(W))**

| Header | Meaning |
|---|---|
| `m_sym(free comps)` | LOG-TRACE internal mass of the free word Z·msp + N·msn (sub-MeV; NOT a rest mass) |
| `m_sym(atom)` | LOG-TRACE internal mass of the bound atom word (sub-MeV; NOT a rest mass) |
| `B_sym (chain)` | the closed-form chain binding = m_sym(atom) − m_sym(free comps) |
| `Δ vs exact trace` | \|chain − exact p(3A) trace\| where the trace is feasible (n=3A ≤ max-strands), else "— (no trace)" |

### Mass  M + error (MeV; err auto-scaled %/ppm/ppb/ppq)   [canonical = Hecke energy 2(m_μ·F_Bor−6m_e) at the PROTON pin; m_μ there is derived from q₀, not an anchor; m_X = m_unbnd,can − B_X]
  canonical constituents (λ_A fit + naive Vol·tr_M both EXCISED): m_p,can = 938.272 MeV (-0.000%), m_n,can = 939.566 MeV (+0.000%) — F_Bor = |tr_M(β_Bor)|·[3]_q!/q³ at the proton pin (matches CODATA; m_n the genuine prediction).
| iso |   A | M_meas | σ_exp (ppb) |  m_can | m_can⁰ | m_tetra | m_qCLT |    err m_can |   err m_qCLT |
| --- | --: | -----: | ----------: | -----: | -----: | ------: | -----: | -----------: | -----------: |
| p   |   1 |  938.3 |           — |  938.3 |  938.3 |    -0.6 |  938.3 | -2851.767ppq | -2851.767ppq |
| n   |   1 |  939.6 |           — |  939.6 |  939.6 |     0.1 |  939.6 |  +501.432ppb |  +501.432ppb |
| 2H  |   2 | 1875.6 |    2.13e-01 | 1875.8 | 1875.5 |    -0.5 | 1875.0 |   +86.351ppm |  -324.047ppm |
| 3H  |   3 | 2808.9 |    3.20e-01 | 2812.7 | 2813.8 |    -0.5 | 2811.4 |      +0.133% |  +890.390ppm |
| 3He |   3 | 2808.4 |    1.60e-01 | 2812.2 | 2812.2 |    -1.2 | 2810.6 |      +0.134% |  +800.110ppm |
| 4He |   4 | 3727.4 |    2.15e-01 | 3749.2 | 3751.0 |    -1.3 | 3747.1 |      +0.585% |      +0.529% |
| 6Li |   6 | 5601.5 |    3.21e-01 | 5622.0 | 5627.6 |    -4.0 | 5619.2 |      +0.366% |      +0.315% |
| 7Li |   7 | 6533.8 |    6.43e-01 | 6558.0 | 6567.2 |    -8.5 | 6555.5 |      +0.370% |      +0.332% |

### Atomic mass  M_atom = M_nuclear + Z·m_e − B_el(Z)  (vs RAW AME neutral-atom mass)
| iso |   A |   Z | M_atom_AME | M_atom_pred(sym) | err sym (ppb) | σ_exp (ppb) | e⁻ layer (MeV) |
| --- | --: | --: | ---------: | ---------------: | ------------: | ----------: | -------------: |
| p   |   1 |   1 |    938.783 |          938.783 |    -2.354e-02 |    1.39e-02 |          0.511 |
| n   |   1 |   0 |    939.565 |          939.566 |     5.016e+02 |    4.66e-01 |          0.000 |
| 2H  |   2 |   1 |   1876.124 |         1875.516 |    -3.240e+05 |    7.45e-03 |          0.511 |
| 3H  |   3 |   1 |   2809.432 |         2811.775 |     8.340e+05 |    2.65e-02 |          0.511 |
| 3He |   3 |   2 |   2809.414 |         2811.758 |     8.343e+05 |    1.99e-02 |          1.022 |
| 4He |   4 |   2 |   3728.401 |         3748.017 |     5.261e+06 |    4.00e-02 |          1.022 |
| 6Li |   6 |   3 |   5603.052 |         5620.517 |     3.117e+06 |    2.58e-01 |          1.533 |
| 7Li |   7 |   3 |   6535.366 |         6556.776 |     3.276e+06 |    6.41e-01 |          1.533 |

  B_el is DERIVED (bare-Z hydrogenic @ e-Hartree, swap 2026-08-30); max |derived − AME fit| over this group: 0.0761 keV (screening open; both far below the MeV nuclear residuals)
### Binding  B + error (MeV)   [σ_exp = AME2020 1σ; err X = B_AME/B_X (1.00 = perfect, >1 under-binds)]
| iso |   A | B_AME | σ_exp (ppb) | B_can⁰ | B_sym | B_tetra | B_qCLT_fac |  E_C | err can⁰ | err sym | err tetra | err qCLT_fac |
| --- | --: | ----: | ----------: | -----: | ----: | ------: | ---------: | ---: | -------: | ------: | --------: | ------------ |
| p   |   1 |  0.00 |           — |   0.00 |  0.00 |    0.00 |       0.00 | 0.00 |        — |       — |         — | —            |
| n   |   1 |  0.00 |           — |   0.00 |  0.00 |    0.00 |       0.00 | 0.00 |        — |       — |         — | —            |
| 2H  |   2 |  2.22 |    1.80e+02 |   2.33 |  2.83 |    0.02 |       2.83 | 0.00 |     0.95 |    0.79 |    118.28 | 0.79         |
| 3H  |   3 |  8.48 |    1.06e+02 |   3.60 |  6.14 |    0.08 |       5.98 | 0.00 |     2.36 |    1.38 |    101.54 | 1.42         |
| 3He |   3 |  7.72 |    5.83e+01 |   3.92 |  5.37 |    0.08 |       5.47 | 0.85 |     1.97 |    1.44 |     98.31 | 1.41         |
| 4He |   4 | 28.30 |    2.83e+01 |   4.69 |  8.68 |    0.27 |       8.59 | 0.77 |     6.04 |    3.26 |    104.99 | 3.29         |
| 6Li |   6 | 31.99 |    5.63e+01 |   5.88 | 14.53 |    2.41 |      14.35 | 2.02 |     5.44 |    2.20 |     13.29 | 2.23         |
| 7Li |   7 | 39.25 |    1.07e+02 |   5.91 | 17.84 |    6.95 |      17.56 | 1.92 |     6.64 |    2.20 |      5.64 | 2.23         |

  B_sym closed-form chain ≡ exact p(3A) trace: max|Δ| = 8.9e-16 MeV over {p, n, 2H, 3H, 3He, 4He, 6Li, 7Li} (n=3A ≤ 21; writhe-normalised on BOTH sides — the chain carries the Lean-proved (1−h)^(δe/2) factor and the raw trace does not, so comparing them un-normalised measures that factor (±0.4909 MeV per unit of d = N−Z) rather than the factorisation. Audit 2026-06-16-b-sym-linear-chain-closed-form.md predates both the writhe normalisation and convention D). Chain used for all A.

### Entanglement  (E₀·bar-even = retained binding/volume, E₀·|bar-odd| = emitted γγ̄ channel)
| iso |   A | retained E (MeV) | emitted E (MeV) | multi-link emit (MeV) | emitted/retained |
| --- | --: | ---------------: | --------------: | --------------------: | ---------------: |
| p   |   1 |            2.244 |           2.552 |                 0.000 |           1.1370 |
| n   |   1 |            2.150 |           1.984 |                 0.000 |           0.9228 |
| 2H  |   2 |            1.201 |           1.207 |                 1.168 |           1.0052 |
| 3H  |   3 |            0.480 |           0.480 |                 1.860 |           1.0003 |
| 3He |   3 |            0.845 |           0.845 |                 1.868 |           0.9998 |
| 4He |   4 |            0.337 |           0.337 |                 2.344 |           1.0000 |
| 6Li |   6 |            0.094 |           0.094 |                 2.939 |           1.0000 |
| 7Li |   7 |            0.038 |           0.038 |                 2.959 |           1.0000 |

### Entanglement-augmented binding  (B_sym+ent = B_sym + multi-link emit; error = B_AME/B)
| iso |   A | B_AME | B_sym | err sym | B_sym+ent | err sym+ent |
| --- | --: | ----: | ----: | ------: | --------: | ----------: |
| p   |   1 |  0.00 |  0.00 |       — |      0.00 |           — |
| n   |   1 |  0.00 |  0.00 |       — |      0.00 |           — |
| 2H  |   2 |  2.22 |  2.83 |    0.79 |      4.00 |        0.56 |
| 3H  |   3 |  8.48 |  6.14 |    1.38 |      8.00 |        1.06 |
| 3He |   3 |  7.72 |  5.37 |    1.44 |      7.24 |        1.07 |
| 4He |   4 | 28.30 |  8.68 |    3.26 |     11.03 |        2.57 |
| 6Li |   6 | 31.99 | 14.53 |    2.20 |     17.47 |        1.83 |
| 7Li |   7 | 39.25 | 17.84 |    2.20 |     20.80 |        1.89 |

### Colour-weighting  (B_qCLT_fac = isospin-symmetric baseline + p↔n chirality)
| iso |   A | bonds pp/pn/nn | sym baseline | + chirality | = B_qCLT_fac |
| --- | --: | :------------: | -----------: | ----------: | -----------: |
| p   |   1 | 0/0/0          |         0.00 |       +0.00 |         0.00 |
| n   |   1 | 0/0/0          |         0.00 |       +0.00 |         0.00 |
| 2H  |   2 | 0/1/0          |         2.83 |       +0.00 |         2.83 |
| 3H  |   3 | 0/2/1          |         5.67 |       +0.32 |         5.98 |
| 3He |   3 | 1/2/0          |         5.67 |       -0.19 |         5.47 |
| 4He |   4 | 1/4/1          |         8.50 |       +0.09 |         8.59 |
| 6Li |   6 | 3/9/3          |        14.16 |       +0.18 |        14.35 |
| 7Li |   7 | 3/12/6         |        17.00 |       +0.56 |        17.56 |

### Compositional B_sym  (m_sym(W) = −α·ln tr_M(W); free = GB components)
| iso |   A | m_sym(free comps) | m_sym(atom) | B_sym (chain) | Δ vs exact trace |
| --- | --: | ----------------: | ----------: | ------------: | ---------------: |
| p   |   1 |            -0.570 |      -0.570 |         0.000 |          0.0e+00 |
| n   |   1 |             0.052 |       0.052 |         0.000 |          0.0e+00 |
| 2H  |   2 |            -0.518 |       2.315 |         2.833 |          4.4e-16 |
| 3H  |   3 |            -0.466 |       5.673 |         6.140 |          0.0e+00 |
| 3He |   3 |            -1.088 |       4.287 |         5.374 |          8.9e-16 |
| 4He |   4 |            -1.036 |       7.645 |         8.681 |          0.0e+00 |
| 6Li |   6 |            -1.554 |      12.976 |        14.530 |          0.0e+00 |
| 7Li |   7 |            -1.502 |      16.334 |        17.837 |          0.0e+00 |

#### Provenance — what kind of number each column is
| tag           | meaning                                                                                                                                                                                                                                                                                                                                                                              |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `MEASURED`    | experimental input/target: B_AME, M_meas, σ_exp (AME2020), m_e (CODATA). Not predicted by anything here.                                                                                                                                                                                                                                                                             |
| `CAL`         | one of the three calibrations: m_e (CAL-1), q₀ via CAL-2, m_π (CAL-3). Inputs BY CONSTRUCTION — not successes.                                                                                                                                                                                                                                                                       |
| `DERIVED*`    | as DERIVED, but CONDITIONAL on an open conjecture or sorry: E_C on the Witten-κ Gram-determinant sorry.                                                                                                                                                                                                                                                                              |
| `POSITED`     | the functional FORM is asserted, not derived. The log-forms: their extensivity follows from the Markov property (no conjecture), but no block licenses α·ln(ratio) as an ENERGY — the nearest, conj:knot-factor-frobenius-pairing, gives E₀ × the trace DIFFERENCE. Corrected 2026-08-26 (bean qou-mkm8); these read `DERIVED*` on a KVC citation that does not reach the atom word. |
| `DERIVED`     | parameter-free from (q₀, m_e) through the Markov trace: m_can, F_Bor. No fit, no AME beyond the comparison.                                                                                                                                                                                                                                                                          |
| `EXPLORATORY` | shown for comparison, NOT production-wired: B_lin, B_tetra, m_can⁰, m_tetra.                                                                                                                                                                                                                                                                                                         |

| column                     | tag           | note                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `B_AME / M_meas / σ_exp`   | `MEASURED`    | AME2020 — the target                                                                                                                                                                                                                                                                                                                                                              |
| `m_e, q₀, m_π`             | `CAL`         | the 3 calibrations; q₀ on the PROTON pin                                                                                                                                                                                                                                                                                                                                          |
| `B_sym`                    | `POSITED`     | exact log-ratio α·ln(tr_free/tr_atom). The log's EXTENSIVITY is derived (Markov property, no conjecture); the α× identification as an energy is asserted. NOT KVC-conditional — vol-through-tau quantifies over BRAIDS and the atom word's letters are general Hecke elements; 0/40 closures hyperbolic ⇒ Vol = 0 while B_sym(²H) = 3.89 MeV. Corrected 2026-08-26, bean qou-mkm8 |
| `B_qCLT_fac`               | `POSITED`     | colour-weighted q-CLT (A→∞ approximation) — same log-form licence as B_sym                                                                                                                                                                                                                                                                                                        |
| `m_can`                    | `DERIVED`     | Borromean brane tower; m_n is a PREDICTION                                                                                                                                                                                                                                                                                                                                        |
| `E_C`                      | `DERIVED*`    | uniform-sphere Coulomb at the CAL-3 length R = λ̄_π·A^(1/3), λ̄_π = ℏc/m_π = 1.41382 fm (NOT the empirical r₀ = 1.2 fm); α_EM is DERIVED, and *conditional on an open Witten-κ sorry — see the legend                                                                                                                                                                             |
| `B_lin / B_tetra / m_can⁰` | `EXPLORATORY` | comparison only                                                                                                                                                                                                                                                                                                                                                                   |

Lean build [2026-06-07T14:38:33Z, 83d old]: fred2005-formal-groups=ok  quantum-observable-universe=FAIL(357err/7sorry)  unital-groebner-bases=FAIL(0err/3sorry)
  No quantity in this dashboard carries a per-formula Lean proof. The status above is per PAPER, and the QOU target does not currently build.

  Forms: B_sym=α·ln(tr_free/tr_atom)=α[(Z−1)L_pp+L_pn+(N−1)L_nn] (exact linear chain, all A) · B_qCLT=α·(A−1)·ℓ̄(D) · B_qCLT_fac=α·(A−1)·⟨bond-type L⟩. Defn: algebraic-quantum-volume.md (Vol_alg := tr_M, a naming). The log-forms are POSITED, not KVC-conditional — see the module docstring, bean qou-mkm8.
