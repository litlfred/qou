# Pre-Registration: Two-Loop $\alpha_{\mathrm{EM}}$ `EmFermionLoop` 4-Topology Identity & Bloch-$B_3(\mathbb{C})$ Working-Assumption Probe (`qou-l4t2`, `qou-9y43`)

**Date:** 2026-11-24  
**Beans:** `qou-l4t2`, `qou-9y43`  
**Posture:** Strict zero-fit working-assumption probe (`NO FITTING, EXCEPT CAL-1/2/3`; owner ruling `qou-aemx`: *"no form is chosen by its residual"*; nothing wired into production dashboards).

---

## 1. Pre-Committed Algebraic Theorem (Part A — Exact 2-Vertex `EmFermionLoop` Coefficient `1`)

Before running any numerical evaluation, we pre-commit to testing whether summing over **all four** signed chiral 2-vertex crossing histories $(\epsilon_1, \epsilon_2) \in \{+1, -1\}^2$ under the Kazhdan–Lusztig bar-Hermitian skein pairing $(-\epsilon_1 \epsilon_2)\,\sigma^{\epsilon_1} \sigma^{\epsilon_2}$ on the fundamental representation $V^{\otimes 3}$ (`photon pair (1,2)` projected onto singlet $e_- = (q I - \hat{R})/[2]_q$, `matter strand 3` = `EmFermionLoop` $V_F = \mathbb{C}^2$, plus cross-position $V^{\otimes 4}$) satisfies:

1. $\operatorname{qTr}_{123}(e_- \otimes I_2) = [2]_q$,
2. $m(\sigma_2^2) - 1 = +h\,m(\sigma_2) = \frac{q^4 - q^2}{q^2 + 1}$ and $m(\sigma_2^{-2}) - 1 = -h\,m(\sigma_2) + h^2 = \frac{1 - q^2}{q^4 + q^2}$,
3. $\sum_{\epsilon_1,\epsilon_2 \in \{+,-\}} (-\epsilon_1 \epsilon_2)\,m(\sigma_2^{\epsilon_1}\sigma_2^{\epsilon_2}) = -1 \cdot h^2$ identically in $\mathbb{Q}(q)$ (cancelling the chiral order-$(q-1)^1$ tadpoles $\pm h\,m(\sigma_2)$), while explicitly recording the open vertex-normalization hypothesis (`S = σ - σ⁻¹` vs `(σ - σ⁻¹)/2`) as `§3b-cond`.

---

## 2. Pre-Committed Zero-Parameter Two-Loop Operator Family (Part B — Bloch-$B_3(\mathbb{C})$ / Bring / QED)

For the two-loop $O(\alpha_{\mathrm{EM}}^2)$ slot $\Delta(1/\alpha_{\mathrm{EM}}) = c_2(q)\,\alpha_{\mathrm{EM}}^2$ in
$$\frac{1}{\alpha_{\mathrm{EM}}} = T_{\mathrm{EM}}(q) + \alpha_{\mathrm{EM}}\,H(q)\,(1 - h^2 \alpha_{\mathrm{EM}}) + c_2(q)\,\alpha_{\mathrm{EM}}^2, \qquad H(q) = \frac{[2]_q}{\pi\,b_1(\Sigma_4)} = \frac{[2]_q}{8\pi},$$
we pre-commit to evaluating the following **fixed, zero-parameter** candidate family at both `q_proton` and `q_muon`, scored transparently against both CODATA 2022 (`qou_substrate.codata` registry) and CODATA 2018 (`137.035999084`, provenance control), alongside the `Form A` and `CS tower` arms (`qou-aemx`):

