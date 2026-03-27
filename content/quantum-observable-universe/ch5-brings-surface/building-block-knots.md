Every particle in the Descartes universe is built from knots and
links embeddable on the genus-$4$ Bring surface.  This remark
collects the complete set of building blocks: their classical
knot names, visual conventions, Jones polynomials, hyperbolic
volumes, and the energy (mass) each contributes.

## Visual convention

- **Solid** (filled ●) = particle (positive time orientation)
- **Outlined** (hollow ○) = antiparticle (negative time / mirror)
- **Dashed** (⊙) = neutral antiparticle (amphichiral mirror)

The mirror operation $\sigma$ reverses all crossings:
$\sigma_i \mapsto \sigma_i^{-1}$.  For chiral knots this
produces a distinct knot type; for amphichiral knots
($0_1$, $4_1$) it returns the same knot.

## Table 1: Fundamental knots (single-component, torus-embeddable)

| Knot | $T_{m,n}$ | AB index | Genus | Crossings | Visual | Particle | Jones $J(q)$ | Vol |
|------|-----------|----------|:-----:|:---------:|:------:|----------|-------------|:---:|
| Unknot | $T_{1,0}$ | $0_1$ | $0$ | $0$ | ○ | $\nu$ (neutrino) | $1$ | $0$ |
| Mirror unknot | $\overline{T_{1,0}}$ | $0_1$ | $0$ | $0$ | ⊙ | $\bar{\nu}$ (antineutrino) | $1$ | $0$ |
| Left trefoil | $T_{2,3}$ | $3_1$ | $1$ | $3$ | ● | $e^-$ (electron) / $u$ (up quark) | $-q^{-4} + q^{-3} + q^{-1}$ | $0$ |
| Right trefoil | $\overline{T_{2,3}}$ | $\overline{3_1}$ | $1$ | $3$ | ○ | $e^+$ (positron) / $d$ (down quark) | $-q^{4} + q^{3} + q$ | $0$ |
| Cinquefoil | $T_{2,5}$ | $5_1$ | $2$ | $5$ | ● | $b$ (bottom quark) | $-q^{-10} + q^{-9} - q^{-8} + q^{-7} + q^{-5}$ | $0$ |
| Mirror cinquefoil | $\overline{T_{2,5}}$ | $\overline{5_1}$ | $2$ | $5$ | ○ | $s$ (strange quark) | $-q^{10} + q^{9} - q^{8} + q^{7} + q^{5}$ | $0$ |
| Septafoil | $T_{2,7}$ | $7_1$ | $3$ | $7$ | ● | $c$ (charm quark) | $-q^{-18} + q^{-17} - q^{-16} + q^{-15} - q^{-14} + q^{-13} + q^{-11}$ | $0$ |
| Mirror septafoil | $\overline{T_{2,7}}$ | $\overline{7_1}$ | $3$ | $7$ | ○ | $\bar{c}$ (anticharm) | mirror of above | $0$ |
| $T_{2,9}$ | $T_{2,9}$ | $9_1$ | $4$ | $9$ | ● | (saturating) | $-q^{-28} + \cdots + q^{-19}$ | $0$ |
| $T_{3,4}$ | $T_{3,4}$ | $8_{19}$ | $3$ | $8$ | ● | $t$ (top quark) | $q^{-7} - q^{-6} + q^{-5} - 2q^{-4} + q^{-3} + q^{-1}$ | $0$ |
| $T_{3,5}$ | $T_{3,5}$ | $10_{124}$ | $4$ | $10$ | ● | (heavy sector) | (10-term polynomial) | $0$ |

**Key observation**: All torus knots have $\mathrm{Vol} = 0$.
They contribute no bare mass from hyperbolic volume.  Their
mass arises entirely from **crossing energy** at $q \neq 1$.

## Table 2: Derived knots (from Skein operations on generators)

| Knot | AB index | Source | Genus | Crossings | Visual | Particle | Vol |
|------|----------|--------|:-----:|:---------:|:------:|----------|:---:|
| Figure-eight | $4_1$ | $\sigma(T_{2,3} \bowtie T_{2,3})$ | $1$ | $4$ | ●=○ | $\mu^-$ (muon) | $2.0299$ |
| Three-twist | $5_2$ | $\sigma(T_{2,3})$ variant | $1$ | $5$ | ● | — | $2.8281$ |

