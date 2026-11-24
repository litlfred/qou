# Audit & Derivation Ledger: Exact 4-Topology `EmFermionLoop` `(1 - h²α)` Identity & Two-Loop Bloch-$B_3(\mathbb{C})$ Working-Assumption Probe (`qou-l4t2`, `qou-9y43`)

**Date:** 2026-11-24  
**Beans:** `qou-l4t2`, `qou-9y43`  
**Pre-Registration:** [`alpha_em_two_loop_bloch_schwinger_preregistration.md`](../../computations/alpha/alpha_em_two_loop_bloch_schwinger_preregistration.md)  
**80-dps Probe:** [`alpha_em_two_loop_bloch_schwinger_probe.py`](../../computations/alpha/alpha_em_two_loop_bloch_schwinger_probe.py)  
**Witness:** [`alpha_em_two_loop_bloch_schwinger_probe.witness.json`](../../computations/alpha/alpha_em_two_loop_bloch_schwinger_probe.witness.json)  
**Lean 4 Formalization (`§7c` Split):** [`EmFermionLoopFourTopology.lean`](../../folio/quantum-observable-universe/lean/QOU/Archimedean/EmFermionLoopFourTopology.lean) (generic `[CommRing]` / `[Field]`) & [`AlphaEmTwoLoopBlochSchwinger.lean`](../../folio/quantum-observable-universe/lean/QOU/Archimedean/AlphaEmTwoLoopBlochSchwinger.lean) (archimedean `ℝ`)

---

## 1. Exact Resolution of the 2026-07-14 `phase3b` Single-Chirality Gap (`(1 - 1 · h² α)`)

In `docs/audits/2026-07-14-alpha-em-phase3-schwinger-coefficient-exact-check.md` (`alpha_em_rt_phase3b_exact_vertex_moments.py`), evaluating the **single-chirality** 2-vertex moments on $V^{\otimes 3}$ (`photon pair (1,2)` projected onto singlet $e_- = (q I - \hat{R})/[2]_q$, `matter strand 3` = `EmFermionLoop` $V_F = \mathbb{C}^2$ with $\operatorname{qTr}_{123}(e_- \otimes I_2) = [2]_q$) gave:
- Over-crossing pair $(+, +)$: $m(\sigma_2^2) - 1 = +h\,m(\sigma_2) = \frac{q^4 - q^2}{q^2 + 1} = +0.1280758$ at $q_p$ (order $(q-1)^1$, wrong sign),
- Under-crossing pair $(-, -)$: $m(\sigma_2^{-2}) - 1 = -h\,m(\sigma_2) + h^2 = \frac{1 - q^2}{q^4 + q^2} = -0.0843705$ at $q_p$ (order $(q-1)^1$, ratio $1.93\times (-h^2)$).

**Unconditional algebraic theorem (`four_topology_bar_hermitian_moment_sum`):**
Neither $(+,+)$ nor $(-,-)$ alone is invariant under the Kazhdan–Lusztig bar / charge-conjugation involution ($\sigma_2 \leftrightarrow \sigma_2^{-1}, q \leftrightarrow q^{-1}$), so each carries an uncancelled order-$(q-1)^1$ chiral tadpole $\pm h\,m(\sigma_2)$, where $m(\sigma_2) = \frac{q^3}{q^2+1}$. Summing over **all four** signed chiral 2-vertex topologies $(\epsilon_1, \epsilon_2) \in \{+1, -1\}^2$ with the bar-Hermitian skein sign $-\epsilon_1 \epsilon_2$:
$$\sum_{\epsilon_1, \epsilon_2 \in \{+,-\}} (-\epsilon_1 \epsilon_2)\,m(\sigma_2^{\epsilon_1}\sigma_2^{\epsilon_2}) = m(\sigma_2 \sigma_2^{-1}) + m(\sigma_2^{-1}\sigma_2) - m(\sigma_2^2) - m(\sigma_2^{-2}) = 2 - \big(1 + h m(\sigma_2)\big) - \big(1 - h m(\sigma_2) + h^2\big) = \mathbf{-1 \cdot h^2}$$
identically in $\mathbb{Q}(q)$ for **every** moment functional $m$ with $m(1) = 1$ (and likewise cross-position on $V^{\otimes 4}$: $m((\sigma_2 - \sigma_2^{-1})(\sigma_3^{-1} - \sigma_3)) = -h^2$). At $q_p$: $-(+0.1280758) - (-0.0843705) = -0.0437053 = -h_p^2$ to 80 digits.

**Remaining `§3b-cond` normalization boundary:** Un-averaged $S = \sigma - \sigma^{-1}$ yields $-S\bar{S} = -1 \cdot h^2$ (electromagnetic Form B), whereas half-averaged $\frac{1}{2}(\sigma - \sigma^{-1})$ yields $-\frac{1}{4} h^2 = -\left(\frac{q+1}{2}\right)^2 \hbar_q^2$ (matching the electroweak $\hbar_q^2$ normalization as $q \to 1$). Selecting un-averaged $S$ on the abelian $U(1)$ `EmFermionLoop` is recorded explicitly as a hypothesis, not smuggled in.

---

## 2. Pre-Registered Zero-Parameter Two-Loop Bloch-$B_3(\mathbb{C})$ / Bring / QED Matrix (`80 dps`)

