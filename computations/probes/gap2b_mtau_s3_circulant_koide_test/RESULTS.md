# Results: $S_3$-Equivariant / $\mathbb{Z}_3$-Circulant Mass Matrix & Algebraic Koide Trace-to-Norm Test on Bring's 3-Generation Subspace `projGen3` (Open Gap 2 Backup, Option 2B / `qou-j96h`)

- **Branch**: `claude/gap2b-mtau-s3-circulant-koide-test-20261123`
- **Pre-Registration**: `computations/probes/gap2b_mtau_s3_circulant_koide_test/PREREGISTRATION.md` (committed & pushed at `5b8b9353c36` **before** any numerical evaluations)
- **Lean 4 Formalization**: `folio/quantum-observable-universe/lean/QOU/StandardModel/S3CirculantKoideTraceIdentity.lean` (`0 sorry`, `0` custom `axiom`s, `set_option autoImplicit false`, generic `[CommRing R]` / `[Field F]`, verified via `lean -j 1 -DautoImplicit=false -s 65536` with exit `0`)
- **80-dps Probe & Witness**:
  - `computations/probes/gap2b_mtau_s3_circulant_koide_test/gap2b_mtau_s3_circulant_koide_probe.py` (`probe-float64-guard.py` clean: `0` hits)
  - `computations/probes/gap2b_mtau_s3_circulant_koide_test/gap2b-mtau-s3-circulant-koide-probe.witness.json` (`ComputationWitness` schema validated, `allPassed = true`, `q0Anchor = "proton"`)

---

## 1. Executive Verdict (`Gate G-2B`: **FALSIFIED** for Un-Tuned Finite-$q_0$ Operators; Classical $q = 1$ Equipartition + QOU Bare $\mathrm{Vol}(4_1)/\hbar_{q_0}^2$ Hits $+61.6\text{ ppm}$)

1. **Exact Algebraic Theorems Proved in Lean 4 (`S3CirculantKoideTraceIdentity.lean`)**:
   - **Hermitian Circulant Trace-to-Norm & Equipartition (`koide_circulant_poly_identity`, `koideCirculantRatio_eq_two_thirds_iff`, `koideVecRatio_eq_two_thirds_iff_equipartition`)**:
     For $S(a, b, \bar{b}) = a I_3 + b C + \bar{b} C^2$ over `QuadI R`, $\mathrm{Tr}(S) = 3a$, $\mathrm{Tr}(S^\dagger S) = \mathrm{Tr}(S^2) = 3(a^2 + 2|b|^2)$, and $3\,\mathrm{Tr}(S^2) - 2(\mathrm{Tr}\,S)^2 = 9(2|b|^2 - a^2)$. Hence $Q_{\mathrm{Koide}} = \frac{1 + 2r^2/a^2}{3} = \frac{2}{3} \iff 2r^2 = a^2 \iff \|\lambda_{\mathrm{doublet}}\|_3^2 = \|\lambda_{\mathrm{dem}}\|_3^2$.
   - **Unbroken $S_3$-Equivariance Degeneracy Obstruction (`commutes_s3_iff_eq_symmetric_circulant`, `symmetric_circulant_doublet_degeneracy`)**:
     Every full $S_3$-equivariant operator on the 3-generation module has $b = c$, annihilating $(X - (a + 2b))(X - (a - b))$ with degenerate doublet eigenvalues $\lambda_1 = \lambda_2 = a - b$. Breaking $S_3 \downarrow A_3 \cong \mathbb{Z}_3$ ($b \neq c$) is strictly required to split all three charged-lepton masses.
   - **Bring `projGen3` Ambient-$F^5$ Metric Stretch (`bring_projGen3_ambient_metric_stretch`)**:
     On Bring's 3-generation subspace `projGen3 = projDem1 + projDoublet2` $\subset V_{\mathrm{std}} \subset F^5$, `demVec3 = (1, 1, 1, -3, 0)` has squared $F^5$ norm $12 = 4 \cdot 3$, stretching the singlet norm squared by an exact factor of $4$ relative to intrinsic generation coordinates $F^3$ (`normSq5 (projDem1 (embedGen3 λ)) = 4 * normSq3 (demProj3 λ)`). Naive ambient-$F^5$ equipartition would yield $Q = 5/3 \neq 2/3$.
   - **Monic Koide Quadratic Resolvent (`koide_quadratic_resolvent_ring_identity`, `koide_quadratic_completed_square_and_discriminant`, `koideVecRatio_two_thirds_iff_resolvent_zero`)**:
     Over every `[CommRing R]`,
     $$3(u^2 + v^2 + x^2) - 2(u + v + x)^2 = x^2 - 4(u + v)x + (u^2 + v^2 - 4uv) = \bigl(x - 2(u + v)\bigr)^2 - 3(u^2 + 4uv + v^2),$$
     with discriminant $\Delta(u, v) = 12(u^2 + 4uv + v^2)$.
   - **Classical $q = 1$ Equipartition vs Universal Finite-$q$ Departure in $TL_3(q)$ (`tl3_classical_equipartition_at_one`, `tl3KoideNormRatio_closed_form_and_deficit`, `tl3_strict_departure_from_two_thirds`)**:
     Temperley–Lieb Convention-D Wedderburn trace weights $y_{(3)}(q) = 1 - 2/[2]_q^2$ and $2 y_{(2,1)}(q) = 2/[2]_q^2$ achieve **exact** $1/2 = 1/2$ singlet–doublet equipartition ($Q_{\mathrm{TL3}}(1) = 2/3$) at $q = 1$, while QOU's ruled chiral photon vertex $\sigma_0 \sigma_1^{-1}$ on $M_{+1}$ reduces at $q = 1$ directly to the cyclic shift $C$ (`stepPlus_at_one_eq_cyclicShift3`). However, for **every** $q > 1$ in an ordered field,
     $$\frac{2}{3} - Q_{\mathrm{TL3}}(q) = \frac{(q - q^{-1})^2}{3(q^2 + q^{-2})} > 0.$$

