Three operations build every particle from the seven torus knot
generators: **Hopf linking** ($\bowtie$), **Skein crossing change**
($\sigma$), and **color-tube linking** ($[\cdot]_c$).  This
appendix table records the result of each operation applied to
pairs of building block knots.

## Table 1: Hopf linking $K_1 \bowtie K_2$

The Hopf link $\mathcal{L}_H$ joins two knots into a
two-component link.  The linking number is always $\pm 1$.

| $K_1$ | $K_2$ | $K_1 \bowtie K_2$ | Components | Physical role |
|-------|-------|--------------------|:----------:|---------------|
| $T_{2,3}$ | $T_{2,3}$ | $T_{2,3} \bowtie T_{2,3}$ | $2$ | $uu$ pair (Hopf-linked quarks) |
| $T_{2,3}$ | $\overline{T_{2,3}}$ | $T_{2,3} \bowtie \overline{T_{2,3}}$ | $2$ | $u\bar{d}$ = $\pi^+$ (pion) |
| $\overline{T_{2,3}}$ | $\overline{T_{2,3}}$ | $\overline{T_{2,3}} \bowtie \overline{T_{2,3}}$ | $2$ | $dd$ pair |
| $T_{2,3}$ | $T_{1,0}$ | $T_{2,3} \bowtie T_{1,0}$ | $2$ | $e\nu$ pair |
| $T_{1,0}$ | $T_{1,0}$ | $\mathcal{L}_H$ | $2$ | Hopf link (pure) |
| $T_{2,3}$ | $T_{2,5}$ | $T_{2,3} \bowtie T_{2,5}$ | $2$ | $ub$ pair |
| $T_{2,3}$ | $\overline{T_{2,5}}$ | $T_{2,3} \bowtie \overline{T_{2,5}}$ | $2$ | $u\bar{s}$ = $K^+$ (kaon) |
| $\mathfrak{p}$ | $\mathfrak{n}$ | $\mathfrak{p} \bowtie \mathfrak{n}$ | $6$ | Deuteron |
| $\mathfrak{p}$ | $\mathfrak{p}$ | $\mathfrak{p} \bowtie \mathfrak{p}$ | $6$ | Diproton (unstable) |
| $\mathfrak{n}$ | $\mathfrak{n}$ | $\mathfrak{n} \bowtie \mathfrak{n}$ | $6$ | Dineutron (unstable) |

## Table 2: Skein crossing change $\sigma(K)$ — mirror and transmutation

The Skein crossing change reverses one crossing.  Applied globally
($\sigma$ = mirror), it maps particle to antiparticle.  Applied
locally (at one crossing), it transmutes quark flavour.

| Input | Operation | Output | Physical meaning |
|-------|-----------|--------|-----------------|
| $T_{2,3}$ ($e^-$, $u$) | Global mirror $\sigma$ | $\overline{T_{2,3}}$ ($e^+$, $d$) | Particle → antiparticle |
| $T_{2,5}$ ($b$) | Global mirror $\sigma$ | $\overline{T_{2,5}}$ ($s$) | Bottom → strange |
| $T_{2,7}$ ($c$) | Global mirror $\sigma$ | $\overline{T_{2,7}}$ ($\bar{c}$) | Charm → anticharm |
| $T_{1,0}$ ($\nu$) | Global mirror $\sigma$ | $\overline{T_{1,0}}$ ($\bar{\nu}$) | Neutrino → antineutrino |
| $4_1$ ($\mu$) | Global mirror $\sigma$ | $4_1$ ($\mu$) | Self-mirror (amphichiral) |
| $\mathfrak{n}$ = $[u,d,d]_c$ | Local $\sigma$ at one $d$ | $\mathfrak{p}$ = $[u,u,d]_c$ | Beta decay ($n \to p$) |
| $T_{2,3} \bowtie T_{2,3}$ | Skein at crossing | $4_1$ | $uu$ Hopf → figure-eight (muon) |

## Table 3: Color-tube linking $[K_1, K_2, K_3]_c$ — Borromean construction

