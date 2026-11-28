# Pre-Registration: Racah Seniority-$0$ Coherent-Pair $\alpha$-Preformation & $q$-Hankel Coulomb Slope Split (2026-11-28)

Bean `qou-q0gw` (under Stability Epic `qou-s028` / parent `qou-myts`).
Written, committed, and pushed **before** evaluating the candidate seniority-$0$ coherent-pair preformation models against experimental half-lives.

## 1. Calibration, Anti-Fit & Precision Discipline (STRICT)

- **Working precision:** `mpmath.workdps(80)` (`OUT_DPS = 50` serialized), `json.load(..., parse_float=str)`, zero `float64` imports, literals, or casts.
- **Aether pin:** `q0Anchor = "proton"` (`qou_substrate.constants.q_at(dps=80)`).
- **Zero fitting:** All single-particle angular momenta $j$, pair degeneracies $\Omega = (2j + 1)/2$, and valence pair counts $k$ are exact integers fixed by the standard Mayer--Jensen spin-orbit shell sequence (`1h_{9/2}` above $Z = 82$, `3p_{1/2}` at closed $N = 126$, `2g_{9/2}` for $126 < N \le 136$, `1i_{11/2}` for $136 < N \le 148$). No preformation normalization, shell occupancy, barrier radius, or Q-value is tuned against NUBASE2020 or AME2020.
- **Comparison boundary:** Experimental half-lives $T_{1/2}^{\mathrm{exp}}$ (`NUBASE2020`) and bare Gamow--Gurney--Condon WKB half-lives $T_{1/2}^{\mathrm{WKB}}$ at `AME2020` $Q_\alpha$ (`computations/probes/alpha_decay_n126_and_derived_qalpha/alpha_decay_n126_qalpha_probe.witness.json`) enter **only** at the comparison residual $\Delta\log_{10} T_{1/2} = \log_{10}\bigl((T_{1/2}^{\mathrm{WKB}} / S_\alpha) / T_{1/2}^{\mathrm{exp}}\bigr)$. If a seniority-$0$ coherent-pair prescription leaves a residual gap or worsens a nucleus relative to bare WKB ($S_\alpha = 1$), that exact residual is reported without adjustment.

## 2. Part A — Racah Seniority-$0$ Coherent-Pair Overlap Algebra (`QOU.Nuclear.AlphaSeniorityPreformation`)

In a single-$j$ shell of magnetic degeneracy $2j + 1 = 2\Omega$ ($\Omega \in \mathbb{N}_+$ Kramers time-reversed pair orbitals $\alpha \in \{1, \dots, \Omega\}$), let $b^\dagger_\alpha$ create pair $\alpha$ ($b_\alpha^{\dagger 2} = 0$) and let
$$
  A^\dagger = \sum_{\alpha = 1}^{\Omega} b^\dagger_\alpha,
  \qquad
  A = \sum_{\alpha = 1}^{\Omega} b_\alpha,
  \qquad
  [A, A^\dagger] = \Omega - 2\hat{K}
$$
be the Racah $\mathfrak{su}(2)$ quasispin pair generators on the $2^\Omega$-dimensional pair Fock space. On the normalized seniority-$0$ states $|j^{2k}, v = 0\rangle$ ($1 \le k \le \Omega$):

1. **Coherent collective pair overlap squared:**
   $$
     W(k, \Omega)
     := \bigl|\langle j^{2k}, v = 0 \mid A^\dagger \mid j^{2k-2}, v = 0 \rangle\bigr|^2
     = k(\Omega - k + 1).
   $$
2. **Single localized Kramers-orbital overlap squared:**
   $$
     \bigl|\langle j^{2k}, v = 0 \mid b^\dagger_{\alpha_0} \mid j^{2k-2}, v = 0 \rangle\bigr|^2
     = \frac{k(\Omega - k + 1)}{\Omega^2}
     = \frac{W(k, \Omega)}{\Omega^2},
   $$
   so $\Omega$-orbital pairing coherence enhances squared pair pickup over a single orbital by $\Omega^2$ (and over an incoherent sum of the $\Omega$ orbitals by $\Omega$).
3. **Half-filling rational capacity bound:**
   $$
     4\,W(k, \Omega) = (\Omega + 1)^2 - \bigl(2k - (\Omega + 1)\bigr)^2 \le (\Omega + 1)^2,
     \qquad
     W_{\mathrm{cap}}(\Omega) := \left(\frac{\Omega + 1}{2}\right)^2,
   $$
   ensuring $0 < W(k, \Omega) / W_{\mathrm{cap}}(\Omega) \le 1$ for every $\Omega \ge 1$ and $1 \le k \le \Omega$ (attaining $1$ at odd-$\Omega$ half-filling $k = (\Omega + 1)/2$).

### Shell Quantum Numbers for the Polonium Chain ($Z = 84 = 82 + 2$)
- **${}^{210}_{84}\mathrm{Po}_{126}$ (closed $N = 126$):** $\pi(1h_{9/2})^2$ ($k_p = 1, \Omega_p = 5, W_p = 5$) $\otimes$ $\nu(3p_{1/2})^{-2}$ ($k_n = 1, \Omega_n = 1, W_n = 1$), joint coherent weight $W_p W_n = 5$.
- **${}^{212}_{84}\mathrm{Po}_{128}$ (open shell):** $\pi(1h_{9/2})^2$ ($k_p = 1, \Omega_p = 5, W_p = 5$) $\otimes$ $\nu(2g_{9/2})^2$ ($k_n = 1, \Omega_n = 5, W_n = 5$), joint coherent weight $W_p W_n = 25$.
- **${}^{214}_{84}\mathrm{Po}_{130}$ (open shell):** $\pi(1h_{9/2})^2$ ($k_p = 1, \Omega_p = 5, W_p = 5$) $\otimes$ $\nu(2g_{9/2})^4$ ($k_n = 2, \Omega_n = 5, W_n = 8$), joint coherent weight $W_p W_n = 40$.

