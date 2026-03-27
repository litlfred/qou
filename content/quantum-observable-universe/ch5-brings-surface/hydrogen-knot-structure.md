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

**Candidate formula.**  Sage computation of the Jones polynomials
at $q = 1.110$ (`sage-cgeom.sage`) gives the best-fit formula

$$
  C_{\mathrm{geom}}
  \;=\;
  \frac{[2]_q \;\cdot\; [7]_q}{J_{\mathrm{Borr}}(q)}
  \;\approx\; 14.74
  \qquad
  \Bigl(\tfrac{1}{\alpha} \approx 141.8,\;\text{error } 3.5\%\Bigr)
$$

where $[2]_q = q + q^{-1}$ is the quantum dimension of the
electron (fundamental representation), $[7]_q$ is the quantum
dimension associated with the Brings surface genus ($2g - 1 = 7$
for genus $g = 4$), and $J_{\mathrm{Borr}}(q) \approx 1.040$ is
the Jones polynomial of the Borromean link (the proton's
topological structure).

**Physical reading:** the electromagnetic coupling is the
electron's quantum dimension times the Brings surface capacity,
normalised by the proton's topological complexity.  The $[7]_q$
factor arises because the Brings surface of genus 4 provides
$2g - 1 = 7$ independent crossing channels between the electron
and proton strands.  The Borromean Jones polynomial in the
denominator accounts for the proton's internal correlations that
screen the electromagnetic interaction.

**Residual (3.5%).**  The remaining discrepancy may arise from:
(a) writhe corrections between the braid closure and the standard
link diagram, (b) higher-order Skein resolution terms beyond the
leading $[2]_q \cdot [7]_q$ product, or (c) the coloured Jones
polynomial in the adjoint representation (the Sage computation
gives $J_{T_{2,3}}^{(3)}(q) = 0.900$ for the trefoil adjoint
colouring, which could enter a refined formula).

The $\alpha^2$ dependence of the ionisation energy reflects
**two Skein resolutions** — the photon mediating the interaction
must resolve one crossing at the electron and one at the proton.

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
