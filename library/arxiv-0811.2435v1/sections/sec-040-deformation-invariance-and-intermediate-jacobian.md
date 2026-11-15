---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-040-deformation-invariance-and-intermediate-jacobian
section_title: "Deformation invariance and intermediate Jacobian"
section_number: null
pages: 112-115
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.963
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 51 sections: Front matter; Introduction; Counting problems for 3-dimensiona"
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
