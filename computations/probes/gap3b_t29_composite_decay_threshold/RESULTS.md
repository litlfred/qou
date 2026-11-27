# Results: Closing Open Gap 3 Backup (Option 3B, `qou-618l`) — Dynamical 3-Body Threshold & Resolvent-Cut Audit of Composite $T(2,9) \to 3 \times T(2,3)$ in $H_2(q_0) / H_3(q_0)$

- **Branch**: `claude/gap3b-t29-composite-decay-threshold-20261123`
- **Bean**: `qou-618l` (Option 3B backup to Open Gap 3, companion to `qou-x4qm`, `qou-xtcl`, `qou-91w7`)
- **Pre-registration commit**: `30143e1b796` (`PREREGISTRATION.md`, committed & pushed prior to probe authoring/execution)
- **Lean 4 formalization**: `folio/quantum-observable-universe/lean/QOU/StandardModel/CompositeT29ThresholdInstability.lean` (`8297fe6c1e2`, `0 sorry`, `0` custom axioms, `[propext, Classical.choice, Quot.sound]` only, generic `[CommRing R]` / `[Field K]` / `[LinearOrder K] [IsStrictOrderedRing K]` per `AGENTS.md §7c`)
- **80-dps probe & witness**: `gap3b_t29_composite_decay_threshold_probe.py` (`a1fcefb39e0`) $\to$ `gap3b-t29-composite-decay-threshold.witness.json` (`940244c5e5c`, `workdps = 80`, `q0Anchor = "proton"`, `8/8` assertions passed, `probe-float64-guard` clean, zero fitted parameters)

---

## 1. Executive Summary of Exact Findings

1. **Exact Arithmetic & Topological 3-Body Threshold (`{3, 5, 7}` vs `9`):**
   Among Bring's four genus-$\le 4$ single-component odd torus knots $T(2,n)$ ($n \in \{3, 5, 7, 9\}$, $\gcd(2,n) = 1$, $g(T_{2,n}) = (n-1)/2 \le 4$), parity forbids **all** 2-body odd-knot splits $n = n_1 + n_2$ (`no_two_odd_winding_split`: even windings $2k \ge 2$ are 2-component links such as the Hopf link $T(2,2)$). For 3-body splits into non-trivial odd torus knots ($n_i \ge 3$ odd), the minimum winding / minimal-crossing sum is $3 + 3 + 3 = 9$ (`three_odd_knot_threshold_nine`, `threeOddKnotChannels_bring_window`):
   - $n \in \{3, 5, 7\}$: **zero** 3-knot channels ($\mathcal{C}_3(n) = \emptyset$; under signed writhe $n_1 - n_2 + n_3 = n$ with antifermion $-n_2$, total crossings still satisfy $n_1 + n_2 + n_3 \ge \max(9, n + 6)$, `signed_three_knot_crossing_budget`).
   - $n = 9$: **unique** admissible winding reaching the threshold, via the **unique** channel $(3, 3, 3)$, with strictly super-additive Seifert genus $g(T_{2,9}) = 4 > 3 = 3\,g(T_{2,3})$.

2. **Exact Hecke Operator Fission & Renormalized Cubic Law (`hecke_pow3_quadratic_and_pow9_fission`):**
   In *any* associative $R$-algebra where $s^2 = h s + 1$, the trefoil cube $\Sigma := s^3$ satisfies its own quadratic Hecke relation $\Sigma^2 = h_3 \Sigma + 1$ with $h_3 = h(h^2 + 3) = q^3 - q^{-3}$, giving the exact operator decomposition
   $$s^9 = P_6(h)\,s^3 + h(h^2 + 3)\,\mathbf{1}, \qquad P_6(h) = h^6 + 6h^4 + 9h^2 + 1 = h_3^2 + 1,$$
   while $\{f_3(h), f_5(h), f_7(h)\}$ are **pairwise Bézout coprime** (`heckeCont_generation_coprime_and_t29_dvd`), so $s^5, s^7 \notin \mathbb{Z}[h]\cdot \mathbf{1} + \mathbb{Z}[h]\cdot s^3$.

