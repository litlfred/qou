# Pre-Registration: Continuous Chen / Picard–Dyson Multiplicative Integral, Non-Abelian KZ Monodromy on $B_3$ & $B_4$, and `MassTraceIdentity` Substrate `nablaEndo` Instantiation (2026-11-23)

Beans `qou-9sj3`, `qou-ywyq`, `qou-wp3h`, `qou-ni4b` (`W7` / `Q-Gap-5`). Written and committed **before** executing any 80-dps numerical KZ monodromy integration or emitting the witness JSON.

## 1. Calibration, Anchor & Precision Discipline (STRICT)

- **Working precision:** `mpmath.workdps(80)` (`WORK_DPS = 80`, `OUT_DPS = 50`, internal quadrature guard `+14` dps inside `mp.workdps` blocks), zero `float64` imports, literals, or casts (`scripts/probe-float64-guard.py --strict` and `--diff` clean).
- **Substrate pin:** `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`), with real hyperbolic KZ coupling $\eta_0 = \ln q_0$ (`q_0 = exp(\eta_0)`), corresponding to imaginary Kohno coupling $\hbar_{\mathrm{KZ}} = \eta_0 / (i\pi)$ so that $\exp(i\pi\hbar_{\mathrm{KZ}}) = \exp(\eta_0) = q_0$.
- **Allowed calibrations:** Only CAL-1 / CAL-2 / proton-pinned $q_0$ (`vol_4_1_at(80)` and CODATA-2022 `proton-electron mass ratio` via `q_at(80)`). Zero fitted parameters, zero post-hoc basis tuning, and zero experimental target selection enter any formula.

---

## 2. Pre-Registered Mathematical Objects & Numerical Tests

### Test Suite A — Picard–Chen Iterated-Integral Multiplicativity, Coalgebra Shuffle Identity, and $O(1/N)$ Euler Convergence

On $B_3$ (`Conf_3(\mathbb{C})`, basepoint $z^{(0)} = (0, 1, 2)$, sector $\lambda = [2,1]$, $\dim = 2$) and $B_4$ (`Conf_4(\mathbb{C})`, basepoint $z^{(0)} = (0, 1, 2, 3)$, sectors $\lambda = [2,2]$ of $\dim = 2$ and $\lambda = [3,1]$ of $\dim = 3$), consider the flat Knizhnik–Zamolodchikov 1-form
$$\omega_{\mathrm{KZ}}^{(\lambda)}(z) = \frac{\eta_0}{i\pi} \sum_{0 \le a < b < n} \Omega_{ab}^{(\lambda)} \, d\log(z_b - z_a), \qquad \Omega_{ab}^{(\lambda)} = \rho_{S_n}^{(\lambda)}\big((a\,b)\big),$$
along the smooth counter-clockwise half-turn generator paths $\gamma_j : [0, 1] \to \mathrm{Conf}_n(\mathbb{C})$ (`KZHolonomy.BraidGeometry.genPath`):
$$\gamma_j(t)_j = j + \tfrac{1}{2} - \tfrac{1}{2} e^{i\pi t}, \qquad \gamma_j(t)_{j+1} = j + \tfrac{1}{2} + \tfrac{1}{2} e^{i\pi t}, \qquad \gamma_j(t)_k = k \quad (k \notin \{j, j+1\}).$$
Integrate $\Phi'(t) = A_\gamma(t) \Phi(t)$, $\Phi(0) = I$, using spectral Gauss–Legendre collocation / Picard–Chen iterated-integral recursion ($N_{\mathrm{sub}} = 16$ uniform subintervals, $s = 36$ Gauss–Legendre nodes per subinterval, order $2s = 72$), defining the elementary braid monodromy $P(\sigma_j) := \rho_{S_n}^{(\lambda)}(s_j) \Phi_{\gamma_j}(1)$ and $P(\sigma_j^{-1}) := P(\sigma_j)^{-1}$ (verified against integrating along the reversed path $\gamma_j^{-1}(t) = \gamma_j(1 - t)$).

