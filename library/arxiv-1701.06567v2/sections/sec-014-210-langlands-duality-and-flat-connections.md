---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-014-210-langlands-duality-and-flat-connections
section_title: "Langlands duality and flat connections"
section_number: 2.10
pages: 24-27
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.988
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
[]{#sec:Langlands label="sec:Langlands"}

Motivated by the results of this paper, combined with [@Gukov:2016njj], we can make another conjecture:

::: conj
Let $G$ be a compact Lie group (not necessarily of ADE type) and $^LG$ its Langlands dual. Then, under S-duality, the boundary condition ${\mathcal B}_a$ corresponding to a connected component in ${\mathcal M}_{\text{flat}}^{\text{ab}} (M_3, G_{{\mathbb C}})$ of $G_{{\mathbb C}}$ flat connections on a 3-manifold $M_3$ maps to $${\mathcal B}_a \quad \mapsto \quad
{}^L{\mathcal B}_a \; = \; \sum_{{b \atop \text{abelian}}} S^{ab} \; (\, {\mathcal B}_b + \sum_{{c \atop \text{non-abelian}}} n_{bc} \; {\mathcal B}_c \, )
\label{Langlands}$$ where $S_{ab}$ is the S-matrix as in Conjecture [\[Conjecture1\]](#Conjecture1){reference-type="ref" reference="Conjecture1"} and $n_{bc}$ are the transseries coefficients from [@Gukov:2016njj]. []{#conjLanglands label="conjLanglands"}
:::

In formulating this Conjecture, we used ${\mathcal B}_a$ (instead of $a$) to emphasize its role as a boundary condition on $\partial (D^2\times_q S^1) = T^2$. The mapping class group $SL(2,{\mathbb Z})$ of the 2-torus acts on the boundary conditions and we claim that, at least for boundary conditions associated with abelian flat connections, the S-transformation is given by [\[Langlands\]](#Langlands){reference-type="eqref" reference="Langlands"}. Indeed, at the "far end" of the cigar, the geometry of the fivebrane world-volume looks like ${\mathbb R}\times M_3 \times T^2$, and we can first reduce on $T^2$ to obtain 4d ${\mathcal N}=4$ super-Yang-Mills on ${\mathbb R}\times M_3$. The mapping class group of $T^2$ then becomes the S-duality group of 4d ${\mathcal N}=4$ SYM, in particular, exchanging $G$ and $^LG$ under the electric-magnetic duality.

When $G$ is of Cartan type A or D, the left-hand side of [\[Langlands\]](#Langlands){reference-type="eqref" reference="Langlands"} is the choice of boundary condition we used in [\[aHW\]](#aHW){reference-type="eqref" reference="aHW"}, whereas the right-hand side describes the boundary condition that gives ${\mathcal H}_a [M_3]$ and is used in most of the paper. Then, Conjecture [\[conjLanglands\]](#conjLanglands){reference-type="ref" reference="conjLanglands"} is basically a statement that both sets of boundary conditions lead to integrality and are compatible.

## 3-manifolds and the "bottom row"

Using a relation between the physical realizations of 3-manifold homology and a HOMFLY-PT homology, respectively, we can produce a purely *mathematical* relation between the familiar knot homologies and less familiar 3-manifold homologies of this paper.

Namely, the familiar setup for homology of a knot $K\subset S^3$ involves $Q$-cohomology (space of BPS states) of the following system: $$\begin{array}{rcl}
\multicolumn{3}{c}{~~\text{doubly-graded}~} \\[.1cm]
\hline
{\mbox{\rm space-time:}} && ~~  {\mathbb R}\times T^* S^3 \times TN \\
{\mbox{\rm $N$ M5-branes:}} && ~~  {\mathbb R}\times ~S^3~ \times ~D^2 \\
{\mbox{\rm M5$'$-branes:}} && ~~  {\mathbb R}\times ~L_K~ \times  ~D^2
\end{array}
\quad \xleftarrow[~\text{transition}]{~\text{phase}} \!\!\! \to \quad

\begin{array}{rcl}
\multicolumn{3}{c}{~~~\text{triply-graded}~~} \\[.1cm]
\hline
&& {\mathbb R}\times X \times  ~TN \\
{\mbox{\rm M5$'$:}} && {\mathbb R}\times L_K \times  D^2
\end{array}
\label{conifoldphases}$$ where $L_K$ is the conormal bundle of the knot $K$, and $X$ is the resolved conifold, *i.e.* the total space of ${\mathcal O}(-1) \oplus {\mathcal O}(-1)$ bundle over ${\mathbb{C}}{\mathbf{P}}^1$.

Note, on the triply-graded ("resolved") side the original M5-branes disappear and we are only left with a system of M5$'$-branes in a non-trivial Calabi-Yau background $X$. This is very similar to a physical realization of 3-manifold homology in [\[CatGeom0\]](#CatGeom0){reference-type="eqref" reference="CatGeom0"} or [\[CatGeom1\]](#CatGeom1){reference-type="eqref" reference="CatGeom1"} where, compared to the right-hand side of [\[conifoldphases\]](#conifoldphases){reference-type="eqref" reference="conifoldphases"}, the Lagrangian 3-manifold $M_3$ plays the role of $L_K$. Indeed, according to the McLean's theorem, the neighborhood of the Lagrangian submanifold $L_K \subset X$ in [\[conifoldphases\]](#conifoldphases){reference-type="eqref" reference="conifoldphases"} can be identified with the total space of the cotangent bundle, $$N (L_K) \; \cong \; T^* L_K$$ which is precisely the setup of [\[CatGeom1\]](#CatGeom1){reference-type="eqref" reference="CatGeom1"}. There is an important difference, however.

While in [\[CatGeom1\]](#CatGeom1){reference-type="eqref" reference="CatGeom1"} the Calabi-Yau space is simply the cotangent bundle to the Lagrangian 3-manifold $M_3$, in [\[conifoldphases\]](#conifoldphases){reference-type="eqref" reference="conifoldphases"} it only looks like $T^* L_K$ in the neighborhood of $L_K$. Globally, the topology of $X$ is different from $T^* L_K$ and, in particular, has non-trivial relative homology group $$H_2 (X,L_K) \cong {\mathbb Z}.$$ It plays an important role in the physical realization of the colored HOMFLY-PT homology of the knot $K$; namely, the conserved charge captured by this relative homology is the so-called $a$-grading of the HOMFLY-PT homology of $K$.

As in [@Gorsky:2013jxa], we can bridge the gap between the two systems [\[CatGeom1\]](#CatGeom1){reference-type="eqref" reference="CatGeom1"} and [\[conifoldphases\]](#conifoldphases){reference-type="eqref" reference="conifoldphases"} by taking the limit[^1] $$\log (a) = \text{Vol} ({\mathbb{C}}{\mathbf{P}}^1) \to \infty.
\label{alimit}$$ This limit has a simple interpretation in almost every duality frame. For example, from the vantage point of the Calabi-Yau 3-fold $X$ it corresponds to the limit $$X \quad \leadsto \quad {\mathbb C}^3
\label{Xlimit}$$ that, on the toric diagram of the resolved conifold $X$, corresponds to moving two trivalent vertices far away from each other. Keeping only one vertex in sight, we end up with ${\mathbb C}^3$ (whose enumerative invariants are counted by the refined topological vertex). After making this replacement in [\[conifoldphases\]](#conifoldphases){reference-type="eqref" reference="conifoldphases"}, we obtain a simpler fivebrane system, whose BPS spectrum ($Q$-cohomology) categorifies only the bottom (resp. top) row of the HOMFLY-PT polynomial that contains the terms with minimal (resp. maximal) $a$-degree [@Gorsky:2013jxa].

::: {#tab:examples}
    Knot $K$     ${\mathcal H}_{\text{bottom}} (K)$
  ------------- ------------------------------------
   ${\bf 3_1}$           $q^{-2} + q^2 t^2$
   ${\bf 4_1}$                $t^{-2}$
   ${\bf 5_1}$        $q^{-4} + t^2 + q^4 t^4$
   ${\bf 5_2}$         $q^{-2} + t + q^2 t^2$
   ${\bf 6_1}$        $t^{-2} + q^{-2} t^{-1}$

  : The reduced Poincaré polynomial of the bottom row of the HOMFLY-PT homology for simple knots colored by $\lambda = \Box$. The unreduced HOMFLY-PT homology is infinite-dimensional and its Poincaré "polynomial" is, in fact, a power series in $q$ and $t$.
:::

Now, after taking the limit [\[alimit\]](#alimit){reference-type="eqref" reference="alimit"}--[\[Xlimit\]](#Xlimit){reference-type="eqref" reference="Xlimit"}, the second cohomology of $X$ is trivial and there is no winding around ${\mathbb{C}}{\mathbf{P}}^1$ that we had in the original system [\[conifoldphases\]](#conifoldphases){reference-type="eqref" reference="conifoldphases"}. This, of course, corresponds to the fact that, by taking the limit, we lost the $a$-grading focusing only on terms with the lowest $a$-degree. The $q$-degree and $t$-degree, however, are still present and come from $U(1)_q \times U(1)_R$ symmetry acting on $D^2 \subset TN$.

To summarize, by taking the limit [\[alimit\]](#alimit){reference-type="eqref" reference="alimit"}--[\[Xlimit\]](#Xlimit){reference-type="eqref" reference="Xlimit"} in the physical system [\[conifoldphases\]](#conifoldphases){reference-type="eqref" reference="conifoldphases"}, we obtain a relation between the bottom row of the HOMFLY-PT homology of $K$ and the homology of the 3-manifold $M_3 = L_K$: $${\mathcal H}_{\text{bottom}} (K) \; \cong \; {\mathcal H}(M_3).
\label{knotsvsmflds}$$ In fact, the geometry and topology of $M_3 = L_K$ is closely related to that of the knot complement $S^3 \setminus K$, see [@Aganagic:2013jpa]. Namely, for a knot (= a link with one component), both $M_3 = L_K$ and $S^3 \setminus K$ have $H_1 \cong {\mathbb Z}$. In particular, in both cases the abelian flat connections are labeled by ${\mathbb C}^*$-valued holonomies $x_1, \ldots, x_N$.

Note, [\[knotsvsmflds\]](#knotsvsmflds){reference-type="eqref" reference="knotsvsmflds"} is a purely mathematical relation whose left-hand side is knot homology and whose right-hand side is a 3-manifold homology. One can explore it and try to make it more concrete, in particular using the physical setup [\[CatGeom1\]](#CatGeom1){reference-type="eqref" reference="CatGeom1"} and [\[conifoldphases\]](#conifoldphases){reference-type="eqref" reference="conifoldphases"}. First, we need to develop a more precise dictionary between the RHS and LHS of [\[knotsvsmflds\]](#knotsvsmflds){reference-type="eqref" reference="knotsvsmflds"}. Following the above derivation, we see that the M5$'$-branes in [\[conifoldphases\]](#conifoldphases){reference-type="eqref" reference="conifoldphases"} correspond to M5-branes in [\[CatGeom1\]](#CatGeom1){reference-type="eqref" reference="CatGeom1"}. Therefore, the $sl(N)$ homology of $M_3 = L_K$ gets related to the bottom row of $\lambda$-colored HOMFLY-PT homology of $K$, where $\lambda$ is a partition with $N$ rows (or $N$ columns). Moreover, as in [@Ooguri:1999bv; @Labastida:2000yw], we need to relate the "partition basis" (natural on the LHS of [\[knotsvsmflds\]](#knotsvsmflds){reference-type="eqref" reference="knotsvsmflds"}) to the "holonomy basis" (natural on the RHS of [\[knotsvsmflds\]](#knotsvsmflds){reference-type="eqref" reference="knotsvsmflds"}). And, finally, it is important to keep in mind that in relating the physical systems [\[CatGeom1\]](#CatGeom1){reference-type="eqref" reference="CatGeom1"} and [\[conifoldphases\]](#conifoldphases){reference-type="eqref" reference="conifoldphases"} we obtain a relation [\[knotsvsmflds\]](#knotsvsmflds){reference-type="eqref" reference="knotsvsmflds"} that involves unreduced knot homology[^2] in the sense of [@khovanov2008matrix].

As a warm-up, let us take a closer look at the simple case of $N=1$ and $\lambda = \Box$. Recall, that $L_K$ is a special Lagrangian submanifold in ${\mathbb R}^6 \cong {\mathbb C}^3$. The moduli space ${\mathcal M}(L_K)$ of its Lagrangian deformations, together with a local system that it carries, is the space of SUSY vacua of 3d ${\mathcal N}=2$ theory $T[L_K;U(1)]$ on a circle, $${\mathcal M}(L_K) \; \cong \; {\mathcal M}_{\text{SUSY}} (T[L_K;U(1)]) \; \cong \; {\mathcal M}_{\text{flat}} (L_K, U(1)_{{\mathbb C}}),
\label{MLK}$$ where in the last relation we used the McLean theorem. The cohomology of this moduli space is precisely the bottom row of the HOMFLY-PT homology of $K$ colored by $\lambda = \Box$ [@Shende:2014ira]: $${\mathcal H}_{\text{bottom}} (K) \; \cong \; H^* ({\mathcal M}(L_K)).$$ In [@Shende:2015mzx], the moduli space ${\mathcal M}(L_K)$ is described as a cluster variety.

Another simple example is $K = \text{unknot}$ and $\lambda = S^r$ (or $\lambda = \Lambda^r$), a single-row Young tableaux. The corresponding superpolynomial is $${\mathcal P}^{S^r}_{\text{bottom}} (\text{unknot}) \; = \; \prod_{i=1}^r \frac{1}{1-q^{2i} t^{2(i-1)}} \,.
\label{SrHOMFLY}$$ These expressions can be found as $x^r$-coefficients of $Z_{\text{vortex}} (x;q,t)$ for a single 3d ${\mathcal N}=2$ chiral multiplet. More generally, for $K = \text{unknot}$ colored by Young diagrams with $n$ rows (or columns) we end up with the $S^1 \times D^2$ vortex partition function of $n$ 3d ${\mathcal N}=2$ chiral multiplets. This has to be compared with $gl(n)$ homology of $M_3 = S^3 \setminus (\text{unknot})$.

It would be useful to develop the relation [\[knotsvsmflds\]](#knotsvsmflds){reference-type="eqref" reference="knotsvsmflds"} between the familiar HOMFLY-PT homology and the less familiar 3-manifold homology further. We leave this to future work and now turn to detailed analysis of the latter.

[^1]: Note, in relating HOMFLY-PT homology to $sl(N)$ knot homology one sets $a = q^N$, so that $\log (a) \sim N$.

[^2]: The reduced HOMFLY-PT homology categorifies normalized HOMFLY-PT polynomial; it is finite-dimensional for $\lambda = \Box$ and links with one component (*i.e.* for knots). The unreduced version, on the other hand, categorifies unnormalized HOMFLY-PT polynomial and is infinite-dimensional for any color $\lambda$. The former has no obvious analogue for 3-manifolds.