3. **Decisive Two-Arm Sign Dichotomy at Proton-Pinned $q_0 = 1.1099785827513808\dots$:**
   Testing $Q_3(q) := E(T_{2,9}; q) - 3\,E(T_{2,3}; q)$ across every QOU trace/energy/resolvent functional without prior sign assumptions reveals an exact structural split between **unsubtracted total traces (Arm A)** and **classical-vacuum-subtracted / hook-channel functionals (Arm B)**:
   - **Arm A (Unsubtracted Total Traces & Toroidal `#9213` Resolvent) is KINEMATICALLY CLOSED at $q_0$ ($Q_3(q_0) < 0$, $\Gamma_9 = 0$):** Because $\sigma^{2m+1}\big|_{q=1} = \sigma$ for every odd winding, unsubtracted traces approach a positive $n$-independent constant $c_0 > 0$ at $q = 1$ ($f_n(0) = 1$, $\tau_D(\sigma_1^n; 1) = 1/2$), forcing $Q_3(1) = -2 c_0 < 0$. The proton pin $q_0 = 1.10997858\dots$ lies **strictly below** the exact algebraic crossover roots $q_{\mathrm{crit}}^{(\tau)} = 1.1789596431\dots$ and $q_{\mathrm{crit}}^{(f)} = \big(\frac{\sqrt{6}+\sqrt{2}}{2}\big)^{1/3} = 1.2454451084\dots$ (`continuant_sub_vs_super_crossover`, `tauTorusOdd_sub_vs_super_crossover`).
   - **Arm B (Subtracted / Hook $(2,1)$ / Quantum-Integer / Genus Functionals) is UNIVERSALLY OPEN for ALL $q > 1$ ($Q_3(q) > 0$):** Removing the classical $q = 1$ transposition baseline—or projecting onto $H_3(q)$'s $(2,1)$ hook character $\chi_{(2,1)}(\sigma_1^{2m+1}) = q^{2m+1} - q^{-(2m+1)}$ or balanced quantum integer $[n]_q$—makes $Q_3(q) > 0$ strictly positive for **every** $q > 1$ (`hook21_t29_strict_superadditive`, `qIntBal_t29_strict_superadditive`, `deltaContinuant_t29_strict_superadditive`, `deltaTauTorus_t29_strict_superadditive`), shifting the dressed resolvent pole strictly into the lower half-plane at $\mathrm{Im}(z_{\mathrm{pole}}) = -\Gamma_9 / 2 < 0$ (`resolvent_second_sheet_above_threshold`).

4. **Perturbative Dalitz Width Suppression vs $O(1)$ Algebraic Fission (`W1` vs `W2`):**
   Even on Arm B where $Q_3(q_0) > 0$ is open ($\delta_3 = Q_3 / E_9 \in [11.89\%, 71.88\%]$), 3-body relativistic Dalitz phase space carries the universal loop/phase-space factor $(256\pi^3 S_{\mathrm{id}})^{-1} \approx 6.31 \times 10^{-5} / S_{\mathrm{id}}$, yielding **narrow** perturbative contact widths $\Gamma_9 / E_9 \in [2.84 \times 10^{-9},\, 9.64 \times 10^{-6}] \ll 1$. By contrast, the **algebraic Hecke operator fission `(W1)`** $\sigma_1^9 = P_6(h_0)\sigma_1^3 + h_3\mathbf{1}$ exhibits an **$O(1)$ scalar-transient component** ($r_{\mathrm{lin}} = h_3 / \tau_D(\sigma_1^9; q_0) = 34.8016\%$, $r_{\mathrm{quad}} = h_3^2 / (P_6(h_0)^2 + h_3^2) = 17.0223\%$). Thus Option 3B excludes a 4th generation via Fock-space compositeness ($\sigma_1^9 \in \mathbb{Z}[h][\sigma_1^3]$) rather than via a broad perturbative 4-fermion width alone.

---