### Pre-Registered Parameter-Free Observables & Normalizations (All Reported Side-by-Side)
1. **Scale-free relative ratios (independent of overall normalization):**
   - Open-shell pair addition: $W({}^{214}\mathrm{Po}) / W({}^{212}\mathrm{Po}) = 8 / 5 = 1.6$ vs $S_\alpha^{\mathrm{emp}}({}^{214}\mathrm{Po}) / S_\alpha^{\mathrm{emp}}({}^{212}\mathrm{Po})$ (and vs $1$ for literal uncorrelated counting).
   - $N = 126$ shell-closure jump: $W({}^{212}\mathrm{Po}) / W({}^{210}\mathrm{Po}) = 25 / 5 = 5$ vs $S_\alpha^{\mathrm{emp}}({}^{212}\mathrm{Po}) / S_\alpha^{\mathrm{emp}}({}^{210}\mathrm{Po})$ (and vs $1/5$ for literal uncorrelated counting).
2. **Absolute preformation prescriptions $S_\alpha = S_p \cdot S_n$:**
   - **M0 (`literal_uncorrelated_MJ`, `alpha_preformation_bound` Scope (a) baseline):** $S = \frac{1}{2\Omega_p}\cdot\frac{1}{2\Omega_n}$.
   - **M1 (`single_orbital_seniority`):** $S = \frac{W(k_p, \Omega_p)}{\Omega_p^2}\cdot\frac{W(k_n, \Omega_n)}{\Omega_n^2} \in (0, 1]$.
   - **M2 (`per_subshell_opnorm_coherent`):** $S = \frac{W(k_p, \Omega_p)}{W_{\mathrm{cap}}(\Omega_p)}\cdot\frac{W(k_n, \Omega_n)}{W_{\mathrm{cap}}(\Omega_n)} \in (0, 1]$ (evaluated across ${}^{210,212,214}\mathrm{Po}$ and also across the open-shell actinides/radon/radium in the `qou-i2jl` emitter list to verify the `AlphaPreformationBound` barrier-side obstruction).
   - **M3 (`valence_shell_opnorm_coherent`):** $S = \frac{W(k_p, \Omega_p)}{W_{\mathrm{cap}}(\Omega_{p,\mathrm{val}})}\cdot\frac{W(k_n, \Omega_n)}{W_{\mathrm{cap}}(\Omega_{n,\mathrm{val}})} \in (0, 1]$ normalized against the $(Z > 82, N > 126)$ valence shell capacities $\Omega_{p,\mathrm{val}} = \Omega_p(1h_{9/2}) = 5$, $\Omega_{n,\mathrm{val}} = \Omega_n(2g_{9/2}) = 5$.
   - **M4 (`single_state_times_racah`):** $S = \frac{W(k_p, \Omega_p)}{2\Omega_p}\cdot\frac{W(k_n, \Omega_n)}{2\Omega_n}$ (documented with the algebraic caveat that $W(k,\Omega)/(2\Omega) > 1$ for $\Omega \ge 7$ near half-filling).

## 3. Part B — $q$-Hankel Coulomb Shape Factor Update on `alpha_qalpha_inheritance`

In `computations/probes/alpha_qalpha_inheritance/alpha_qalpha_inheritance_probe.py`, report side-by-side over the $1,051$ scorecard $\alpha$-emitters:
- **Uniform-ball baseline ($f_{\mathrm{ball}} = (3/5)^{3/2}$):** $E_C^{\mathrm{ball}}(Z, A) = \frac{3}{5}\frac{Z(Z-1)\alpha_q\hbar c}{r_0^{\mathrm{FCC}} A^{1/3}}$.
- **Derived $0s$ $q$-Hankel shape factor ($f_{\mathrm{qHankel}}$ from $J_{1/2}(p^k; p^2)$, $p = 1/q_0$ on the Jackson lattice, `coulomb_shape_factor_qbessel_probe.py`):**
  $$
    E_C^{\mathrm{qHankel}}(Z, A)
    = \frac{f_{\mathrm{qHankel}}}{\sqrt{3/5}}\,\frac{Z(Z-1)\alpha_q\hbar c}{r_0^{\mathrm{FCC}} A^{1/3}}
    = \frac{f_{\mathrm{qHankel}}}{f_{\mathrm{ball}}}\,E_C^{\mathrm{ball}}(Z, A),
  $$
  recording both $\Delta E_C$ $\alpha$-line slopes and the resulting median nuclear $\alpha$-line slope targets $\mathrm{median}(\Delta B_{\mathrm{AME}} + \Delta E_C)$, with the explicit scope caveat that $f_{\mathrm{qHankel}}$ is derived strictly for the $A \le 4$ $0s$ shell (`coulomb_energy.py`) and is an extrapolation at $A \ge 6$.
