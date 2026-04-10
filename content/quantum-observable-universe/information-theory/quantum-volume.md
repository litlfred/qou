Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe
and $\mathcal{S} \to M$ the state bundle with Reeb bundle
$S^3 \to \mathcal{S}_p$ at each brane point $p$
([Reeb bundle](#def:reeb-bundle)).  The **quantum volume**
of a region $U \subset M$ is

$$
  V_q(U) \;:=\;
  \int_U \epsilon_q \;\in\;
  \mathrm{End}_{\mathbf{C}}(\mathbf{1}),
$$

where $\epsilon_q$ is the categorical volume form on
$\Lambda^2 V$ preserved by the rigid duality of
$(\mathbf{C}, A, \tau)$
([quantum observable universe](#def:quantum-observable-universe)).

**Fibre structure.**
Each brane point $p \in U$ contributes a fibre
$\mathcal{S}_p$, which is a copy of $S^3$ carrying the
Reeb flow.  The quantum volume is **not** a naive count of
points in $U$ — it is weighted by the fibre volume:

$$
  V_q(U)
  \;=\; \int_U
  \mathrm{Vol}_{S^3}(\mathcal{S}_p)\;
  \epsilon_q(p),
$$

where $\mathrm{Vol}_{S^3}(\mathcal{S}_p)$ is the volume of the
$S^3$ fibre at $p$.  For a homogeneous gas (uniform
$q$ throughout $U$), all fibres are isometric and

$$
  V_q(U) \;=\;
  |U| \cdot \mathrm{Vol}(S^3_q),
$$

where $|U|$ is the number of brane points in $U$ and
$\mathrm{Vol}(S^3_q)$ is the $q$-dependent fibre volume.

**$S^3$ fibre volume.**
The Reeb flow on $S^3$ is the Hopf fibration
$S^1 \hookrightarrow S^3 \to S^2$.  The volume of $S^3$
in the $q$-deformed metric is

$$
  \mathrm{Vol}(S^3_q)
  \;=\; 2\pi^2 \cdot [2]_q,
$$

where $[2]_q = (q^2 - q^{-2})/(q - q^{-1}) = q + q^{-1}$
is the quantum $2$-number.  At $q = 1$ this recovers the
standard $\mathrm{Vol}(S^3) = 2\pi^2$.  The $q$-deformation
stretches or compresses the Hopf fibres according to the
substrate parameter.

**Relation to knot capacity.**
The quantum volume determines the **configuration space**
$\mathrm{Conf}(U)$ available to particle knots.  A knot $K$
with $n$ crossings requires a minimal $S^3$ volume
proportional to $n \cdot \hbar_q$ to fit within a fibre.
The number of single-fibre configurations at brane
point $p$ is therefore

$$
  |\mathrm{Conf}_p|
  \;\sim\;
  \frac{\mathrm{Vol}(S^3_q)}{n_K \cdot \hbar_q},
$$

where $n_K$ is the crossing number of $K$.  For a gas of
$N$ hydrogen atoms, each with the knot structure
$\mathcal{A}(1,0)$
([hydrogen knot structure](#ex:hydrogen-knot-structure)),
the total configuration count scales as
$|\mathrm{Conf}(U)| \sim |\mathrm{Conf}_p|^{|U|}$.

**Classical limit.**
As $q \to 1$: $[2]_q \to 2$, the fibre volume approaches
$2\pi^2 \cdot 2 = 4\pi^2$, and $V_q(U)$ reduces to the
Riemannian volume of $U$ times the standard $S^3$ volume.
The categorical volume form $\epsilon_q$ degenerates to the
classical Riemannian volume element.
