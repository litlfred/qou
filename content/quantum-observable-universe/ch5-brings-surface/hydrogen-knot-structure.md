**Example.**
Hydrogen $\mathcal{A}(1, 0)$ is the simplest atom: one proton,
zero neutrons, one electron.

$$
  \mathcal{A}(1, 0)
  \;=\;
  \underbrace{
    \mathcal{B}_3(\nu_r, \nu_g, \nu_b) \bowtie \mathcal{L}_H
  }_{\mathfrak{p}\text{ (proton)}}
  \;\bowtie\;
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
| $\bowtie$ | Hopf link | 1 | Electron--proton binding |

Total: **3 unknots** + **1 trefoil**, linked by **1 Borromean**
+ **2 Hopf** links.

**Mass budget.**

| Source | Mechanism | Mass |
|--------|-----------|-----:|
| $\mathrm{Vol}(\mathcal{B}_3) = 7.328$ | Borromean volume | $\sim 938$ MeV |
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
  E_{\mathrm{ion}} \;=\; \frac{m_e \cdot \alpha^2}{2}
  \;=\; 13.6 \text{ eV}
$$

where $\alpha$ is the fine structure constant.  In the QOU
framework, $\alpha$ relates to the substrate parameter via

$$
  \alpha \;=\; \frac{\tanh(\ln q)}{C_{\mathrm{geom}}}
$$

where $\tanh(\ln q) = (q - q^{-1})/(q + q^{-1})$ is the
electromagnetic-to-strong ratio derived from $q$ alone
([crossing asymmetry](#rem:skein-crossing-asymmetry)).
The geometric factor $C_{\mathrm{geom}}$ is the total Skein
weight of the electron--proton crossing evaluation — the
Markov trace of the Hopf link between the trefoil ($T_{2,3}$)
and the Borromean proton structure, summed over all crossing
resolutions.

**Open computation:** Deriving $C_{\mathrm{geom}}$ from the
Skein algebra of $\mathrm{Hopf}(T_{2,3}, \mathcal{B}_3)$
requires evaluating the full Markov trace of the
electron--proton link at $q = 1.110$.  The trefoil has 3
self-crossings and the Borromean link has 6; the Hopf linking
adds inter-component crossings whose Skein weights sum to a
non-integer total.  The target value $C_{\mathrm{geom}} \approx
14.25 = \tanh(\ln q)/\alpha$ is fixed by CODATA; the open task
is to reproduce this from the Skein algebra independently.

The $\alpha^2$ dependence reflects **two Skein resolutions** —
the photon mediating the interaction must resolve one crossing
at the electron and one at the proton.

**Shell transitions.**

Exciting the electron from shell $n$ to shell $n'$ changes the
Hopf linking level.  The energy is

$$
  \Delta E_{n \to n'}
  \;=\; 13.6 \left(\frac{1}{n^2} - \frac{1}{n'^2}\right)
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