1. **Path-Concatenation Multiplicativity (`ChenMultiplicativeIntegralBridge.orderedProd_append`):**
   - Split smooth paths $\gamma = \gamma_1 \star \gamma_2$ at non-midpoint parameter $t_* = 3/7 \in (0, 1)$ (as well as two-generator concatenated paths $\gamma_{\sigma_0} \star (s_0 \cdot \gamma_{\sigma_1})$ in $\mathrm{Conf}_n(\mathbb{C})$) and integrate $\gamma_1$, $\gamma_2$, and $\gamma_1 \star \gamma_2$ independently via single-domain Gauss–Legendre Picard–Chen series.
   - **Pre-registered criterion:** $\|P(\gamma_1 \star \gamma_2) - P(\gamma_2) P(\gamma_1)\|_\infty < 10^{-76}$ across all three sectors ($B_3\,[2,1]$, $B_4\,[2,2]$, $B_4\,[3,1]$), and $\|P(\gamma_j)^{-1} - P(\gamma_j^{-1})\|_\infty < 10^{-76}$.
2. **Chen Shuffle / Tensor-Coalgebra Group-Like Identity (`IsShuffleGroupLike`):**
   - Compute the scalar Chen iterated integrals $J_w(\gamma)$ up to word length $|w| \le 4$ for independent logarithmic 1-forms $\alpha_0 = d\log(z_1 - z_0)$, $\alpha_1 = d\log(z_2 - z_1)$, $\alpha_2 = d\log(z_2 - z_0)$ along a smooth path in $\mathrm{Conf}_3(\mathbb{C})$, verifying both $\langle \Delta_{\mathrm{sh}} J(\gamma), u \otimes v \rangle = J_{u \sqcup\!\!\sqcup v}(\gamma) = J_u(\gamma) J_v(\gamma)$ and Chen deconcatenation $J_w(\gamma_1 \star \gamma_2) = \sum_{w = u v} J_u(\gamma_2) J_v(\gamma_1)$ to $< 10^{-76}$.
3. **Discrete Gronwall $O(1/N)$ Contraction Bound (`eulerOrderedProd_error_bound`):**
   - Evaluate the $N$-step ordered matrix product $P_N = \prod_{k=1}^N \big(I + \int_{(k-1)/N}^{k/N} A(s)\,ds\big)$ for $N \in \{16, 32, 64, 128, 256\}$ on $B_3\,[2,1]$, verifying both the rigorous upper bound $\|\Phi(1) - P_N\|_\infty \le M^2 e^{2M} / N$ ($M = \sup_{t \in [0,1]} \|A(t)\|_\infty$) for every $N$ and first-order $O(1/N)$ Richardson scaling $N \|\Phi(1) - P_N\|_\infty \to C_1$.

---

### Test Suite B — Yang–Baxter Braid Relations, Far Commutativity, and Drinfeld Associator Conjugacy on $B_3$ & $B_4$

1. **Artin Braid & Far-Commutation Relations from Continuous KZ Monodromy:**
   - $B_3$ on $[2,1]$ ($\dim = 2$): $\|P(\sigma_0 \sigma_1 \sigma_0) - P(\sigma_1 \sigma_0 \sigma_1)\|_\infty < 10^{-75}$.
   - $B_4$ on $[2,2]$ ($\dim = 2$) and $[3,1]$ ($\dim = 3$):
     * $\|P(\sigma_0 \sigma_1 \sigma_0) - P(\sigma_1 \sigma_0 \sigma_1)\|_\infty < 10^{-75}$,
     * $\|P(\sigma_1 \sigma_2 \sigma_1) - P(\sigma_2 \sigma_1 \sigma_2)\|_\infty < 10^{-75}$,
     * $\|P(\sigma_0 \sigma_2) - P(\sigma_2 \sigma_0)\|_\infty < 10^{-76}$.
   - **Hecke Quadratic Relation:** Verify $\|(P(\sigma_j) - q_0 I)(P(\sigma_j) + q_0^{-1} I)\|_\infty < 10^{-75}$ for every generator $j$ in all three sectors, and verify the $\mathfrak{sl}_2$ traceless Casimir shift $\Omega_{ab}^{\mathfrak{sl}_2} = \Omega_{ab} - \frac{1}{2} I$ reproduces $q_0^{-\mathrm{writhe}(w)/2} P(w)$ to $< 10^{-76}$.