2. **Pre-Registered `Gate G-2B` Numerical Outcome (`mp.dps = 80`, `q0Anchor = "proton"`)**:
   - **Equipartition at $q_0$ (`Part B`)**: **Falsified** for un-dressed finite-$q_0$ weights. At $q_0 = 1.1099785827513808...$, $Q_{\mathrm{TL3}}(q_0) = 0.6595380803186473...$, which lies $-0.00712859$ (`-1.0693%`, $-10{,}734\sigma$) below empirical $Q_{\mathrm{Koide}}^{\mathrm{exp}} = 0.66666050(66)$.
   - **Zero-Parameter $q_0$ Phases (`Part C`)**: **Falsified** across all six $q_0$-derived expressions $\{\theta_1, \theta_2, \theta_3, \theta_4, \theta_6, \theta_7\}$. Because $\theta_{\mathrm{exp}} = 0.222222047073...$ rad sits within $0.03958$ rad of the electron chiral zero $\theta_{\mathrm{crit}} = \pi/12 = 0.2617993878...$, logarithmic mass-ratio sensitivities exceed $50\times$ ($\frac{d\ln(m_\mu/m_e)}{d\theta} = +56.14$, $\frac{d\ln(m_\tau/m_e)}{d\theta} = +51.23$). Even the closest $q_0$ expression $\theta_3 = 2(q_0 - 1) = 0.21995717$ (`-1.02%` in $\theta$) misses $m_\mu / m_e$ by `-11.66%` and $m_\tau / m_e$ by `-10.67%`, and $q_0$-deforming Brannen's rational $\theta_5 = 2/9 = 2/[3]_{q=1}^2$ (`+9.83 ppm` on $m_\mu/m_e$, `+70.41 ppm` on $m_\tau/m_e$) to $\theta_6 = 2/[3]_{q_0}^2$ degrades the prediction to `-28.30%` and `-26.02%`.
   - **Hybrid Classical-$Q=2/3$ + QOU Zero-`CAL-2` Muon Resolvent (`R2a` in `Part A`)**: Feeding QOU's proton-anchored bare figure-eight muon prediction $(m_\mu / m_e)_{\mathrm{QOU}} = \mathrm{Vol}(4_1)/\hbar_{q_0}^2 = 206.76832637...$ into the exact $q = 1$ Koide resolvent $Q = 2/3$ yields **$m_\tau / m_e = 3477.44230642$** (`+0.006163% = +61.63 ppm`, $+0.923\sigma$ vs NIST CODATA-2022 $3477.23 \pm 0.23$, $+9.318\sigma$ vs Belle-II/PDG-2024 $3477.228 \pm 0.023$), virtually identical to classic `CAL-1 + CAL-2` Koide (`3477.44163628`, `+61.44 ppm`), but **conditional** on an unproved $q$-undeformed ($q \to 1$) Koide equipartition mechanism (`KoideCirculantEquipartitionHypothesis`, Rule 13a).

