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

| Knot type | Symbol | Particle | Crossing number | Role in bundle |
|-----------|--------|----------|-----------------|----------------|
| Point (empty) | $\varnothing$ | Photon | $0$ | Background flux on $\mathcal{S}_p$ |
| Unknot | $\mathcal{O}$ ($0_1$) | Neutrino | $0$ | Trivial braiding; vacuum drag |
| Trefoil | $3_1$ | Electron | $3$ | Simplest stable vortex (gen. 1) |
| Figure-eight | $4_1$ | Muon | $4$ | Hyperbolic volume residue (gen. 2) |
| Cinquefoil | $5_1$ | Tau | $5$ | Higher-genus lift (gen. 3) |
| Three-twist | $5_2$ | Strange quark | $5$ | Quark sector, distinct volume |
| Torus$(7,2)$ | $7_1$ | Charm quark | $7$ | Heavy quark sector |

A hadron ([Definition](#def:hadron)) is then a composite:

- **Proton**: $(p, 3_1) \otimes (p, 3_1) \otimes (p, 5_2)$
  bound by $\mathcal{L}_{\mathrm{Hopf}}$ (two up-quarks + one down-quark
  in the knot picture: trefoil $\leftrightarrow$ up, three-twist
  $\leftrightarrow$ down).
- **Neutron**: $(p, 3_1) \otimes (p, 5_2) \otimes (p, 5_2)$
  bound by $\mathcal{L}_{\mathrm{Hopf}}$ (one up + two down).

The mass of each hadron is determined by the terminal resolution
([terminal resolution](#prop:terminal-resolution)) and matches CODATA values to
sub-keV precision.

In a bundle initial condition $\mathcal{S}_0$, each entry $(p_i, K_i)$ is one row
of this dictionary placed at a specific point on $\mathbb{P}(V)$.