2. **Drinfeld Associator $\Phi_{\mathrm{KZ}}$ Non-Triviality & Exact Trace Invariance on Knots and Links:**
   - Measure the non-trivial Drinfeld associator basis shift on $B_3\,[2,1]$ (via cross-ratio $x \in (0, 1)$ reduced 1D KZ equation $\frac{dG}{dx} = \frac{\eta_0}{i\pi}\big(\frac{\Omega_{01}}{x} + \frac{\Omega_{12}}{x - 1}\big) G$, extracting the regularized Drinfeld associator $\Phi_{\mathrm{KZ}}(\Omega_{01}, \Omega_{12}) = G_1(x)^{-1} G_0(x)$ at $x = 1/2$ and verifying $P(\sigma_1) = \Phi_{\mathrm{KZ}}^{-1} (\text{local } R_{12}) \Phi_{\mathrm{KZ}}$ with $\|\Phi_{\mathrm{KZ}} - I_2\|_\infty > 10^{-2}$ non-trivial at $q_0$!).
   - Verify exact trace agreement $|\operatorname{Tr}(P_{\mathrm{KZ}}^{(\lambda)}(w)) - \operatorname{Tr}(\rho_{\mathrm{Hecke}}^{(\lambda)}(w))| < 10^{-75}$ across:
     * Elementary generators $\sigma_j$,
     * **Trefoil $3_1$:** $w_{3_1} = (\sigma_0 \sigma_1)^2 \in B_3$ ( closure = $(3,2)$ torus link/knot; plus $\sigma_0^3$ and 4-strand Markov stabilization $(\sigma_0 \sigma_1)^2 \sigma_2 \in B_4$),
     * **Figure-eight $4_1$:** $w_{4_1} = (\sigma_0 \sigma_1^{-1})^2 \in B_3$ (and 4-strand stabilization $(\sigma_0 \sigma_1^{-1})^2 \sigma_2^{-1} \in B_4$),
     * **Genus-4 Torus Knot $T(3,5)$:** $w_{T(3,5)} = (\sigma_0 \sigma_1)^5 \in B_3$ (and 4-strand stabilization $(\sigma_0 \sigma_1)^5 \sigma_2 \in B_4$),
     * **Borromean Rings $L6a4$:** $w_{\mathrm{Bor}} = (\sigma_0 \sigma_1^{-1})^3 \in B_3$, and 4-strand torus braid $w_{T(4,3)} = (\sigma_0 \sigma_1 \sigma_2)^3 \in B_4$.
   - Verify gauge-transformation trace invariance $|\operatorname{Tr}(g_0 P(w) g_0^{-1}) - \operatorname{Tr}(P(w))| < 10^{-76}$ for non-abelian $g_0 \in \mathrm{GL}_d$.

---

### Test Suite C — Concrete `MassTraceIdentity` & `CategoricalLagrangian` (`nablaEndo` / `hReebP` / `hReebN`) Verification

- Verify at 80 dps on `matFrobHopf` ($d = 2$ for $[2,1],[2,2]$ and $d = 3$ for $(2,1),(1,2),[3,1]$):
  1. `MassTraceIdentity` Option-1 functional $\int_A (\Psi \circ \mathrm{hol}(w)) = \operatorname{Tr}(P_{\mathrm{KZ}}(w))$ and regular trace $\operatorname{tr}_{\mathrm{End}(A)}(L_{\mathrm{hol}(w)} \circ \Psi) = d \cdot \operatorname{Tr}(P_{\mathrm{KZ}}(w))$ with $\int_A = \varepsilon$.
  2. Non-vanishing commutator connection $\nabla_\Omega(X) = [\Omega_{01}, X] \ne 0$, Leibniz identity $\|\nabla_\Omega(XY) - \nabla_\Omega(X)Y - X\nabla_\Omega(Y)\|_\infty = 0$, automatic vanishing of spatial-Reeb cross-trace $\tau(\nabla_\Omega \circ \mathcal{R} + \mathcal{R} \circ \nabla_\Omega) = 0$ (`hCross`), and exact reproduction of the Convention-D Markov trace $\operatorname{tr}_M^D(w) = \sum_{\ell(\lambda) \le 2} y_\lambda^D \operatorname{Tr}(P_{\mathrm{KZ}}^{(\lambda)}(w))$ on $B_3$ and $B_4$ to $< 10^{-75}$, plus the concrete Borromean $(n - p)$ two-term traced Lagrangian identity at $q_0$.
