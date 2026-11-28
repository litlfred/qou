# Impact of Twisted & Adjoint Reidemeister Torsion Determinants Across Open Gaps (`2026-11-28`)

**Date:** 2026-11-28  
**Owner Research Prompt:** *"explore impact of 'That makes twisted torsion determinants a prime candidate whenever a per-loop measure or Stokes normalization factor (`A_0`, $\alpha_{\mathrm{EM}}$ loop measure, or $5_2$ saddle weight) needs a canonical geometric prefactor'. can we close gaps?"* + *"can we step the knot word through reeb flow (sub plank?? next order down) steps and generate a path on the tesselation? use that in our na-stokes?"*  
**Pin & Anti-Fit Discipline:** Strictly proton-pinned $q_0 = q_{\mathrm{at}}(95) = 1.10997858275138080759\ldots$ (`q0Anchor = "proton"`, `physical_proton` in `computations/q0_anchor_manifest.json`; muon pin on hold per owner ruling `2026-11-28`), `80`-dps `mpmath` (`probe-float64-guard` clean), **zero fitted parameters**.

## Artefacts Delivered

1. **Lean 4 Formalization (`0 sorry`, standard 3 axioms, `0` `[Field]`/`field_simp`, `0` transcendental tokens):**  
   [`folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/AdjointTorsionSaddlePrefactors.lean`](../../folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/AdjointTorsionSaddlePrefactors.lean) (wired into `QOU.lean`)
2. **80-dps Proton-Pinned Verification Probe & Witness:**  
   [`computations/probes/twisted_torsion_gap_exploration_probe.py`](../../computations/probes/twisted_torsion_gap_exploration_probe.py) & [`computations/probes/twisted-torsion-gap-exploration-probe.witness.json`](../../computations/probes/twisted-torsion-gap-exploration-probe.witness.json)

---

## Executive Verdict Table

