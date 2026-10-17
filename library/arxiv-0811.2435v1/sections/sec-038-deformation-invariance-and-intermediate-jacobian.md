---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-038-deformation-invariance-and-intermediate-jacobian
section_title: "Deformation invariance and intermediate Jacobian"
section_number: null
pages: 112-120
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
toc_source: outline
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.963
---
We also expect the following (not very precise) conjecture to be true as well.

::: conj
The collection $(\Omega(\gamma))_{\gamma \in \Gamma}$ is invariant with respect to the "polarization preserving\" deformations of $\CC$, in the case when $\CC$ is homologically smooth in the sense of [@KoSo3].
:::

The motivation for the last Conjecture is the deformation invariance of the virtual fundamental class in the "classical\" Donaldson-Thomas theory. Recall that homologically smooth $Ext$-finite categories can be thought as non-commutative analogs of smooth proper schemes. Hence, we can expect that the moduli stacks of semistable objects in such categories are also proper in some sense. Therefore, we can also expect that the degree of the virtual fundamental class is invariant under deformations.

Also, we expect the following generalization of our theory in the case when $\k=\C$ and the $3d$ Calabi-Yau category is homologically smooth (see [@KoSo3]).

1\) First, we recall that even without imposing the Calabi-Yau condition one expects that a triangulated compact homologically smooth $\A$-category $\CC$ (possibly $\Z/2\Z$-graded) admits (conjecturally) a non-commutative pure Hodge structure (see [@Ko2], [@KKP], [@KoSo3] about motivations, definitions as well as some conjectures and applications of this notion). In particular, periodic cyclic homology groups $HP_{even}(\CC)$ (resp. $HP_{odd}(\CC)$) carry descending Hodge filtrations $$\begin{array}{l}HP_{even}(\CC)\dots\supset F^i_{even}\supset F^{i-1}_{even}\supset\dots,\, i\in \Z\\
HP_{odd}(\CC)\dots\supset F^i_{odd}\supset F^{i-1}_{odd}\supset\dots,\, i\in \Z+{1\over{2}}\,\,.
\end{array}$$ In $3d$ Calabi-Yau case we assume that the smallest non-trivial term of the filtration $F^{\bullet}_{odd}$ is $F^{-3/2}, \dim F^{-3/2}=1$. Moreover, in general, it is expected that there are lattices $K_{top}^{even}(\CC)$ and $K_{top}^{odd}(\CC)$ which belong to the corresponding periodic cyclic homology groups (they represent the non-commutative version of the image of the topological $K$-theory in the de Rham cohomology).

2\) If $\CC$ is homologically smooth Calabi-Yau category then it is easy to see that (assuming the degeneration of the Hodge-to-de Rham conjecture, see [@KoSo3]) the moduli space ${\cal M}$ of formal deformations of $\CC$ is smooth of dimension $\dim {\cal M}={1\over{2}}\dim HP_{odd}(\CC)$ (this is a corollary of the formality of the little disc operad as well as the fact that the action of the Connes differential is represented by the rotation of the circle, which is homotopically trivial under the assumption). It is expected that the global moduli space also exists. Notice that the Calabi-Yau structure on $\CC$ induces a symplectic structure on the vector space $HP_{odd}(\CC)$ and in the $3d$ case the moduli space ${\cal M}$ is locally embedded into $HP_{odd}(\CC)$ as a Lagrangian cone.

3\) We expect that for an arbitrary triangulated compact homologically smooth $\A$-category $\CC$ one has a non-commutative version of the Deligne cohomology $H_{D}(\CC)$ which fits into a short exact sequence $$0\to HP_{odd}(\CC)/(F^{1/2}_{odd}+ K^{top}_{odd}(\CC))\to H_D(\CC)\to F^0_{even}\cap K^{top}_{even}(\CC)\to 0\,\,.$$ Morally, $H_D(\CC)$ should be thought as zero cohomology group of the homotopy colimit of the following diagram of cohomology theories: $$\begin{CD}  @. HC_\bullet^-(\CC)\\
  @. @VVV  \\
