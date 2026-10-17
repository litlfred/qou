---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS"
section_id: sec-004-14-representation-varieties
section_title: "Representation varieties"
section_number: 1.4
pages: 3-4
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.991
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry between a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
[]{#Sec:RepVar label="Sec:RepVar"}

Fix a point $p\in \Sigma_g$ and denote by $\EuScript{M}(\Sigma_g)$ the moduli space of rank two, fixed odd determinant stable bundles on a complex curve of genus $g$, equivalently the space of conjugacy classes of $SU(2)$-representations of $\pi_1(\Sigma\backslash\{p\})$ which have holonomy $-I$ at the puncture. $\EuScript{M}(\Sigma_g)$ admits a natural symplectic structure; the symplectic volume of $\EuScript{M}(\Sigma_g)$ was computed by Witten and Jeffrey-Weitsman [@Witten; @JW], and techniques from number theory, gauge theory and birational geometry have all been brought to bear on understanding its cohomology [@NS; @AtiyahBott; @Thaddeus]. The connection to pencils of quadrics goes back to Newstead [@Newstead], who constructed an isomorphism $\EuScript{M}(\Sigma_2) \cong Q^{4}_0\cap Q^{4}_1 \subset {\mathbb P}^5$. Theorem [\[Thm:Embed\]](#Thm:Embed){reference-type="ref" reference="Thm:Embed"} therefore computes part of the Fukaya category of $\EuScript{M}(\Sigma_2)$.

In the topological setting, there is an extension $\widehat\Gamma(\Sigma_g)$ of the (full, not hyperelliptic) classical mapping class group $\Gamma_g=\pi_0\operatorname{Diff}^+(\Sigma_g)$ by ${\mathbb Z}_2^{2g} = H^1(\Sigma_g;{\mathbb Z}_2)$ which acts on the moduli space via a homomorphism $\widehat\Gamma(\Sigma_g) \rightarrow \operatorname{Symp}\EuScript{M}(\Sigma_g)$. Goldman [@Goldman] proved $\widehat{\Gamma}(\Sigma_g)$ acts ergodically. Let $\hat\rho: \widehat\Gamma(\Sigma_g) \rightarrow \pi_0\operatorname{Symp}\EuScript{M}(\Sigma_g)$ denote the associated representation on groups of components.

::: Theorem
[]{#Thm:NotSymplectic label="Thm:NotSymplectic"} For $g\geq 2$, $\hat{\rho}: \widehat\Gamma(\Sigma_g) \longrightarrow \pi_0\operatorname{Symp}\EuScript{M}(\Sigma_g)$ does not factor through the symplectic group (i.e. $\hat\rho$ is non-trivial on the Torelli group). When $g=2$, $\hat\rho$ is faithful.
:::

The second statement is just Corollary [\[Cor:Faithful2\]](#Cor:Faithful2){reference-type="ref" reference="Cor:Faithful2"}, and it implies the first statement by an argument of Wehrheim and Woodward which we recall in Corollary [\[Cor:TorelliNontrivial\]](#Cor:TorelliNontrivial){reference-type="ref" reference="Cor:TorelliNontrivial"}. By contast, the action of $\widehat{\Gamma}(\Sigma_g)$ on $H^*(\EuScript{M}(\Sigma_g))$ factors through the symplectic group. Theorem [\[Thm:NotSymplectic\]](#Thm:NotSymplectic){reference-type="ref" reference="Thm:NotSymplectic"} answers a question of Dostoglou and Salamon [@DS2 Remark 5.6]. Donaldson's former student Michael Callahan proved (unfinished Oxford D. Phil thesis, circa 1993) that $\hat\rho$ distinguished the Dehn twist on a separating curve $\sigma \subset \Sigma_2$ from the identity. Callahan apparently used the gauge theoretic methods recalled in Section [\[Subsec:3manifolds\]](#Subsec:3manifolds){reference-type="ref" reference="Subsec:3manifolds"}, which seem less well suited to treat the general case. A related faithfulness result, for the action of a cousin of the 5-strand spherical braid group on a four-dimensional moduli space ${\mathbb P}^2\# 5\overline{{\mathbb P}}^2$ of parabolic bundles on $S^2$, was established by Seidel [@Seidel:4dim Example 2.13] using Gromov-Witten invariants and positivity of intersections of closed holomorphic curves in 4-manifolds.

There is also a fixed-point theorem valid at any genus: this is something of a digression from the main theme of the paper, but has some relevance in light of the conjectural description of $\EuScript{F}(\EuScript{M}(\Sigma_g))$ discussed in Section [\[Sec:Speculative\]](#Sec:Speculative){reference-type="ref" reference="Sec:Speculative"} below, and is needed for Corollary [\[Cor:AllSummands\]](#Cor:AllSummands){reference-type="ref" reference="Cor:AllSummands"}.

::: Theorem
[]{#Thm:FixPoint label="Thm:FixPoint"} If $\phi \in \operatorname{Symp}\EuScript{M}(\Sigma_g)$ represents a class in $im(\hat{\rho})$ then $\phi$ fixes a point of $\EuScript{M}(\Sigma_g)$.
:::

If $\psi \in \widehat\Gamma(\Sigma_g)$ lies in the Torelli group, then the Lefschetz number of $\hat\rho(\psi)$ is zero, and $\hat\rho(\psi)$ is isotopic to a diffeomorphism of $\EuScript{M}(\Sigma_g)$ without fixed points. Thus Theorem [\[Cor:Faithful2\]](#Cor:Faithful2){reference-type="ref" reference="Cor:Faithful2"} and [\[Thm:FixPoint\]](#Thm:FixPoint){reference-type="ref" reference="Thm:FixPoint"} both detect essentially symplectic phenomena. There is an obvious correspondence between fixed points of the action of $\phi$ on $\EuScript{M}(\Sigma_g)$, and representations of the fundamental group of the mapping torus of $\phi$. This gives a purely topological application of the main theorems.

::: Corollary
[]{#Cor:RepnGrowth label="Cor:RepnGrowth"} Let $Y \rightarrow S^1$ be a closed 3-manifold fibring over the circle with fibre $\Sigma_g$.

-   There is a non-abelian $SO(3)$-representation of $\pi_1(Y)$.

-   Suppose $g=2$ and $Y$ is hyperbolic. There are cyclic degree $d$ covers $Y_d\rightarrow Y$ for which the number of conjugacy classes of non-abelian $SO(3)$-representations of $\pi_1(Y_d)$ grows exponentially in $d$.
:::

The first result was proved by Kronheimer-Mrowka [@KM2] using gauge theory; the second (which should generalise to higher genus fibres) appears to be new though closely related results are in the literature, cf. Section [\[Subsec:3manifolds\]](#Subsec:3manifolds){reference-type="ref" reference="Subsec:3manifolds"}. In any case, it's interesting that these are amenable to techniques of symplectic geometry.