For $\frac{1}{\alpha_{\mathrm{EM}}} = T_{\mathrm{EM}}(q) + \alpha_{\mathrm{EM}} H(q)(1 - h^2 \alpha_{\mathrm{EM}}) + c_2(q)\alpha_{\mathrm{EM}}^2$, CODATA 2022 (`137.035999177(21)`) corresponds to diagnostic window $c_{2,\mathrm{req}}^{\mathrm{C22}} = +9.39865 \times 10^{-4} \pm 3.94356 \times 10^{-4}$ (`ladder` sign convention $c_2^{\mathrm{ladder}} = -c_2 = -9.39865 \times 10^{-4}$), whereas CODATA 2018 (`137.035999084(21)`) had opposite sign $c_{2,\mathrm{req}}^{\mathrm{C18}} = -8.06569 \times 10^{-4}$.

| Pre-Committed Zero-Parameter Candidate ($q = q_{\mathrm{proton}}$) | $c_2(q_p)$ | $1/\alpha_{\mathrm{EM}}(q_p)$ | vs CODATA 2022 (`ppb` / `σ`) | vs CODATA 2018 (`ppb` / `σ`) |
|---|---:|---:|---:|---:|
| `C0_FormB_baseline` ($c_2 = 0$) | `0` | `137.0359991269509` | `-0.3652 ppb` (`-2.38 σ`) | `+0.3134 ppb` (`+2.05 σ`) |
| **`C1_BlochB3_EmFermionLoop`** ($H(q)\frac{\zeta(3)-\operatorname{Li}_3(q^{-2})}{8\pi} = \frac{[2]_q \Delta_{B_3}}{(\pi b_1)^2}$) | **`+0.000877819`** | **`137.0359991736958`** | **`-0.0241 ppb` (`-0.16 σ`)** | `+0.6545 ppb` (`+4.27 σ`) |
| `C2_BlochB3_bare_64pi2` ($\frac{\zeta(3)-\operatorname{Li}_3(q^{-2})}{(8\pi)^2}$) | `+0.000436531` | `137.0359991501967` | `-0.1956 ppb` (`-1.28 σ`) | `+0.4831 ppb` (`+3.15 σ`) |
| `C3_JostLuttinger_QED_3over4pi_H` ($H(q)\frac{3}{4\pi}$) | `+0.01910123` | `137.036000144113` | `+7.0574 ppb` (`+46.1 σ`) | `+7.7360 ppb` (`+50.5 σ`) |
| `C4_PetermannSommerfield_H_CPS_over_pi` ($H(q)\frac{C_{\mathrm{PS}}}{\pi}$) | `-0.00836580` | `137.035998681462` | `-3.6161 ppb` (`-23.6 σ`) | `-2.9375 ppb` (`-19.2 σ`) |
| `C5_BringZeroMode_h2` ($\frac{2}{3\pi}h^2$) | `+0.00927475` | `137.035999620842` | `+3.2389 ppb` (`+21.1 σ`) | `+3.9175 ppb` (`+25.6 σ`) |
| `C6_ThetaGraph_residual` ($-\frac{[3]_q}{(8\pi)^2} + H(q)h^2$) | `-0.00132164` | `137.035999056572` | `-0.8788 ppb` (`-5.74 σ`) | `-0.2002 ppb` (`-1.31 σ`) |
| *(Comparison arm)* `Form A` quadratic ($L=2$) | — | `137.0359993132` | `+0.9937 ppb` (`+6.48 σ`) | `+1.6723 ppb` (`+10.9 σ`) |
| *(Comparison arm)* `CS tower` all-orders | — | `137.0359350940` | `-467.64 ppb` | `-466.96 ppb` |

*(At $q = q_{\mathrm{muon}}$, all Form-B variants sit near $+79.0$ to $+91.9\text{ ppb}$ and CS-tower arms near $-387.9\text{ ppb}$, recorded in full in the witness.)*

**Honest epistemic conclusion (`qou-aemx`):**
1. Both Bloch-$B_3(\mathbb{C})$ harmonic-period candidates (`C1` at `-0.16σ` and `C2` at `-1.28σ` vs CODATA 2022) vanish identically at $q = 1$ ($\Delta_{B_3}(1) = \zeta(3) - \operatorname{Li}_3(1) = 0$), use the exact 2-loop Bring harmonic-1-form denominator $(8\pi)^2 = (\pi b_1(\Sigma_4))^2$, and land inside `1.3σ` (`0.16σ` with `[2]_q`) of CODATA 2022 with **zero fitted parameters**.
2. Simultaneously, `C6` (`-\frac{[3]_q}{(8\pi)^2}`) sits at `-1.31σ` against CODATA 2018 (`-5.74σ` against CODATA 2022), illustrating directly why owner ruling `qou-aemx` forbids selecting a form by its empirical residual while the experimental Rb/Cs recoil shift (`0.679 ppb`) exceeds $\sigma_{\mathrm{exp}}$ (`0.153 ppb`). All arms remain tracked side by side, and the physical Bloch-$B_3$ two-loop coupling step is formalized strictly as `AlphaEmTwoLoopBlochSchwingerClass` (`§3b-cond`, zero global instances).