---

## 2. Detailed 80-dps Tables

### 2.1 Substrate & Empirical Benchmarks (`mp.dps = 80`)

| Quantity | Value | Notes |
|---|---|---|
| $q_0 = \mathrm{q\_at}(80)$ (`proton`) | `1.1099785827513808075916690956107688798744991218736` | `CAL-1` + $\mathrm{Vol}(4_1)$ + CODATA $m_p/m_e$ |
| $\hbar_{q_0} = 1 - q_0^{-1}$ | `0.099081716044258507839177117518906063985258373389446` | Semi-classical expansion parameter |
| $h_{q_0} = q_0 - q_0^{-1}$ | `0.20906029879563931543084621312967494385975749526302` | Hecke skein parameter |
| $(m_\mu / m_e)_{\mathrm{CODATA-2022}}$ | `206.7682827 ± 0.0000046` | NIST `allascii.txt` (`10.1103/RevModPhys.97.025002`) |
| $(m_\tau / m_e)_{\mathrm{PDG-2024}}$ | `3477.228 ± 0.023` | Belle-II / PDG-2024 (`10.1103/PhysRevD.110.030001`) |
| $(m_\tau / m_e)_{\mathrm{NIST-2022}}$ | `3477.23 ± 0.23` | NIST `allascii.txt` (`10.1103/RevModPhys.97.025002`) |
| $Q_{\mathrm{Koide}}^{\mathrm{exp}}$ (PDG-2024) | `0.66666050352627157727 ± 6.6355e-7` | $Q_{\mathrm{exp}} - 2/3 = -6.16314 \times 10^{-6}$ (`-9.29σ`) |
| $\theta_{\mathrm{exp}}$ (from CODATA $m_\mu/m_e$) | `0.22222204707308784876 rad` | Margin to $\pi/12$ zero: `0.03957734 rad` |

---

### 2.2 Part A — Quadratic Resolvent $m_\tau / m_e$ Predictions under Exact $Q_{\mathrm{Koide}} = 2/3$

| Model | Input $m_\mu / m_e$ | Predicted $m_\tau / m_e = x_+^2$ | Diff vs PDG `3477.228` | Rel. Error | Pull vs PDG (`±0.023`) | Pull vs NIST (`±0.23`) |
|---|---:|---:|---:|---:|---:|---:|
| **`R1_codata_cal1_cal2`** | `206.76828270` | `3477.44163628` | `+0.21364` | `+0.006144%` (`+61.4 ppm`) | `+9.29σ` | `+0.92σ` |
| **`R2a_qou_bare_vol41`** (zero `CAL-2`) | `206.76832637` | `3477.44230642` | `+0.21431` | `+0.006163%` (`+61.6 ppm`) | `+9.32σ` | `+0.92σ` |
| **`R2b_qou_inhomogeneous_9213`** | `207.17372167` | `3483.66286778` | `+6.43487` | `+0.185057%` (`+1851 ppm`) | `+279.78σ` | `+27.97σ` |

---

### 2.3 Part B — Un-Tuned $H_3(q_0)$ & Bring `projGen3` Operator Equipartition Tests

| Candidate Operator | $\rho_{2/1} = 2r^2 / a^2$ | $Q(q=1)$ | $Q(q_0)$ | $Q(q_0) - 2/3$ | Verdict |
|---|---:|---:|---:|---:|---|
| **`Op_B1_identity`** ($I_3$) | `0` | `0.33333333` | `0.33333333` | `-0.333333` | Fails ($m_e = m_\mu = m_\tau$) |
| **`Op_B2_democratic_D3`** ($\frac{1}{3} D_3$) | `2` | `1.00000000` | `1.00000000` | `+0.333333` | Fails ($m_e = m_\mu = 0$) |
| **`Op_B3_isotropic_Z3` / `projGen3` DOF** | `2` | `1.00000000` | `1.00000000` | `+0.333333` | Fails ($1:2$ DOF ratio $\neq 1:1$) |
| **`Op_B4_TL3_convD_wedderburn_norm`** (`y3` vs `2y21`) | `0.97861424` | **`0.66666667` (`2/3` exact)** | `0.65953808` | `-0.007129` (`-1.069%`) | Exact at $q=1$; **fails at $q_0$** (`-10734σ`) |
| **`Op_B5_H3_regular_plancherel_qdim`** | `4.02179373` | `1.66666667` | `1.67393124` | `+1.007265` | Fails ($Q > 1$, non-positive roots) |
| **`Op_B6_chiral_vertex_Mplus1`** ($\kappa = 1$) | — | — | `0.51761243` | `-0.149054` | Fails ($m_\mu/m_e = 4.99, m_\tau/m_e = 45.7$) |
| **`Op_B6_chiral_vertex_Mplus1`** ($\kappa = 1/\sqrt{2}$) | — | — | `0.42468007` | `-0.241987` | Fails ($m_\mu/m_e = 2.29, m_\tau/m_e = 11.6$) |

