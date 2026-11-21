---
doc_id: arxiv-1504.07260v3
doc_title: "Fricke S-duality in CHL models"
section_id: sec-001-11-fricke-s-duality
section_title: "Fricke S-duality"
section_number: 1.1
pages: 3-8
source_pdf: 1504.07260v3.pdf
source_sha256: 707cb014400a3f05
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.92
doc_brief: "Fricke S-duality in CHL models — We consider four dimensional CHL models with sixteen spacetime supersym- metries obtained from orbifolds of type IIA superstring on K3×T 2 by a ZN symmetry acting"
---
Consider heterotic string theory on $T^6$ and decompose the torus according to $T^6=T^4 \times S^1\times \tilde{S}^1$. We want to take the orbifold of this by a cyclic group $G$ of symmetries that preserve all the spacetime supersymmetries. This implies, in particular, that $G$ must act trivially on the left-moving (supersymmetric) sector. From the type IIA perspective, the target space is $K3\times S^1\times \tilde{S}^1$ and the orbifold group must be a symmetry of the $\mathcal{N}=(4,4)$ superconformal sigma model $\mathcal{C}$ on $K3$. All such symmetries were classified in [@K3symm] and shown to correspond to elements of the Conway group $Co_0$. The group $G$ acts by an automorphism $g\in O(\Gamma^{4,20})$ of order $N$ on the $K3$-sigma model and by a shift on the circle $S^1$.

Consider the limit where the heterotic axio-dilaton $S_{\text{het}}$ is large (i.e. $\mathop{\mathrm{Im}}S_{\text{het}} \to \infty$) so that the theory is weakly coupled. On the IIA side, this means that the radii of the circles $S^1\times \tilde{S}^1$ are large (but their ratio is fixed) since string-string duality interchanges $S_{\text{het}}$ with the type IIA Kähler modulus $T_{\text{IIA}}$. In this limit, the IIA theory decompactifies to a six dimensional theory, with the internal superconformal theory being the K3 sigma model $\mathcal{C}$. What is the strong-coupling limit of the theory? On the heterotic side this means $\mathop{\mathrm{Im}}S_{\text{het}} \to 0$ and it corresponds to the small-volume limit of the torus $S^1\times \tilde{S}^1$ in type IIA. For this reason it is natural to perform a double T-duality: first dualizing on $S^1$ to type IIB and then back to type IIA by T-dualizing on $\tilde{S}^1$. Let us call the dual torus $S'^1\times \tilde{S}'^1$. We show that this has the following effect on the Kähler modulus:

$$T_{\text{IIA}}\longrightarrow T^{\prime}_{\text{IIA}}= -\frac{1}{N T_{\text{IIA}}}.
\label{DoubleT}$$ Notice the unusual factor of $N$ in the denominator which is a consequence of the fact that we are T-dualizing on the 'special circle' $S^1$ upon which the orbifold group acts. The T-dual type IIA theory in the $\mathop{\mathrm{Im}}T'_{\text{IIA}}\to \infty$ limit is a six-dimensional theory described by a compactification $\mathcal{N}=(4,4)$ superconformal field theory $\mathcal{C}'$, which is simply the orbifold of $\mathcal{C}$ by $g$. For large but finite $\mathop{\mathrm{Im}}T'_{\text{IIA}}$, the theory is an orbifold of type IIA on $\mathcal{C}'\times {S'^1}\times{\tilde {S}'^1}$ by a group $G'$ acting by a shift along ${S'}^1$ and by an automorphism of $\mathcal{C}'$ (the quantum symmetry). As discussed in [@Gaberdiel:2012um], the theory $\mathcal{C}'$ can be either a non-linear sigma model on K3, or a sigma model on $T^4$. A similar construction was considered in [@Vafa:1997mh], where it was used to provide a geometrical interpretation of Montonen-Olive duality for non simply-laced groups.

<figure id="fig:case1">
<div class="center">
<embed src="Case1.pdf" style="width:14cm" />
</div>
<figcaption><span>The web of dualities in the case when the CHL model is self-dual under Fricke S-duality. The strongly coupled limit is given by the same CHL model at a different point in the moduli space.</span></figcaption>
</figure>

