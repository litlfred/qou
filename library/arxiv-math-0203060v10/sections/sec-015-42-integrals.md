---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-015-42-integrals
section_title: "Integrals"
section_number: 4.2
pages: 15-16
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
toc_source: outline
text_source: latex
latex_prose_ratio: 0.817
latex_coverage_ratio: 0.927
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
[]{#subsection about integrals label="subsection about integrals"}

The following notion of an integral in a weak Hopf algebra is a generalization of that of an integral in a usual Hopf algebra [@M].

::: definition
[]{#integral label="integral"} A left *integral* in $A$ is an element $\ell\in A$ such that $$h\ell =\varepsilon_t(h)\ell, \qquad (rh = r\varepsilon_s(h)) \qquad \mbox{ for all } h\in A.$$
:::

The space of left integrals in $A$ is a left ideal of $A$ of dimension equal to $\dim_k(A_t)$.

Any left integral $\lambda$ in $A^*$ satisfies the following invariance property : $$\label{left invariance}
g_{(1)} \lambda(hg_{(2)}) = S(h_{(1)})\lambda(h_{(2)}g),
\qquad g,h\in A.$$

In what follows we use the Sweedler arrows $\rightharpoonup$ and $\leftharpoonup$ for the dual actions : $$\label{Sweedler arrows}
h\rightharpoonup\phi (g) = \phi(gh)
\quad \text { and } \quad
\phi\leftharpoonup h (g)= \phi(hg).$$ for all $g,\,h\in A,\phi\in A^*$.

Recall that a functional $\phi\in A^*$ is *non-degenerate* if $\phi\circ m$ is a non-degenerate bilinear form on $A$. Equivalently, $\phi$ is non-degenerate if the linear map $h\mapsto (h \rightharpoonup\phi)$ is injective. An integral (left or right) in a weak Hopf algebra $A$ is called *non-degenerate* if it defines a non-degenerate functional on $A^*$. A left integral $\ell$ is called *normalized* if $\varepsilon_t(\ell)=1$.

It was shown by P. Vecsernyes [@V] that a finite dimensional weak Hopf algebra always possesses a non-degenerate left integral. In particular, a finite dimensional weak Hopf algebra is a Frobenius algebra (this extends the well-known result of Larson and Sweedler for usual Hopf algebras).

Maschke's theorem for weak Hopf algebras, proved in [@BNSz 3.13], states that a weak Hopf algebra $A$ is semisimple if and only if $A$ is separable, and if and only if there exists a normalized left integral in $A$. In particular, every semisimple weak Hopf algebra is finite dimensional.

For a finite dimensional $A$ there is a useful notion of duality between non-degenerate left integrals in $A$ and $A^*$ [@BNSz 3.18]. If $\ell$ is a non-degenerate left integral in $A$ then there exists a unique $\lambda\in A^*$ such that $\lambda\rightharpoonup\ell = 1$. This $\lambda$ is a non-degenerate left integral in $A^*$. Moreover, $\ell\rightharpoonup\lambda =\epsilon$. Such a pair of non-degenerate integrals $(\ell,\,\lambda)$ is called a pair of *dual* integrals.

An invertible element $g\in A$ is called *group-like* if $\Delta(g) = (g\otimes g)\Delta(1) = \Delta(1)(g\otimes g)$ [@N Definition 4.1]. Group-like elements of $A$ form a group $G(A)$ under multiplication. This group has a normal subgroup $G_0(A) := G(A_{{\rm min}})$ of *trivial* group-like elements. If $A$ is finite dimensional, the quotient group $\widetilde{G}(A) = G(A)/ G_0(A)$ is finite. It was shown in [@N] that if $A$ is finite dimensional and $\ell\in A$ and $\lambda\in A^*$ is a dual pair of left integrals, then there exist group-like elements $\alpha\in G(A^*)$ and $a\in G(A)$, called *distinguished* group-like elements, whose classes in $\widetilde{G}(A^*)$ and $\widetilde{G}(A)$ do not depend on the choice of $\ell$ and $\lambda$, such that $$S(\ell) = \alpha\rightharpoonup\ell \qquad \mbox{ and  } \qquad S(\lambda)=a \rightharpoonup\lambda.$$ (Note that $\alpha$ and $a$ themselves depend on the choice of $\ell$ and $\lambda$).

The following result is crucial for this paper. It is an analogue of Radford's formula for usual Hopf algebras.

::: theorem
[]{#S4 label="S4"} [@N Theorem 5.13] One has $$S^4(h) = a^{-1}(\alpha\rightharpoonup h \leftharpoonup\alpha^{-1})a.$$ for all $h\in A$.
:::

A weak Hopf algebra $A$ is said to be *unimodular* if it contains a non-degenerate $2$-sided integral; equivalently, $A$ is unimodular if the coset of $\alpha$ in $G(A^*)$ is trivial. A semisimple weak Hopf algebra is automatically unimodular [@BNSz].

## Proof of Theorem [\[fourstars\]](#fourstars){reference-type="ref" reference="fourstars"} {#pffourstars}

Let ${\mathcal C}$ be a fusion category over $k$. By Theorem [\[Schlah1\]](#Schlah1){reference-type="ref" reference="Schlah1"}, ${\mathcal C}$ is the representation category of a semisimple connected weak Hopf algebra $A$. Since $A$ is semisimple, it is unimodular, and hence one can choose a left integral $\ell$ such that the corresponding element $\alpha=\epsilon$. Thus, by Theorem [\[S4\]](#S4){reference-type="ref" reference="S4"}, one has $S^4(h)=a^{-1}ha$, for some group-like element $a\in G(H)$, and hence for any simple object $V\in {\mathcal C}=\text{Rep}(A)$, the operator $a^{-1}|_V$ defines an isomorphism $V\to V^{****}$. Since $a$ is grouplike, this isomorphism respects the tensor product. The theorem is proved.
