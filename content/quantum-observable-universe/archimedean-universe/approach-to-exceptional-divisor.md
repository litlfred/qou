## Approach: from base $M$ to fibre $\mathcal{S}_p$

In the QOU archimedean tuple $(\mathbf{C}, \varTheta, G, \mathcal{S})$
the base manifold $M$ carries the smooth metric in which two
free vortices propagate. As the vortex cores approach a brane
point $p \in M$, the smooth metric becomes degenerate: the
base coordinate ratio $z = \sqrt{q} - 1/\sqrt{q}$ drives the
exceptional divisor $\mathcal{S}_p$
([state bundle fibre](#def:exceptional-divisor)) into the
foreground.  *"Below Planck scale"* in QOU is therefore not a
metric statement (there is no metric below Planck) but a
**categorical** one: the relevant geometry has switched from the
base $M$ to the fibre $\mathcal{S}_p$, and morphisms in
$\mathcal{S}_p$ are knot operators
([knot-operator energy](#def:knot-operator-energy)).

Concretely, the encounter has three moments:

1. **Approach.**  Two vortex tubes propagate on $M$ and approach
   a common brane point $p$.  The Reeb flow on $M$ does the
   accounting; nothing new is needed.

2. **Crossing onto the fibre.**  At the threshold where
   $\partial F / \partial \mathbf{c} = 0$ on the colour-tube
   cubic ([Picard--Lefschetz thimble](#rem:picard-lefschetz-thimble)
   §setup), the base coordinate $z$ hits a discriminant zero,
   the smooth base structure pinches, and the operative
   morphisms are now those of $\mathcal{S}_p$ — the
   $\Phi_q$-piece $K_S$
   ([$\Phi_q$-piece](#def:phi-q-piece)).

3. **Merging of fundamental groups.**  The two vortex cores
   become parallel strands in a single braid.  Their previously
   independent fundamental groups
   $\pi_1(\nu_1)$, $\pi_1(\nu_2)$ amalgamate into the
   fundamental group $\pi_1(U \setminus K)$ of the merged knot
   complement, where $U$ is a tubular neighbourhood of $p$ and
   $K$ is the link formed by the two strands inside it.

After moment (3) the encounter is a knot-theoretic question, not
a metric one.  The remaining sections of this chapter trace what
happens next: the merged complement admits a hyperbolic
structure ([Thurston relaxation](#sec:thurston-relaxation)), the
SDP/LP machinery of [Chapter 12](#chap:particle-interactions)
selects the lowest-energy link representative
([SDP as thimble flow](#rem:sdp-as-thimble-flow)), and Mostow
rigidity ([geometric confinement](#prop:mostow-confinement))
makes the resulting topology --- and hence the mass --- discrete.