| Candidate Gap / Target | Twisted / Adjoint Torsion Datum | Outcome | Lean 4 / 80-dps Evidence |
|---|---|---|---|
| **1. `4₁` Kashaev 1-Loop Prefactor (`hτ` in `OneLoopPrefactorInvariance.lean`) & `A_ω(4₁)`** | Meridian DG torsion $|\tau_{\mathrm{DG},\mu}(4_1)| = \sqrt{3}/2$; longitude $|\tau_{\mathrm{DG},\lambda}(4_1)| = 3$; deformed $A$-poly disc | **GAP CLOSED IN LEAN (`0 sorry`)** | `fourOne_dg_torsion_mu_lam_and_cusp_shape` proves $(2\tau_{\mathrm{DG},\mu})^2 = -3$ (**discharging `hτ`**), $\tau_{\mathrm{DG},\lambda} = -3$ ($|\tau_\lambda| = 3 = \mathrm{tr}(RL) = s(1) = A_\omega(4_1)$), and `fourOne_deformed_apoly_disc_factors` proves $4-(L+L^{-1})^2 = (M-M^{-1})^2 [2]_M^2 \Delta_{4_1}(M^2) s(M^2)$. |
| **2. `5₂` Three-Saddle 1-Loop Weights & Euler–Jacobi Cancellation** | $2\tau_{\mathrm{DG},\mu}(5_2; \xi_j) = 3\xi_j^2 - 3\xi_j + 5 = P'(\xi_j)/\xi_j$ over $P(\xi) = \xi^3 - 2\xi^2 + 3\xi - 1 = 0$ (`disc = -23`) | **GAP CLOSED IN LEAN (`0 sorry`)** | `fiveTwo_dg_torsion_eq_saddle_deriv` & `fiveTwo_three_saddle_norm_and_euler_jacobi` prove the closed form over `[CommRing A]`, norm $\prod_{j=0}^2 \tau_{\mathrm{DG},\mu}(5_2; \xi_j) = 23/8$, and exact cancellation of the 3 squared Ohtsuki saddle weights $\sum \omega_j^2 \propto \sum 1/(2\tau_j) = 0$, $\sum \xi_j/\tau_j = 2$. |
| **3. `(-2,3,7)` Pretzel (`m016`, `#9778`) 6-Block & 1-Loop Saddle Prefactors** | `2 τ_{DG,μ}(-2,3,7) = 10ξ² - 16ξ + 20`, `2 τ_{DG,λ}(-2,3,7) = 6ξ² - 6ξ + 10` | **NEW EXACT SISTER BRIDGE PROVED (`0 sorry`)** | `pretzel_sister_torsion_bridge` proves **$\tau_{\mathrm{DG},\lambda}(-2,3,7) = 2\,\tau_{\mathrm{DG},\mu}(5_2)$ identically** and cusp shape $1 - \xi$ ($|1 - \xi_0| = \rho = 1.3247179572\ldots$, plastic constant); `pretzel_state_integral_saddle_splits` proves `6 = 3 (disc -23) + 3 (disc +49)` saddle split. |
| **4. Archimedean `A_0 = π²/5` vs Stokes `A_ω = 3`** | Longitude torsion $|\tau_{\mathrm{DG},\lambda}(K)|$ vs Rogers $\operatorname{Li}_2(\phi^{-2})$ | **SEPARATED (Structural Scope)** | Torsion gives algebraic numbers ($|\tau_{\mathrm{DG},\lambda}(4_1)| = 3 = A_\omega(4_1)$, $|\tau_{\mathrm{DG},\lambda}(5_2)| = 4.50890\ldots \in \overline{\mathbb{Q}}$), NOT transcendental $A_0 = \pi^2/5$ (which is weight-2 dilogarithmic, cf. `golden_dilog_quartic_vs_classical_separation`). |
| **5. `α_EM` Form B (`μ₁ = 1/(8π)`) & Form C (`Δ_{B₃}(q₀)`)** | $1/\sqrt{8\pi \mathbb{T}_{\mathrm{Ad}}(4_1)}$, $\mathbb{T}(4_1; u)/\mathbb{T}(0)$ ($u \in \{\ln q_0, \hbar_{q_0}\}$), $\Delta_{4_1}(q_0)$ | **CLEANLY REFUTED (`60σ`–`47,068σ`)** | Every $4_1$ torsion replacement/dressing of $\mu_1 = 1/(8\pi)$ degrades Form B from `-0.365 ppb` (`-2.38σ`) to `-9.20 ppb`..`+7212.9 ppb` (`60σ`–`47,068σ`); 1-loop torsion shifts are `5.8×`–`128×` smaller than Form C's weight-3 $\delta_{\mathrm{req}}(q_0) = 0.295228$. $\mu_1$ is a 2D Bring-surface period, not a 3D knot torsion. |
| **6. Lepton Links `(e, μ, τ)` & EW Torus Links `{T(2,4), T(2,6), T(2,8)}` (`Gap C`)** | $\Delta_e = 1$, $\Delta_\mu = 1 + t_1 t_2$, $\Delta_\tau = (t_1 - 1)(t_2 - 1)$; $\Omega_{T(2,2k)}$ | **LEPTON ORDER REFUTED; EW `[k]_q` PROVED** | `lepton_two_var_alexander_inverts_tau_order` proves $0 < |\Delta_\tau| \ll \Delta_e < \Delta_\mu$ at both $(q_0, q_0)$ (`0.0121 < 1 < 2.2321`) and $(q_0, q_0^{-1})$ (`0.0109 < 1 < 2`), inverting $\tau$ because $\mathrm{lk}(\tau) = 0$. Conversely, `symTorusLinkAlex_telescopes_to_qInt` proves diagonal symmetrized Alexander torsion of $T(2,2k)$ equals $[k]_q$ (`k = 1..4`). |
| **7. Stepwise Word / Reeb / Farey Gluing $\leftrightarrow$ `na-Stokes` (`Cross-Fertilization`)** | Stallings $R \cdot L$ (`4₁`), Farey `RL` (`5₂`), 1D $\Phi_b$ state-integral Hessians | **EXACT IN $b \to 0$ SADDLE; POLYNOMIAL AT FINITE $n$** | Word-stepped gluing/state-integral Hessians equal $2|\tau_{\mathrm{DG},\mu}|$ to 80 dps on `4₁` ($\sqrt{3}$), `5₂` ($2.322325\ldots$), and framed `(-2,3,7)` ($3.506143\ldots$). At finite strand count $n$ and real $q_0 > 1$, `na-Stokes` traces stay in $\mathbb{Z}[q_0^{\pm 1}]$ (`[k]_{q_0}`); non-abelian $\tau_{\mathrm{DG}}$ enters only in the continuum $\Phi_b$ double-scaling limit. |

---

## 1. Gaps Closed & Hypotheses Discharged in Lean 4 (`0 sorry`)

