We compute the topological mass
([mass formula](#prop:topological-mass-formula)) for two specific
knots: the trefoil $\tau(2,3)$ and the figure-eight knot $4_1$.

**Trefoil knot $\tau(2,3)$ — the electron.**
The trefoil is a torus knot, so its complement in $S^3$ admits a
Seifert fibration and is *not* hyperbolic.  Its hyperbolic volume
is $\mathrm{Vol}(S^3 \setminus \tau(2,3)) = 0$.  Therefore the
mass formula does not use the volume directly; instead, the
quantum dilogarithm provides the analytic continuation:

$$
  \mathfrak{m}(\tau(2,3))
  = 
  \frac{\mathrm{Li}_2(q^{-2})}{\hbar_q^{2}},
$$

where $\mathrm{Li}_2$ is the quantum dilogarithm and
$\hbar_q = (q - 1)/q$ is the quantum Planck constant
([mass identity](#def:mass-identity)).  The quantum dilogarithm
interpolates between the classical volume (for hyperbolic knots)
and the Chern--Simons invariant (for non-hyperbolic knots such as
torus knots).  Evaluating at the substrate parameter
$q \approx 1.110$:

$$
  \hbar_q  \approx  \frac{0.110}{1.110}  \approx  0.0990.
$$

**Figure-eight knot $4_1$ — the Higgs field (mass mechanism).**
The figure-eight knot *is* hyperbolic, with complement volume

$$
  \mathrm{Vol}(S^3 \setminus 4_1)  \approx  2.0299.
$$

By the mass formula, the topological mass associated with $4_1$ is

$$
  \mathfrak{m}(4_1)
  = 
  \frac{\mathrm{Vol}(S^3 \setminus 4_1)}{\hbar_q^{2}}
   \approx 
  \frac{2.0299}{(0.0990)^2}
   \approx 
  \frac{2.0299}{0.00980}
   \approx  207.1.
$$

**Physical interpretation.**
The figure-eight knot $4_1$ is the Higgs field
([cohomological embedding](#prop:cohomological-embedding)).
It is the unique amphichiral knot in $H^{0,1}(\Sigma_4)$, and
its hyperbolic volume drives the mass mechanism.  The muon
($T_{2,5}$, cinquefoil) acquires its mass through the Higgs
field ($4_1$), which universally couples to all knot-particles
with crossings $> 0$.  The dimensionless mass of $4_1$ is

$$
  \mathfrak{m}(4_1)
  = 
  \frac{\mathrm{Vol}(4_1)}{\hbar_q^2}
  \approx 207.1,
$$

which matches the muon-to-electron mass ratio
$\mathfrak{m}_\mu / \mathfrak{m}_e \approx :val[m_mu_over_e]{precision=6}$ to within $0.2\%$
(the electron mass $\mathfrak{m}_e = 1$ is the dimensionless unit).
The correspondence

$$
  \tau(2,3) \longleftrightarrow e^-
  \qquad\text{and}\qquad
  4_1 \longleftrightarrow H \text{ (Higgs field)}
$$

is determined entirely by the knot topology — no free parameters
beyond the single substrate parameter $q$.