K^{top}_\bullet(\CC) @>>>  HP_\bullet(\CC)
\end{CD}$$ where $HC_\bullet^-(\CC)$ is the negative cyclic homology.

Any object of $\CC$ should have its characteristic class in $H_{D}(\CC)$. More precisely, there should be a homomorphism of groups $ch_D: K_0(\CC)\to H_{D}(\CC)$ (in the case of Calabi-Yau manifold it is related to holomorphic Chern-Simons functional). The reason for this is that every object $E\in Ob(\CC)$ has natural characteristic classes in $K^{top}_0(\CC)$ and in $HC_0^-(\CC)$ whose images in $HP_0(\CC)$ coincide with each other. The total space ${\cal M}^{tot}$ of the fibration ${\cal M}^{tot}\to {\cal M}$ with the fiber $H_{D}(\CC)$ over the point $[\CC]\in {\cal M}$ should be a holomorphic symplectic manifold (cf. [@DonM]). Moreover, any fiber of this fibration (i.e. the group $H_{D}(\CC)$ for given $[\CC]$) is a countable union of complex Lagrangian tori. By analogy with the commutative case we expect that the locus ${\cal L}\subset {\cal M}^{tot}$ consisting of values of $ch_D$ is a countable union of Lagrangian subvarieties. Every such subvariety can be either a finite ramified covering of ${\cal M}$ or a fibration over a proper subvariety of ${\cal M}$ with the fibers which are abelian varieties.

4\) For generic $[\CC]\in {\cal M}$ one can use the triple $(K_0(\CC),H_{D}(\CC),ch_D)$ instead of the triple $(K_0(\CC),\Gamma,\op{cl})$. Analogs of our motivic Donaldson-Thomas invariants $A_V^{mot}\in {\cal R}_V$ will be formal countable sums of points in $H_{D}(\CC)$ with "weights\" which are elements of the motivic ring ${\overline{D^{\mu}}}$. The pushforward map from $H_{D}(\CC)$ to $\Gamma=F^0_{even}\cap K^{top}_{0}(\CC)$ gives the numerical DT-invariants. The continuity of motivic DT-invariants means that after taking the quasi-classical limit the weights become integer-valued functions on the set of those irreducible components of ${\cal L}$ which are finite ramified coverings on ${\cal M}$.

These considerations lead to the following

::: que
Is there a natural extension of the numerical DT-invariants to those components of ${\cal L}$ which project to a proper subvariety of ${\cal M}$?
:::

::: rmk
Let us notice the similarity of the above considerations with those in the theory of Gromov-Witten invariants. Suppose $X$ is a $3d$ complex compact Calabi-Yau manifold with $H^1(X,\Z)=0$. Then we have an exact sequence $$0\to H^3_{DR}(X)/(F^2H^3_{DR}(X)+H^3(X,\Z))\to H^4_D(X)\to H^4(X,\Z)\to 0\,\,,$$ where $H^4_D(X)={\mathbb H}^4(X,\Z\to {\cal O}_X\to \Omega^1_X)$ is the Deligne cohomology. Then any curve $C\subset X$ defines the class $[C]\in H^4_D(X)$. For a generic complex structure on $X$ the class is constant in any smooth connected family of curves. Moreover, a stable map to $X$ defines a class in $H^4_D(X)$. Then we have exactly the same picture with holomorphic symplectic fibration ${\cal M}^{tot}\to {\cal M}$ with the Lagrangian fibers, as we discussed above. Similarly to the case of DT-invariants the GW-invariants appear as infinite linear combinations of points in $H^4_D(X)$, but this time with rational coefficients. We expect that the well-known relationship "GW=DT\" (see [@MaNOP]) should be a statement about the equality of the above-discussed counting functions (assuming positive answer to the above question).
:::

## Absence of poles in the series $A_V^{\op{Hall}}$

Here we are going to discuss a stronger version of the Conjecture 5.

