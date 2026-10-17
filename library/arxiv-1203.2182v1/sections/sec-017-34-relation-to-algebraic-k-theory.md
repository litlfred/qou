---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-017-34-relation-to-algebraic-k-theory
section_title: "Relation to algebraic K-theory"
section_number: 3.4
pages: 50-54
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.99
---
[]{#sec:quantizability label="sec:quantizability"}

So far in this section we have discovered a number of refined $A$-polynomials $A^{\textrm{ref}}(x,y;t)$ for various knots, including the unknot ([\[At-unknot\]](#At-unknot){reference-type="ref" reference="At-unknot"}), the trefoil knot ([\[deformed_A-poly_trefoil\]](#deformed_A-poly_trefoil){reference-type="ref" reference="deformed_A-poly_trefoil"}), and more general $(2,2p+1)$ torus knots discussed in section [\[sec:saddle_point\]](#sec:saddle_point){reference-type="ref" reference="sec:saddle_point"}. For the unknot and for the trefoil knot we also found an explicit form of the quantum $A$-polynomial, given respectively in ([\[qAt-unknot\]](#qAt-unknot){reference-type="ref" reference="qAt-unknot"}) and [\[trefoil-Aqt\]](#trefoil-Aqt){reference-type="eqref" reference="trefoil-Aqt"}.

There is no doubt that such refined and quantum $A$-polynomials exist for other knots as well, and can be determined either by (generalizations of) the techniques we used here or via some other methods. In any case, when lifting the classical $t$-deformed $A$-polynomial to a quantum operator, one encounters an important subtlety: not all classical curves are quantizable, and the existence of a consistent quantum curve depends in a delicate way on the complex structure[^1] (*i.e.* on the coefficients in the defining equation) of the classical polynomial $A^{\textrm{ref}}(x,y;t)$. Therefore, one should always verify whether a classical $t$-deformed curve actually admits a consistent quantization.

We should stress that this issue of quantizability is much more delicate for refined $A$-polynomials compared to the ordinary ones. The coefficients of ordinary $A$-polynomials are merely integer numbers, and quantizability imposes non-trivial constraints on these numbers. Magically, all $A$-polynomials of knots and 3-manifolds automatically meet these conditions. In retrospect, this is not too surprising, for otherwise $SL(2,{\mathbb C})$ Chern-Simons would simply make no sense on 3-manifolds whose $A$-polynomials fail to meet these constraints [@Apol].

The coefficients of refined $A$-polynomials, on the other hand, are functions of an arbitrary continuous parameter $t$. Hence, at first it may not be entirely obvious how to reconcile arbitrariness of $t$ with the fact that certain functions of this parameter should satisfy rather strong constraints. In all examples that we have analyzed, something beautiful happens: as we explain below, it turns out that $t$ can be any root of unity. Therefore, it is also natural to think of $\hbar=\log q$ as a purely imaginary number, valued in $i \mathbb{Q}$. We conjecture that this is a general phenomenon: for any knot, quantizability of the refined $A$-polynomial $A^{\textrm{ref}}(x,y;t)$ requires $t$ to be a root of unity. This statement could be verified if new examples of refined $A$-polynomials are found or, conversely, this property could help in *finding* new examples of refined $A$-polynomials.

Before we explain the condition on $t$, let us recall in more detail the general quantizability criteria for curves [@Apol]. Let us consider a curve [\[Acurve\]](#Acurve){reference-type="eqref" reference="Acurve"}: $${\cal C }:\qquad \left\{(x,y)\in\mathbb{C}^*\times \mathbb{C}^*\Big|
A(x,y) \; = \; 0 \right\}\,,$$ and the corresponding partition function $Z=\exp(\frac{1}{\hbar}S_0+\ldots)=\exp(\frac{1}{\hbar}\int \log y \frac{dx}{x}+\ldots)$, as in ([\[VCparamref\]](#VCparamref){reference-type="ref" reference="VCparamref"}). One has to make sure that this partition function is well defined, which means that all periods of the 1-form ${\rm Im} \, \log y \frac{dx}{x}$ on the curve ${\cal C }$ are trivial, $$\oint_{\gamma} \Big( \log |x| d ({\rm arg} \, y) - \log |y| d ({\rm arg} \, x) \Big) \; = \; 0 \,,
\label{qcond0}$$ and that the periods of the 1-form ${\rm Re} \, \log y \frac{dx}{x}$ are rational multiples of $2 \pi i$, so that for all closed paths $\gamma$ on the curve ${\cal C }$ $$\frac{1}{4 \pi^2} \oint_{\gamma} \Big( \log |x| d \log |y| + ({\rm arg} \, y) d ({\rm arg} \, x) \Big) \; \in \; \mathbb{Q} .
\label{qcondQ}$$ The above conditions can be nicely reformulated in terms of algebraic K-theory [@abmodel]. Thus, the integrand $\eta(x,y)=\log |x| d ({\rm arg} \, y) - \log |y| d ({\rm arg} \, x)$ in [\[qcond0\]](#qcond0){reference-type="eqref" reference="qcond0"} is the image of the symbol $\{ x,y \} \in K_2 ({\cal C })$ under the regulator map [@Beilinson; @Bloch]. For curves it is not hard to see that $\eta(x,y)$ is closed, $d\eta=0$. However, the condition ([\[qcond0\]](#qcond0){reference-type="ref" reference="qcond0"}) means that $\eta(x,y)$ must actually be exact. In the language of algebraic K-theory, this means that the symbol $\{ x,y \} = 0$ must be trivial in $K_2 ({\mathbb C}({\cal C })) \otimes {\mathbb Q}$. This led two of the authors of the present paper to propose the following criterion for quantizability [@abmodel]: $${\cal C }~ \text{is quantizable} \qquad \Longleftrightarrow \qquad \{ x,y \} \in K_2 ({\mathbb C}({\cal C })) ~\text{is a torsion class}.
\label{quantcritK2}$$ Moreover, it is known that the above condition is equivalent to the existence of a decomposition [@Fernando] $$x \wedge y \; = \; \sum_i r_i z_i \wedge (1 - z_i) \qquad \qquad {\rm in~} \wedge^2 ({\mathbb C}({\cal C })^*) \otimes {\mathbb Q}
\label{qcondzz}$$ for some $z_i \in {\mathbb C}({\cal C })^*$ and $r_i \in {\mathbb Q}$. In turn, this also means that [@Fernando]: $$\text{$A(x,y)$ is tempered, {\it i.e.} the roots of all its face polynomials are roots of unity.}   \label{tempered}$$ By face polynomials we mean the following. We construct a Newton polygon corresponding to $A(x,y)=\sum_{i,j} c_{(i,j)} x^i y^j$, and to each point $(i,j)$ of this polygon we associate the coefficient $c_{(i,j)}$. Then, each face of the polygon consists of several points labeled, in order, by $k=0,1,2,\ldots$, so that the corresponding monomial coefficients for a given face can be relabeled as $c_k=c_{(i,j)}$. The face polynomial is defined, then, as $f(z)=\sum_k c_k z^k$. The condition ([\[tempered\]](#tempered){reference-type="ref" reference="tempered"}) states that all roots of face polynomials $f(z)$, constructed for all boundaries of the Newton polygon, must be roots of unity. It is this latter condition that we shall consider below in order to test quantizability of the refined $A$-polynomials.

### Quantizability of refined $A$-polynomials

We can now analyze under what conditions the refined $A$-polynomials which we found earlier are quantizable. Since we already found the explicit form of such refined polynomials $A^{\textrm{ref}}(x,y;t)$, in order to test quantizability we can simply apply the condition ([\[tempered\]](#tempered){reference-type="ref" reference="tempered"}). To this end, we need to identify face polynomials associated to the Newton polygons of various knots discussed earlier. We will analyze separately of the unknot, the trefoil knot, and more general $(2,2p+1)$ torus knots. We will also discuss an interesting relation between Newton polygons in the refined and unrefined cases.

<figure id="fig-unknotNewtonMatrix">
<div class="center">
<img src="AtUnknotNewtonMatrix" style="width:60.0%" />
</div>
<figcaption>Newton polygon for the unknot (left). Red circles denote monomials of the refined polynomial, and smaller yellow crosses denote monomials of the unrefined polynomial. In this example both Newton polygons look the same, so that positions of all circles and crosses overlap. More detailed structure of the refined <span class="math inline"><em>A</em></span>-polynomial is also shown in a matrix form on the right. Note, that the role of rows and columns is exchanged in both pictures: the monomial <span class="math inline"><em>c</em><sub><em>i</em>, <em>j</em></sub><em>x</em><sup><em>i</em></sup><em>y</em><sup><em>j</em></sup></span> is put in the place <span class="math inline">(<em>i</em>,<em>j</em>)</span> in the Newton polygon, and it corresponds to the entry <span class="math inline"><em>c</em><sub><em>i</em>, <em>j</em></sub></span> in the <span class="math inline">(<em>i</em>+1)<sup>th</sup></span> row and in the <span class="math inline">(<em>j</em>+1)<sup>th</sup></span> column of the matrix on the right.</figcaption>
</figure>

To start with we consider the unknot; as we will see, general features of this example will also be present for more general torus knot. The refined $A$-polynomial of the unknot has been found in ([\[At-unknot\]](#At-unknot){reference-type="ref" reference="At-unknot"}), and in the limit $t=-1$ it reduces as follows: $$A^{\text{ref}}_{{\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}} \; = \;
(1 + t^3 x) ( - t^{-3})^{1/2} - (1 - x) y \qquad \xrightarrow[\ t\to -1\ ]{}  \qquad  (1-x)(1-y).$$ We present Newton polygons for these two polynomials in Figure [1](#fig-unknotNewtonMatrix){reference-type="ref" reference="fig-unknotNewtonMatrix"} (left). Bigger red circles denote monomials of the refined polynomial, while smaller yellow crosses denote monomials of the unrefined polynomial. In the unknot case, both Newton polygons coincide. From the matrix presentation of the refined $A$-polynomial given in Figure [1](#fig-unknotNewtonMatrix){reference-type="ref" reference="fig-unknotNewtonMatrix"} we can immediately write down face polynomials for all faces of the Newton polygon. These face polynomials are summarized in table [1](#tab-unknot){reference-type="ref" reference="tab-unknot"}; they are all linear in $z$ and their roots are $t^3$, $1$, $(-t)^{-3/2}$, and $-(-t)^{3/2}$. If we insist that the criterion ([\[tempered\]](#tempered){reference-type="ref" reference="tempered"}) should be satisfied, we conclude that the deformation parameter $t$ should be a root of unity.

::: {#tab-unknot}
       face             face polynomial
  -------------- ------------------------------
   first column   $(-t)^{-3/2} z + (-t)^{3/2}$
   last column               $z-1$
    first row          $(-t)^{-3/2} - z$
     last row           $(-t)^{3/2} + z$

  : Face polynomials for the unknot.
:::

Next, let us consider the class of $(2,2p+1)$ torus knots, for which the refined $A$-polynomials were found in section [\[sec:saddle_point\]](#sec:saddle_point){reference-type="ref" reference="sec:saddle_point"}. When $t=-1$ these polynomials reduce, for general $p$, to the following form[^2] $$A^{\text{ref}}_{T^{2,2p+1}}(x,y;t=-1) \; = \; (x - 1)^p (y - 1)  (y + x^{2p+1})^p \,.
\label{Atorus-nonrefined}$$ Interestingly, this form is closely related to the standard $A$-polynomials of $(2,2p+1)$ torus knots $(y-1)(y+x^{2p+1})$, up to an extra factor $(x-1)^p$ and the power of $p$ in the last factor. While it is desirable to understand the meaning of the form ([\[Atorus-nonrefined\]](#Atorus-nonrefined){reference-type="ref" reference="Atorus-nonrefined"}) better, here we note that its Newton polygon is related in an interesting way to the Newton polygon of the refined $A$-polynomial. Namely, Newton polygons of refined $A$-polynomials for $(2,2p+1)$ knots have hexagonal shape, as shown in Figure [2](#fig-31NewtonMatrix){reference-type="ref" reference="fig-31NewtonMatrix"} (left) for the trefoil, and in appendix [\[sec:AppendixB\]](#sec:AppendixB){reference-type="ref" reference="sec:AppendixB"} for other torus knots. (In all of these figures we use the same conventions as in Figure [1](#fig-unknotNewtonMatrix){reference-type="ref" reference="fig-unknotNewtonMatrix"}.) Then, the Newton polygons for the unrefined $A$-polynomials ([\[Atorus-nonrefined\]](#Atorus-nonrefined){reference-type="ref" reference="Atorus-nonrefined"}) have the same overall shape, with only one small difference: in their center a "rhomboidal" collection of points of size $p\times p$ is absent, as clearly seen in the figures in appendix [\[sec:AppendixB\]](#sec:AppendixB){reference-type="ref" reference="sec:AppendixB"}.

<figure id="fig-31NewtonMatrix">
<div class="center">
<img src="At31NewtonMatrix" style="width:86.0%" />
</div>
<figcaption>Newton polygons for the trefoil (left). Bigger red circles denote monomials of the refined polynomial, and smaller yellow crosses denote monomials of the unrefined polynomial. More detailed structure of the refined <span class="math inline"><em>A</em></span>-polynomial is also shown in matrix representation (right). All conventions are the same as in figure <a href="#fig-unknotNewtonMatrix" data-reference-type="ref" data-reference="fig-unknotNewtonMatrix">1</a>.</figcaption>
</figure>

Apart from Newton polygons, in Figure [2](#fig-31NewtonMatrix){reference-type="ref" reference="fig-31NewtonMatrix"} (right) and in appendix [\[sec:AppendixB\]](#sec:AppendixB){reference-type="ref" reference="sec:AppendixB"} we also present the matrix form of refined $A$-polynomials. From this presentation it is not hard to read off the face polynomials, and conjecture their form for general $p$, along each six faces of the hexagonal shape. These face polynomials are listed in table [2](#tab-torus){reference-type="ref" reference="tab-torus"}. Interestingly, all these polynomials factor into linear factors in $z$, and the constraint ([\[tempered\]](#tempered){reference-type="ref" reference="tempered"}) again leads to the aforementioned conclusion: the deformation parameter $t$ must be a root of unity.

::: {#tab-torus}
        face                 face polynomial
  ---------------- -----------------------------------
    first column         $-t^{2p(p+1)} (z-1)^p$
    last column            $(-1)^p (z+t^3)^p$
     first row                    $z-1$
      last row          $-t^{2p(p+1)} (z-t^{2p})$
   lower diagonal   $(-1)^p  t^{3p} (z - t^{2p+1})^p$
   upper diagonal     $(-1)^{p+1} (z + t^{2p+2})^p$

  : Face polynomials for $(2,2p+1)$ torus knots.
:::

Finally, let us consider the $A$-polynomials for the trefoil knot in

grading conventions of [@DGR], *cf.* [\[gradingtabl\]](#gradingtabl){reference-type="eqref" reference="gradingtabl"}. Newton polygons for both refined and unrefined $A$-polynomials are shown in Figure [\[fig-At31dgr-Newton\]](#fig-At31dgr-Newton){reference-type="ref" reference="fig-At31dgr-Newton"}. They are also of a hexagonal shape, though much bigger than the Newton polygon for the trefoil grading conventions of [@GS] shown in Figure [2](#fig-31NewtonMatrix){reference-type="ref" reference="fig-31NewtonMatrix"}. The matrix form of the refined $A$-polynomials in grading conventions of [@DGR] is presented in Figure [\[fig-At31dgr-matrix\]](#fig-At31dgr-matrix){reference-type="ref" reference="fig-At31dgr-matrix"}, and the corresponding face polynomials are listed in table [3](#tab-dgr){reference-type="ref" reference="tab-dgr"}. Again, it is easy to see that the quantizability condition ([\[tempered\]](#tempered){reference-type="ref" reference="tempered"}) is satisfied only if $t$ is a root of unity. Therefore, we conclude that, even though the explicit form of the refined $A$-polynomial $A^{\text{ref}} (x,y;t)$ may be sensitive to the choice of grading, the quantizability is independent of this choice.

::: {#tab-dgr}
        face                 face polynomial with $a=q^2$
  ---------------- -------------------------------------------------
    first column     $-t^3 (z - 1)^4 (t^2 z - 1)^2 (t^2 z + 1)^2$
    last column     $-t^{23} (t z - 1)^2 (t z + 1)^2 (t^3 z + 1)^4$
     first row               $-t^{34} (z - t) (t^5 z - 1)$
      last row                 $-(z - t^3) (t^3 z - 1)$
   lower diagonal                $-t^3 (t^5 z - 1)^4$
   upper diagonal               $-t^{11} (t^6 z + 1)^4$

  : Face polynomials for the trefoil knot in grading conventions of [@DGR].
:::

[^1]: At first, this may seem a little surprising, because the quantization problem is about symplectic geometry and not about complex geometry of ${\cal C }$. (Figuratively speaking, quantization aims to replace all classical objects in symplectic geometry by the corresponding quantum analogs.) However, our phase space ${\mathbb C}^* \times {\mathbb C}^*$ is very special in a sense that it comes equipped with a whole ${\mathbb{C}}{\mathbf{P}}^1$ worth of complex and symplectic structures, so that each aspect of the geometry can be looked at in several different ways, depending on which complex or symplectic structure we choose. This hyper-Kähler nature of our geometry is responsible, for example, for the fact that a curve ${\cal C }$ "appears" to be holomorphic (or algebraic). We put the word "appears" in quotes because this property of ${\cal C }$ is merely an accident, caused by the hyper-Kähler structure on the ambient space, and is completely irrelevant from the viewpoint of quantization. What is important to the quantization problem is that ${\cal C }$ is Lagrangian with respect to the symplectic form $\Omega = \frac{i}{\hbar} \frac{dx}{x} \wedge \frac{dy}{y}$.

[^2]: Here and in what follows, we multiply $A^{\text{ref}}_{T^{2,2p+1}}$ by a factor $(1+xt^3)^p$ to turn them into a nicer polynomial form.
