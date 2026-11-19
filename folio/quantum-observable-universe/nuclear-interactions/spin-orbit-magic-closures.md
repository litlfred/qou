*Let $\ell \in \mathbb{N}$ denote the orbital angular momentum quantum number on the graded nucleon spin–isospin Pauli fiber. For each nucleon species ($p$ or $n$):*

1. ***Spin–orbit subshell multiplicities ($2j + 1$):*** *The spin-aligned subshell $j = \ell + \tfrac{1}{2}$ has single-species magnetic degeneracy $g_+(\ell) = 2\ell + 2$, and for $\ell \ge 1$ the spin-antialigned partner $j = \ell - \tfrac{1}{2}$ has degeneracy $g_-(\ell) = 2\ell$, satisfying*

$$
  g_+(\ell) + g_-(\ell) \;=\; 2(2\ell + 1),
  \qquad
  g_+(\ell) - g_-(\ell) \;=\; 2,
  \qquad
  2\bigl(g_+(\ell) + g_-(\ell)\bigr) \;=\; 4(2\ell + 1).
$$

   *At $\ell = 0$, $g_+(0) = 2$ and $g_-(0) = 0$, recovering the four-state $s$-wave spin–isospin fiber of ${}^{4}\mathrm{He}$ ($2 \times 2 = 4$).*

2. ***Harmonic-oscillator shell degeneracies and tetrahedral cumulative closures:*** *The $N$-th three-dimensional isotropic harmonic-oscillator major shell ($N = 2n_r + \ell \ge 0$) has single-species degeneracy $D_{\mathrm{osc}}(N) = 2\binom{N+2}{2} = (N+1)(N+2)$, and cumulative single-species occupancy across $0 \le N \le K$ is*

$$
  C_{\mathrm{osc}}(K)
  \;=\; \sum_{N=0}^{K} (N + 1)(N + 2)
  \;=\; \frac{(K + 1)(K + 2)(K + 3)}{3}
  \;\in\; \{2, 8, 20, 40, 70, 112, 168\}
  \qquad (0 \le K \le 6).
$$

3. ***Carbon-12 ($Z = N = 6$) spin–orbit subshell closure and Oxygen-16 ($Z = N = 8$) completion:*** *Filling the $N = 0$ ($1s_{1/2}$) core together with the lowered spin-aligned $1p_{3/2}$ subshell closes at*

$$
  D_{\mathrm{osc}}(0) + g_+(1) \;=\; 2 + 4 \;=\; 6
  \qquad (Z = N = 6,\; A = 12,\; {}^{12}\mathrm{C}),
$$

   *before the spin-antialigned $1p_{1/2}$ partner of degeneracy $g_-(1) = 2$ completes the $N = 1$ major shell at $2 + 4 + 2 = C_{\mathrm{osc}}(1) = 8$ ($Z = N = 8$, $A = 16$, ${}^{16}\mathrm{O}$).*

4. ***Universal Mayer–Jensen spin–orbit intruder magic numbers:*** *For every major shell index $K \ge 2$, spin–orbit coupling depresses the stretched $n_r = 0$, $\ell = K + 1$, $j = K + \tfrac{3}{2}$ intruder subshell of degeneracy $g_+(K + 1) = 2K + 4$ from oscillator shell $K + 1$ into major shell $K$, yielding the closed-form magic sequence*

$$
  M_K
  \;=\; C_{\mathrm{osc}}(K) + g_+(K + 1)
  \;=\; \frac{(K + 1)(K + 2)(K + 3)}{3} + (2K + 4)
  \;=\; \frac{(K + 2)(K^2 + 4K + 9)}{3},
$$

   *which evaluates at $K = 2, 3, 4, 5, 6$ to*

$$
  (M_2, M_3, M_4, M_5, M_6) \;=\; (28, 50, 82, 126, 184)
$$

   *and satisfies the shell-step recurrence $M_{K+1} - M_K = \bigl(D_{\mathrm{osc}}(K+1) - g_+(K+1)\bigr) + g_+(K+2) = D_{\mathrm{osc}}(K+1) + 2 = (K+2)(K+3) + 2$.*

5. ***Discrete Pauli Fermi-asymmetry quadratic promotion law:*** *For any non-decreasing single-particle level spectrum $\varepsilon_0 \le \varepsilon_1 \le \cdots$, the cumulative Fermi filling energy $E_{\mathrm{fill}}(M) = \sum_{i=0}^{M-1} \varepsilon_i$ satisfies, for any balanced core occupancy $M$ and half-excess $d \le M$ ($Z = M - d$, $N = M + d$, $A = 2M$, $N - Z = 2d$),*

$$
  \Delta E_{\mathrm{Pauli}}(M, d)
  \;=\; E_{\mathrm{fill}}(M + d) + E_{\mathrm{fill}}(M - d) - 2 E_{\mathrm{fill}}(M)
  \;=\; \sum_{k=0}^{d-1} \bigl(\varepsilon_{M+k} - \varepsilon_{M-d+k}\bigr)
  \;\ge\; 0,
$$

   *vanishing at $Z = N$ ($d = 0$). Under uniform local level spacing $\Delta\varepsilon > 0$ ($\varepsilon_i = \varepsilon_0 + i\,\Delta\varepsilon$), every promoted pair shifts by $d\,\Delta\varepsilon$ and the Pauli asymmetry penalty is identically quadratic in neutron excess:*

$$
  \Delta E_{\mathrm{Pauli}}(M, d)
  \;=\; d^2 \Delta\varepsilon
  \;=\; \frac{(N - Z)^2}{4}\,\Delta\varepsilon.
$$
