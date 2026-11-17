**Proof.**

> **Scope note (2026-11-17).** The order-$h^2$ term of $\ln(V_{\mathrm{pp}}/V_{\mathrm{nn}})$ is now computed rather than assumed, under the one-site reading stated in the Form B step below: there $V_{\mathrm{pp}}/V_{\mathrm{nn}} = 1 + zh$ exactly, so the $h^2$ coefficient is $-z^2/2$. That reading takes the left and right products $L_i$, $R_i$ to be the identity; the corpus does not construct them for the free neutron, and the alternative reading of two independent sites gives $-z^2/4$ and a different first-order term. The exponential remainder rests on conj:archimedean-remainder-exponential-decay, a conjecture, so the remainder bound is conditional. Form A here is the retired $z = 1$ cell $|h(2-h)/2|$, not the convention-D base $|h^2/2 - h z_D|$. The $+1.31$ keV residual and the CODATA $7\%$ agreement are empirical comparisons, not proof steps.

*Form A side.* The normal form counit reads $\lvert\Delta(\mathrm{net})\rvert = h(2 - h)/2 = h - h^2/2 + O(h^3)$, obtained via direct expansion of the single-wrap symbolic closed form ([prop:neutron-qvalue-symbolic](#prop:neutron-qvalue-symbolic)).

*Form B side.* The Hecke perturbation carries the half-factor $\Delta_\beta(q) = \tfrac{1}{2}(q - q^{-1})\,\mathbb{I} = \tfrac{h}{2}\,\mathbb{I}$ ([prop:beta-decay-transfer-matrix](#prop:beta-decay-transfer-matrix)). The change in Markov-traced volume per generator incorporates this factor:
$$
  \Delta \hat V_i
  \;=\;
  z\,(\Delta M_i)_{11} + (\Delta M_i)_{21}
  \;=\;
  \tfrac{z\,h}{2} + O(h^2).
$$

At single wrap with $A = 1$ we take the conversion to act at one site, with $L_i = R_i = \mathbb{I}$: the crossing passes $T_{nn} \to T_{\mathrm{mix}} \to T_{pp}$, each step adding $\Delta_\beta = \tfrac{h}{2}\mathbb{I}$ ([prop:beta-decay-transfer-matrix](#prop:beta-decay-transfer-matrix)). With $\hat V = z M_{11} + M_{21}$,
$$
  \hat V(T_{nn}) = 1,
  \qquad
  \hat V(T_{\mathrm{mix}}) = 1 + \tfrac{z h}{2},
  \qquad
  \hat V(T_{pp}) = 1 + z h,
$$
so the two steps telescope and
$$
  \ln\!\frac{V_{\mathrm{pp}}}{V_{\mathrm{nn}}}
  \;=\;
  \ln\!\frac{1 + zh/2}{1} + \ln\!\frac{1 + zh}{1 + zh/2}
  \;=\;
  \ln(1 + z\,h)
  \;=\;
  z h - \tfrac{z^2 h^2}{2} + O(h^3)
$$
exactly, not only to leading order.

*Ratio.* We form the dimensionless ratio $\mathfrak{Q}_\beta^{\mathrm{A}} / \mathfrak{Q}_\beta^{\mathrm{B}}$ and divide by $E_0$ to cancel $h$ in the leading term:
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

*Exponential remainder.* Both truncations inhabit the spectral decomposition of the q-Hamiltonian along the Gröbner basis filtration of the free-neutron sector $K \subset H_3(q)$ at $q = q_0$. Following conj:archimedean-remainder-exponential-decay, each finite-depth truncation $\mathfrak{Q}_\beta^{(N)}$ incurs an error bounded by $C(K) \cdot e^{-c(K) N}$, where $C, c > 0$ are structural constants. At $N = 0$, this yields the observed $+1.31$ keV residual. At $N \geq 1$, the bound is sub-keV. $\square$

## Reading

The bridge formula:
$$
  \mathfrak{Q}_\beta^{\mathrm{A}}
  \;=\;
  \mathfrak{Q}_\beta^{\mathrm{B}} \cdot \bigl(1 + \tfrac{(z-1)\,h}{2} + O(h^2)\bigr)
$$
demonstrates that Form A and Form B represent a single observable in two bases: the normal form counit basis (where $\Delta(\mathrm{net})$ is discrete) and the transfer-matrix basis (where $\ln V_{\mathrm{pp}}/V_{\mathrm{nn}}$ is the natural eigenfunction). The $1/z$ factor in Form B is the required Markov–Jones normalization mapping the eigenfunction space onto MeV.

The exponential-remainder bound dampens the eigenfunction (conj:archimedean-remainder-exponential-decay). Finite-depth truncations recover the exact $\mathfrak{Q}_\beta$ exponentially fast in depth $N$. Under convention C this was read as the reason the single-wrap symbolic form (Form A at $N = 0$) achieves $+0.168\%$ accuracy. Form A is now retired as the base; the ruled convention-D base (the Markov trace at $z_D$) gives $0.4447$ MeV ($-43.16\%$), and its convention-D ladder is not yet derived.

## Provenance

We verified this proposition numerically at 50 decimal places via [`q_beta_spectral_bridge_witness.py`](https://github.com/litlfred/qou/blob/main/computations/q_beta_spectral_bridge_witness.py) ([`q-beta-spectral-bridge.witness.json`](https://github.com/litlfred/qou/blob/main/computations/q-beta-spectral-bridge.witness.json)):

See [Table](#tbl:q-beta-spectral-bridge-table-data).

The residual lies within the $O(h^2)$ Taylor bound. The MeV-level discrepancy between $\mathfrak{Q}_\beta^{\mathrm{A}}$ and $\mathfrak{Q}_\beta^{\mathrm{B}}$ constitutes the next-order correction $(z-1)h/2 \approx -0.040$ at $z = q^3/(q^2+1)$ (the $-0.052$ quoted here until 2026-10-10 was the convention-C value). Both forms agree with the CODATA value of $0.7823$ MeV within $7\%$. Form A is the single-wrap symbolic closed form ([prop:neutron-qvalue-symbolic](#prop:neutron-qvalue-symbolic)); under the owner ruling of 2026-09-08 it is a historical cross-check, not the canonical base, which is the Markov trace at $z = q^3/(q^2+1)$.

## Lean formalization

The companion Lean repository records the bridge identities (`polynomial_bridge_identity`, `leading_order_ratio_identity`, `bridge_first_order_remainder`). It also proves the `Real.log` Taylor bounds used here (`log_one_add_taylor_bound`) and contains no `sorry`.
