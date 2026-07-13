
  MASS-BINDING DASHBOARD [SWEEP]   α = E₀ = 4.1860 MeV   (bond-type L: pp=0.695 pn=0.534 nn=1.237)
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
| `B_vol` | ALL-KNOTS entanglement binding = the liquid-drop **volume term** `a_V·A`, with `a_V = E₀·ln(1/W_free)` ≈ **7.584 MeV/nucleon DERIVED parameter-free** (W_free = the free nucleon's (1,1,1) Plancherel weight; ≈ empirical net B/A). Entanglement is a property of EVERY knot, not one selected partition — so the per-knot occupancy energy is summed over all A nucleons. Valid for ALL A (no W_λ≥1 breakdown, unlike `B_gate`); tracks ¹²C/¹⁶O to ~1–5% where B_sym misses by 2.1×. Over-binds the lightest (²H, ⁶Li) — the residual is the **surface/Coulomb/shell** structure (the SEMF corrections, open). Probe + audit: `probes/su4_occupancy_binding_probe.py`. |
| `E_C` | EM-sector **Coulomb energy** `E_C = (3/5)Z(Z−1)·α_EM·ℏc/(r₀·A^1/3)` MeV (standard uniform-sphere; r₀=1.2 fm, α_EM·ℏc=1.43996 MeV·fm — not fit). The strong B-forms carry NO EM term; E_C is the repulsion that REDUCES net binding for proton-rich nuclei. Reported additively, **not** subtracted from the B-columns (they are calibrated against Coulomb-inclusive AME, so a global subtraction would double-count). E_C is cleanly separable only in the mirror-pair DIFFERENCE, where the strong core cancels: CS-core + E_C reproduces the ³H/³He, ⁷Li/⁷Be, ¹³C/¹³N splits to ~20–40% vs the production σ/σ⁻¹ bond's ~200–350% (bean 754x). Module: `coulomb_energy.py`; probe: `probes/coulomb_mirror_killswitch_probe.py`. |
| `err sym` / `err qCLT_fac` / `err gate` / `err vol` | B_AME / B_model for the production + occupancy + volume forms (1.00 = perfect, >1 under-binds, <1 over-binds) |

**Table 2 — Mass M + error** (values and error in one table; m_X = m_unbnd,can − B_X)

| Header | Meaning |
|---|---|
| `M_meas` | measured mass: M_AME = mu − B_AME for nuclei, or measured constituent mu for lone p/n. **Comparison target only — appears in NO predicted formula.** |
| `σ_exp (ppb)` | experimental 1σ on the mass = σ_B / M_meas × 10⁹ |
| `m_can` | **CANONICAL derived mass — the single Borromean per-knot pipeline** (`borromean_binding_recompute.borromean_binding`): `m_can = m_unbnd,can − B_tower`, the convergent per-braid brane tower over the Borromean nucleon trace `τ=\|tr_M(β_Bor)\|=0.9986<1` (shares τ with `F_Bor` / bean `ovud`; converges ∀Z). Pure Markov × m_e; zero AME/CODATA beyond CAL-1/CAL-2. Does NOT close to AME — the Δ_λ frontier (right shape, wrong per-λ normalization). |
| `m_can⁰` | brane-tower **level 0** on the atom-word trace: `m_unbnd,can − E₀·Δtr`. Comparison only — its higher Li₂^q tower diverges for Z≥2 (atom-word `tr_p>1`); the Borromean `m_can` is the canonical one. |
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

This dashboard's q₀ is the **canonical 3-CAL (muon-anchored) value** — the CAL-2
experimental ideal m_μ/m_e (q₀ ≈ 1.10998), so masses/binding are the
canonical-derivation numbers. The proton re-pin m_p/m_e (0.06 ppb) is a
*precision substitution* in the separate Physical-Observations layer — not a 4th
calibration, not used here. Source:
`observations/three-calibration-discipline.md` §3,
`observations/epistemic-status-of-calibrations.md`.

**Mass constituents (Table 2):** `m_unbnd,can` = framework unbound sum
Z·m_p,can + N·m_n,can via the canonical muon-anchored Hecke energy
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

### Mass  M + error (MeV; err in ppb)   [canonical = muon-anchored Hecke energy 2(m_μ·F_Bor−6m_e); m_X = m_unbnd,can − B_X]
  canonical constituents (λ_A fit + naive Vol·tr_M both EXCISED): m_p,can = 938.272 MeV (+0.000%), m_n,can = 939.565 MeV (+0.000%) — m_μ-anchored F_Bor = |tr_M(β_Bor)|·[3]_q!/q³ (matches CODATA; m_n the genuine prediction).
| iso  |   A |  M_meas | σ_exp (ppb) |   m_can |  m_can⁰ |                     m_tetra |  m_qCLT | err m_can (ppb) | err m_qCLT (ppb) |
| ---- | --: | ------: | ----------: | ------: | ------: | --------------------------: | ------: | --------------: | ---------------: |
| p    |   1 |   938.3 |           — |   938.3 |   938.3 |                        -0.3 |   938.3 |           1.351 |            1.351 |
| n    |   1 |   939.6 |           — |   939.6 |   939.6 |                         0.3 |   939.6 |           2.389 |            2.389 |
| 2H   |   2 |  1875.6 |        0.21 |  1875.4 |  1876.1 |                         0.1 |  1875.6 |     -136342.920 |        -4833.421 |
| 4He  |   4 |  3727.4 |        0.21 |  3749.3 |  3752.0 |                        -0.1 |  3747.2 |     5877670.138 |      5308238.182 |
| 7Li  |   7 |  6533.8 |        0.64 |  6559.6 |  6569.4 |                        -6.5 |  6554.1 |     3950413.779 |      3094434.522 |
| 9Be  |   9 |  8392.8 |        9.12 |  8430.9 |  8447.3 |                       -56.2 |  8425.6 |     4544322.097 |      3914558.595 |
| 12C  |  12 | 11174.9 |        0.21 | 11234.4 | 11263.2 |                     -1299.9 | 11233.4 |     5326257.901 |      5239172.587 |
| 16O  |  16 | 14895.1 |        0.21 | 14966.6 | 15019.0 |                    -84458.5 | 14976.5 |     4802062.537 |      5468395.410 |
| 24Mg |  24 | 22335.8 |        0.64 | 22410.1 | 22530.6 |                -356298782.6 | 22462.8 |     3327205.449 |      5685272.524 |
| 40Ca |  40 | 37214.7 |        0.64 | 37213.3 | 37553.7 |         -6340889590615775.0 | 37435.3 |      -37057.864 |      5926972.782 |
| 56Fe |  56 | 52089.8 |        5.16 | 51896.9 | 52580.1 | -112845967092774483263488.0 | 52405.6 |    -3702350.090 |      6063564.099 |

### Atomic mass  M_atom = M_nuclear + Z·m_e − B_el(Z)  (vs RAW AME neutral-atom mass)
| iso  |   A |   Z | M_atom_AME | M_atom_pred(sym) | err sym (ppb) | σ_exp (ppb) | e⁻ layer (MeV) |
| ---- | --: | --: | ---------: | ---------------: | ------------: | ----------: | -------------: |
| p    |   1 |   1 |    938.783 |          938.783 |        -0.910 |        0.01 |          0.511 |
| n    |   1 |   0 |    939.565 |          939.565 |         1.037 |        0.47 |          0.000 |
| 2H   |   2 |   1 |   1876.124 |         1876.115 |     -4833.896 |        0.01 |          0.511 |
| 4He  |   4 |   2 |   3728.401 |         3746.378 |   4821588.732 |        0.04 |          1.022 |
| 7Li  |   7 |   3 |   6535.366 |         6551.029 |   2396652.061 |        0.64 |          1.533 |
| 9Be  |   9 |   4 |   8394.795 |         8421.292 |   3156312.312 |        9.10 |          2.044 |
| 12C  |  12 |   6 |  11177.929 |        11227.431 |   4428488.228 |           — |          3.065 |
| 16O  |  16 |   8 |  14899.169 |        14967.956 |   4616873.601 |        0.02 |          4.086 |
| 24Mg |  24 |  12 |  22341.925 |        22449.006 |   4792842.070 |        0.54 |          6.127 |
| 40Ca |  40 |  20 |  37224.918 |        37411.100 |   5001546.567 |        0.55 |         10.201 |
| 56Fe |  56 |  26 |  52103.063 |        52370.214 |   5127355.587 |        5.13 |         13.251 |
### Binding  B + error (MeV)   [σ_exp = AME2020 1σ; err X = B_AME/B_X (1.00 = perfect, >1 under-binds)]
| iso  |   A |  B_AME | σ_exp (ppb) | B_can⁰ |  B_sym |                     B_tetra | B_qCLT_fac | B_gate |  B_vol |    E_C | err can⁰ | err sym | err tetra | err qCLT_fac | err gate | err vol |
| ---- | --: | -----: | ----------: | -----: | -----: | --------------------------: | ---------: | -----: | -----: | -----: | -------: | ------: | --------: | -----------: | -------: | ------: |
| p    |   1 |   0.00 |           — |   0.00 |   0.00 |                        0.00 |       0.00 |   7.58 |   7.58 |   0.00 |        — |       — |         — |            — |     0.00 |    0.00 |
| n    |   1 |   0.00 |           — |   0.00 |   0.00 |                        0.00 |       0.00 |   7.58 |   7.58 |   0.00 |        — |       — |         — |            — |     0.00 |    0.00 |
| 2H   |   2 |   2.22 |      179.81 |   1.70 |   2.23 |                        0.02 |       2.23 |   9.18 |  15.17 |   0.00 |     1.31 |    1.00 |    140.66 |         1.00 |     0.24 |    0.15 |
| 4He  |   4 |  28.30 |       28.27 |   3.71 |  10.32 |                        0.28 |       8.51 |  29.99 |  30.33 |   0.91 |     7.64 |    2.74 |    100.32 |         3.33 |     0.94 |    0.93 |
| 7Li  |   7 |  39.25 |      107.02 |   3.66 |  23.58 |                        7.03 |      19.03 |  26.81 |  53.08 |   2.26 |    10.71 |    1.66 |      5.58 |         2.06 |     1.46 |    0.74 |
| 9Be  |   9 |  58.16 |     1315.25 |   3.61 |  31.67 |                       56.81 |      25.31 |  31.95 |  68.25 |   4.15 |    16.09 |    1.84 |      1.02 |         2.30 |     1.82 |    0.85 |
| 12C  |  12 |  92.16 |       26.04 |   3.79 |  42.66 |                     1300.31 |      33.61 |  51.92 |  91.00 |   9.43 |    24.33 |    2.16 |      0.07 |         2.74 |     1.78 |    1.01 |
| 16O  |  16 | 127.62 |       25.07 |   3.67 |  58.83 |                    84459.03 |      46.17 |  30.78 | 121.34 |  16.00 |    34.82 |    2.17 |      0.00 |         2.76 |     4.15 |    1.05 |
| 24Mg |  24 | 198.26 |       72.63 |   3.43 |  91.17 |                356298783.40 |      71.27 |      — | 182.01 |  32.95 |    57.81 |    2.17 |      0.00 |         2.78 |        — |    1.09 |
| 40Ca |  40 | 342.05 |       70.16 |   3.00 | 155.85 |         6340889590615776.00 |     121.48 |      — | 303.34 |  80.00 |   113.91 |    2.19 |      0.00 |         2.82 |        — |    1.13 |
| 56Fe |  56 | 492.26 |      546.05 |   1.97 | 225.07 | 112845967092774483263488.00 |     176.41 |      — | 424.68 | 122.32 |   249.30 |    2.19 |      0.00 |         2.79 |        — |    1.16 |

  B_sym closed-form chain ≡ exact p(3A) trace: max|Δ| = 1.7e+00 MeV over {p, n, 2H, 4He, 7Li} (n=3A ≤ 21; float64 dashboard noise — the chain ≡ trace to the 50-dps floor through ¹²C, audit 2026-06-16-b-sym-linear-chain-closed-form.md). Chain used for all A.

### Entanglement  (E₀·bar-even = retained binding/volume, E₀·|bar-odd| = emitted γγ̄ channel)
| iso  |   A | retained E (MeV) | emitted E (MeV) | multi-link emit (MeV) | emitted/retained |
| ---- | --: | ---------------: | --------------: | --------------------: | ---------------: |
| p    |   1 |            2.373 |           2.087 |                 0.000 |           0.8796 |
| n    |   1 |            2.327 |           1.538 |                 0.000 |           0.6609 |
| 2H   |   2 |            0.829 |           0.797 |                 1.235 |           0.9608 |
| 4He  |   4 |            0.116 |           0.116 |                 1.908 |           0.9987 |
| 7Li  |   7 |            0.004 |           0.004 |                 1.834 |           1.0000 |
| 9Be  |   9 |                — |               — |                     — |                — |
| 12C  |  12 |                — |               — |                     — |                — |
| 16O  |  16 |                — |               — |                     — |                — |
| 24Mg |  24 |                — |               — |                     — |                — |
| 40Ca |  40 |                — |               — |                     — |                — |
| 56Fe |  56 |                — |               — |                     — |                — |

### Entanglement-augmented binding  (B_sym+ent = B_sym + multi-link emit; error = B_AME/B)
| iso  |   A |  B_AME |  B_sym | err sym | B_sym+ent | err sym+ent |
| ---- | --: | -----: | -----: | ------: | --------: | ----------: |
| p    |   1 |   0.00 |   0.00 |       — |      0.00 |           — |
| n    |   1 |   0.00 |   0.00 |       — |      0.00 |           — |
| 2H   |   2 |   2.22 |   2.23 |    1.00 |      3.47 |        0.64 |
| 4He  |   4 |  28.30 |  10.32 |    2.74 |     12.23 |        2.31 |
| 7Li  |   7 |  39.25 |  23.58 |    1.66 |     25.42 |        1.54 |
| 9Be  |   9 |  58.16 |  31.67 |    1.84 |         — |           — |
| 12C  |  12 |  92.16 |  42.66 |    2.16 |         — |           — |
| 16O  |  16 | 127.62 |  58.83 |    2.17 |         — |           — |
| 24Mg |  24 | 198.26 |  91.17 |    2.17 |         — |           — |
| 40Ca |  40 | 342.05 | 155.85 |    2.19 |         — |           — |
| 56Fe |  56 | 492.26 | 225.07 |    2.19 |         — |           — |

### Colour-weighting  (B_qCLT_fac = isospin-symmetric baseline + p↔n chirality)
| iso  |   A | bonds pp/pn/nn | sym baseline | + chirality | = B_qCLT_fac |
| ---- | --: | :------------: | -----------: | ----------: | -----------: |
| p    |   1 | 0/0/0          |         0.00 |       +0.00 |         0.00 |
| n    |   1 | 0/0/0          |         0.00 |       +0.00 |         0.00 |
| 2H   |   2 | 0/1/0          |         2.23 |       +0.00 |         2.23 |
| 4He  |   4 | 1/4/1          |         6.70 |       +1.81 |         8.51 |
| 7Li  |   7 | 3/12/6         |        13.40 |       +5.62 |        19.03 |
| 9Be  |   9 | 6/20/10        |        17.87 |       +7.44 |        25.31 |
| 12C  |  12 | 15/36/15       |        24.57 |       +9.04 |        33.61 |
| 16O  |  16 | 28/64/28       |        33.50 |      +12.66 |        46.17 |
| 24Mg |  24 | 66/144/66      |        51.37 |      +19.90 |        71.27 |
| 40Ca |  40 | 190/400/190    |        87.11 |      +34.37 |       121.48 |
| 56Fe |  56 | 325/780/435    |       122.85 |      +53.56 |       176.41 |

### Compositional B_sym  (m_sym(W) = −α·ln tr_M(W); free = GB components)
| iso  |   A | m_sym(free comps) | m_sym(atom) | B_sym (chain) | Δ vs exact trace |
| ---- | --: | ----------------: | ----------: | ------------: | ---------------: |
| p    |   1 |            -0.265 |      -0.265 |         0.000 |          0.0e+00 |
| n    |   1 |             0.334 |       0.334 |         0.000 |          0.0e+00 |
| 2H   |   2 |             0.070 |       2.303 |         2.234 |          1.7e+00 |
| 4He  |   4 |             0.139 |      10.458 |        10.319 |          1.7e+00 |
| 7Li  |   7 |             0.543 |      24.125 |        23.582 |          1.7e+00 |
| 9Be  |   9 |             0.612 |      32.280 |        31.667 |    —  (no trace) |
| 12C  |  12 |             0.417 |      43.077 |        42.659 |    —  (no trace) |
| 16O  |  16 |             0.556 |      59.386 |        58.830 |    —  (no trace) |
| 24Mg |  24 |             0.834 |      92.005 |        91.170 |    —  (no trace) |
| 40Ca |  40 |             1.391 |     157.242 |       155.852 |    —  (no trace) |
| 56Fe |  56 |             3.145 |     228.220 |       225.075 |    —  (no trace) |

### SU(4) Dynamic Occupancy  (E_gate = E₀·ln(1/W_λ), c_λ = B_AME/E_gate)
| iso  |   A |   S | partition λ   |               W_λ | E_gate (MeV) | B_AME (MeV) |     c_λ | err gate (%) |
| ---- | --: | --: | ------------- | ----------------: | -----------: | ----------: | ------: | -----------: |
| p    |   1 | 0.5 | (1,1,1)       |          0.163383 |         7.58 |        0.00 |       — |            — |
| n    |   1 | 0.5 | (1,1,1)       |          0.163383 |         7.58 |        0.00 |       — |            — |
| 2H   |   2 | 1.0 | (2,2,1,1)     |          0.111452 |         9.18 |        2.22 |  0.2422 |        312.9 |
| 4He  |   4 | 0.0 | (3,3,3,3)     |          0.000774 |        29.99 |       28.30 |  0.9435 |          6.0 |
| 7Li  |   7 | 1.5 | (6,6,5,4)     |          0.001655 |        26.81 |       39.25 |  1.4640 |        -31.7 |
| 9Be  |   9 | 1.5 | (8,7,6,6)     |          0.000484 |        31.95 |       58.16 |  1.8204 |        -45.1 |
| 12C  |  12 | 0.0 | (9,9,9,9)     |          0.000004 |        51.92 |       92.16 |  1.7750 |        -43.7 |
| 16O  |  16 | 0.0 | (12,12,12,12) |          0.000641 |        30.78 |      127.62 |  4.1468 |        -75.9 |
| 24Mg |  24 | 0.0 | (18,18,18,18) | 9611580844.572039 |       -96.22 |      198.26 | -2.0605 |       -148.5 |
| 40Ca |  40 | 0.0 | (30,30,30,30) |               nan |          nan |      342.05 |     nan |          nan |
| 56Fe |  56 | 0.0 | (43,43,41,41) |               nan |          nan |      492.26 |     nan |          nan |

  Forms: B_sym=α·ln(tr_free/tr_atom)=α[(Z−1)L_pp+L_pn+(N−1)L_nn] (exact linear chain, all A) · B_qCLT=α·(A−1)·ℓ̄(D) · B_qCLT_fac=α·(A−1)·⟨bond-type L⟩. Defn: standard-part-functor.md.