::: conj
Let $\overline{D^+}:=\overline{{\cal M}^{\mu}}(Spec(\k))[{\mathbb L}^{-1/2}]$ be the ring of equivalence classes of motivic functions. Then the automorphism of the motivic quantum torus given by $x\mapsto A_V^{mot}x(A_V^{mot})^{-1}$ preserves the subring $\prod_{\gamma\in C(V)\cap \Gamma}\overline{D^+}\hat{e}_{\gamma}$ for all strict sectors $V\subset \R^2$.
:::

It is enough to check the conjecture for all $x=\hat{e}_{\gamma}, \gamma\in \Gamma$. Moreover, because of Factorization Property it is enough to consider the case when $V=l$ is a ray. In the latter case we can split the infinite product into those corresponding to different arithmetic progression, hence reducing the conjecture to the case when $Z(\Gamma)\cap \,l=\Z_{>0}\cdot\gamma_0$ for some non-zero $\gamma_0\in \Gamma$. Then we have $$A_l^{mot}=A_l^{mot}(\hat{e}_{\gamma_0})=1+\sum_{n\geqslant 1}c_n\hat{e}_{\gamma_0}^n\in \overline{D^{\mu}}[[\hat{e}_{\gamma_0}]]\,\,.$$ Using the commutation relations in the motivic quantum torus we have: $$A_l^{mot}(\hat{e}_{\gamma_0})\,\hat{e}_{\gamma}(A_l^{mot}(\hat{e}_{\gamma_0}))^{-1}=
\hat{e}_{\gamma}\,A_l^{mot}({\mathbb L}^{\langle \gamma_0,\gamma\rangle} \hat{e}_{\gamma_0})A_l^{mot}(\hat{e}_{\gamma_0})^{-1}\,\,.$$

Since for any series $f(t)=1+\dots$ we have $${f({\mathbb L}^nt)\over{f(t)}}={f({\mathbb L}^nt)\over{f({\mathbb L}^{n-1}t)}}\dots{f({\mathbb L}t)\over{f(t)}}\,\,,$$ in order to prove the conjecture it suffices to check that $$A_l^{mot}({\mathbb L} \hat{e}_{\gamma_0})A_l^{mot}(\hat{e}_{\gamma_0})^{-1}\in \overline{D^+}[[\hat{e}_{\gamma_0}]]\,\,.$$ Since in that case we are dealing with objects whose central charges belong to the ray $l$, we can restrict ourselves to the subcategory $\CC_l$. The latter can be thought of as a heart of the $t$-structure of an ind-constructible $3d$ Calabi-Yau category with *vanishing* Euler form. More precisely, $\CC_l(\kk)$ is an abelian artinian category with $\op{Hom}_{\CC_l(\kk)}(E,F):=\op{Ext}^0_{\CC(\kk)}(E,F)$. Then $K_0(\CC_l(\kk))\simeq \oplus_{E\ne 0}\Z\cdot[E]$, where the sum runs over the set of non-zero simple objects of $\CC_l(\kk)$.

Next, we can reduce the conjecture to a special case when $\op{cl}_{\k}(E)=\gamma_0$ is a fixed class for all simple objects $E$ of $\CC_l(\kk)$. Indeed, let us consider an ind-constructible homomorphism $\op{cl}_{\k}^{\prime}:K_0(\CC_l(\kk))\to \Gamma^{\prime}:=\Z\oplus \Z$ such that $\op{cl}_{\k}^{\prime}(E)=(1,0)$ if $\op{cl}_{\k}(E)=\gamma_0$ and $\op{cl}_{\k}^{\prime}(E)=(0,1)$ if $\op{cl}_{\k}(E)\in \{2\gamma_0,3\gamma_0,\dots\}$ for a simple object $E$. Let choose two complex numbers $z_1,z_2$ in such a way that $0<\op{Arg}(z_1)<\op{Arg}(z_2)<\pi$ and define a central charge $Z^{\prime}:\Gamma^{\prime}\to \C$ by the formula $Z^{\prime}((1,0))=z_1, Z^{\prime}((0,1))=z_2$. In this way we obtain a new stability structure on the triangulated envelope of $\CC_l(\kk)$ with the same heart. In particular, the element $A_l^{mot}$ will be decomposed into an infinite product: $$A_l^{mot}=\prod^{\longrightarrow}A_{l^{\prime}}^{mot}$$ of series $A_{l^\prime}^{mot}$ corresponding to abelian categories $\CC_{l^{\prime}}(\kk)$ for the new stability structure. One of these categories will be the subcategory generated by simple objects $E$ such that $\op{cl}_{\k}^{\prime}(E)=\gamma_0$. Let us call such category *pure of class $\gamma_0$*. All other categories $\CC_{l^{\prime}}(\kk)$ do not contain objects with the class $\gamma_0$. Repeating the procedure we reduce the conjecture to the case of pure category of the class $m\gamma_0$ for some $m\geqslant 1$. Similarly to the above arguments we can reduce it further to the case $m=1$. In this case the conjecture follows from the one below which concerns Hall algebras of categories which are no longer required to carry a Calabi-Yau structure.

