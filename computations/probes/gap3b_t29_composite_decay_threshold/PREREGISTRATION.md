# Pre-Registration: Closing Open Gap 3 Backup (Option 3B, `qou-618l`) — Dynamical 3-Body Threshold Instability of the Composite 4th Harmonic $T(2,9) \to 3 \times T(2,3)$ in $H_3(q_0)$

- **Branch**: `claude/gap3b-t29-composite-decay-threshold-20261123`
- **Base commit**: `origin/main` (`e330ab6aa048abefe34a93474f667f3284483d71`)
- **Bean**: `qou-618l` (Option 3B backup to Open Gap 3, companion to `qou-x4qm` / `qou-xtcl`)
- **Companion Lean 4 module**: `folio/quantum-observable-universe/lean/QOU/StandardModel/CompositeT29ThresholdInstability.lean`
- **Companion 80-dps probe**: `computations/probes/gap3b_t29_composite_decay_threshold/gap3b_t29_composite_decay_threshold_probe.py`
- **Companion witness**: `computations/probes/gap3b_t29_composite_decay_threshold/gap3b-t29-composite-decay-threshold.witness.json`
- **Precision & anti-fit lock**: `workdps = 80`, `q0Anchor = "proton"` (`q0 = q_at(80)` matching `Q_MP`), zero `float64`, zero free or fitted parameters (`NO FITTING, EXCEPT CAL-1/2/3`), zero empirical literals inside `.lean` files (`0 sorry`, `0` custom `axiom`s, generic `[CommRing R]` / `[Field K]` / `[LinearOrder K] [IsStrictOrderedRing K]` per AGENTS.md §7c).
- **Pre-registration gate**: Committed and pushed **prior** to writing or executing `gap3b_t29_composite_decay_threshold_probe.py` or evaluating any numerical threshold margins or decay widths at $q_0$.

---

## 1. Scientific Question & Honest Two-Arm Mandate

Within the two-strand torus family $T(2,n) = \widehat{\sigma_0^n}$ embedded in Bring's genus-$4$ surface $\Sigma_4$, Seifert's genus bound $g(T_{2,n}) = (n - 1)/2 \le 4$ admits four non-trivial single-component odd-winding torus knots:
$$n \in \{3, 5, 7, 9\}.$$
At the normal-form level (`QOU.Archimedean.lepton_continuant_generation_exclusion`), the Morgan–Voyce continuant $f_n(h)$ ($\sigma^n = f_n(h)\sigma + f_{n-1}(h)\cdot \mathbf{1}$, $h = q - q^{-1}$) singles out $n = 9 = 3 \times 3$ via $f_9(h) = f_3(h)(h^6 + 6h^4 + 9h^2 + 1)$ while $\{f_3, f_5, f_7\}$ are pairwise coprime. However, prior audits (`2026-08-02-generation-count-t29-continuant-divisibility.md`, `2026-10-10-generation-count-two-independent-countings.md`) rightly noted that polynomial divisibility alone is a normal-form distinction, not yet a dynamical instability or exclusion mechanism.

Option 3B (`qou-618l`) tests the **dynamical 3-body threshold & resolvent-cut mechanism** $T(2,9) \to 3 \times T(2,3)$ in $H_2(q)$ and $H_3(q)$ with **100% mathematical honesty across all QOU energy/trace/resolvent functionals** (never assuming the sign of $E(T_{2,9}) - 3\,E(T_{2,3})$ at $q_0$ in advance):

1. **Arithmetic & Topological 3-Body Selection Rule:**
   - Even windings $n = 2k \ge 2$ close to **2-component torus links** ($\gcd(2, 2k) = 2$, e.g. Hopf link $T(2,2)$ or EW links $T(2,4), T(2,6)$), not single-component knots; $n = 1$ closes to the genus-$0$ unknot fold.
   - Because the sum of two odd integers is even, **no** odd torus knot $T(2,n)$ admits a winding-conserving 2-body split $n = n_1 + n_2$ into two odd torus knots.
   - For a 3-body decay into three non-trivial odd-winding torus knots ($n_1, n_2, n_3 \ge 3$, each odd), the minimum winding / minimal-crossing sum is $3 + 3 + 3 = 9$:
     * $n \in \{3, 5, 7\}$: **strictly zero** 3-knot decompositions ($\mathcal{C}_3(n) = \emptyset$, kinematically below the $(3,3,3)$ winding/crossing threshold).
     * $n = 9$: **unique** admissible winding in $\{3, 5, 7, 9\}$ with $\mathcal{C}_3(9) \ne \emptyset$, and its unique decomposition is $(3, 3, 3)$.
