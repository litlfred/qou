# Pre-Registration: Solver-Free `ECatLPDualRadical` Shadow-Price Evaluation on the 6D $H_3(q_0)$ Normal-Form Basis (2026-11-23)

Bean `qou-udad` (`critical`). Written and committed **before** evaluating any numerical inner product, shadow price $y_0$, MeV conversion, or dual-feasibility interval.

## 1. Formalize-First Context (`ECatLPDualRadical.lean` & `qbeta_ecat_lp_radical_pairing_probe.py`)

In the operator-selection linear program (`prop:operator-selection-lp`)

$$
\text{primal: } \min \sum_{j=0}^{5} t_j x_j \;\;\text{s.t.}\;\; \sum_{j=0}^{5} x_j = n_{\mathrm{target}},\;\; G_D x \ge 0,
\qquad
\text{dual: } \max n_{\mathrm{target}}\, y_0 \;\;\text{s.t.}\;\; y_0 \mathbf{1} + G_D y = t,\;\; y \ge 0,
$$

`QOU.QBeta.ECatLPDualRadical.dual_price_determined_by_radical` proves over any field that pairing the dual equality with a radical vector $v \in \ker(G_D)$ annihilates $G_D y$ and pins the shadow price per bond **before any LP solver runs**:

$$
y_0 = \frac{\langle t, v \rangle}{\langle \mathbf{1}, v \rangle}, \qquad \text{provided } \langle \mathbf{1}, v \rangle \neq 0.
$$

On the 3D Wedderburn block basis (`qbeta_ecat_lp_radical_pairing_probe.py`), the diagonal Gram $\mathrm{diag}(y_\lambda \dim_\lambda)$ and every $y_\lambda$-weighted block cost $t_\lambda = y_\lambda f(\lambda)$ share the vanishing Convention-D factor $y_{(1^3)} = 0$, forcing $\langle t, v \rangle = 0$ and $y_0 = 0$ identically (scope-(b) exclusion on the block basis). That probe explicitly left open the **6D $H_3(q_0)$ Coxeter normal-form operator basis**:

$$
b = (\gamma,\; \sigma_0,\; \sigma_1,\; L_+,\; L_-,\; e^-) = (\mathbf{1},\; \sigma_0,\; \sigma_1,\; \sigma_0\sigma_1,\; \sigma_1\sigma_0,\; \sigma_0\sigma_1\sigma_0),
\qquad \ell(w_i) = (0, 1, 1, 2, 2, 3),
$$

where $G_{D,ij} = \mathrm{tr}_M(b_i b_j)$ at $z_D = q_0^3 / (q_0^2 + 1)$ is a dense symmetric $6 \times 6$ matrix of rank $5$ whose 1D radical is spanned by the $q$-antisymmetriser

$$
v_{(1^3), i} = (-q_0)^{-\ell(w_i)} = \bigl(1,\; -q_0^{-1},\; -q_0^{-1},\; q_0^{-2},\; q_0^{-2},\; -q_0^{-3}\bigr)
\qquad\bigl(\text{polynomial rescale } \tilde{v}_{(1^3)} = -q_0^3 v_{(1^3)} = (-q_0^3, q_0^2, q_0^2, -q_0, -q_0, 1)\bigr).
$$

## 2. Pre-Registered Candidate 6D Cost Vectors $t_{\mathrm{geom}} \in \mathbb{R}^6$

No cost vector is invented or tuned against nuclear binding data. We evaluate strictly the natural zero-parameter 6D $H_3(q_0)$ normal-form cost vectors already present in the corpus:

- **C0 (`hecke_trace_control`, expected collapse):** $t_i = \mathrm{tr}_M(b_i) = (1, z_D, z_D, z_D^2, z_D^2, h_0 z_D^2 + z_D) = (G_D e_0)_i$, with $h_0 = q_0 - q_0^{-1}$. Must satisfy $\langle t, v_{(1^3)} \rangle = 0$, $y_0 = 0$, and dual feasibility via $y = e_0 \ge 0$.
- **C1a (`ecat_pair_kernel_cyclic`, from `ECatProbeAssertions` & `qbeta_ecat_pair_kernel_probe.py`):** Separation-weighted ordered-letter pair kernel on each Coxeter word $w_i$ of length $L_i = \ell(w_i)$ with cyclic arc distance $d_{\mathrm{arc}}(a,b;L) = \min(b-a, L-(b-a))$:
  $$t_{\mathrm{pair,cyc}, i} = \sum_{0 \le a < b < L_i} \frac{\mathrm{tr}_M(w_{i,a} w_{i,b})}{d_{\mathrm{arc}}(a,b;L_i)^2} = \bigl(0,\; 0,\; 0,\; z_D^2,\; z_D^2,\; 2 z_D^2 + (h_0 z_D + 1)\bigr).$$
