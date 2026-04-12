The localized knot framework ([Definition](#def:localized-knot)) assigns
a topological identity to each fundamental particle.  This dictionary is
*derived* from the categorical braiding on $V = V_{1/2}$, not postulated:
the $R$-matrix of $\mathcal{U}_q(\mathfrak{su}(2))$ endows
$V^{\otimes n}$ with a faithful $B_n$-action
([Proposition](#prop:braid-action-tensor)), and
$q$-Schur--Weyl duality
([Theorem](#prop:knot-eigenbasis-complete)) decomposes
$V^{\otimes n}$ into irreducible summands labelled by partitions
$\lambda \vdash n$. By Alexander's theorem, every oriented knot is the
closure of a braid $\beta \in B_n$, so the Markov trace on the
Iwahori--Hecke algebra $H_n(q)$ identifies each irreducible summand
with a knot type.

**Fermion--boson principle**
([fermions are knots, bosons are links](#prop:fermion-boson-knot-link)).
In the $T(2,n)$ torus family on the Bring's surface, the number of
connected components is $\gcd(2,n)$.  **Fermions** ($n$ odd) are knots
(1 component, half-integer spin); **bosons** ($n$ even) are links (2
components, integer spin).  Quarks are Borromean-linked unknots in the
exceptional divisor
([Borromean baryon](#def:borromean-baryon)).

**Table 1: Fermion sector** (knots, 1 component).

| Knot type | Symbol | Particle / field | Genus | Crossings | $J(q_0)$ | Role in bundle |
|-----------|--------|------------------|:-----:|:---------:|:---------:|----------------|
| Unknot | $T_{1,0}$ ($0_1$) | Neutrino $\nu$ | $0$ | $0$ | $1$ | Trivial braiding; vacuum drag |
| Trefoil | $T_{2,3}$ ($3_1$) | Electron $e^-$ | $1$ | $3$ | $\approx 0.817$ | Simplest stable vortex (gen. 1) |
| Cinquefoil | $T_{2,5}$ ($5_1$) | Muon $\mu^-$ | $2$ | $5$ | $\approx 0.485$ | Gen. 2 lepton on Reeb divisor |
| Septafoil | $T_{2,7}$ ($7_1$) | Tau $\tau^-$ | $3$ | $7$ | — | Gen. 3 lepton on Reeb divisor |
| $T_{2,9}$ | $T_{2,9}$ ($9_1$) | Strong binding | $4$ | $9$ | — | Gluonic binding; saturating genus |
| $T_{3,4}$ | $T_{3,4}$ ($8_{19}$) | Hopf${}^2$ color binding | $3$ | $8$ | — | Force carrier sector $H^{0,1}$ |
| $T_{3,5}$ | $T_{3,5}$ ($10_{124}$) | Weak force ($\beta$-decay) | $4$ | $10$ | — | Mediates $\beta$-decay vertex |

**Table 2: Boson sector** (links, 2 components).

| Link | Symbol | Particle / field | Components | Crossings | Role |
|------|--------|------------------|:----------:|:---------:|------|
| Hopf link | $T(2,2)$ ($L2a1$) | Gluon | $2$ | $2$ | Strong force |
| Torus link | $T(2,4)$ | $W$ boson | $2$ | $4$ | Charged weak force |
| Torus link | $T(2,6)$ | $Z$ boson | $2$ | $6$ | Neutral weak force |
| Torus link | $T(2,8)$ | Higgs boson ($\approx 125$ GeV) | $2$ | $8$ | Scalar boson; spans 3 exceptional divisors |

**Table 3: Derived knots and mass mechanism.**

| Knot type | Symbol | Particle / field | Genus | Crossings | Vol | Role |
|-----------|--------|------------------|:-----:|:---------:|:---:|------|
| Point (empty) | $\varnothing$ | Photon $\gamma$ | $0$ | $0$ | $0$ | Background flux on $\mathcal{S}_p$ |
| Figure-eight | $4_1$ | Higgs field | $1$ | $4$ | $2.030$ | Mass mechanism; amphichiral ($H = H^{\sigma}$) |

**Table 4: Quark sector** (on the exceptional divisor).

Each lepton's torus knot descends to a quark flavour on the
exceptional divisor:

| Quark | Symbol | Knot formula | Generation | Lepton partner |
|-------|--------|-------------|:----------:|----------------|
| Up | $\mathfrak{u}$ | $T_{2,3}$ | 1 | $e^-$ |
| Down | $\mathfrak{d}$ | $T_{2,3}^{\sigma}$ | 1 | $e^-$ (mirror) |
| Strange | $\mathfrak{s}$ | $T_{2,5}^{\sigma}$ | 2 | $\mu^-$ (mirror) |
| Charm | $\mathfrak{c}$ | $T_{2,7}$ | 3 | $\tau^-$ |
| Bottom | $\mathfrak{b}$ | $T_{2,5}$ | 2 | $\mu^-$ |
| Hopf${}^2$ color | $\mathfrak{t}$ | $T_{3,4}$ | — | *(force carrier; "top quark" label deprecated)* |

**Precision data.** All torus knots have zero hyperbolic volume
($\mathrm{Vol} = 0$), so their bare mass vanishes.  Mass arises
entirely from crossing energy $\mathbf{E}_{\times}(q) =
\tfrac{1}{2}(q - q^{-1})$ at each self-crossing and from Hopf
linking.  The figure-eight knot ($4_1$) is the unique amphichiral
knot driving the mass mechanism, with
$\mathrm{Vol}(4_1) = 2.0299$.  Jones polynomial values at
$q = q_0 \approx 1.1097$ are listed for the building-block knots
([building-block knots](#rem:building-block-knots)).

In a bundle initial condition $\mathcal{S}_0$, each entry $(p_i, K_i)$
is one row of this dictionary placed at a specific point on
$\mathbb{P}(V)$.
