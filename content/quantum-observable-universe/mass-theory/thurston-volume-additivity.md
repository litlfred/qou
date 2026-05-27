## Thurston volume additivity

Every hyperbolic knot or link complement $S^3 \setminus \mathcal{K}$
admits an ideal triangulation — a decomposition into finitely many
ideal tetrahedra $\Delta_1, \ldots, \Delta_N$ whose vertices lie on
the sphere at infinity $\partial \mathbb{H}^3$.  Each ideal
tetrahedron is determined up to isometry by a single complex **shape
parameter** $z_i \in \mathbb{C} \setminus \{0, 1\}$ — the cross-ratio
of its four ideal vertices.

## Statement

**Proposition.** \cite{thurston1978}
*Let $\mathcal{K} \subset S^3$ be a hyperbolic knot or link, and
fix an ideal triangulation of $S^3 \setminus \mathcal{K}$ with
shape parameters $z_1, \ldots, z_N$ determined by the hyperbolic
gluing equations.  The hyperbolic volume is the sum of tetrahedral
volumes:*

$$
  V(\mathcal{K})
  \;=\;
  \sum_{i = 1}^N D(z_i),
  \qquad
  D(z) \;=\; \Im\,\mathrm{Li}_2(z) + \arg(1 - z)\,\log\lvert z \rvert,
$$

*where $D$ is the **Bloch–Wigner dilogarithm**.  Degenerate (flat)
tetrahedra with $z_i \in \mathbb{R}$ contribute $D(z_i) = 0$.*

## Braid-theoretic consequence

A knot diagram with $c$ crossings induces an ideal triangulation of
$S^3 \setminus \mathcal{K}$ with one ideal tetrahedron per crossing
(possibly merged or degenerate under simplification).  The volume
is therefore **additive over crossings**:

$$
  V(\mathcal{K}) \;=\; \sum_{\text{crossings } c} D(z_c).
$$

Torus knots have all crossings pressed onto a torus surface — every
$z_c$ is real — so $V(T_{m,n}) = 0$.  This is the categorical
explanation of why Seifert-fibered nucleons contribute zero hyperbolic
volume in the [JSJ decomposition of the atomic braid](#thm:wedderburn-mass-formula).

## Extremality

Among all $z \in \mathbb{C}$, the Bloch–Wigner function attains its
maximum at the regular shape $z = e^{i\pi/3}$:

$$
  D(e^{i\pi/3}) \;=\; \mathrm{Cl}_2(\pi/3) \;=\;
  \sum_{n \geq 1} \frac{\sin(n\pi/3)}{n^2}
  \;\approx\; 1.01494 \;=:\; v_3,
$$

the **Lobachevsky constant**.  The figure-eight knot $4_1$ has two
ideal tetrahedra both of shape $e^{i\pi/3}$, giving
$V(4_1) = 2 v_3 \approx :val[Vol_4_1]{precision=6}$ — the minimum volume among
hyperbolic knots.  This is the normalization used to pin the
substrate parameter $q_0$ via
[$\hbar_q^2 = V(4_1) / (m_\mu / m_e)$](#prop:local-substrate-q).