### 1.1 Discharging `hτ` on $4_1$, Proving $|\tau_{\mathrm{DG},\lambda}(4_1)| = 3 = A_\omega(4_1)$, and Factoring Deformed Cusp Torsion
- **Upstream gap (`MathlibExt/OneLoopPrefactorInvariance.lean`, lines 362–371):** In the $4_1$ Kashaev 1-loop prefactor chain ($c_\sigma = 3^{-1/4}$, $k = 2^{-1/2}$), `hc` was already derived in `FigureEightVolume`, leaving **`hτ` ($|\tau_{\mathrm{DG}}(4_1)| = |\cot\theta^*|/2 = \sqrt{3}/2$) as the single open hypothesis**.
- **Closed (`fourOne_dg_torsion_mu_lam_and_cusp_shape`):** Over any `[CommRing A]` at $\omega^2 - \omega + 1 = 0$, every shape inverse $\zeta = 1 - \omega$ and $\zeta' = \omega$ and the Neumann flattening inverse $(\zeta'_0 \zeta'_1)^{-1} = -\omega$ are integral polynomials in $\omega$. Evaluating the exact $2 \times 2$ Dimofte–Garoufalidis HNF edge + peripheral determinants proves:
  $$2\tau_{\mathrm{DG},\mu}(4_1) = 1 - 2\omega, \quad (2\tau_{\mathrm{DG},\mu}(4_1))^2 = -3, \quad 2\tau_{\mathrm{DG},\lambda}(4_1) = -6, \quad (2\tau_{\mathrm{DG},\lambda})^2 = -12\,(2\tau_{\mathrm{DG},\mu})^2.$$
  Thus $|\tau_{\mathrm{DG},\mu}(4_1)| = \sqrt{3}/2$ (discharging `hτ`), $|\tau_{\mathrm{DG},\lambda}(4_1)| = 3 = \mathrm{tr}(R \cdot L) = s(1) = A_\omega(4_1)$, and $|\tau_\lambda / \tau_\mu| = 2\sqrt{3}$ (cusp shape).
- **Deformed $A$-polynomial factorization (`fourOne_deformed_apoly_disc_factors`):** Over any `[CommRing A]` and unit `M : Aˣ`, with $L + L^{-1} = M^4 - M^2 - 2 - M^{-2} + M^{-4}$:
  $$4 - (L + L^{-1})^2 = (M - M^{-1})^2 (M + M^{-1})^2 (-M^2 + 3 - M^{-2})(M^2 + 1 + M^{-2}),$$
  factoring the squared deformed cusp torsion into $[2]_M^2 \cdot \Delta_{4_1}(M^2) \cdot s(M^2)$ — uniting the abelian Alexander polynomial $\Delta_{4_1}$ and GGM's non-abelian Stokes meridian character $s(x) = x + 1 + x^{-1}$!