## 2. Arm A: Unsubtracted Trace, Continuant & Toroidal Resolvent Audit at $q_0$ (`workdps = 80`)

At $q_0 = 1.10997858275138080759\dots$ ($h_0 = q_0 - q_0^{-1} = 0.2090602988\dots$, $\tau_e(q_0) = 0.6911664784\dots$), all five unsubtracted functionals satisfy $Q_3(q_0) = E(9) - 3\,E(3) < 0$:

| Functional | $E(3)$ | $E(5)$ | $E(7)$ | $E(9)$ | $Q_3(q_0) = E(9) - 3 E(3)$ | Critical Root $q_{\mathrm{crit}}$ | Status at $q_0$ |
|---|---:|---:|---:|---:|---:|---:|---|
| **(A1)** Chebyshev $q^n + q^{-n}$ | `2.0987855445` | `2.2784041810` | `2.5576032257` | `2.9485854103` | **`-3.3477712232`** | `1.2454451084` | **CLOSED** ($q_0 < q_{\mathrm{crit}}$) |
| **(A2)** Continuant $f_n(h)$ | `1.0437062085` | `1.1330288583` | `1.2718719035` | `1.4663036475` | **`-1.6648149781`** | `1.2454451084` | **CLOSED** ($q_0 < q_{\mathrm{crit}}$) |
| **(A2b)** Normal-form $\mathrm{net}_n(h)$ | `1.2527665073` | `1.5602866889` | `1.9360010858` | `2.3963307499` | **`-1.3619687721`** | `1.1943913840` | **CLOSED** ($q_0 < q_{\mathrm{crit}}$) |
| **(A3)** Markov $\tau_D(\sigma_1^n; q)$ | `0.8485266071` | `1.1214510578` | `1.4433898823` | `1.8284138061` | **`-0.7171660151`** | `1.1789596431` | **CLOSED** ($q_0 < q_{\mathrm{crit}}$) |
| **(A4)** `#9213` Resolvent $W = \tau_D / \tau_e$ | `1.2276732649` | `1.6225483916` | `2.0883389567` | `2.6454028998` | **`-1.0376168949`** | `1.1789596431` | **CLOSED** ($q_0 < q_{\mathrm{crit}}$) |

*(Note: for `(A1)` and `(A2)`, $q_{\mathrm{crit}} = \big(\frac{\sqrt{6}+\sqrt{2}}{2}\big)^{1/3}$ is exact in radicals, matching numerical Newton–Raphson to $4.22 \times 10^{-80}$.)*

---

## 3. Arm B: Universally Super-Additive Functionals & 3-Body Decay Widths (`workdps = 80`)

With fixed zero-parameter couplings $\lambda_4^{\mathrm{Hecke}} = h_3 = q_0^3 - q_0^{-3} = 0.6363181294\dots$ and $\lambda_4^{\mathrm{EM}} = 4\pi\alpha_q(q_0) = 0.0917016274\dots$ ($\alpha_q(q_0)^{-1} = 137.0354154444\dots$):
- **(W1) Direct Hecke Operator Fission Ratios ($\sigma_1^9 = P_6(h_0)\sigma_1^3 + h_3\mathbf{1}$, $P_6(h_0) = 1.4049007618\dots$):**
  $$r_{\mathrm{lin}}(q_0) = \frac{h_3}{\tau_D(\sigma_1^9; q_0)} = 0.3480164760\dots \;(34.80\%), \qquad r_{\mathrm{quad}}(q_0) = \frac{h_3^2}{P_6(h_0)^2 + h_3^2} = 0.1702231465\dots \;(17.02\%).$$
- **(W2) Relativistic Dalitz Contact Widths $\Gamma_{9 \to 333}^{\mathrm{rel}} / E(9)$ & (W3) NR Threshold Asymptotics:**