Three knots threaded through the three color tubes of the Bring
surface form a Borromean-linked baryon.

| $K_1$ | $K_2$ | $K_3$ | Result | Physical baryon |
|-------|-------|-------|--------|----------------|
| $T_{2,3}$ | $T_{2,3}$ | $\overline{T_{2,3}}$ | $\mathcal{B}_3(u,u,d)$ | Proton $\mathfrak{p}$ |
| $T_{2,3}$ | $\overline{T_{2,3}}$ | $\overline{T_{2,3}}$ | $\mathcal{B}_3(u,d,d)$ | Neutron $\mathfrak{n}$ |
| $T_{2,3}$ | $\overline{T_{2,3}}$ | $\overline{T_{2,5}}$ | $\mathcal{B}_3(u,d,s)$ | Lambda $\Lambda$ |
| $T_{2,3}$ | $T_{2,3}$ | $\overline{T_{2,5}}$ | $\mathcal{B}_3(u,u,s)$ | Sigma$^+$ $\Sigma^+$ |
| $\overline{T_{2,3}}$ | $\overline{T_{2,3}}$ | $\overline{T_{2,5}}$ | $\mathcal{B}_3(d,d,s)$ | Sigma$^-$ $\Sigma^-$ |
| $\overline{T_{2,5}}$ | $\overline{T_{2,5}}$ | $T_{2,3}$ | $\mathcal{B}_3(s,s,u)$ | Xi$^0$ $\Xi^0$ |
| $\overline{T_{2,5}}$ | $\overline{T_{2,5}}$ | $\overline{T_{2,3}}$ | $\mathcal{B}_3(s,s,d)$ | Xi$^-$ $\Xi^-$ |
| $\overline{T_{2,5}}$ | $\overline{T_{2,5}}$ | $\overline{T_{2,5}}$ | $\mathcal{B}_3(s,s,s)$ | Omega$^-$ $\Omega^-$ |

## Table 4: Connected sum $K_1 \# K_2$ — genus-additive composition

The connected sum joins knots end-to-end.  Seifert genus is
additive: $g(K_1 \# K_2) = g(K_1) + g(K_2)$.  This operation
does NOT produce a physical composite (unlike Hopf linking); it is
a mathematical operation that arises in the Skein resolution tree.

| $K_1$ | $K_2$ | $K_1 \# K_2$ | Genus | Vol |
|-------|-------|--------------|:-----:|:---:|
| $3_1$ | $3_1$ | Granny knot | $2$ | $0$ |
| $3_1$ | $\overline{3_1}$ | Square knot | $2$ | $0$ |
| $3_1$ | $4_1$ | $3_1 \# 4_1$ | $2$ | $2.0299$ |
| $4_1$ | $4_1$ | $4_1 \# 4_1$ | $2$ | $4.0598$ |

**Volume additivity**: $\mathrm{Vol}(K_1 \# K_2) = \mathrm{Vol}(K_1) + \mathrm{Vol}(K_2)$
(JSJ decomposition — each knot contributes its hyperbolic piece).

## Table 5: $L_0$ smoothing — beta decay emission products

The $L_0$ smoothing at a crossing in a braid word replaces the
crossing with parallel strands, splitting one component into two.

| Parent crossing | $L_0$ product | Physical decay |
|----------------|---------------|----------------|
| $d \to u$ in $\mathfrak{n}$ | $T_{2,3} \sqcup \overline{T_{1,0}}$ | $e^- + \bar{\nu}_e$ ($\beta^-$) |
| $u \to d$ in $\mathfrak{p}$ | $\overline{T_{2,3}} \sqcup T_{1,0}$ | $e^+ + \nu_e$ ($\beta^+$) |
| $s \to u$ in $\Lambda$ | $T_{2,3} \sqcup \overline{T_{1,0}}$ | $e^- + \bar{\nu}_e$ (weak decay) |

In each case the $L_0$ smoothing produces exactly one charged
lepton (trefoil or mirror trefoil) and one (anti)neutrino
(unknot or mirror unknot).  Lepton number is conserved by
construction.