### 1.2 Exact $5_2$ Three-Saddle Adjoint Torsion, Norm `23/8`, and Euler–Jacobi Saddle Cancellation
- **Closed (`fiveTwo_dg_torsion_eq_saddle_deriv` & `fiveTwo_three_saddle_norm_and_euler_jacobi`):** On `GeneratedGluing.K52` (`z = (\xi, \xi^2 - \xi + 2, \xi)`, $P(\xi) = \xi^3 - 2\xi^2 + 3\xi - 1 = 0$), all shape inverses and the Neumann flattening inverse $\xi^2 - \xi$ lie in $\mathbb{Z}[\xi]$. The $3 \times 3$ DG determinants evaluate over `[CommRing A]` to:
  $$2\tau_{\mathrm{DG},\mu}(5_2; \xi) = 3\xi^2 - 3\xi + 5 = \frac{P'(\xi)}{\xi}, \qquad 2\tau_{\mathrm{DG},\lambda}(5_2; \xi) = -26\xi^2 + 38\xi - 50.$$
  Along the Vieta locus $(\xi_0 + \xi_1 + \xi_2, \sum \xi_i\xi_j, \xi_0\xi_1\xi_2) = (2, 3, 1)$, the product over all 3 saddles is $\prod_{j=0}^2 (2\tau_{\mathrm{DG},\mu}(5_2; \xi_j)) = 23 = |\mathrm{disc}(K_{5_2})|$, and the squared Ohtsuki 1-loop saddle weights $\omega_j^2 = (2 i \tau_j)^{-1}$ satisfy the exact Euler–Jacobi sum rules:
  $$\sum_{j=0}^2 \frac{1}{\tau_{\mathrm{DG},\mu}(5_2; \xi_j)} = 0, \qquad \sum_{j=0}^2 \frac{\xi_j}{\tau_{\mathrm{DG},\mu}(5_2; \xi_j)} = 2.$$

### 1.3 Sister-Manifold Torsion Identity (`5_2` $\leftrightarrow$ `(-2,3,7)` Pretzel) & 6-Block Saddle Split
- **Closed (`pretzel_sister_torsion_bridge` & `pretzel_state_integral_saddle_splits`):** The Weeks sister manifold `m016` (`(-2,3,7)` pretzel, `#9778` `PretzelLevelTwoBlockFactorization`) has complete shapes $(\xi, \xi^2 - \xi + 2, \xi^2 - \xi + 2)$ in the same $\mathrm{disc} = -23$ field $\mathbb{Q}(\xi)$. Its exact $3 \times 3$ DG determinants over `[CommRing A]` satisfy:
  $$2\tau_{\mathrm{DG},\mu}(-2,3,7) = 10\xi^2 - 16\xi + 20, \qquad 2\tau_{\mathrm{DG},\lambda}(-2,3,7) = 6\xi^2 - 6\xi + 10 = 2 \cdot \big(2\tau_{\mathrm{DG},\mu}(5_2)\big),$$
  with cusp shape $\tau_\lambda / \tau_\mu = 1 - \xi$ ($|1 - \xi_0| = \rho = 1.324717957244746\ldots$, the plastic constant $\rho^3 = \rho + 1$), so $|\tau_{\mathrm{DG},\mu}(-2,3,7)| = (2/\rho)|\tau_{\mathrm{DG},\mu}(5_2)| = 1.7530716358\ldots$. Furthermore, the $q \to 1$ saddle polynomial of `#9778`'s degree-6 descendant operator splits as:
  $$(1 - Z)^2(1 - Z^2)^2 - Z^2 = (Z^3 - Z^2 + 1)(Z^3 - Z^2 - 2Z + 1),$$
  partitioning the `6` holomorphic blocks into `3` hyperbolic sister saddles ($\mathrm{disc} = -23$) plus `3` abelian $\mathbb{Z}/7$ dihedral saddles ($\mathrm{disc} = +49 = 7^2$, matching $\det(-2,3,7) = 1$, $|H_1(\Sigma_2)| = 1$, and pretzel twist $7$).

---

## 2. Quantitative Refutations on $\alpha_{\mathrm{EM}}$ & Lepton Mass Ordering (80-dps Proton Pin)

### 2.1 Why $4_1$ Reidemeister Torsion Does NOT Supply $\alpha_{\mathrm{EM}}$'s $\mu_1$ or $\Delta_{B_3}$ (`Gap B`)

| Pre-Registered $\mu_1$ Candidate (`Form B` Cubic at Proton $q_0$) | $\mu_1$ Value | $\alpha_{\mathrm{EM}}^{-1}$ Prediction | Residual vs CODATA-22 (`ppb`) | Pull (`σ`) | Verdict |
|---|---:|---:|---:|---:|---|
| **Baseline Bring Period `1 / (8π)`** | `0.039788735773` | `137.035999126951` | **`-0.365 ppb`** | **`-2.38σ`** | Retained (`FormBMinimalKernelClass`) |
| `1 / √(8π · 2√3)` (`T_Porti(4₁) = 2√3`) | `0.107172844763` | `137.036987609713` | `+7212.94 ppb` | `+47,068σ` | **Refuted** |
| `1 / (8π · |τ_{DG,μ}(4₁)|)` (`√3 / 2`) | `0.045944074619` | `137.036089422516` | `+658.55 ppb` | `+4,297σ` | **Refuted** |
| `(1/(8π)) · T_Porti(4₁; u = ln q₀) / T(0)` | `0.039697119391` | `137.035997782986` | `-10.17 ppb` | `-66.38σ` | **Refuted** (`28×` worse, wrong sign) |
| `(1/(8π)) · T_Porti(4₁; u = ħ_{q₀}) / T(0)` | `0.039706244040` | `137.035997916840` | `-9.20 ppb` | `-60.01σ` | **Refuted** (`25×` worse, wrong sign) |
| `(1/(8π)) · Δ_{4₁}(q₀) / Δ_{4₁}(1)` | `0.039355163223` | `137.035992766666` | `-46.78 ppb` | `-305.25σ` | **Refuted** |
| `(1/(8π)) / Δ_{4₁}(q₀)` | `0.040227084956` | `137.036005557306` | `+46.56 ppb` | `+303.82σ` | **Refuted** |

On **Form C**, $\delta_{\mathrm{req}}(q_0) = 0.2952278\ldots$ (`Δ_{B₃}(q₀) = ζ(3) - Li₃(q₀⁻²) = 0.2757369...`, `-0.024 ppb = -0.16σ`), whereas $1 - \Delta_{4_1}(q_0) = 0.010897$, $1 - \mathbb{T}(\ln q_0)/\mathbb{T}(0) = 0.002303$, $\ln(s(q_0)/3) = 0.003626$, and $2 h_0^2/\sqrt{3} = 0.050468$ miss by **`5.8×` to `128×`**. Physically and mathematically, $\alpha_{\mathrm{EM}}$ lives on the **2D genus-4 Bring surface** ($\mu_1 = 1/(8\pi)$ at weight 1, $\zeta(3) - \operatorname{Li}_3(q_0^{-2})$ at weight 3), not on a 3D knot complement.

### 2.2 Two-Variable Alexander Torsion on `(e, μ, τ)` vs Torus-Link `[k]_q` (`Gap C`)
- **Lepton ordering inversion (`lepton_two_var_alexander_inverts_tau_order`):** Because $\mathrm{lk}(e)=1, \mathrm{lk}(\mu)=2, \mathrm{lk}(\tau)=0$, $\Delta_\tau(t_1, t_2) = (t_1 - 1)(t_2 - 1)$ vanishes to second order at $t_1 = t_2 = 1$, giving `(Δ_e, Δ_μ, Δ_τ) = (1, 2.23205, 0.01210)` at $(q_0, q_0)$ and `(1, 2, -0.01090)` at $(q_0, q_0^{-1})$ — strictly inverting $|\Delta_\tau| \ll \Delta_e < \Delta_\mu$. Non-abelian $\tau_{\mathrm{DG}}$ exists on hyperbolic $\tau$ (`L5a1`, $|\tau_{\mathrm{DG}}| = \sqrt{2}$) but not on Seifert $e, \mu$.
- **Positive EW torus-link bridge (`symTorusLinkAlex_telescopes_to_qInt`):** For 2-component torus links $T(2, 2k)$, the diagonal symmetrized Conway–Alexander torsion at $\sqrt{t_1 t_2} = q_0$ is **identically $[k]_{q_0}$** (`1, 2.01090, 3.04371, 4.10968` for $k = 1..4$), identifying the electroweak carrier factors with abelian Reidemeister link torsions.

---

## 3. Cross-Fertilization: Stepwise Word / Tessellation Paths, `na-Stokes`, and 1-Loop Torsion

1. **Where the Word-Step $\to$ Tessellation $\to$ Torsion Bridge Works Exactly:**
   - Stepping a 3-braid word such as $4_1 = (\sigma_1 \sigma_2^{-1})^2$ (`FigureEightGluingFromMonodromy`) or a 2-bridge Farey path such as $5_2 \leftrightarrow RL$ (`FiveTwoGluingFromFareyWord`) generates a discrete path in the Farey / $(2,4,5)$-adjacent modular tessellation whose elementary steps are $\mathrm{SL}(2,\mathbb{Z})$ Dehn twists ($R, L$) / Pachner 2–3 tetrahedral flips.
   - Quantizing each flip step into a Faddeev $\Phi_b$ non-abelian Stokes operator (`aomega_m3_pretzel_level2_stokes_probe.py`) produces the 1D state integral $Z_K(b)$. Our probe verifies to `80 dps` that the **1-loop Gaussian saddle Hessian** $|V''(v_*)|$ of this word-stepped state integral equals $2|\tau_{\mathrm{DG},\mu}(K)|$ on **$4_1$** ($\sqrt{3}$), **$5_2$** ($2.322325476\ldots$), and — after dividing by the framing monomial $|Z_0|^3 = |\xi_0|$ — on **`(-2,3,7)` pretzel** ($3.506143272\ldots$)!
2. **Where the Regime Boundary Sits (`NaStokesKeystone` vs Continuum State Integrals):**
   - In `NaStokesKeystone.lean`, finite-$n$ Hecke / `na-Stokes` holonomies at real $q_0 > 1$ have eigenvalues $(q_0, -q_0^{-1})$ and evaluate via Markov trace to rational functions in $\mathbb{Q}(q_0)$ (such as `[k]_{q_0}`, matching abelian torus-link Alexander torsion).
   - Non-abelian hyperbolic volumes $\mathrm{Vol}(K)$ and algebraic-irrational torsions $\tau_{\mathrm{DG}}(K) \in \{\sqrt{3}/2, \overline{\mathbb{Q}}_{-23}\}$ **cannot** appear at finite polynomial order in $H_n(q_0)$ (Melvin–Morton–Rozansky); they emerge **only** when the word-stepped `na-Stokes` product is lifted from finite-dimensional $H_n(q_0)$ to the infinite-dimensional Faddeev $\Phi_b$ representation on $L^2(\mathbb{R})$ and evaluated at its $b \to 0$ saddle.
