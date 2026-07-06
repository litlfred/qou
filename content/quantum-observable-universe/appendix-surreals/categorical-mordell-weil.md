Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a QOU with substrate parameter $q$ and Descartes elliptic curve $\mathcal{E}_q$ ([Descartes elliptic curve](#prop:descartes-elliptic-curve)).

The **categorical Mordell--Weil group** is the abelian group of $\mathbf{1}$-rational points:

$$
\mathcal{E}_q(\mathbf{1})
 :=  \mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, E_q).
$$

Here, $E_q \in \mathrm{Ob}(\mathbf{C})$ is the object whose fibre functor image $\tau(E_q) = H^1(\mathcal{E}_q, \mathbb{Z})$ is the first cohomology of the elliptic fiber. The group law is induced by the chord-tangent addition on $\mathcal{E}_q$. Let $r_q := \mathrm{rank}\,\mathcal{E}_q(\mathbf{1})$. The Tannaka–Krein equivalence ([reconstruction](#thm:tannaka-krein-isomorphism)) identifies $\mathbf{C} \simeq \mathrm{Rep}(G)$. Therefore:

$$
\mathcal{E}_q(\mathbf{1})
 \cong  \tau(E_q)^G
=  H^1(\mathcal{E}_q)^G.
$$

The rank $r_q$ is exactly the multiplicity of the trivial representation $\mathbf{1}$ in the $G$-module $H^1(\mathcal{E}_q)$.

### The $q$-Deformed $L$-Function

The local $q$-zeta function ([local $q$-zeta](#def:local-q-zeta-function)) acts on $H^1(\mathcal{B})$, the first étale cohomology of Bring's curve. It possesses Frobenius eigenvalues $\alpha_1, \ldots, \alpha_8$. The elliptic fiber $\mathcal{E}_q \hookrightarrow \mathcal{B}$ is a genus-$1$ sub-curve. Restricting the Frobenius action to $H^1(\mathcal{E}_q) \subset H^1(\mathcal{B})$ yields a conjugate pair $\alpha_{\mathcal{E}}, \bar{\alpha}_{\mathcal{E}}$. By the Hasse–Weil bound, $|\alpha_{\mathcal{E}}| = q^{1/2}$. 

We define the $L$-function:

$$
L(\mathcal{E}_q, s)
 :=  \prod_{\mathfrak{m} \in \mathrm{Spec}(R_q)}
  \frac{1}{1 - \alpha_{\mathcal{E}}(\mathfrak{m})
  N(\mathfrak{m})^{-s}
  + N(\mathfrak{m})^{1-2s}}.
$$

This product runs over the maximal ideals of the coordinate ring $R_q$ of Bring's curve, with norm $N(\mathfrak{m}) = q^{f(\mathfrak{m})}$.

### The $q$-Tate--Shafarevich Group

The $q$-Tate–Shafarevich group is the kernel of the local-global map. The fibre functor atlas of the QOU forms a $G$-gerbe over the spectral base. For each Reeb eigenvalue $\rho \in \mathrm{Spec}(\xi_q)$, let $\mathbf{C}_\rho$ be the localization of $\mathbf{C}$ at $\rho$ (the full subcategory of objects supported on $\rho$). We define:

$$
\mathrm{Sha}_q(\mathcal{E}_q)
 :=  \ker\!\left(
  H^1_{\otimes}(\mathbf{C}, E_q)
   \longrightarrow 
  \prod_{\rho \in \mathrm{Spec}(\xi_q)}
  H^1_{\otimes}(\mathbf{C}_\rho, E_q)
\right).
$$

Here $H^1_{\otimes}$ denotes the first cohomology of the :refterm[monoidal category]{#monoidal-category}, which classifies torsors under $\mathcal{E}_q$ in $\mathbf{C}$. This group measures the failure of the local-global principle at the $q$-scale. It counts torsors that are globally non-trivial yet trivial at every spectral localization.
