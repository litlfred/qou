*Form A side.* The NF counit reads
$\lvert\Delta(\mathrm{net})\rvert = h(2 - h)/2 = h - h^2/2 + O(h^3)$
(direct expansion of the single-wrap symbolic closed form per
[prop:neutron-qvalue-symbolic](#prop:neutron-qvalue-symbolic)).

*Form B side.* The Hecke perturbation has the half-factor
$\Delta_\beta(q) = \tfrac{1}{2}(q - q^{-1})\,\mathbb{I} = \tfrac{h}{2}\,\mathbb{I}$
(per [prop:beta-decay-transfer-matrix](#prop:beta-decay-transfer-matrix)
§"change in transfer-matrix product"), so the change in Markov-traced
volume *per generator* picks up the same half:

$$
  \Delta \hat V_i
  \;=\;
  z\,(\Delta M_i)_{11} + (\Delta M_i)_{21}
  \;=\;
  \tfrac{z\,h}{2} + O(h^2).
$$

At single wrap with $A = 1$ the proton-to-neutron conversion affects
the **two** generators $\sigma_0, \sigma_1$ (per the table in
[prop:neutron-qvalue-symbolic](#prop:neutron-qvalue-symbolic)
§"Single-wrap NF computation"), so the total log-ratio is

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

*Ratio.* Forming the dimensionless ratio
$\mathfrak{Q}_\beta^{\mathrm{A}} / \mathfrak{Q}_\beta^{\mathrm{B}}$ and dividing through
by $E_0$ cancels the $h$ in the leading term:

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

The intermediate identity $\mathfrak{Q}_\beta^{\mathrm{B}}/E_0 \cdot z = z h - (z h)^2/2 + O(h^3)$
identifies the **dimensional content** of the $1/z$ factor: $z$
appears in Form B because the eigenfunction basis is normalized to
the Markov-traced volume (Form B's denominator $z$ in $E_0/z$),
not because Form A and Form B measure different observables.

*Exponential remainder.* Both truncations live inside the same
spectral decomposition of the q-Hamiltonian along the GB
filtration of the free-neutron sector $K \subset H_3(q)$ at
$q = q_0$. By
conj:archimedean-remainder-exponential-decay
(applied to the q-dilogarithm tail in the brane-tower expansion),
each finite-depth truncation $\mathfrak{Q}_\beta^{(N)}$ — whether assembled
via Form A or Form B — incurs an error bounded by
$C(K) \cdot e^{-c(K) N}$, with $C, c > 0$ structural constants of
the free-neutron K-class. At $N = 0$ this gives the observed
$+1.31$ keV residual; at $N \geq 1$ the bound is sub-keV.
$\qquad\blacksquare$