Consider the case when $\mathcal{C}'$ is a K3-sigma model. We can then use string-string duality to map $T_{\text{IIA}}$ to $S_{\text{het}}$ and the map ([\[DoubleT\]](#DoubleT){reference-type="ref" reference="DoubleT"}) becomes $$S_{\text{het}} \longrightarrow -\frac{1}{NS_{\text{het}}}.
\label{Fricke}$$ We call this transformation a *Fricke S-duality*. It relates the strongly coupled limit of a heterotic CHL model to the weakly coupled limit of another CHL model. The most interesting situation is when the dual models are just different points in the same connected component of the moduli space. In this case, we say that the CHL model is self-dual. We also show that the symmetry under Fricke S-duality extends to the full Atkin-Lehner subgroup of $SL(2,\mathbb{R})$. See Figure [1](#fig:case1){reference-type="ref" reference="fig:case1"} for a pictorial overview of the web of dualities; the non self-dual case is depicted in Figure [2](#fig:case2){reference-type="ref" reference="fig:case2"}.

This new type of S-duality yields non-trivial predictions for heterotic-type II duality. Let $\Lambda=\Lambda_e \oplus \Lambda_m$ be the electric-magnetic charge lattice of a *self-dual* CHL model. In the non-orbifold case, these are simply the Narain lattices of the compactification: $\Lambda_e\cong \Lambda_m\cong \Gamma^{6,22}$ but in general they will be sublattices. Now, although Fricke S-duality relates two CHL models at different points in the moduli space, the associated lattices are moduli-independent and must therefore be isomorphic. For this to hold the lattices must be $N$*-modular*, i.e. satisfy $$\begin{aligned}
{} && \Lambda_e\cong  \Lambda_e^{*}(1/N), 
\nonumber \\ 
{} && \Lambda_m\cong \Lambda_m^{*}(N).
\end{aligned}$$ Here, $\Lambda^{*}_{e}$ and $\Lambda^{*}_{m}$ denote the dual lattices and the parentheses $(n)$ indicates that the quadratic form of the lattice is rescaled by $n$. This is a very non-trivial prediction of Fricke S-duality that we verify explicitly by computing the charge lattices for several CHL models.

A particular class of CHL models can be defined by considering a symmetry $g$ of the K3 sigma model induced a symplectic automorphism of the K3 target space. It can be verified that all such 'geometric' CHL models are self-dual. In these cases, $N$-modularity of the electric-magnetic charge lattice immediately translates into the $N$-modularity of the $g$-invariant sublattice $(H^{*}(K3,\mathbb{Z}))^g$ of the (even) integral homology of the K3 surface. While these sublattices have been studied in the mathematical literature [@GarbagnatiSarti2009], their modularity properties have never been noticed before (to the best of our knowledge). It natural to wonder whether this observation admits a purely geometric interpretation, besides the present string theoretical analysis.

<figure id="fig:case2">
<div class="center">
<embed src="Case2.pdf" style="width:14cm" />
</div>
<figcaption><span>The web of dualities in the case when the Fricke S-duality maps from a strongly coupled heterotic CHL model to the weakly coupled limit of a different model, i.e. a different connected component in the moduli space of <span class="math inline">𝒩 = 4</span> theories.</span> </figcaption>
</figure>

The third case occurs when the orbifold non-linear sigma model $\mathcal{C}'$, obtained after the double T-duality, is a torus model. In this case, the six dimensional type IIA theory compactified on $\mathcal{C}'$ has no heterotic dual. Thus, the standard heterotic-type IIA duality does not hold and the above argument cannot be used to give a weak-coupling description of the CHL model. However, there exists another theory which is dual to type IIA on $(\mathcal{C}'\times {S'^1}\times{\tilde {S}'^1})/G'$ under the interchange of the Kähler and axio-dilaton moduli: this is again an orbifold of type IIA on $T^4\times S^1\times \tilde{S}^1$, where the orbifold symmetry acts by a shift on $S^1$ and only on the right-moving oscillators of the sigma model. Thus, this breaks all spacetime supersymmetries in the right-moving sector of the type IIA superstring. Following [@Sen:1995ff] we call this a theory of *(4,0)-type*. This should be contrasted with the previous case where the orbifold breaks half of the supersymmetries in both the right- and left-moving sector, giving rise to theories of *(2,2)-type*.

To summarise, in the first case the heterotic description of the CHL model is self-dual under the Fricke S-duality, while the corresponding type IIA description is self-dual under Fricke T-duality (see Figure [1](#fig:case1){reference-type="ref" reference="fig:case1"}), i.e. relates different points in the same connected component of the moduli space. In the second and third case we have webs of dualities with 4 corners. In case 2, Fricke S-duality maps a strongly coupled CHL model to the weakly coupled limit of a different CHL model (see Figure [2](#fig:case2){reference-type="ref" reference="fig:case2"}), i.e. relates two different components of the moduli space. In case 3, on the other hand, the weakly coupled description of the heterotic CHL model is instead given in terms of a genuinely different theory, namely a type IIA torus orbifold of $(4,0)$-type (see Figure [3](#fig:case3){reference-type="ref" reference="fig:case3"}).

<figure id="fig:case3">
<div class="center">
<embed src="Case3.pdf" style="width:14cm" />
</div>
<figcaption><span>The web of dualities in the case when the CHL model is not self-dual under Fricke S-duality, but maps from a strongly coupled heterotic theory to a genuinely different, weakly coupled type IIA theory. Note in particular that the weakly coupled theory in the lower left corner is of (4,0)-type (i.e. all supersymmetries in the right-moving sector are broken) while the type IIA theory on the right hand side is of (2,2)-type. </span> </figcaption>
</figure>

Inequivalent CHL models can be characterised via the eigenvalues of $g\in O(\Gamma^{4,20})$ in the defining 24-dimensional representation. This fact allows to characterise the order $N$ orbifold element $g$ in terms of its *generalised Frame shape* $$g \longleftrightarrow \prod_{a|N} a^{m(a)},
\label{frameshape}$$ where $m(a)$ are integers such that $\sum_{a|N} m(a) \, a=24$. For example, the identity element $e$ is represented by the Frame shape $1^{24}$ corresponding to a product of 24 identity permutations. The three different cases for the Fricke S-duality are easily distinguished by the Frame shape of $g$. For example, the Witten index of the non-linear sigma model $\mathcal{C}'$ (or equivalently, the Euler characteristic of its target space) is given by: $$\mathcal{I}^{\mathcal{C}'}=\sum_{a|N} m(N/a)\, a.$$ This reveals, in particular, that whenever the Frame shape is *balanced*, i.e. such that $$m(N/a)=m(a),$$ then $\mathcal{C}'$ is a K3-sigma model. This corresponds to the self-dual case, displayed in Figure [1](#fig:case1){reference-type="ref" reference="fig:case1"}. It turns out that it is also possible to have $\mathcal{I}^{\mathcal{C}'} =24$ even when the Frame shape is not balanced; this gives rise to case 2 (Figure [2](#fig:case2){reference-type="ref" reference="fig:case2"}). The third case then corresponds to $\mathcal{I}^{\mathcal{C}'} =0$ and yields the duality web in Figure [3](#fig:case3){reference-type="ref" reference="fig:case3"}.
