---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-023-341-quantizability-of-refined-a-polynomials
section_title: "Quantizability of refined $A$-polynomials"
section_number: 3.4.1
pages: 52-54
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.99
doc_brief: "Volume Conjecture: Reﬁned and Categoriﬁed — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebraic curve, the zero"
---
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

Next, let us consider the class of $(2,2p+1)$ torus knots, for which the refined $A$-polynomials were found in section [\[sec:saddle_point\]](#sec:saddle_point){reference-type="ref" reference="sec:saddle_point"}. When $t=-1$ these polynomials reduce, for general $p$, to the following form[^1] $$A^{\text{ref}}_{T^{2,2p+1}}(x,y;t=-1) \; = \; (x - 1)^p (y - 1)  (y + x^{2p+1})^p \,.
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

[^1]: Here and in what follows, we multiply $A^{\text{ref}}_{T^{2,2p+1}}$ by a factor $(1+xt^3)^p$ to turn them into a nicer polynomial form.
