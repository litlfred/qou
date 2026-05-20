Three operations build every particle from the seven torus knot
generators: **Hopf linking** ($\oplus$), **Skein crossing change**
($\sigma$), and **color-tube linking** ($[\cdot]_p$).  This
appendix table records the result of each operation applied to
pairs of building block knots.

## Table 1: Hopf linking $K_1 \oplus K_2$

The Hopf link $\mathcal{L}_H$ joins two knots into a
two-component link.  The linking number is always $\pm 1$.

| $K_1$ | $K_2$ | $K_1 \oplus K_2$ | Components | Physical role |
|-------|-------|--------------------|:----------:|---------------|
| $T_{2,3}$ | $T_{2,3}$ | $T_{2,3} \oplus T_{2,3}$ | $2$ | $\mathfrak{u}\mathfrak{u}$ pair (Hopf-linked quarks) |
| $T_{2,3}$ | $T_{2,3}^{\sigma}$ | $T_{2,3} \oplus T_{2,3}^{\sigma}$ | $2$ | $\mathfrak{u}\mathfrak{d}^{\sigma}$ = $\pi^+$ (pion) |
| $T_{2,3}^{\sigma}$ | $T_{2,3}^{\sigma}$ | $T_{2,3}^{\sigma} \oplus T_{2,3}^{\sigma}$ | $2$ | $\mathfrak{d}\mathfrak{d}$ pair |
| $T_{2,3}$ | $T_{1,0}$ | $T_{2,3} \oplus T_{1,0}$ | $2$ | $e\nu$ pair |
| $T_{1,0}$ | $T_{1,0}$ | $\mathcal{L}_H$ | $2$ | Hopf link (pure) |
| $T_{2,3}$ | $T_{2,5}$ | $T_{2,3} \oplus T_{2,5}$ | $2$ | $\mathfrak{u}\mathfrak{b}$ pair |
| $T_{2,3}$ | $T_{2,5}^{\sigma}$ | $T_{2,3} \oplus T_{2,5}^{\sigma}$ | $2$ | $\mathfrak{u}\mathfrak{s}^{\sigma}$ = $K^+$ (kaon) |
| $\mathfrak{p}$ | $\mathfrak{n}$ | $\mathfrak{p} \oplus \mathfrak{n}$ | $6$ | Deuteron |
| $\mathfrak{p}$ | $\mathfrak{p}$ | $\mathfrak{p} \oplus \mathfrak{p}$ | $6$ | Diproton (unstable) |
| $\mathfrak{n}$ | $\mathfrak{n}$ | $\mathfrak{n} \oplus \mathfrak{n}$ | $6$ | Dineutron (unstable) |

## Table 2: Skein crossing change $K^{\sigma}$ — mirror and transmutation

The Skein crossing change reverses one crossing.  Applied globally
($\sigma$ = mirror), it maps particle to antiparticle.  Applied
locally (at one crossing), it transmutes quark flavour.

| Input | Operation | Output | Physical meaning |
|-------|-----------|--------|-----------------|
| $T_{2,3}$ ($e^-$, $u$) | Global mirror $\sigma$ | $T_{2,3}^{\sigma}$ ($e^+$, $d$) | Particle → antiparticle |
| $T_{2,5}$ ($\mu$, $b$) | Global mirror $\sigma$ | $T_{2,5}^{\sigma}$ ($\mu^+$, $s$) | Muon/bottom → antimuon/strange |
| $T_{2,7}$ ($\tau$, $c$) | Global mirror $\sigma$ | $T_{2,7}^{\sigma}$ ($\tau^+$, $c^{\sigma}$) | Tau/charm → antitau/anticharm |
| $T_{1,0}$ ($\nu$) | Global mirror $\sigma$ | $T_{1,0}^{\sigma}$ ($\nu^{\sigma}$) | Neutrino → antineutrino |
| $4_1$ ($H$) | Global mirror $\sigma$ | $4_1$ ($H$) | Self-mirror (amphichiral Higgs) |
| $\mathfrak{n}$ = $[u,d,d]_p$ | Local $\sigma$ at one $d$ | $\mathfrak{p}$ = $[u,u,d]_p$ | Beta decay ($n \to p$) |
| $T_{2,3} \oplus T_{2,3}$ | Skein at crossing | $4_1$ | $\mathfrak{u}\mathfrak{u}$ Hopf → figure-eight (Higgs) |

## Table 3: Color-tube linking $[K_1, K_2, K_3]_p$ — Borromean construction

