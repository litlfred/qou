Every particle in the Descartes universe is built from knots and
links embeddable on the genus-$4$ Bring's surface.  This remark
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
  \mathfrak{m}(K) \;=\; \frac{\mathrm{Vol}(K)}{\hbar_q^2}
  \;+\; \sum_{\text{crossings}} \mathbf{E}_{\times}(q)

$$

where $\hbar_q = 1 - q^{-1}$ and
$\mathbf{E}_{\times}(q) = \tfrac{1}{2}(q - q^{-1})$ is the crossing
energy at each self-crossing.

- **Torus knots** ($\mathrm{Vol} = 0$): mass comes entirely
  from crossing energy.  The trefoil has 3 crossings, so
  $m_{e} = 3 \cdot \mathbf{E}_{\times}(q) \cdot \mu_0$ where $\mu_0$ is
  the mass scale.
- **Hyperbolic knots** ($\mathrm{Vol} > 0$): mass has both
  a volume term and a crossing term.  The figure-eight has
  $\mathrm{Vol} = 2.0299$ and 4 crossings; its mass ratio
  $m_\mu / m_e = \mathrm{Vol}(4_1) / \hbar_q^2$ fixes $q = q_0$.
- **Links** ($> 1$ component): the linking number contributes
  additional inter-component crossing energy (binding).

## Jones polynomial at $q = q_0$

| Knot | $J(q_0)$ |
|------|:----------:|
| $0_1$ (unknot) | $1.0000$ |
| $3_1$ (trefoil) | $0.8168$ |
| $\overline{3_1}$ (mirror trefoil) | $3.5832$ |
| $4_1$ (figure-eight) | $0.7854$ |
| $5_1$ (cinquefoil) | $0.4854$ |
| $L2a1$ (Hopf link) | $-2.2662$ |

The Jones polynomial at $q = 1$ gives the number of
components: $J(1) = (-2)^{c-1}$ where $c$ is the
component count.  At $q = q_0$, the polynomial
encodes the $q$-deformation of the knot's contribution
to the categorical action.

## Table 5: Categorical action at $q = q_0$

The categorical action $S_q(K) = \mathrm{tr}_\tau(\rho(\beta_K))$
decomposes into a hyperbolic volume term and a crossing energy
term.  For torus knots ($\mathrm{Vol} = 0$), the entire action
comes from crossings.  All quantities below are functions of
$q$ alone (plus one dimensional scale $\mu_0$ for mass).

**Fundamental constants from $q$:**

| Symbol | Formula | Value at $q = q_0$ |
|--------|---------|:--------------------:|
| $\hbar_q$ | $1 - q^{-1}$ | $0.09910$ |
| $\mathbf{E}_{\times}$ | $\tfrac{1}{2}(q - q^{-1})$ | $0.10450$ |
| $s$ (Skein amplitude) | $q^{1/2} - q^{-1/2}$ | $0.05049$ |
| $[2]_q$ | $q + q^{-1}$ | $2.01099$ |

**Categorical action per building block:**

| Particle | Knot | $n_c$ | $\mathrm{Vol}$ | $\mathbf{E}_{\mathrm{cross}}(q)$ | $S_q(K)$ | Mass ($\mu_0$ units) |
|----------|------|:-----:|:---------------:|:-----------------------:|:---------:|:--------------------:|
| $\nu$ | $0_1$ | $0$ | $0$ | $0$ | $0$ | $0$ |
| $e^-$ | $T_{2,3}$ | $3$ | $0$ | $3q = 3.330$ | $3\,\mathbf{E}_{\times}$ | $3\,\mathbf{E}_{\times}\,\mu_0$ |
| $e^+$ | $\overline{T_{2,3}}$ | $3$ | $0$ | $3q^{-1} = 2.703$ | $3\,\mathbf{E}_{\times}$ | $3\,\mathbf{E}_{\times}\,\mu_0$ |
| $\mu^-$ | $4_1$ | $4$ | $2.0299$ | $4\,\mathbf{E}_{\times}$ | $\mathrm{Vol}/\hbar_q^2 + 4\,\mathbf{E}_{\times}$ | $207.1\,\mu_0$ |
| $u,\,d$ (quarks) | $T_{2,3}$ | $3$ | $0$ | $3q$ | $3\,\mathbf{E}_{\times}$ | (bound; see below) |
| $b$ | $T_{2,5}$ | $5$ | $0$ | $5q = 5.550$ | $5\,\mathbf{E}_{\times}$ | $5\,\mathbf{E}_{\times}\,\mu_0$ |
| $t$ | $T_{3,4}$ | $8$ | $0$ | $8q = 8.880$ | $8\,\mathbf{E}_{\times}$ | $8\,\mathbf{E}_{\times}\,\mu_0$ |
| Proton $\mathfrak{p}$ | $\mathcal{B}_3(u,u,d) \bowtie \mathcal{L}_H$ | — | $7.328$ | (internal) | $\mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2$ | $746\,\mu_0$ |
| Neutron $\mathfrak{n}$ | $\mathcal{B}_3(u,d,d) \bowtie \mathcal{L}_H$ | — | $7.328$ | (internal) | $\mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2 + \delta_{\mathrm{Skein}}$ | $747\,\mu_0$ |

The neutron--proton mass difference $\delta_{\mathrm{Skein}} =
\mathcal{S}_{\mathfrak{d}\mathfrak{d}}(q) - \mathcal{S}_{\mathfrak{u}\mathfrak{u}}(q) \approx 1.293$ MeV
arises from the pair Skein asymmetry between $\mathfrak{d}\mathfrak{d}$ and $\mathfrak{u}\mathfrak{u}$
crossings — a pure function of $q$.

**Key consequence for beta decay.**  The electron's categorical
action $S_q(e) = 3\,\mathbf{E}_{\times}(q) \cdot \mu_0$, the neutrino's
$S_q(\nu) = 0$, and the nuclear actions $S_q(\mathcal{N})$
from the Markov trace product are all computable from $q$.
The $\mathcal{Q}_q$-value
([transition energy](#def:q-value-transition))
$\mathcal{Q}_q = S_q(\mathrm{par}) - S_q(\mathrm{dau}) - S_q(e)$
therefore depends on $q$ and $\mu_0$ alone — no external
constants.