| Arm B Functional | $E(3)$ | $E(9)$ | $Q_3 = E(9) - 3 E(3)$ | $\delta_3 = Q_3 / E(9)$ | $I_{\mathrm{Dalitz}}(\mu)$ | $\Gamma^{\mathrm{rel}} / E_9$ ($\lambda_4^{\mathrm{Hecke}}, S_{\mathrm{id}}=2$) | $\Gamma^{\mathrm{rel}} / E_9$ ($\lambda_4^{\mathrm{EM}}, S_{\mathrm{id}}=2$) |
|---|---:|---:|---:|---:|---:|---:|---:|
| **(B1)** Hook $\chi_{(2,1)} = q^n - q^{-n}$ | `0.6363181294` | `2.1666000836` | **`+0.2576456953`** | `11.8917%` | `0.0160677527` | `4.098115 × 10⁻⁷` | `8.511177 × 10⁻⁹` |
| **(B2)** $q$-integer $[n]_q$ | `3.0437062085` | `10.3635175881` | **`+1.2323989625`** | `11.8917%` | `0.0160677527` | `4.098115 × 10⁻⁷` | `8.511177 × 10⁻⁹` |
| **(B3)** $\Delta f_n = f_n(h) - 1$ | `0.0437062085` | `0.4663036475` | **`+0.3351850219`** | `71.8813%` | `0.3777705561` | `9.635120 × 10⁻⁶` | `2.001072 × 10⁻⁷` |
| **(B4)** $\Delta\tau_D = \tau_D - 1/2$ | `0.3485266071` | `1.3284138061` | **`+0.2828339849`** | `21.2911%` | `0.0488227845` | `1.245236 × 10⁻⁶` | `2.586170 × 10⁻⁸` |
| **(B5)** Seifert genus $(n-1)/2$ | `1.0000000000` | `4.0000000000` | **`+1.0000000000`** | `25.0000%` | `0.0658302273` | `1.679014 × 10⁻⁶` | `3.487064 × 10⁻⁸` |

---

## 4. Honest Epistemic Scope & Rule-13a Guardrail (`CompositeT29DecayExclusionHypothesis`)

- **What is unconditionally proved (`0` free parameters, `0` empirical literals):**
  1. $n = 9$ is the unique Bring-admissible odd torus winding in $\{3, 5, 7, 9\}$ above the 3-odd-knot $(3,3,3)$ arithmetic/crossing threshold, and $\sigma^9 = P_6(h)\sigma^3 + h(h^2+3)\mathbf{1} \in \mathbb{Z}[h][\sigma^3]$ whereas $\{f_3, f_5, f_7\}$ are pairwise Bézout coprime.
  2. Unsubtracted trace/resolvent functionals (`Arm A`) give $E(9) < 3 E(3)$ at $q_0$ (3-body channel closed), whereas classical-subtracted and $(2,1)$-hook functionals (`Arm B`) give $E(9) > 3 E(3)$ for **every** $q > 1$ (3-body channel open, shifting the resolvent pole off the real axis).
- **What remains open (isolated in zero-instance `CompositeT29DecayExclusionHypothesis`):**
  1. **Physical mass map `T(2,n) ↦ m_phys(n)`:** Neither Arm A nor Arm B reproduces the observed $O(10^2\text{--}10^3)$ charged-lepton hierarchy ($m_\mu / m_e \approx 206.77$, $m_\tau / m_e \approx 3477.23$) without the inhomogeneous hyperbolic/satellite carrier (`#9213`, `C_{2,7}(4_1)`).
  2. **Narrow decay vs chiral generation counting:** Because 3-body Dalitz phase space suppresses perturbative contact widths to $\Gamma_9 / E_9 \sim 10^{-9}\text{--}10^{-5}$ (narrow resonance, just as unstable $\mu, \tau$ remain chiral generations), excluding $T(2,9)$ from the fundamental chiral spectrum relies on **algebraic Fock-space compositeness** ($\sigma^9 \in \mathbb{Z}[h][\sigma^3]$, `W1` transient fraction $17.02\%\text{--}34.80\%$) or the primary Riemann–Roch + gauge-anomaly mechanism (Option 3A, `BringPrymRiemannRochGenerations.lean`), rather than perturbative decay width alone.
