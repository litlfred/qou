Two prototypical *non-torus* Reeb-flow trajectories carry
positive hyperbolic volume in the JSJ decomposition of their
knot complement: the Garside element
$\Delta_3 = \sigma_1\sigma_2\sigma_1$ and the Borromean braid
$(\sigma_1\sigma_2^{-1})^3$.  Both are direct constructions in
the $q$-Reeb-flow framework
([six canonical knot operators](#prop:six-canonical-knot-operators),
[Garside as compound Reeb flow](#rem:garside-as-compound-flow)).

**Garside complement.**  The Garside compound flow swaps the
red and blue tubes via the green spectator across three latitude
sub-intervals.  In each sub-interval, the active pair spirals
around its shared axis; between sub-intervals, the active pair
switches.  The resulting trajectory does *not* lie on a single
Heegaard torus inside $\mathcal{R}_p \cong S^3$: the
non-adjacent-transposition signature
([$\rho$ as $S_3$ holonomy on Lagrange resolvents](#rem:rho-s3-holonomy-exposition))
forces the trajectory to cross between the two Heegaard tori,
so the complement is *not* Seifert-fibered.  The JSJ
decomposition therefore contains a hyperbolic piece, and
[Thurston volume additivity](#prop:thurston-volume-additivity)
gives a strictly positive Bloch–Wigner sum.

**Borromean complement: the canonical example.**  The Borromean
braid $(\sigma_1\sigma_2^{-1})^3$ traces a three-component link
in $\mathcal{R}_p$ whose complement is the *Gieseking–Meyerhoff
arithmetic 3-manifold*.  Its hyperbolic volume is the closed
form

$$
  V_{\mathrm{hyp}}(\mathrm{Borromean}) \;=\; 8\,G
  \;\approx\; 7.327724753\ldots,
$$

where $G$ is the Catalan constant.  Geometrically the
Borromean complement decomposes into **two regular ideal
octahedra**: each ideal octahedron of shape $z = i$ has volume
$4 \cdot \mathrm{Cl}_2(\pi/2) = 4 G$, and the two-octahedron sum
gives $V_{\mathrm{hyp}} = 8 G$.  (Note that $G \neq v_3$:
the Catalan constant $G = \mathrm{Cl}_2(\pi/2) \approx 0.91596$ is the
Lobachevsky function evaluated at $\pi/2$ — the contribution of
a regular ideal octahedron's eighth — whereas
$v_3 = \mathrm{Cl}_2(\pi/3) \approx 1.01494$ is its value at
$\pi/3$ — the contribution of a regular ideal tetrahedron.  The
$8 v_3$ decomposition does not apply here; the Borromean complement
is *not* built from eight regular ideal tetrahedra.)

**Figure-eight as the threshold case.**  Between the torus
trefoil $T_{2,3}$ (volume zero) and the Borromean link (volume
$8G$) sits the figure-eight knot $4_1$ with volume
$V_{\mathrm{hyp}}(4_1) = 2 v_3 \approx 2.0299$
([Thurston volume additivity](#prop:thurston-volume-additivity)).
This is the *smallest* hyperbolic volume among knots in $S^3$
and is the substrate-fixing observable used to pin $q_0$ via
$\hbar_q^2 = V(4_1) / (m_\mu/m_e)$.  The corresponding Reeb-flow
trajectory is the four-crossing braid $\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1}$;
it again crosses between Heegaard tori twice, producing a
hyperbolic complement of minimal volume.

**Why this is the mass-bearing regime.**  Combining with
[Reeb-bundle complement equals volume](#prop:reeb-bundle-complement-equals-volume),
the Markov-trace observable for a non-torus braid receives a
non-zero topological-mass contribution proportional to
$V_{\mathrm{hyp}}$.  In the JSJ-graded form of
[mass-volume factorization](#conj:mass-volume-factorization),
only hyperbolic pieces contribute; torus pieces are
geometrically invisible.  The Reeb-flow picture explains *why*
this geometric vanishing happens: the strands lie on a Heegaard
torus and never enter the bulk hyperbolic regime of the bundle.

Together with
[torus-knot zero volume via Reeb](#rem:torus-knot-zero-volume-via-reeb),
this remark closes the geometric dichotomy: torus trajectories
$\Rightarrow$ Seifert-fibered complement $\Rightarrow V_{\mathrm{hyp}} = 0$;
non-torus trajectories $\Rightarrow$ hyperbolic complement $\Rightarrow V_{\mathrm{hyp}} > 0$.
The trajectory pattern, read off from the Reeb-flow ODE, is what
determines the JSJ verdict in advance.
