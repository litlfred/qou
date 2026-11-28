Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a quantum observable universe with aether parameter $q$ and Descartes elliptic curve $\mathcal{E}_q$ ([Descartes elliptic curve](#prop:descartes-elliptic-curve)).

The **invariant Hom-group** of an object $E_q \in \mathrm{Ob}(\mathbf{C})$ whose fibre-functor image is $\tau(E_q) = H^1(\mathcal{E}_q, \mathbb{Z})$ is

$$
\mathcal{E}_q(\mathbf{1}) := \mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, E_q),
$$

with rank $r_q := \mathrm{rank}\,\mathcal{E}_q(\mathbf{1})$. Under Tannaka--Krein reconstruction ([reconstruction](#conj:tannaka-krein-isomorphism)), $\mathbf{C} \simeq \mathrm{Rep}(G)$ identifies $\mathcal{E}_q(\mathbf{1}) \cong \tau(E_q)^G = H^1(\mathcal{E}_q)^G$, the multiplicity space of the trivial representation $\mathbf{1}$ in $\tau(E_q)$. On the adjoint object $\mathrm{Ad}(A)$ (and on any non-trivial irreducible $G$-representation such as $V_{1/2}$ of $\mathrm{SU}(2)$), the categorical observability condition $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ forces $r_q = 0$. This invariant Hom-group is a representation-theoretic construction in $\mathbf{C}$, not the arithmetic Mordell--Weil group $E(\mathbb{Q})$ of rational points; for the rational elliptic curve Cremona $50\mathrm{a}1$ associated with Bring's Jacobian, $\mathrm{rank}\,E(\mathbb{Q}) = 0$ is a classical theorem of Kolyvagin.

The **finite-place Euler product** attached to a finite set $S$ of maximal ideals $\mathfrak{m} \in \mathrm{Spec}(R_q)$ of Bring's coordinate ring, with local Frobenius pair $\alpha_{\mathcal{E}}(\mathfrak{m}), \bar{\alpha}_{\mathcal{E}}(\mathfrak{m})$ restricted from the [local $q$-zeta function](#def:local-q-zeta-function) and norm $N(\mathfrak{m}) = q^{f(\mathfrak{m})}$, is

$$
L_S(\mathcal{E}_q, t) := \prod_{\mathfrak{m} \in S} \frac{1}{1 - \alpha_{\mathcal{E}}(\mathfrak{m}) t_{\mathfrak{m}} + N(\mathfrak{m}) t_{\mathfrak{m}}^2}.
$$

The **monoidal localisation kernel** for a family of localisation homomorphisms $\mathrm{loc}_\rho \colon H^1_\otimes(\mathbf{C}, E_q) \to H^1_\otimes(\mathbf{C}_\rho, E_q)$ on first cohomology of the :refterm[monoidal category]{#monoidal-category} is the subgroup intersection

$$
\mathrm{Sha}_q(\mathcal{E}_q) := \ker\!\left( H^1_{\otimes}(\mathbf{C}, E_q) \longrightarrow \prod_{\rho} H^1_{\otimes}(\mathbf{C}_\rho, E_q) \right) = \bigcap_{\rho} \ker(\mathrm{loc}_\rho).
$$
