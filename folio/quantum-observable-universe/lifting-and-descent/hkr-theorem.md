Let $R$ be a commutative algebra over a field $k$ of characteristic zero, and suppose $R$ is smooth (for a reader who prefers geometry: $R$ is the coordinate ring of a smooth affine variety, or the algebra of functions on a smooth manifold). The Hochschild–Kostant–Rosenberg theorem \cite{hkr-1962} identifies the Hochschild homology of $R$ with its differential forms and the Hochschild cohomology with its polyvector fields:

$$
  HH_n(R) \;\cong\; \Omega^{n}_{R/k}, \qquad HH^{n}(R) \;\cong\; \Lambda^{n} \operatorname{Der}_k(R),
$$

where the first map sends the class of $r_0 \otimes r_1 \otimes \cdots \otimes r_n$ to $\tfrac{1}{n!}\, r_0\, dr_1 \wedge \cdots \wedge dr_n$ \cite{loday-1998}. For a smooth projective curve $M_0$ the same statement holds sheaf by sheaf, and taking cohomology gives

$$
  HH_n(M_0) \;=\; \bigoplus_{i} H^{i}\bigl(M_0, \Omega^{\,i+n}\bigr), \qquad
  HH^{n}(M_0) \;=\; \bigoplus_{i+j = n} H^{i}\bigl(M_0, \Lambda^{j} T M_0\bigr).
$$

For a curve of genus $g$ this reads: $HH_0 = H^0(\mathcal{O}) \oplus H^1(\Omega^1)$ of dimension $2$; $HH_1 = H^0(\Omega^1)$ and $HH_{-1} = H^1(\mathcal{O})$, each of dimension $g$; and on the cohomology side $HH^0 = k$, $HH^1 = H^1(\mathcal{O})$ of dimension $g$, and $HH^2 = H^1(TM_0)$ of dimension $3g - 3$, the space of first-order deformations of the curve. The alternating sum of the homology is $2 - 2g$, the Euler characteristic of the surface.

**What the theorem does not say.** Its hypotheses are commutativity, smoothness and characteristic zero. The [classical limit obstruction](#def:classical-limit-obstruction) is $HH^2(\mathcal{U}_q(\mathfrak{g}), \mathrm{Ad})$, the Hochschild cohomology of a *noncommutative* algebra at $q \neq 1$, and the Hochschild–Kostant–Rosenberg theorem says nothing about it. The comparison arrow written as "HKR" in the [Hochschild–Kummer connection](#rem:hochschild-kummer-connection) is therefore not an instance of this theorem: it is an identification between a deformation-theoretic obstruction of the substrate and a gerbe-theoretic obstruction on the base that the axioms of a quantum observable universe do not supply. At $q = 1$ the algebra is the enveloping algebra of a semisimple Lie algebra, and Whitehead's lemmas make $HH^2(\mathcal{U}(\mathfrak{g}), M)$ vanish for finite-dimensional $M$, so the obstruction space of the classical fibre is zero, not a line.

The closest statement in the literature is Kontsevich's formality theorem \cite{kontsevich-2003}: for a smooth algebra the cohomological Hochschild–Kostant–Rosenberg map is the first term of a quasi-isomorphism of differential graded Lie algebras between polyvector fields and Hochschild cochains, which classifies the *formal* deformations of $R$ in a parameter $\hbar$. That is the correct setting for a first-order comparison, and it is a setting the substrate parameter does not occupy: $q - 1 \approx 0.11$ is a real number at which everything is evaluated, not a formal variable in which everything is expanded. This is the fibre-versus-observable wall, and it is why the one-dimensionality of the obstruction space is stated as the Wigner axiom rather than derived.