2. **Exact Operator Fission Identity in $H_m(R, q)$:**
   - Setting $\Sigma := \sigma^3$ and $h_3 := h(h^2 + 3)$, $\Sigma$ satisfies the renormalized Hecke relation $\Sigma^2 = h_3 \Sigma + \mathbf{1}$ and the exact operator split
     $$\sigma^9 = P_6(h)\,\sigma^3 + h(h^2 + 3)\,\mathbf{1}, \qquad P_6(h) = h^6 + 6h^4 + 9h^2 + 1 = h_3^2 + 1,$$
     whereas $\sigma^5, \sigma^7 \notin R[h]\cdot \mathbf{1} + R[h]\cdot \sigma^3$ over $R = \mathbb{Z}$.
3. **Two-Arm Sign & Critical-Root Audit of $Q_3(q) := E(T_{2,9}; q) - 3\,E(T_{2,3}; q)$:**
   - **Arm A — Unsubtracted Total Trace / Continuant / Toroidal Resolvent Functionals** (which approach a positive $n$-independent classical transposition baseline $c_0 > 0$ as $q \to 1^+$, so $Q_3(1) = -2c_0 < 0$):
     * **(A1)** Symmetrized Laurent / Chebyshev trace numerator $C_n(q) = q^n + q^{-n} = (q + q^{-1}) f_n(h)$.
     * **(A2)** Morgan–Voyce continuant $f_n(h)$ and normal-form net $\mathrm{net}_n(h) = f_n(h) + f_{n-1}(h)$.
     * **(A3)** Convention-D Markov trace $\tau_D(\sigma_1^n; q) = f_n(h) z_D(q) + f_{n-1}(h)$ (identically equal on $\sigma_0^n \in H_2(q)$ and $\sigma_1^n \in H_3(q)$, with stabilized knot trace $\tau_D^{(3)}(\sigma_0^n \sigma_1) = z_D(q)\tau_D(\sigma_1^n; q)$ where $z_D(q) = q^3 / (q^2 + 1)$).
     * **(A4)** Toroidal Inhomogeneous Loop Resolvent (`InhomogeneousLeptonLoopResolvent.lean`, `#9213`): since $\mathrm{Vol}(T(2,n)) = 0$, the hyperbolic saddle cut vanishes identically (`eval_eq_wAlg_of_vol_zero`) and $W(T_{2,n}; q) = \tau_D(\sigma_1^n; q) / \tau_e(q)$.
     * **Pre-registered test for Arm A:** Determine the exact polynomial sign condition for $Q_3(q) \gtrless 0$, solve for the exact critical root $q_{\mathrm{crit}} > 1$ at 80 dps for each of (A1)–(A4), and record honestly whether $q_0 = q_{\mathrm{at}}(80)$ lies **below** $q_{\mathrm{crit}}$ ($Q_3(q_0) < 0$, channel kinematically closed under unsubtracted traces) or **above** $q_{\mathrm{crit}}$ ($Q_3(q_0) > 0$).
   - **Arm B — Classical-Vacuum-Subtracted / Hook-Channel / Quantum-Integer / Genus Functionals** (where the $q = 1$ single-transposition baseline is subtracted or projected onto the $H_3(q)$ hook sector):
     * **(B1)** $H_3(q)$ $(2,1)$-hook character $\chi_{(2,1)}(\sigma_1^n; q) = q^n - q^{-n}$ (odd $n$).
     * **(B2)** Balanced quantum integer $[n]_q = (q^n - q^{-n}) / (q - q^{-1})$.
     * **(B3)** Subtracted Hecke continuant excitation $\Delta f_n(h) = f_n(h) - 1$.
     * **(B4)** Subtracted Convention-D Markov trace excitation $\Delta\tau_D(\sigma_1^n; q) = \tau_D(\sigma_1^n; q) - \tau_D(\sigma_1^n; 1) = \tau_D(\sigma_1^n; q) - 1/2$.
     * **(B5)** Seifert topological genus $g(T_{2,n}) = (n - 1)/2$.
     * **Pre-registered test for Arm B:** Prove over every ordered field that $Q_3(q) = E(T_{2,9}; q) - 3\,E(T_{2,3}; q) > 0$ **strictly for all $q > 1$** across (B1)–(B5), and evaluate $E(n)$ ($n \in \{3,5,7,9\}$), $Q_3(q_0)$, and dimensionless excess $\delta_3 = Q_3(q_0) / E(T_{2,9}; q_0)$ at 80 dps.

---

## 2. Pre-Registered Zero-Parameter Resolvent-Cut & Decay-Width Models (`workdps = 80`)

In the self-energy resolvent $R_n(z) = \big(z - E_n - \Delta_n + \tfrac{i}{2}\Gamma_n\big)^{-1}$, 3-knot channel emptiness forces $\Gamma_n^{(3\text{-knot})} = 0$ (exact real-axis pole) for $n \in \{3, 5, 7\}$. For $n = 9$, whenever $Q_3 = E(9) - 3\,E(3) > 0$ (Arm B, and Arm A only if $q > q_{\mathrm{crit}}$; if $Q_3(q_0) \le 0$ then $\Gamma_9(q_0) = 0$ identically by phase-space theta function $\Theta(Q_3)$), we pre-register three zero-parameter width-to-energy ratios $\Gamma(T_{2,9} \to 3\,T_{2,3}) / E(T_{2,9})$:

1. **(W1) Algebraic Hecke Operator Fission Ratios (from $\sigma_1^9 = P_6(h_0)\sigma_1^3 + h_3\mathbf{1}$, $h_3 = h_0(h_0^2 + 3) = q_0^3 - q_0^{-3}$):**
   - Linear trace-fission fraction: $r_{\mathrm{lin}}(q_0) = \dfrac{h_3}{\tau_D(\sigma_1^9; q_0)}$.
   - Quadratic Born / Gram coefficient fraction: $r_{\mathrm{quad}}(q_0) = \dfrac{h_3^2}{P_6(h_0)^2 + h_3^2}$.
2. **(W2) Exact Relativistic 3-Body Dalitz Contact Width ($\mu := E(3)/E(9) < 1/3$ when $Q_3 > 0$):**
   For a local 4-fermion contact amplitude $|\mathcal{M}|^2 = \lambda_4^2 E(9)^2$ into three equal-mass states of mass $E(3)$ (including the $1/(2 E(9))$ flux factor so $I_{\mathrm{Dalitz}}(0) = 1/2$ reproduces $\Gamma(0)/E(9) = \lambda_4^2 / (512\pi^3 S_{\mathrm{id}})$), the exact 1D Dalitz integral over dimensionless pair invariant mass $u = s_{12} / E(9)^2 \in [4\mu^2, (1 - \mu)^2]$ is
   $$I_{\mathrm{Dalitz}}(\mu) = \int_{4\mu^2}^{(1-\mu)^2} \sqrt{1 - \frac{4\mu^2}{u}}\,\sqrt{\big(1 + \mu^2 - u\big)^2 - 4\mu^2}\,du,$$
   giving
   $$\frac{\Gamma_{9 \to 333}^{\mathrm{rel}}}{E(9)} = \frac{\lambda_4^2}{256\,\pi^3\,S_{\mathrm{id}}}\,I_{\mathrm{Dalitz}}(\mu), \qquad S_{\mathrm{id}} \in \{2, 6\},$$
   evaluated at two fixed zero-parameter QOU couplings:
   - **Hecke braid-fission coupling:** $\lambda_4^{\mathrm{Hecke}} = h_0(h_0^2 + 3) = q_0^3 - q_0^{-3}$,
   - **Derived Form-B electromagnetic coupling:** $\lambda_4^{\mathrm{EM}} = 4\pi\,\alpha_q(q_0)$ with $\alpha_q(q_0) = \big(q_0\,[9]_{q_0}\,[10]_{q_0} + \frac{2}{3\pi}\big)^{-1}$.
3. **(W3) Non-Relativistic 3-Body Threshold Asymptotic ($\delta_3 = 1 - 3\mu \to 0^+$, $I_{\mathrm{Dalitz}}(\mu) \sim \frac{2\pi}{3\sqrt{3}}\delta_3^2$):**
   $$\frac{\Gamma_{9 \to 333}^{\mathrm{NR}}}{E(9)} = \frac{\lambda_4^2}{384\sqrt{3}\,\pi^2\,S_{\mathrm{id}}}\,\delta_3^2.$$

---

## 3. Pre-Registered Epistemic Guardrails & Rule-13a Scope

- **No silent selection between Arm A and Arm B:** Both arms are reported side-by-side in the witness and `RESULTS.md`. If Arm A gives $Q_3(q_0) < 0$ at the proton pin $q_0$, that negative result is reported prominently as a **kinematically closed / bound** outcome for unsubtracted trace functionals at $q_0$, alongside the exact $q_{\mathrm{crit}}$ where Arm A opens.
- **Instability vs Chiral Generation Count (Devil's-Advocate Guardrail):** Weakly decaying fermions ($\mu, \tau$) still count as chiral generations in gauge anomaly cancellation and $Z$-width below $M_Z / 2$. Excluding $T(2,9)$ as a 4th generation via Option 3B requires *either* (i) non-independent Fock-space compositeness ($\sigma^9 \in \mathbb{Z}[h][\sigma^3]$ represents a 3-body excitation in the generation-1 continuum rather than an independent fundamental UV fermion field), *or* (ii) an established $T(2,n) \mapsto m_{\mathrm{phys}}(n)$ map placing $M_9$ above $M_Z / 2$ or $\Gamma_9 / M_9 \sim O(1)$. Both open bridges are isolated in a zero-instance Rule-13a class `CompositeT29DecayExclusionHypothesis` in Lean.
