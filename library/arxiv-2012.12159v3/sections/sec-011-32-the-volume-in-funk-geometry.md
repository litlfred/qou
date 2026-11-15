---
doc_id: arxiv-2012.12159v3
doc_title: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME"
section_id: sec-011-32-the-volume-in-funk-geometry
section_title: "The volume in Funk geometry"
section_number: 3.2
pages: 11-13
source_pdf: 2012.12159v3.pdf
source_sha256: 473ec6959e82cd98
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.961
doc_brief: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME — We explore connections furnished by the Funk metric, a relative of the Hilbert metric, between projective geometry, billiards"
---
[]{#sec:volume_funk label="sec:volume_funk"}

For a convex set $K\subset \mathbb{P}$, let us construct a smooth measure $\widetilde \mu$ on $\mathop{\mathrm{int}}(K)$. Given $x\in \mathop{\mathrm{int}}(K)$, choose a density $d_x=\alpha_x\otimes\nu_x\in \mathop{\mathrm{Dens}}(T_x\mathbb{P})=\mathop{\mathrm{Dens}}(x^*\otimes V/x)=\mathop{\mathrm{Dens}}(V^*/x^\perp)\otimes \mathop{\mathrm{Dens}}((x^\perp)^*)$. Then $\nu_x^*\in \mathop{\mathrm{Dens}}(x^\perp)$ is defined by having $\nu_x^*\otimes\nu_x$ the symplectic (Liouville) volume on $x^\perp\oplus (x^\perp)^*$. Choose $\xi\in V^*/x^\perp$ with $\alpha_x(\xi)=1$, and consider the intersection in $V^*$ of the cone $K^\vee$ with the affine subspace $x^\perp+\xi$. We evaluate $c(x)=\nu_x^*(K^\vee\cap (x^\perp +\xi))$ and set $\widetilde\mu_x:=c(x)d_x\in\mathop{\mathrm{Dens}}(T_x\mathbb{P})$. It is easily verified that the choice of $\alpha_x,\nu_x$ does not matter. Thus $\widetilde\mu$ is well-defined in $\mathop{\mathrm{int}}(K)$.

::: Lemma
[]{#lem:holmes_thompson label="lem:holmes_thompson"} $\frac{1}{\omega_n}\widetilde\mu$ is the Holmes-Thompson volume of the projective co-nomadic Finsler structure inside $K$.
:::

Immediate from the construction.

Next we construct a measure on $\mathbb P\times \mathbb P^\vee$, which is analogous to the symplectic volume on $V\oplus V^*$. The group of projective automorphisms $\mathop{\mathrm{PGL}}(V)$ acts on $\mathbb{P}^\vee$ by $g(\xi):=g^{-*}\xi$. It holds that $$\begin{aligned}
    \mathop{\mathrm{Dens}}(T_{x,\xi}(\mathbb{P}\times \mathbb{P}^\vee))&=\mathop{\mathrm{Dens}}(x^*\otimes V/x\oplus \xi^*\otimes V^*/\xi)\\&=\mathop{\mathrm{Dens}}^*(x)^{n+1}\otimes\mathop{\mathrm{Dens}}^*(\xi)^{n+1}\otimes \mathop{\mathrm{Dens}}(V\oplus V^*)\\&=\mathop{\mathrm{Dens}}^*(x)^{n+1}\otimes\mathop{\mathrm{Dens}}^*(\xi)^{n+1}=\mathop{\mathrm{Dens}}^*(x\oplus \xi)^{n+1},
\end{aligned}$$ where all equalities are equviariant for the stablizer of $(x,\xi)$ in $\mathop{\mathrm{PGL}}(V)$.

Denote the incidence manifold $\mathcal Z=\{(x,\xi): x\perp \xi \}\subset \mathbb P\times \mathbb P^\vee$. We thus arrive at

::: Proposition
[]{#prop:invariant_measure label="prop:invariant_measure"} There is a one-dimensional space of projective-invariant measures on $\mathbb P\times \mathbb P^\vee\setminus \mathcal Z$, with canonic normalization. Using the standard Euclidean structure on $\mathbb{R}^{n+1}$ to identify $\mathbb{P}$ and $\mathbb{P}^\vee$ locally with the unit sphere, it is given by $$d\mu(x,\xi)= |\langle x,\xi \rangle| ^{-(n+1)}d\sigma_x d\sigma_\xi$$ where $\sigma_x,\sigma_\xi$ are the standard rotationally-invariant measures on each sphere.
:::

::: Lemma
[]{#lem:two_measures label="lem:two_measures"} For a measurable set $A\subset \mathop{\mathrm{int}}(K)$, it holds that $\widetilde\mu(A)=\mu(A\times K^\vee)$.
:::

We have $$\mu(A\times K^\vee)=\int_{A}dx\int_{K^\vee}\frac{d\xi}{|\langle x,\xi\rangle|^{n+1}}.$$

Next we use the Euclidean structure for all choices in the definition of $\widetilde\mu$. Assume $x=e_{n+1}$, so $T_x\mathbb P=T_x^*\mathbb P=e_{n+1}^\perp$. Choose $d_x=dx$, $\alpha_x=x$, so that $\xi=x$, and $\nu_x$, $\nu_x^*$ are both the Euclidean volume. So it remains to check that $$\int_{K^\vee\cap S^n}\frac{d\xi}{|\xi_{n+1}|^{n+1}}=|K^\vee\cap (e_{n+1}+e_{n+1}^\perp)|.$$ As the jacobian of the map $$\label{eq:projection} S^n\to e_{n+1}+e_{n+1}^\perp,\quad \xi\mapsto \xi/\xi_{n+1}$$ is $1/|\xi_{n+1}|^{n+1}$, the claim follows.

::: Corollary
[]{#cor:dual_volumes label="cor:dual_volumes"} The Holmes-Thompson volume of the Funk metric in the interior of $L$, denoted $\mathop{\mathrm{vol}}^F_L$, is a projective invariant of $L$, that is independent of a choice of a hyperplane at infinity. Furthermore, if $K\subset\mathop{\mathrm{int}}(L)$ is convex, there is a duality of Funk volumes: $\mathop{\mathrm{vol}}_L^F(K)=\mathop{\mathrm{vol}}_{K^\vee}^F(L^\vee)$.
:::

The first part follows from Proposition [\[prop:projective_funk\]](#prop:projective_funk){reference-type="ref" reference="prop:projective_funk"} and the paragraph after Definition [\[def:conomadic\]](#def:conomadic){reference-type="ref" reference="def:conomadic"}. The second is immediate from Lemmas [\[lem:holmes_thompson\]](#lem:holmes_thompson){reference-type="ref" reference="lem:holmes_thompson"} and [\[lem:two_measures\]](#lem:two_measures){reference-type="ref" reference="lem:two_measures"}.

Let $\mathop{\mathrm{vol}}^H_K$ denote the Holmes-Thompson volume of the Hilbert metric in $\mathop{\mathrm{int}}(K)$.

::: Corollary
[]{#cor:hilbert_volume_sec3 label="cor:hilbert_volume_sec3"} Given $K\subset \mathop{\mathrm{int}}(L)$ in $\mathbb{R}\mathbb{P}^n$, $\mathop{\mathrm{vol}}^H_L(K)\leq\frac{1}{2^n}{2n\choose n} \mathop{\mathrm{vol}}_{K^\vee}^H(L^\vee)$. Equality is uniquely attained when $L$ is a simplex, and $K$ is an ellipsoid.
:::

Choose an affine chart and assume $0\in\mathop{\mathrm{int}}(K)$. By the Rogers-Shephard inequality and the duality of volumes, $$\begin{aligned}
\mathop{\mathrm{vol}}^H_L(K)=\frac{1}{\omega_n}\int_K|\frac12 (L^z-L^z)|dz\leq \frac1{2^n\omega_n}{2n\choose n}\int_K |L^z|dz&=\frac1{2^n}{2n\choose n}\mathop{\mathrm{vol}}^F_{L}(K)\\&=\frac1{2^n}{2n\choose n}\mathop{\mathrm{vol}}^F_{K^o}(L^o).
\end{aligned}$$ On the other hand by the Brunn-Minkowski inequality, $$\mathop{\mathrm{vol}}^F_{K^o}(L^o)=\frac{1}{\omega_n}\int_{L^o}|(K^o)^z|dz\leq \frac{1}{\omega_n}\int_{L^o}|\frac12 ((K^o)^z-(K^o)^z)|dz=\mathop{\mathrm{vol}}^H_{K^o}(L^o).$$

The Rogers-Shephard inequality becomes an equality when $L$ is a simplex, while the Brunn-Minkowski inequality above gives equality for symmetric bodies, that is $(K^o)^z$ must have antipodal symmetry (with respect to some point) for every $z\in L^o$.

A *projective center* of a convex body in $\mathbb{R}\mathbb{P}^n$ is a center of antipodal symmetry for the body in some affine chart containing $K$. The sets $(K^o)^z$ are projectively equivalent to $K$, and we find that the set $L^o\subset \mathop{\mathrm{int}}(K^\vee)$ parametrizes different choices of hyperplanes $\eta^\perp$ at infinity, for which $K\subset\mathbb{R}\mathbb{P}^n\setminus \eta^\perp$ has antipodal symmetry with some center point. But that implies that every $\eta\in L^o$ is a projective center for $K^\vee\subset\mathbb{P}^\vee$. By [@kelly_straus Theorem 9-3.], we conclude that $K^\vee$, and therefore $K$, must be a convex quadric, that is an ellipsoid.
