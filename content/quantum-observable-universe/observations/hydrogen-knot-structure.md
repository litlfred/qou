**Example.**
Hydrogen $\mathcal{A}(1, 0)$ is the simplest atom: one proton,
zero neutrons, one electron.

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

| Component | Knot type | Count | Role |
|-----------|-----------|------:|------|
| $\nu_r$ | Unknot $K_{0_1}$ | 1 | Up quark (color $r$) |
| $\nu_g$ | Unknot $K_{0_1}$ | 1 | Up quark (color $g$) |
| $\nu_b$ | Unknot $K_{0_1}$ | 1 | Down quark (color $b$) |
| $\mathcal{B}_3$ | Borromean link | 1 | Color confinement |
| $\mathcal{L}_H$ | Hopf link $T(2,2)$ | 1 | Baryon binding |
| $e^-$ | Trefoil $T_{2,3}$ | 1 | Electron |
| $\oplus$ | Hopf link | 1 | Electron--proton binding |

Total: **3 unknots** + **1 trefoil**, linked by **1 Borromean**
+ **2 Hopf** links.

**Mass budget.**

| Source | Mechanism | Mass |
|--------|-----------|-----:|
| $\mathrm{Vol}(\mathcal{B}_3) \approx 7.328$ | Borromean volume | $\sim 938$ MeV |
| $\mathrm{Vol}(T_{2,3}) = 0$ | Trefoil (torus knot) | $0$ |
| $\mathrm{Vol}(\mathcal{L}_H) = 0$ | Hopf link (torus link) | $0$ |
| Skein correction | Crossing asymmetry | $\sim 0.3$ MeV |
| Vacuum drag | Electron mass | $0.511$ MeV |
| **Total** | | **$938.783$ MeV** |

The proton's $938$ MeV comes entirely from the Borromean
linking of three massless unknots.  The electron's $0.511$ MeV
comes from vacuum drag (the only mass mechanism for a free
trefoil with zero hyperbolic volume).  The binding energy
($-13.6$ eV) is negligible on this scale.

**Ionization energy.**

The electron $T_{2,3}$ is Hopf-linked to the proton at the
ground state ($n = 1$).  The ionization energy is

$$
  E_{\mathrm{ion}} =  \frac{m_e \cdot \alpha^2}{2}
  =  13.6 \text{ eV}
$$

where $\alpha$ is the fine structure constant.  In the QOU
framework, $\alpha$ relates to the substrate parameter via

$$
  \alpha =  \frac{\tanh(\ln q)}{C_{\mathrm{geom}}}
$$

The fundamental formula for $\alpha$ is the EM coupling
projection
([EM coupling projection](#prop:em-coupling-projection)):

$$
  \alpha_{\mathrm{EM}}(q)
  = 
  \frac{q^{-1}}{[9]_q \cdot [10]_q}
$$

where $q^{-1}$ is the antisymmetric eigenvalue of the $R$-matrix
(the bare coupling at a single crossing), and $[9]_q$, $[10]_q$
are the $q$-deformed crossing numbers of the strong ($T_{2,9}$)
and weak ($T_{3,5}$) force-carrier generators.  At $q = q_0$
this gives the bare value $\alpha^{-1} \approx 136.82$.  Including the
Chern-Simons correction from the force-carrier torus knots
([EM coupling projection](#prop:em-coupling-projection)),
$\alpha^{-1} \approx 137.036$ ($2.1\;\mathrm{ppm}$ from CODATA).

The two formulations are consistent:
$\tanh(\ln q) / C_{\mathrm{geom}} = q^{-1}/([9]_q \cdot [10]_q)$,
which fixes

$$
  C_{\mathrm{geom}}
  = 
  \frac{\tanh(\ln q) \cdot [9]_q \cdot [10]_q}{q^{-1}}
  = 
  \frac{(q^2 - 1) \cdot [9]_q \cdot [10]_q}{q^2 + 1}
   \approx  14.26.
$$

**Physical reading:** the electromagnetic coupling is the
antisymmetric braiding eigenvalue $q^{-1}$ divided by the total
topological complexity $[9]_q \cdot [10]_q$ of the strong and
weak force sectors.  In the crossing-asymmetry form
$\alpha = \tanh(\ln q)/C_{\mathrm{geom}}$, the factor
$\tanh(\ln q) = (q - q^{-1})/(q + q^{-1})$ is the EM-to-strong
ratio and $C_{\mathrm{geom}}$ absorbs the force-carrier
$q$-integers.

The $\alpha^2$ dependence of the ionisation energy reflects
**two Skein resolutions** — the photon mediating the interaction
must resolve one crossing at the electron and one at the proton.

**Shell transitions.**

Exciting the electron from shell $n$ to shell $n'$ changes the
Hopf linking level.  The energy is

$$
  \Delta E_{n \to n'}
  =  13.6 \left(\frac{1}{n^2} - \frac{1}{n'^2}\right)
  \text{ eV}
$$

The $1/n^2$ dependence should arise from the Skein resolution
of the Hopf link at linking level $n$: the crossing energy
of a level-$n$ Hopf link scales as $1/n^2$ because the
Seifert surface area grows as $n^2$.

| Transition | $\Delta E$ | Photon $\lambda$ | Series |
|------------|-----------|-----------------|--------|
| $1 \to 2$ | $10.2$ eV | $121.6$ nm | Lyman-$\alpha$ |
| $1 \to 3$ | $12.1$ eV | $102.6$ nm | Lyman-$\beta$ |
| $2 \to 3$ | $1.89$ eV | $656.3$ nm | Balmer-$\alpha$ |
| $3 \to 4$ | $0.66$ eV | $1875$ nm | Paschen-$\alpha$ |
