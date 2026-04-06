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
closure of a braid $\beta \in B_n$, so the Markov trace on the Hecke
algebra $H_n(q)$ identifies each irreducible summand with a knot type.
The resulting dictionary is:

| Knot type | Symbol | Particle / field | Crossing number | Role in bundle |
|-----------|--------|------------------|-----------------|----------------|
| Point (empty) | $\varnothing$ | Photon | $0$ | Background flux on $\mathcal{S}_p$ |
| Unknot | $\mathcal{O}$ ($0_1$) | Neutrino | $0$ | Trivial braiding; vacuum drag |
| Trefoil | $T_{2,3}$ ($3_1$) | Electron | $3$ | Simplest stable vortex (gen. 1) |
| Figure-eight | $4_1$ | Higgs field | $4$ | Mass mechanism; $\mathrm{Vol}(4_1)/\hbar_q^2$ couples universally |
| Cinquefoil | $T_{2,5}$ ($5_1$) | Muon | $5$ | Gen. 2 lepton on Reeb divisor |
| Septafoil | $T_{2,7}$ ($7_1$) | Tau | $7$ | Gen. 3 lepton on Reeb divisor |

In a bundle initial condition $\mathcal{S}_0$, each entry $(p_i, K_i)$ is one row
of this dictionary placed at a specific point on $\mathbb{P}(V)$.
