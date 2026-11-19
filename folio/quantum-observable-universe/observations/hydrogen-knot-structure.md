**Example.**
Hydrogen $\mathcal{A}(1, 0)$ is the simplest atom: one proton, zero neutrons, one electron.

$$
  \mathcal{A}(1, 0)
  = 
  \underbrace{
    \mathcal{B}_3(\nu_r, \nu_g, \nu_b) \oplus \mathcal{L}_H
  }_{\mathfrak{p}\text{ (proton)}}
   \oplus 
  \underbrace{T_{2,3}}_{e^-\text{ (electron)}}
$$

**Knot inventory.**

See [Table 1](#tbl:hydrogen-knot-structure-table1-data).

Total: **3 unknots** + **1 trefoil**, linked by **1 Borromean** + **2 Hopf** links.

**Mass budget.**

See [Table 2](#tbl:hydrogen-knot-structure-table2-data).

The proton's $938$ MeV derives entirely from the Borromean linking of three massless unknots. The electron's $0.511$ MeV derives from vacuum drag (the only mass mechanism for a free trefoil with zero hyperbolic volume). The binding energy ($-13.6$ eV) is negligible on this scale.

**Ionization energy.**

The electron $T_{2,3}$ is Hopf-linked to the proton at the ground state ($n = 1$). The ionization energy is:

$$
  E_{\mathrm{ion}} =  \frac{m_e \cdot \alpha^2}{2}
  =  13.6 \text{ eV}
$$

Here $\alpha$ is the fine structure constant. The framework relates $\alpha$ to the aether parameter via:

$$
  \alpha =  \frac{\tanh(\ln q)}{C_{\mathrm{geom}}}
$$

The fundamental formula for $\alpha$ is the EM coupling projection ([EM coupling projection](#prop:em-coupling-projection)):

$$
  \alpha_{\mathrm{EM}}(q)
  = 
  \frac{q^{-1}}{[9]_q \cdot [10]_q}
$$

The antisymmetric eigenvalue of the $R$-matrix $q^{-1}$ provides the bare coupling at a single crossing. The terms $[9]_q$ and $[10]_q$ are the $q$-deformed crossing numbers of the strong ($T_{2,9}$) and weak ($T_{3,5}$) force-carrier generators. At $q = q_0$, this yields the bare value $\alpha^{-1} \approx 136.823$, which is $-0.155\%$ from CODATA. With the multiplicative Chern–Simons pairing tower resummed at the Witten Gram-determinant ratio $\kappa \approx 1.722$ ([the Chern-Simons block](#rem:em-coupling-chern-simons)), the proton-pinned value is $\alpha^{-1} \approx 137.035935$ ($-468\;\mathrm{ppb}$ from CODATA 2022; exact closure via $\kappa$ alone would require $\kappa \approx 1.9153$). Incorporating the proved genus-$4$ Bring topological invariants — the cohomological genus $g = 4$ Gauss–Bonnet infrared zero-mode $b_1/\mathrm{Area} = 2/(3\pi)$, the Jacobian $E^4$ Hodge zero-mode, and the Form-B Bring–Schwinger cubic self-energy fixed point $q[9]_q[10]_q + \frac{2}{3\pi} + \alpha H(1 - h^2\alpha)$ with $H = [2]_q/(8\pi)$ — brings $\alpha_{\mathrm{EM}}^{-1}$ to $\approx 137.036009$ ($+71\;\mathrm{ppb}$ bare, or $\sim 16\;\mathrm{ppb}$ with the Schwinger shift), leaving only the higher-loop analytic Bloch-group bridge open ([open problems](#rem:alpha-em-derivation-open-problems)).

The two formulations are consistent: $\tanh(\ln q) / C_{\mathrm{geom}} = q^{-1}/([9]_q \cdot [10]_q)$. This fixes $C_{\mathrm{geom}}$:

$$
  C_{\mathrm{geom}}
  = 
  \frac{\tanh(\ln q) \cdot [9]_q \cdot [10]_q}{q^{-1}}
  = 
  \frac{(q^2 - 1) \cdot [9]_q \cdot [10]_q}{q^2 + 1}
   \approx  14.26.
$$

**Physical reading:** the electromagnetic coupling is the antisymmetric braiding eigenvalue $q^{-1}$ divided by the total topological complexity $[9]_q \cdot [10]_q$ of the strong and weak force sectors. In the crossing-asymmetry form $\alpha = \tanh(\ln q)/C_{\mathrm{geom}}$, the factor $\tanh(\ln q) = (q - q^{-1})/(q + q^{-1})$ acts as the EM-to-strong ratio, while $C_{\mathrm{geom}}$ absorbs the force-carrier $q$-integers.

The $\alpha^2$ dependence of the ionisation energy reflects **two Skein resolutions**: the mediating photon must resolve one crossing at the electron and one at the proton.

**Shell transitions.**

Exciting the electron from shell $n$ to shell $n'$ alters the Hopf linking level. The energy is:

$$
  \Delta E_{n \to n'}
  =  13.6 \left(\frac{1}{n^2} - \frac{1}{n'^2}\right)
  \text{ eV}
$$

The $1/n^2$ dependence emerges from the Skein resolution of the Hopf link at linking level $n$: the crossing energy of a level-$n$ Hopf link scales as $1/n^2$ because the Seifert surface area grows as $n^2$.

See [Table 3](#tbl:hydrogen-knot-structure-table3-data).
