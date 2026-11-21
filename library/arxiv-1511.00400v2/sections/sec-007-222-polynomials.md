---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-007-222-polynomials
section_title: "Polynomials"
section_number: 2.2.2
pages: 8-10
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.984
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
[]{#subsection:polynomial label="subsection:polynomial"}

Here some properties of twisted Alexander polynomials viewed as torsions are briefly discussed, since they are convenient for describing some results of Reidemeister torsion. See the recent surveys [@Morifuji15; @FV11] fore more details on twisted Alexander polynomials.

Start with a surjective morphism $\phi\colon\pi_1 K\to \mathbb{Z}$. Instead of a representation $\rho\colon\pi_1K\to \mathrm{SL}_n(F)$, consider the twisted representation $$\rho\otimes \phi\colon\pi_1 K\to \operatorname{GL}_n(F(t))$$ where $F(t)$ is the field of fractions of the polynomial ring $F[t]$.

If $H_*(K;\rho)=0$, then $H_*(K;\rho\otimes \phi)=0$ [@Milnor68; @Kitano96] and there is a well defined torsion, or twisted polynomial: $$\Delta_{K,\rho,\phi}(t)=\operatorname{tor}(K,\rho,\phi)\in F(t)/\pm t^{n\, \mathbb{Z}}.$$ As the determinant is not one, there is an indeterminacy factor $t^{k\, n}$, for some integer $k\in\mathbb{Z}$.

::: remark
[]{#rem:evaluation label="rem:evaluation"} Assume $H_*(K;\rho)=0$. Then $$\Delta_{K,\rho,\phi}(1)= \operatorname{tor}(K,\rho).$$ This is proved from the map at the chain level $C_*(K;\rho\otimes\phi)\to 
C_*(K;\rho)$ induced by evaluation $t=1$.
:::

If $\Delta_{K,\rho,\phi}=\sum_i a_i t^i$, then its degree can be defined as: $$\deg ( \Delta_{K,\rho,\phi} )   =\max \{i-j\mid a_i,a_j\neq 0\}.$$

::: prop
[]{#prop:degree label="prop:degree"} If $M^3$ is a three-manifold and $\Sigma\subset M^3$ is a surface dual to $\phi$ such that $H_0(\Sigma;\rho)=0$, then $$\deg \Delta_{M^3,\rho,\phi} \leq -\chi(\Sigma) n.$$
:::

This proposition can be proved using Mayer-Vietoris to a tubular neighborhood of the surface and its exterior.

For a knot ${\mathcal K}\subset S^3$, there is a natural surjection $\phi\colon\pi_1(S^3-{\mathcal K})\to \mathbb{Z}$. Let $A_{\mathcal K}$ denote its Alexander polynomial. In [@Lin01] (this reference is based on a preprint from 1990) Lin defined a twisted Alexander polynomial $A_{\mathcal K}^\rho$ that lives in $F(t)$, that was later modified by Wada [@Wada94].

Milnor in 1962 for the untwisted Alexander polynomials, and Kitano in 1996 for the twisted ones, proved:

::: thm
For a knot exterior $S^3-{\mathcal K}$, we have:

(a) [@Milnor62] For the trivial representation: $$\Delta_{S^3-\mathcal K,1,\phi} =\operatorname{tor}(S^3-{\mathcal K}, \phi)= \frac{A_{\mathcal 
    K}(t)}{(t-1)}.$$

(b) [@Kitano96] For $\rho$ a non-trivial acyclic representation: $$\Delta_{S^3-\mathcal K,\rho,\phi}=
    \operatorname{tor}(S^3-{\mathcal K},\rho\otimes \phi)= A_{\mathcal K}^\rho(t).$$
:::

Milnor's formula, for the untwisted polynomial, has been generalized to links and to other three-manifolds in 1986 by Turaev [@Turaev86]. See also [@FV11; @Morifuji15].

The following is straightforward from Mayer-Vietoris, Proposition [\[prop:MV\]](#prop:MV){reference-type="ref" reference="prop:MV"}:

::: prop
[]{#prop:MapTorus label="prop:MapTorus"} Let $K$ be a CW complex, $f\colon \vert K\vert \to \vert K\vert$ a homeomorphism with mapping torus $M_f$. Then $$\Delta _{M_f,\rho,\phi}=\prod_{i=0}^{\dim K} \det (f_i - 
t\operatorname{Id})^{(-1)^{i+1}}\, ,$$ where $f_i\colon H_i(K;\rho)\to H_i(K;\rho)$ denotes the induced map in homology. In particular, by Remark [\[rem:evaluation\]](#rem:evaluation){reference-type="ref" reference="rem:evaluation"}, $$\operatorname{tor}(M_f,\rho)=\prod_{i=0}^{\dim K} \det (f_i - 
\operatorname{Id})^{(-1)^{i+1}}.$$
:::

Another relevant issue for this polynomial is Turaev's interpretation of the twisted Alexander polynomial: namely this polynomial encodes the torsion of the finite cyclic coverings ([@Turaev86], see also [@DY12; @Porti04; @SW02; @Raimbault12; @Yamaguchi12]).

::: prop
[]{#prop:Fox label="prop:Fox"} Let $K$, $\rho\colon\pi_1 K\to \mathrm{SL}_n(F)$, and $\phi\colon\pi_1 K\to \mathbb{Z}$ be as above. Let $K_m\to K$ be the cyclic covering of order $m$ corresponding to the kernel of $\phi$ composed with the projection $\mathbb{Z}\to\mathbb{Z}/m\mathbb{Z}$. Then

(a) $H_*(K_m;\rho)=0$ if and only if $\Delta_{M^3,\rho,\phi} (\zeta)\neq 0$ for every $\zeta\in\mathbb{C}$ satisfying $\zeta^m=1$.

(b) If $H_*(K_m;\rho)=0$ then $$\operatorname{tor}(K_m, \rho)=\prod\limits_{i=0}^{m-1} \Delta_{M^3,\rho,\phi} ( \zeta^i)$$ for $\zeta\in\mathbb{C}$ a primitive $m$-root of the unity.
:::
