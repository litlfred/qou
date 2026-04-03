The localized knot framework ([Definition](#def:localized-knot)) assigns
a topological identity to each fundamental particle.  This dictionary is
*derived* from the categorical braiding on $V = V_{1/2}$, not postulated:
the $R$-matrix of $\mathcal{U}_q(\mathfrak{su}(2))$ endows
$V^{\otimes n}$ with a faithful $B_n$-action
([Proposition](#prop:braid-action-tensor)), and
$q$-Schur--Weyl duality
([Theorem](#thm:knot-eigenbasis-complete)) decomposes
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

**Quarks and hadrons (Borromean picture).** The original dictionary
assigned individual knot types to quarks (three-twist $5_2$ for strange,
torus $7_1$ for charm, etc.).  The revised picture
([Conjecture](#conj:borromean-quark)) identifies quarks not as
fundamental knots but as **unknots (neutrinos) Borromean-linked in the
exceptional divisor** of Bring's surface.  A baryon is the Borromean
link $\mathcal{B}_3(\nu_r, \nu_g, \nu_b)$ bound by the Hopf link
$\mathcal{L}_H$ ([Definition](#def:borromean-baryon)):

- **Proton**: $\mathcal{B}_3(\nu_r, \nu_g, \nu_b) \bowtie \mathcal{L}_H$
  with the $2 + 1$ crossing-orientation partition (two up + one down).
- **Neutron**: $\mathcal{B}_3(\nu_r, \nu_g, \nu_b) \bowtie \mathcal{L}_H$
  with the $1 + 2$ partition (one up + two down).

Up/down flavour arises from the **crossing orientation** of each unknot
within $\mathcal{B}_3$, not from distinct knot types.  The baryon mass
comes almost entirely from the Borromean linking volume
$\mathrm{Vol}(S^3 \setminus \mathcal{B}_3) = 7.328\ldots$, matching
the QCD result that ${\sim}99\%$ of proton mass is binding energy.

The mass of each hadron is determined by the terminal resolution
([terminal resolution](#prop:terminal-resolution)) and matches CODATA values to
sub-keV precision.

In a bundle initial condition $\mathcal{S}_0$, each entry $(p_i, K_i)$ is one row
of this dictionary placed at a specific point on $\mathbb{P}(V)$.