1. `C0_FormB_baseline`: $c_2(q) = 0$ (1-loop Form-B baseline).
2. `C1_BlochB3_EmFermionLoop`: $c_2(q) = H(q)\,\frac{\zeta(3) - \operatorname{Li}_3(q^{-2})}{\pi\,b_1(\Sigma_4)} = \frac{[2]_q\,(\zeta(3) - \operatorname{Li}_3(q^{-2}))}{(8\pi)^2}$ (one `EmFermionLoop` factor $H(q) = [2]_q/(8\pi)$ times the weight-3 Bloch-$B_3(\mathbb{C})$ trilogarithm $q$-defect $\Delta_{B_3}(q) = \operatorname{Li}_3(1) - \operatorname{Li}_3(q^{-2})$ per Bring harmonic period $8\pi$; vanishes identically at $q = 1$).
3. `C2_BlochB3_bare_64pi2`: $c_2(q) = \frac{\zeta(3) - \operatorname{Li}_3(q^{-2})}{(8\pi)^2}$ (bare weight-3 $B_3(\mathbb{C})$ defect without `[2]_q`).
4. `C3_JostLuttinger_QED_3over4pi_H`: $c_2(q) = H(q)\,\frac{3}{4\pi}$ (4D QED 2-loop/1-loop Jost–Luttinger vacuum-polarization ratio $\beta_1/\beta_0 = 3/(4\pi)$).
5. `C4_PetermannSommerfield_H_CPS_over_pi`: $c_2(q) = H(q)\,\frac{C_{\mathrm{PS}}}{\pi}$, where $C_{\mathrm{PS}} = \frac{197}{144} + \frac{\pi^2}{12} - \frac{\pi^2}{2}\ln 2 + \frac{3}{4}\zeta(3) \in \operatorname{span}_{\mathbb{Q}}\{1, \pi^2, \pi^2\ln 2, \zeta(3)\}$.
6. `C5_BringZeroMode_h2`: $c_2(q) = \frac{2}{3\pi}\,h^2$ (Bring zero-mode dressed by $h^2$).
7. `C6_ThetaGraph_residual`: $c_2(q) = -\frac{[3]_q}{(8\pi)^2} + H(q)\,h^2$ (total $\theta(1,1,2) = -[3]_q/(8\pi)^2$ replacement of Form B's $O(\alpha^2)$ term).

**Addendum 2026-11-28 (research arm, not scored, not wired).** Registered after the 2026-11-24 evaluation, so it carries no pre-registration standing and must not be scored against CODATA here:

8. `R1_FlatSunset_zeta3` (research arm): connected two-loop period $\kappa_2 = r\,\zeta(3)$, from the flat-torus sunset identity $C_{1,1,1}(\tau) - E_3(\tau) = \zeta(3)$ (Zagier / D'Hoker–Green–Vanhove, cited) on a torus quotient of Bring. Lean: `QOU.Transcendental.MassTheory.FlatSunsetConnectedPeriod` (identity carried as a hypothesis field); slot decomposition $\theta\mu_2 = \theta\mu_1^2 + \theta\kappa_2$ in `QOU.MassTheory.EmTwoLoopMeasureConnected`. Underived: the rational normalization $r$ (probability measure gives $1$, un-normalized gives $|H|^2$, $|H| \in \{2,4,4,6,6,12\}$), the ratio to $\mu_1 = 1/(8\pi)$, and the identification of the α_EM slot with this sunset. It is a bare, $q$-independent $\zeta(3)$, distinct from `C1`. Since the owner ruling of 2026-11-28 (01:11Z), the default under Form B is the one-factor measure ($\mu_2 = \mu_1$, `QOU.MassTheory.EmFormBLoopMeasure`); the product measure ($\kappa_2 = 0$) is a fallback. Audit: `docs/audits/2026-11-28-alpha-em-two-loop-measure-bring.md`.

**Decision & Falsification Rule:**
- Because CODATA 2022 (`±0.153 ppb` $\iff \sigma(c_2) \approx 3.94 \times 10^{-4}$) constrains $c_2$ to only `~1` significant digit (`alpha_em_two_loop_structure_probe.py` entropy bound) and the 2018$\to$2022 edition shift (`+0.679 ppb`) flips the sign of $c_{2,\mathrm{req}}$ (`-8.07e-4 -> +9.40e-4`), **no candidate may be declared proved by numerical proximity** and **none is wired into production**. Any candidate landing within `2σ` of CODATA 2022 remains strictly a `working-assumption probe` / `§3b-cond` hypothesis pending an independent categorical measure derivation.
