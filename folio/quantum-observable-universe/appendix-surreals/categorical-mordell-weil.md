Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a QOU with substrate parameter $q$ and Descartes elliptic curve $\mathcal{E}_q$ ([Descartes elliptic curve](#prop:descartes-elliptic-curve)).

The categorical Mordell--Weil group is the abelian group of $\mathbf{1}$-rational points

$$
\mathcal{E}_q(\mathbf{1}) := \mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, E_q),
$$

where $E_q \in \mathrm{Ob}(\mathbf{C})$ is the object whose fibre functor image $\tau(E_q) = H^1(\mathcal{E}_q, \mathbb{Z})$ is the first cohomology of the elliptic fiber. The group law is induced by chord-tangent addition on $\mathcal{E}_q$. Set $r_q := \mathrm{rank}\,\mathcal{E}_q(\mathbf{1})$. The Tannaka--Krein equivalence ([reconstruction](#conj:tannaka-krein-isomorphism)) identifies $\mathbf{C} \simeq \mathrm{Rep}(G)$, giving

$$
\mathcal{E}_q(\mathbf{1}) \cong \tau(E_q)^G = H^1(\mathcal{E}_q)^G.
$$

Equivalently, $r_q$ is the multiplicity of the trivial representation $\mathbf{1}$ in the $G$-module $H^1(\mathcal{E}_q)$.

The $q$-deformed $L$-function is built from the Frobenius eigenvalues $\alpha_1, \ldots, \alpha_8$ of the local $q$-zeta function ([local $q$-zeta](#def:local-q-zeta-function)) acting on $H^1(\mathcal{B})$, the first étale cohomology of Bring's curve. The elliptic fiber $\mathcal{E}_q \hookrightarrow \mathcal{B}$ is a genus-$1$ sub-curve. The restriction of Frobenius to $H^1(\mathcal{E}_q) \subset H^1(\mathcal{B})$ yields a conjugate pair $\alpha_{\mathcal{E}}, \bar{\alpha}_{\mathcal{E}}$ with $|\alpha_{\mathcal{E}}| = q^{1/2}$ (by the Hasse--Weil bound). Define

$$
L(\mathcal{E}_q, s) := \prod_{\mathfrak{m} \in \mathrm{Spec}(R_q)} \frac{1}{1 - \alpha_{\mathcal{E}}(\mathfrak{m}) N(\mathfrak{m})^{-s} + N(\mathfrak{m})^{1-2s}},
$$

where the product runs over maximal ideals of the coordinate ring $R_q$ of Bring's curve, and $N(\mathfrak{m}) = q^{f(\mathfrak{m})}$ is the norm.

The $q$-Tate--Shafarevich group is the kernel of the local-global map. The fibre functor atlas of the QOU forms a $G$-gerbe over the spectral base. For each Reeb eigenvalue $\rho \in \mathrm{Spec}(\xi_q)$, let $\mathbf{C}_\rho$ be the localization of $\mathbf{C}$ at $\rho$ (the full subcategory of objects whose spectral support contains $\rho$). Define

$$
\mathrm{Sha}_q(\mathcal{E}_q) := \ker\!\left( H^1_{\otimes}(\mathbf{C}, E_q) \longrightarrow \prod_{\rho \in \mathrm{Spec}(\xi_q)} H^1_{\otimes}(\mathbf{C}_\rho, E_q) \right),
$$

where $H^1_{\otimes}$ denotes the first cohomology of the :refterm[monoidal category]{#monoidal-category} (classifying torsors under $\mathcal{E}_q$ in $\mathbf{C}$).
