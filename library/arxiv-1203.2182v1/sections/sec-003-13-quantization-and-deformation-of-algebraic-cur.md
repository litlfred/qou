---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-003-13-quantization-and-deformation-of-algebraic-cur
section_title: "Quantization and deformation of algebraic curves"
section_number: 1.3
pages: 4-6
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.891
latex_coverage_ratio: 0.929
doc_brief: "Volume Conjecture: Reﬁned and Categoriﬁed — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebraic curve, the zero"
---
The above structure -- and its "refinement" that we are going to construct -- is not limited to applications in knot theory. Similar mathematical structure appears in matrix models [@BIPZ; @Dijkgraaf:1990rs; @Fukuma:1990jw], in four-dimensional ${\mathcal{N}}=2$ supersymmetric gauge theories [@SW-I; @Nekrasov; @NS; @Braverman:2004cr], and in topological string theory [@ADKMV; @DHSV; @DHS; @ACDKV].

In all of these problems, the semiclassical limit is described by a certain "spectral curve" [\[Acurve\]](#Acurve){reference-type="eqref" reference="Acurve"} defined by the zero locus of $A(x,y)$. Motivated by application to knots, we shall refer to the function $A(x,y)$ as the $A$-polynomial even in situations where its form is not at all polynomial.

![Deformation and quantization of the $A$-polynomial. The horizontal arrows describe a deformation / refinement, such that the unrefined case corresponds to $t=-1$. The vertical arrows represent quantization, *i.e.* a lift of classical polynomials $A(x,y)$ and $A(x,y;t)$ to quantum operators.](AAAA){#fig:AAAA width="4.0in"}

Furthermore, in most of these problems the classical curve [\[Acurve\]](#Acurve){reference-type="eqref" reference="Acurve"} admits two canonical deformations with the corresponding parameters $q$ and $t$. The first one is the deformation quantization in which $x$ and $y$ turn into non-commutative generators of the Weyl algebra, *cf.* [\[xycomm\]](#xycomm){reference-type="eqref" reference="xycomm"}. The second deformation, parametrized by $t$, does not affect commutativity of $x$ and $y$, *i.e.* it is an ordinary deformation. How these deformations affect the classical curve defined by the zero locus of $A(x,y)$ is illustrated in Figure [1](#fig:AAAA){reference-type="ref" reference="fig:AAAA"}.

A systematic procedure for lifting the polynomial $A(x,y)$ to the quantum operator $\widehat A (\widehat x, \widehat y; q)$ is described in [@Tudor] for curves coming from triangulated 3-manifolds and, more generally, in [@abmodel] for abstract curves defined by the equation $A(x,y)=0$. The general approach of [@abmodel] is based on the topological recursion, which allows to compute $\widehat A (\widehat x, \widehat y; q)$ order by order in the $q$-expansion following the steps of [@Mironov; @Marino:2006hs; @eyn-or; @BKMP; @DijkgraafFuji-2] where similar computations of the partition function were discussed. Thus, under favorable conditions described in [@abmodel], the quantum operator $$\widehat A (\widehat x, \widehat y; q) \; = \; \sum_{m,n}\, a_{m,n}\, q^{c_{m,n}}\, \widehat x^m\, \widehat y^n
\label{Aqnice}$$ can be obtained simply from the data $\{ a_{m,n} \}$ of the original polynomial $A(x,y) = \sum a_{m,n} x^m y^n$ and from the data $\{ c_{m,n} \}$ of the Bergman kernel $B(u_1,u_2)$ which, for curves of arbitrary genus, is given by a derivative of the logarithm of the odd characteristic theta function. Specifically, given the Bergman kernel $B(u_1,u_2)$ for the classical curve [\[Acurve\]](#Acurve){reference-type="eqref" reference="Acurve"}, one can first compute the "torsion" $T(u)$, $$\log T (u) \; = \; \lim_{u_1 \to u_2=u} \int
\left( \frac{du_1 \, du_2}{(u_1 - u_2)^2} - B(u_1,u_2) \right) \,,$$ and then find the exponents $\{ c_{m,n} \}$ by solving $$\sum_{m,n}\, a_{m,n}\, c_{m,n}\, x^m y^n \; = \;
\frac{1}{2} \left( \frac{\partial_u A}{\partial_v A} \partial_v^2 + \frac{\partial_u T}{T} \partial_v \right) \; A$$ together with $A(x,y) = 0$. Substituting the resulting data $\{ c_{m,n} \}$ into [\[Aqnice\]](#Aqnice){reference-type="eqref" reference="Aqnice"} gives the quantization of $A(x,y)$. In the above equations we used the relations $$x = e^u, \qquad  \qquad y = e^v \,.  \label{xuyv}$$

In this paper, our main focus will be the deformation in the other direction, associated with the parameter $t$. Some prominent examples of classical $A$-polynomials and their $t$-deformations which we find are given in table [1](#table){reference-type="ref" reference="table"}. Important examples of quantum refined $A$-polynomials, which we will derive in this paper, are revealed in table [\[table-qt\]](#table-qt){reference-type="ref" reference="table-qt"}.

::: {#table}
    **Model**                 $A(x,y)$                                    $A^{\text{ref}} (x,y;t)$                       
  ------------- ------------------------------------ ------------------------------------------------------------------- --
     unknot                 $(1-x)(1-y)$                         $(1 + t^3 x) ( - t^{-3})^{1/2} - (1 - x) y$             
     trefoil             $(y-1) (y + x^3)$               $y^2 -\frac{1 - x t^2 + x^3 t^5 + x^4 t^6 + 2 x^2 t^2 (t+1)}{1  
                                                              + x t^3} y + \frac{(x-1) x^3 t^4}{1 + x t^3}$              
   tetrahedron           $1 - y + x(-y)^f$                                 $1 + t y - t x (-y)^f$                        
    conifold     $1 - y + x(-y)^f + Q x (-y)^{f+1}$         $1 + t y - t x (-y)^f + Q \sqrt{-t} \, x (-y)^{f+1}$         

  : Classical curves in prominent examples, in unrefined limit (which are well known, left column) and for general $t$ (derived in this paper, right column). In this paper we also derive refined $A$-polynomials for general $T^{2,2p+1}$ torus knots; for explicit examples for low values of $p$ see table [\[table_A-poly4\]](#table_A-poly4){reference-type="ref" reference="table_A-poly4"}. Note that in section [\[sec:Bmodel\]](#sec:Bmodel){reference-type="ref" reference="sec:Bmodel"} the deformation parameter $t$ is identified with $-q_1$ (when $q_2 = q = 1$).
:::