---

### 2.4 Part C — Pre-Registered Zero-Parameter Phase Tests $\theta_j$ under Exact $Q = 2/3$

| Phase Candidate | $q_0$-Derived? | $\theta_j$ (rad) | $\theta_j - \theta_{\mathrm{exp}}$ | Pred. $m_\mu / m_e$ | Rel. Err ($m_\mu/m_e$) | Pred. $m_\tau / m_e$ | Rel. Err ($m_\tau/m_e$) | `< 1%` Both? |
|---|:---:|---:|---:|---:|---:|---:|---:|:---:|
| **`theta_1`** $= 2\hbar_{q_0}$ | Yes | `0.1981634321` | `-0.0240586` (`-10.83%`) | `69.70800` | `-66.2869%` | `1322.8248` | `-61.9575%` | No |
| **`theta_2`** $= 2\ln q_0$ | Yes | `0.2086814406` | `-0.0135406` (`-6.09%`) | `106.30914` | `-48.5854%` | `1912.4710` | `-45.0001%` | No |
| **`theta_3`** $= 2(q_0 - 1)$ | Yes | `0.2199571655` | `-0.0022649` (`-1.02%`) | `182.65038` | `-11.6642%` | `3106.2918` | `-10.6676%` | No |
| **`theta_4`** $= q_0 - q_0^{-1}$ | Yes | `0.2090602988` | `-0.0131617` (`-5.92%`) | `108.07609` | `-47.7308%` | `1940.5564` | `-44.1924%` | No |
| **`theta_5`** $= 2/9 = 2/[3]_{q=1}^2$ | **No** (lit. benchmark) | `0.2222222222` | `+1.7515e-7` (`+0.79 ppm`) | `206.77032` | **`+0.000983%` (`+9.83 ppm`)** | `3477.4728` | **`+0.007041%` (`+70.41 ppm`)** | Benchmark only |
| **`theta_6`** $= 2/[3]_{q_0}^2$ | Yes | `0.2158860277` | `-0.0063360` (`-2.85%`) | `148.24844` | `-28.3021%` | `2572.5777` | `-26.0164%` | No |
| **`theta_7`** $= \alpha_{\mathrm{chiral}}(q_0) - 2\pi/3$ | Yes | `0.0254231003` | `-0.1967989` (`-88.56%`) | `1.53183` | `-99.2592%` | `84.8835` | `-97.5589%` | No |

---

## 3. Structural Interpretation & Rule-13a Boundary

Both halves of the empirical Koide–Brannen structure ($Q = 2/3$ and $\theta \approx 2/9$) appear inside the Temperley–Lieb / Hecke generation algebra **strictly at the classical undeformed point $q = 1$** ($y_{(3)}(1) = 2 y_{(2,1)}(1) = 1/2 \implies Q_{\mathrm{TL3}}(1) = 2/3$, and $2 / [3]_{q=1}^2 = 2/9$), while replacing $q = 1 \mapsto q_0 \approx 1.10998$ introduces $O((q_0 - q_0^{-1})^2) \approx 4.37\%$ quantum deformations that spoil both relations (`-1.07%` on $Q$, `-28.30%` on $m_\mu / m_e$ via $2/[3]_{q_0}^2$). Conversely, if $Q = 2/3$ is protected as a topological $q \to 1$ representation-ring invariant while the 2-generation scale $m_\mu / m_e = \mathrm{Vol}(4_1)/\hbar_{q_0}^2$ comes from the hyperbolic saddle cut (`R2a`), $m_\tau / m_e = 3477.4423$ (`+61.6 ppm`) follows with zero `CAL-2` input. Until a first-principles QOU operator theorem derives why the square-root mass operator is protected from finite-$q_0$ Wedderburn drift, Option 2B remains **open** and gated behind the zero-instance class `KoideCirculantEquipartitionHypothesis` in `S3CirculantKoideTraceIdentity.lean`.