Three knots threaded through the three coral tubes of the Bring
surface form a Borromean-linked baryon.

| $K_1$ | $K_2$ | $K_3$ | Result | Physical baryon |
|-------|-------|-------|--------|----------------|
| $T_{2,3}$ | $T_{2,3}$ | $T_{2,3}^{\sigma}$ | $\mathcal{B}_3(u,u,d)$ | Proton $\mathfrak{p}$ |
| $T_{2,3}$ | $T_{2,3}^{\sigma}$ | $T_{2,3}^{\sigma}$ | $\mathcal{B}_3(u,d,d)$ | Neutron $\mathfrak{n}$ |
| $T_{2,3}$ | $T_{2,3}^{\sigma}$ | $T_{2,5}^{\sigma}$ | $\mathcal{B}_3(u,d,s)$ | Lambda $\Lambda$ |
| $T_{2,3}$ | $T_{2,3}$ | $T_{2,5}^{\sigma}$ | $\mathcal{B}_3(u,u,s)$ | Sigma$^+$ $\Sigma^+$ |
| $T_{2,3}^{\sigma}$ | $T_{2,3}^{\sigma}$ | $T_{2,5}^{\sigma}$ | $\mathcal{B}_3(d,d,s)$ | Sigma$^-$ $\Sigma^-$ |
| $T_{2,5}^{\sigma}$ | $T_{2,5}^{\sigma}$ | $T_{2,3}$ | $\mathcal{B}_3(s,s,u)$ | Xi$^0$ $\Xi^0$ |
| $T_{2,5}^{\sigma}$ | $T_{2,5}^{\sigma}$ | $T_{2,3}^{\sigma}$ | $\mathcal{B}_3(s,s,d)$ | Xi$^-$ $\Xi^-$ |
| $T_{2,5}^{\sigma}$ | $T_{2,5}^{\sigma}$ | $T_{2,5}^{\sigma}$ | $\mathcal{B}_3(s,s,s)$ | Omega$^-$ $\Omega^-$ |

## Table 4: Connected sum $K_1 \# K_2$ — genus-additive composition

The connected sum joins knots end-to-end.  Seifert genus is
additive: $g(K_1 \# K_2) = g(K_1) + g(K_2)$.  This operation
does NOT produce a physical composite (unlike Hopf linking); it is
a mathematical operation that arises in the Skein resolution tree.

| $K_1$ | $K_2$ | $K_1 \# K_2$ | Genus | Vol |
|-------|-------|--------------|:-----:|:---:|
| $3_1$ | $3_1$ | Granny knot | $2$ | $0$ |
| $3_1$ | $3_1^{\sigma}$ | Square knot | $2$ | $0$ |
| $3_1$ | $4_1$ | $3_1 \# 4_1$ | $2$ | $2.0299$ |
| $4_1$ | $4_1$ | $4_1 \# 4_1$ | $2$ | $4.0598$ |

**Volume additivity**: $\mathrm{Vol}(K_1 \# K_2) = \mathrm{Vol}(K_1) + \mathrm{Vol}(K_2)$
(JSJ decomposition — each knot contributes its hyperbolic piece).

## Table 5: $L_0^{\pm}$ smoothing — beta decay emission products

The $L_0^{\pm}$ smoothing at a crossing in a braid word replaces
the crossing with parallel strands, splitting one component into
two.  The sign on $L_0$ matches the decay type ($\beta^{\pm}$).

| Parent crossing | Smoothing | Products | Decay |
|----------------|-----------|----------|-------|
| $\mathfrak{d} \to \mathfrak{u}$ in $\mathfrak{n}$ | $L_0^{-}$ | $T_{2,3} \sqcup T_{1,0}^{\sigma}$ | $e^- + \nu_e^{\sigma}$ ($\beta^-$) |
| $\mathfrak{u} \to \mathfrak{d}$ in $\mathfrak{p}$ | $L_0^{+}$ | $T_{2,3}^{\sigma} \sqcup T_{1,0}$ | $e^+ + \nu_e$ ($\beta^+$) |
| $\mathfrak{s} \to \mathfrak{u}$ in $\Lambda$ | $L_0^{-}$ | $T_{2,3} \sqcup T_{1,0}^{\sigma}$ | $e^- + \nu_e^{\sigma}$ (weak) |

In each case the $L_0^{\pm}$ smoothing produces exactly one
charged lepton (trefoil or mirror trefoil) and one (anti)neutrino
(unknot or mirror unknot).  Lepton number is conserved by
construction.
