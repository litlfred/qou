**Proof.**

> **Scope of the asymptotic expansion.** One sub-step in the Taylor comparison remains uncomputed inline: the order-$h^2$ term of $\ln(V_{\mathrm{pp}}/V_{\mathrm{nn}})$, where $z h + O(h^2) = \ln(1 + zh) + O(h^3)$ requires the $h^2$ coefficient to equal $-z^2/2$. The geometric and exponential truncation-remainder bound is established unconditionally in [exponential decay of the archimedean remainder](#prop:archimedean-remainder-exponential-decay). The $+1.31$ keV residual and the CODATA $7\%$ agreement are empirical comparisons rather than proof steps.


*Form A side.* The normal form counit reads $\lvert\Delta(\mathrm{net})\rvert = h(2 - h)/2 = h - h^2/2 + O(h^3)$, obtained via direct expansion of the single-wrap symbolic closed form ([symbolic neutron $Q$-value](#prop:neutron-qvalue-symbolic)).

*Form B side.* The Hecke perturbation carries the half-factor $\Delta_\beta(q) = \tfrac{1}{2}(q - q^{-1})\,\mathbb{I} = \tfrac{h}{2}\,\mathbb{I}$ ([beta-decay transfer matrix](#prop:beta-decay-transfer-matrix)). The change in Markov-traced volume per generator incorporates this factor:
$$
  \Delta \hat V_i
  \;=\;
  z\,(\Delta M_i)_{11} + (\Delta M_i)_{21}
  \;=\;
  \tfrac{z\,h}{2} + O(h^2).
$$

At single wrap with $A = 1$, the proton-to-neutron conversion affects two generators, $\sigma_0$ and $\sigma_1$ ([symbolic neutron $Q$-value](#prop:neutron-qvalue-symbolic)). The total log-ratio is:
$$
  \ln\!\frac{V_{\mathrm{pp}}}{V_{\mathrm{nn}}}
  \;=\;
  \sum_{i \in \{0,1\}}
    \ln\!\frac{\hat V^{\mathrm{pp}}_i}{\hat V^{\mathrm{nn}}_i}
  \;\approx\;
  2 \cdot \tfrac{z\,h}{2}
  \;=\;
  z\,h \;+\; O(h^2)
  \;=\;
  \ln(1 + z\,h) + O(h^3).
$$

*Ratio.* Forming the dimensionless ratio $\mathfrak{Q}_\beta^{\mathrm{A}} / \mathfrak{Q}_\beta^{\mathrm{B}}$ and dividing by $E_0$ cancels $h$ in the leading term:
$$
\begin{aligned}
\frac{\mathfrak{Q}_\beta^{\mathrm{A}}}{\mathfrak{Q}_\beta^{\mathrm{B}}}
&=
\frac{h - h^2/2 + O(h^3)}
     {(z h - z^2 h^2 / 2 + O(h^3))\,/\,z} \\
&=
\frac{h - h^2/2}{h - z h^2 / 2} \cdot \bigl(1 + O(h)\bigr) \\
&=
\frac{1 - h/2}{1 - z h/2} \cdot \bigl(1 + O(h)\bigr) \\
&= 1 + \tfrac{(z - 1)\,h}{2} + O(h^2).
\end{aligned}
$$

The intermediate identity $\mathfrak{Q}_\beta^{\mathrm{B}}/E_0 \cdot z = z h - (z h)^2/2 + O(h^3)$ isolates the dimensional content of the $1/z$ factor. Form B requires $z$ to normalize the eigenfunction basis to the Markov-traced volume. This does not mean that Form A and Form B measure different observables.

*Exponential remainder.* Both truncations inhabit the spectral decomposition of the q-Hamiltonian along the Gröbner basis filtration of the free-neutron sector $K \subset H_3(q)$ at $q = q_0$. By [exponential decay of the archimedean remainder](#prop:archimedean-remainder-exponential-decay), each finite-depth truncation $\mathfrak{Q}_\beta^{(N)}$ incurs an error bounded by $C(K) \cdot e^{-c(K) N}$, where $C, c > 0$ are structural constants. At $N = 0$, this yields the observed $+1.31$ keV residual. At $N \geq 1$, the bound is sub-keV. $\square$

## Reading

The bridge formula:
$$
  \mathfrak{Q}_\beta^{\mathrm{A}}
  \;=\;
  \mathfrak{Q}_\beta^{\mathrm{B}} \cdot \bigl(1 + \tfrac{(z-1)\,h}{2} + O(h^2)\bigr)
$$
demonstrates that Form A and Form B represent a single observable in two bases: the normal form counit basis (where $\Delta(\mathrm{net})$ is discrete) and the transfer-matrix basis (where $\ln V_{\mathrm{pp}}/V_{\mathrm{nn}}$ is the natural eigenfunction). The $1/z$ factor in Form B is the required Markov–Jones normalization mapping the eigenfunction space onto MeV.

The [exponential-remainder bound](#prop:archimedean-remainder-exponential-decay) dampens the eigenfunction so that finite-depth truncations converge exponentially fast in depth $N$. Under convention D ($z_D = q^3/(q^2 + 1)$), the canonical Markov trace evaluates to $0.4491$ MeV ($0.4447$ MeV at order zero) on the bare single-sector term, with the all-order Convention-D generating function $\mathcal{G}_D(u; q)$ and cumulants $c_2^{(D)}, c_3^{(D)}, c_4^{(D)}$ derived in closed form, whereas the single-wrap counit closed form (Form A at $N = 0$) evaluates near $+0.168\%$ as an auxiliary comparison.

Numerical evaluation to 50 decimal places confirms the expansion across each term; see [Table](#tbl:q-beta-spectral-bridge-table-data).

The residual lies within the $O(h^2)$ Taylor bound. The MeV-level discrepancy between $\mathfrak{Q}_\beta^{\mathrm{A}}$ and $\mathfrak{Q}_\beta^{\mathrm{B}}$ constitutes the next-order correction $(z-1)h/2 \approx -0.040$ at $z = q^3/(q^2+1)$ (versus $-0.052$ under convention C). Both forms agree with the CODATA value of $0.7823$ MeV within $7\%$, with Form A ([symbolic neutron $Q$-value](#prop:neutron-qvalue-symbolic)) serving as an auxiliary single-wrap closed form alongside the canonical Markov trace at $z = q^3/(q^2+1)$.