In order to formulate this new conjecture we are going to use the following set-up. Let $({\CC},{\cal A})$ be a pair consisting of an ind-constructible triangulated $\A$-category over a ground field $\k$ and ${\cal A}\subset Ob({\CC})$ be an ind-constructible subset such that ${\cal A}(\overline{\k})$ is the heart of a bounded $t$-structure in ${\CC}(\overline{\k})$. We assume that simple objects of the abelian category ${\cal A}(\overline{\k})$ form a constructible subset of $Ob({\CC})(\overline{\k})$ and every object in ${\cal A}(\overline{\k})$ is a finite extension of simple ones. These data are equivalent to a special kind of an ind-constructible category with a stability structure. Namely, let us take $\Gamma:=\Z$ and define $\op{cl}_{\overline{\k}}(E)=1$ for every simple object of ${\cal A}(\overline{\k})$. It follows that $\op{cl}_{\overline{\k}}(F)=length(F)$ for any object of ${\cal A}(\overline{\k})$. Furthermore, we choose a complex number $z_0$ in the upper-half plane and define a central charge $Z:\Gamma\to \C$ by the formula $Z(1)=z_0$. Then ${\cal A}=\CC_l$ for $l=\R_{>0}\cdot z_0$. Therefore the element $A_l^{\op{Hall}}$ defined for this stability structure can be thought of as a series in one variable: $$A_l^{\op{Hall}}(t)=1+\sum_{n\geqslant 1}c_nt^n.$$

Let us define a subalgebra $H^+(\CC) \subset H(\CC)$ to be the set of linear combination of elements of the form $${\mathbb L}^n \cdot [Z\to Ob(\CC)]$$ where $n\in \Z$ and $Z\to Ob(\CC)$ is a 1-morphism of ind-constructible stacks (see Section 4.2) with $Z$ being an ordinary constructible set endowed with trivial action of the trivial group. The multiplication law in $H(\CC)$ preserves such class of elements.

::: conj
The element $F_l(t):=A_l^{\op{Hall}}({\mathbb L}t)A_l^{\op{Hall}}(t)^{-1}$ belongs to the completed Hall algebra $\widehat{H^+}(\CC)$ (i.e. we do not invert motives $[GL(n)], n\geqslant 1$ of the general linear groups).
:::

Below we discuss two special cases in which the above conjecture holds. But first we present a similar motivating statement in the case of finite fields. Let $R$ be finitely generated algebra over a finite field ${\bf F}_q$, and $R-mod^f$ denotes the category of finite-dimensional (over ${\bf F}_q$) left $R$-modules. We define the Hall algebra $H(R-mod^f)$ as a unital associative algebra over the ring $\Z[{1\over{q}}]$ generated by the isomorphism classes $[M]$ of objects of $R-mod^f$ with the multiplication $$[E]\cdot [F]=q^{-\dim \op{Hom}(F,E)}\sum_{\alpha\in \op{Ext}^1(F,E)}[E_{\alpha}]\,\,,$$ where, as before, $E_{\alpha}$ denotes an extension with the class $\alpha$.