The figure-eight knot $4_1$ is **amphichiral** (self-mirror),
so $\mu^- = \overline{\mu^-}$ as knot types.  The muon-antimuon
distinction is carried by orientation, like the neutrino.

## Table 3: Links (multi-component, for force carriers and composites)

| Link | AB index | Components | Visual | Role | Jones $J(q)$ | Vol |
|------|----------|:----------:|:------:|------|-------------|:---:|
| Hopf link | $L2a1$ | $2$ | ●●  | Strong force / boson | $-(q^{1/2} + q^{5/2})$ | $0$ |
| Borromean rings | $L6a4$ | $3$ | ●●● | Nucleon (baryon) | (6-term) | $7.3277$ |
| Solomon link | $L4a1$ | $2$ | ●● | (doubly-linked pair) | — | $\approx 6.45$ |
| Whitehead link | $L5a1$ | $2$ | ●● | — | — | $3.6639$ |

## Table 4: Antiparticle completion

Every particle has an antiparticle obtained by the mirror
operation $\sigma$.  For completeness:

| Particle | Knot | Antiparticle | Knot | Same type? |
|----------|------|-------------|------|:----------:|
| $\nu$ | $T_{1,0}$ | $\bar{\nu}$ | $\overline{T_{1,0}}$ | Yes (amphichiral) |
| $e^-$ | $T_{2,3}$ | $e^+$ | $\overline{T_{2,3}}$ | No (chiral) |
| $\mu^-$ | $4_1$ | $\mu^+$ | $\overline{4_1}$ | Yes (amphichiral) |
| $u$ | $T_{2,3}$ | $\bar{u}$ | $\overline{T_{2,3}}$ | No (chiral) |
| $d$ | $\overline{T_{2,3}}$ | $\bar{d}$ | $T_{2,3}$ | No (chiral) |
| $p$ | $\mathcal{B}_3(u,u,d)$ | $\bar{p}$ | $\sigma(\mathcal{B}_3(u,u,d))$ | No |
| $n$ | $\mathcal{B}_3(u,d,d)$ | $\bar{n}$ | $\sigma(\mathcal{B}_3(u,d,d))$ | No |

## Mass from knot energy

The mass of a knot $K$ is:

$$
  m(K) \;=\; \frac{\mathrm{Vol}(K)}{\hbar_q^2}
  \;+\; \sum_{\text{crossings}} E_{\times}(q)
$$

where $\hbar_q = 1 - q^{-1}$ and
$E_{\times}(q) = \tfrac{1}{2}(q - q^{-1})$ is the crossing
energy at each self-crossing.

- **Torus knots** ($\mathrm{Vol} = 0$): mass comes entirely
  from crossing energy.  The trefoil has 3 crossings, so
  $m_{e} = 3 \cdot E_{\times}(q) \cdot \mu_0$ where $\mu_0$ is
  the mass scale.
- **Hyperbolic knots** ($\mathrm{Vol} > 0$): mass has both
  a volume term and a crossing term.  The figure-eight has
  $\mathrm{Vol} = 2.0299$ and 4 crossings; its mass ratio
  $m_\mu / m_e = \mathrm{Vol}(4_1) / \hbar_q^2$ fixes $q = 1.110$.
- **Links** ($> 1$ component): the linking number contributes
  additional inter-component crossing energy (binding).

## Jones polynomial at $q = 1.110$

| Knot | $J(1.110)$ |
|------|:----------:|
| $0_1$ (unknot) | $1.0000$ |
| $3_1$ (trefoil) | $0.8168$ |
| $\overline{3_1}$ (mirror trefoil) | $3.5832$ |
| $4_1$ (figure-eight) | $0.7854$ |
| $5_1$ (cinquefoil) | $0.4854$ |
| $L2a1$ (Hopf link) | $-2.2662$ |

The Jones polynomial at $q = 1$ gives the number of
components: $J(1) = (-2)^{c-1}$ where $c$ is the
component count.  At $q = 1.110$, the polynomial
encodes the $q$-deformation of the knot's contribution
to the categorical action.
