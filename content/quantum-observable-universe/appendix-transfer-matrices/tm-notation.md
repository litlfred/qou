This appendix is **self-contained**.  Every transfer matrix in the
paper is listed here in explicit closed form, with all notation
defined locally.  No prior reading is required.

## Symbols

| Symbol | Name | Definition |
|--------|------|------------|
| $q$ | Substrate parameter | A real number $q > 1$ (the single free parameter of the theory) |
| $s$ | Skein amplitude | $s = q^{1/2} - q^{-1/2}$ |
| $z$ | Markov parameter | $z(q) = \dfrac{1}{q^{1/2} + q^{-1/2}}$ |
| $\sigma_i$ | Braid / Hecke generator | Generator of the braid group $B_n$ and its image in $H_n(q)$ (same symbol); in the latter satisfies the Hecke relation $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ |
| $J_K(q)$ | Jones polynomial | Knot invariant of knot $K$, polynomial in $q^{\pm 1}$ |
| $\mathrm{M}_2(R)$ | $2 \times 2$ matrices | Over ring $R = \mathbb{Z}[q^{\pm 1/2}]$ |
| $\mathbb{I}$ | Identity matrix | $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ |

## Knot dictionary

Every transfer matrix is labelled by a **pair of knots** $(K_1, K_2)$
meeting at a crossing.  The knots relevant to this paper are:

| Knot | Notation | Classical name | Crossings | Jones polynomial $J_K(q)$ |
|------|----------|---------------|:---------:|--------------------------|
| Unknot | $T_{1,0}$ | $0_1$ | $0$ | $1$ |
| Left trefoil | $T_{2,3}$ | $3_1$ | $3$ | $-q^{-4} + q^{-3} + q^{-1}$ |
| Right trefoil | $T_{2,3}^{\sigma}$ | $3_1^{\sigma}$ | $3$ | $-q^{4} + q^{3} + q$ |
| Figure-eight | $4_1$ | $4_1$ | $4$ | $q^2 - q + 1 - q^{-1} + q^{-2}$ |
| Cinquefoil | $T_{2,5}$ | $5_1$ | $5$ | $-q^{-10} + q^{-9} - q^{-8} + q^{-7} + q^{-5}$ |
| Septafoil | $T_{2,7}$ | $7_1$ | $7$ | $-q^{-18} + q^{-17} - q^{-16} + q^{-15} - q^{-14} + q^{-13} + q^{-11}$ |
| $T_{3,4}$ knot | $T_{3,4}$ | $8_{19}$ | $8$ | $q^{-7} - q^{-6} + q^{-5} - 2q^{-4} + q^{-3} + q^{-1}$ |
| $T_{3,5}$ knot | $T_{3,5}$ | $10_{124}$ | $10$ | (10-term polynomial; see body text) |

## Particle assignments

| Particle | Knot | Antiparticle | Knot |
|----------|------|-------------|------|
| Neutrino $\nu$ | $T_{1,0}$ | $\nu^{\sigma}$ | $T_{1,0}^{\sigma} = T_{1,0}$ |
| Electron $e^-$ | $T_{2,3}$ | Positron $e^+$ | $T_{2,3}^{\sigma}$ |
| Up quark $\mathfrak{u}$ | $T_{2,3}$ | $\mathfrak{u}^{\sigma}$ | $T_{2,3}^{\sigma}$ |
| Down quark $\mathfrak{d}$ | $T_{2,3}^{\sigma}$ | $\mathfrak{d}^{\sigma}$ | $T_{2,3}$ |
| Bottom quark $\mathfrak{b}$ | $T_{2,5}$ | $\mathfrak{b}^{\sigma}$ | $T_{2,5}^{\sigma}$ |
| Strange quark $\mathfrak{s}$ | $T_{2,5}^{\sigma}$ | $\mathfrak{s}^{\sigma}$ | $T_{2,5}$ |
| Charm quark $\mathfrak{c}$ | $T_{2,7}$ | $\mathfrak{c}^{\sigma}$ | $T_{2,7}^{\sigma}$ |
| $T_{3,4}$ (Hopf${}^2$ binding) | $T_{3,4}$ | (self-conjugate in $H^{0,1}$) | $T_{3,4}^{\sigma}$ |

## Nucleons

| Nucleon | Composition | Crossing types with a partner $\mathfrak{p}$ or $\mathfrak{n}$ |
|---------|------------|---------------------------------------------------------------|
| Proton $\mathfrak{p}$ | $[\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]$ | $\mathfrak{p}$-$\mathfrak{p}$: both up-type |
| Neutron $\mathfrak{n}$ | $[\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]$ | $\mathfrak{n}$-$\mathfrak{n}$: both down-type |
| Mixed | (one of each) | $\mathfrak{p}$-$\mathfrak{n}$: up meets down |

## How transfer matrices are used

Given a nucleus with $A = Z + N$ nucleons, the braid word has
$A - 1$ generators $\sigma_0, \ldots, \sigma_{A-2}$.  At each
generator $\sigma_i$, the transfer matrices of all crossings
are composed as operators acting by left-multiplication,
with crossings applied from right to left in the braid word:

$$
  M_i(q) =  \prod_{j=A-1}^{i+1} T_{K_j, K_i}(q)
$$

where the product is taken in decreasing order of $j$.

The **Markov-traced volume** at generator $\sigma_i$ is:

$$
  \hat{V}_i(q) =  z(q) \cdot (M_i)_{11} + (M_i)_{21}
$$

The **nuclear Skein polynomial** is:

$$
  P_{\mathcal{N}}(q) =  \prod_{i=0}^{A-2} \hat{V}_i(q)
$$

This requires exactly $\binom{A}{2}$ transfer matrix
multiplications (one per nucleon pair).