::: prp
Let $$A(t):=\sum_{[M]\in Iso(R-mod^f)}{[M]\over{\#\op{Aut}(M)}}t^{\,\dim M}\,\,.$$ Then $$F(t):=A(qt)A(t)^{-1}\in H(R-mod^f)[[t]]\,\,.$$ Moreover, $$F(t)=\sum_{I\subset R, I=RI,\, \dim R/I<\infty}[R/I]t^{\,\dim R/I}\,\,.$$
:::

Hence the quotient $F(t)$ does not have denominator $(q^n-1), n\geqslant 1$ and can be represented in terms of the "non-commutative Hilbert scheme\" of left ideals in $R$ of finite codimension.

*Proof.* Let us make use of the basis of "renormalized\" elements $$\widehat{[E]}:={[E]\over{\#\op{Aut}(E)}}$$ in the $\Q$-algebra $H(R-mod^f)\otimes \Q$. Then the product can be rewritten in a more familiar form: $$\widehat{[E]}\cdot\widehat{[F]} =\sum_{[G]}c_{\widehat{[E]},\widehat{[F]}}^{\widehat{[G]}}\widehat{[G]},$$ where the structure constant $c_{\widehat{[E]},\widehat{[F]}}^{\widehat{[G]}}\in \Z$ denotes the number of subobjects in $G$ isomorphic to $E$ and such that the quotient is isomorphic to $F$. In these notation we have: $$A(t)=\sum_{[M]}\widehat{[M]}t^{\dim M}\,\,.$$ Since first statement of the Proposition follows from the second one, we are going to show the latter. In the new notation it becomes: $$\sum_{I\subset R, I=RI, \,\dim R/I<\infty}\widehat{[R/I]}\#\op{Aut}(R/I)\,t^{\dim R/I}\cdot\sum_{[M]}\widehat{[M]}\,t^{\dim M}=$$ $$=\sum_{[N]}\widehat{[N]}\,q^{\dim N}t^{\dim N}\,\,.$$ Let us fix an object $N$, and consider the coefficient of the term $\widehat{[N]}t^{\dim N}$. In the RHS it is equal to $q^{\dim N}$. It is easy to see that the corresponding coefficient in the LHS is of the form $$\sum_{I\subset R, I=RI, \,\dim R/I<\infty}\,\,\sum_{N^{\prime}\subset N,\, N^{\prime}\simeq R/I}\#\op{Aut}(R/I)=$$ $$=\sum_{I\subset R, I=RI, \,\dim R/I<\infty}\,\,\sum_{R/I\hookrightarrow N}1=\#N=q^{\dim N}.$$ Notice that in the last sum we consider all possible embeddings of $R/I$ to $N$ and every summand corresponds to a choice of a cyclic vector in a cyclic submodule in $N$. This proves the Proposition. $\blacksquare$

The above Proposition suggest to interpret our category as a category of modules and then apply similar arguments which reduce the sum (or even the motivic integral) to the sum over all cyclic submodules. It is useful to keep this in mind when considering two examples in the next subsection.

::: rmk
The subalgebra $H^+(\CC)$ of the Hall algebra has the advantage that one can apply the Euler characteristic $\chi$ to its elements fiberwise over $Ob(\CC)$ , and get a constructible $\Z$-valued function (with constructible support) on the ind-constructible set $Iso(\CC)$ of isomorphism classes of objects of $\CC(\kk)$. The multiplication in $H^+(\CC)$ descends to a multiplication on the abelian group of such functions. It is easy to see that this multiplication is commutative, and one has $$\nu_E \times \nu_F=\nu_{E\oplus F}$$ where $\nu_E$ etc. are delta-functions (see Section 6.1). This follows from the fact that for any non-zero $\alpha \in \op{Ext}^1(F,E)$ all objects $E_{t \alpha}$ are isomorphic to each other for $t\in \kk^\times$, and the Euler characteristic of ${\mathbf G}_m$ is zero.
:::