- **C1b (`ecat_pair_kernel_open`, open-strand distance control):** Same pair kernel with open-word separation $d_{\mathrm{open}}(a,b) = b - a$:
  $$t_{\mathrm{pair,open}, i} = \sum_{0 \le a < b < L_i} \frac{\mathrm{tr}_M(w_{i,a} w_{i,b})}{(b - a)^2} = \Bigl(0,\; 0,\; 0,\; z_D^2,\; z_D^2,\; 2 z_D^2 + \tfrac{1}{4}(h_0 z_D + 1)\Bigr).$$
- **C2a (`thomae_jackson_bwd_crossing`, from `ThomaeJacksonCoulombAndAlphaTunneling.lean`):** Backward $q_0^{-2}$-scaled proper-time cost per crossing $t_i = q_0^{-2} \ell(w_i) = q_0^{-2}(0, 1, 1, 2, 2, 3)$ (alongside bare crossing count $\ell(w_i)$).
- **C2b (`thomae_jackson_bwd_geom_lattice`):** Cumulative backward Thomae–Jackson integral across $\ell(w_i)$ geometric proper-time steps $\tau_j = (q_0^2)^j$, $t_i = \sum_{j=0}^{\ell(w_i)-1} (1 - q_0^{-2})(q_0^2)^j = q_0^{-2}((q_0^2)^{\ell(w_i)} - 1)$.
- **C3a (`full_twist_markov_trace_control`):** Markov-traced full-twist pairing $t_i = \mathrm{tr}_M(\Delta_3^2 b_i)$ where $\Delta_3^2 = (\sigma_0\sigma_1\sigma_0)^2 = e_-^2$. By `operator_selection_lp.lean` (`confinement_lp_braid_gram_probe.py`), since $y_{(1^3)} = 0$, this cost must also collapse: $\langle t, v_{(1^3)} \rangle = 0$.
- **C3b (`full_twist_wedderburn_casimir`):** Unweighted regular/Wedderburn central Casimir shift $t_i = \frac{1}{6}\sum_{\lambda \vdash 3} \dim(\lambda)\,(c_\lambda(q_0) - 1)\,\chi_\lambda(b_i)$, where $\Delta_3^2|_{\lambda} = c_\lambda(q_0) \cdot I = q_0^{2\,\mathrm{cont}(\lambda)} I$ with contents $(+3, 0, -3)$ for $\lambda \in \{(3), (2,1), (1^3)\}$, so $(1^3)$ is **not** killed by $y_{(1^3)} = 0$.
- **C3c (`full_twist_nf_vector`):** Normal-form coefficient vector $t_i = \mathrm{nf}(\Delta_3^2)_i$ in $H_3(q_0)$ (`radical_pairing_sign_rep_probe.py` predicts $\langle \mathrm{nf}(\Delta_3^2), v_{(1^3)} \rangle = (-1/q_0)^6 = q_0^{-6} \neq 0$).

## 3. Pre-Registered Exact Dual-Feasibility Reduction & Energy-Unit Reporting

1. **Exact quotient solve + 1D dual cone interval:** Because $\mathrm{Im}(G_D) = v_{(1^3)}^\perp$ and $\langle t - y_0 \mathbf{1}, v_{(1^3)} \rangle = 0$ identically at $y_0 = \langle t, v_{(1^3)} \rangle / \langle \mathbf{1}, v_{(1^3)} \rangle$, the linear equation $y_0 \mathbf{1} + G_D y = t$ is **always** solvable on $H_3(q_0)$, with 1-parameter solution line
   $$y(\alpha) = y_{\min} + \alpha\, v_{(1^3)}, \qquad y_{\min} = G_D^+(t - y_0 \mathbf{1}) \perp v_{(1^3)}.$$
   Dual cone non-negativity ($y(\alpha) \ge 0$ componentwise) holds **if and only if**
   $$\alpha_{\mathrm{lo}} := \max_{i \in \{0,3,4\}} \left(-\frac{y_{\min,i}}{v_{(1^3),i}}\right) \;\le\; \min_{j \in \{1,2,5\}} \left(-\frac{y_{\min,j}}{v_{(1^3),j}}\right) =: \alpha_{\mathrm{hi}}.$$
2. **Energy-scale conversions (comparison only, no selection):** Report dimensionless $y_0(q_0)$ alongside $y_0 \cdot E_0(q_0)$ ($E_0 = m_e / (q_0(q_0 - 1))$) and $y_0 \cdot E_{\mathrm{osc}}(q_0)$ ($E_{\mathrm{osc}} = \mathfrak{E}_e = m_e / (q_0 - 1)^2$).
3. **Precision & pins:** `mpmath.workdps(80)` (serialized at 50 dps), `q0Anchor = "proton"`, cross-checked against exact `sympy` rational evaluation at $q = 11/10, 7/5$. Zero `float64`, zero fitting.
4. **Honest verdict rule:** Every candidate is reported whether $\langle t, v_{(1^3)} \rangle = 0$ or $\neq 0$, whether $y_0$ is positive or negative, and whether the dual cone interval $[\alpha_{\mathrm{lo}}, \alpha_{\mathrm{hi}}]$ is non-empty (dual feasible, bounded primal) or empty (dual infeasible, primal unbounded below without box floor $-M$). Nothing is selected by proximity to an experimental binding energy.
