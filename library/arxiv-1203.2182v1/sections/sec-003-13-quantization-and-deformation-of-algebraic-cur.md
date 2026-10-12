---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-003-13-quantization-and-deformation-of-algebraic-cur
section_title: "Quantization and deformation of algebraic curves"
section_number: 1.3
pages: 4-8
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.898
latex_coverage_ratio: 0.929
---
The above structure -- and its "refinement" that we are going to construct -- is not limited to applications in knot theory. Similar mathematical structure appears in matrix models [@BIPZ; @Dijkgraaf:1990rs; @Fukuma:1990jw], in four-dimensional ${\mathcal{N}}=2$ supersymmetric gauge theories [@SW-I; @Nekrasov; @NS; @Braverman:2004cr], and in topological string theory [@ADKMV; @DHSV; @DHS; @ACDKV].

In all of these problems, the semiclassical limit is described by a certain "spectral curve" [\[Acurve\]](#Acurve){reference-type="eqref" reference="Acurve"} defined by the zero locus of $A(x,y)$. Motivated by application to knots, we shall refer to the function $A(x,y)$ as the $A$-polynomial even in situations where its form is not at all polynomial.

![Deformation and quantization of the $A$-polynomial. The horizontal arrows describe a deformation / refinement, such that the unrefined case corresponds to $t=-1$. The vertical arrows represent quantization, *i.e.* a lift of classical polynomials $A(x,y)$ and $A(x,y;t)$ to quantum operators.](AAAA){#fig:AAAA width="4.0in"}

Furthermore, in most of these problems the classical curve [\[Acurve\]](#Acurve){reference-type="eqref" reference="Acurve"} admits two canonical deformations with the corresponding parameters $q$ and $t$. The first one is the deformation quantization in which $x$ and $y$ turn into non-commutative generators of the Weyl algebra, *cf.* [\[xycomm\]](#xycomm){reference-type="eqref" reference="xycomm"}. The second deformation, parametrized by $t$, does not affect commutativity of $x$ and $y$, *i.e.* it is an ordinary deformation. How these deformations affect the classical curve defined by the zero locus of $A(x,y)$ is illustrated in Figure [1](#fig:AAAA){reference-type="ref" reference="fig:AAAA"}.

A systematic procedure for lifting the polynomial $A(x,y)$ to the quantum operator $\widehat A (\widehat x, \widehat y; q)$ is described in [@Tudor] for curves coming from triangulated 3-manifolds and, more generally, in [@abmodel] for abstract curves defined by the equation $A(x,y)=0$. The general approach of [@abmodel] is based on the topological recursion, which allows to compute $\widehat A (\widehat x, \widehat y; q)$ order by order in the $q$-expansion following the steps of [@Mironov; @Marino:2006hs; @eyn-or; @BKMP; @DijkgraafFuji-2] where similar computations of the partition function were discussed. Thus, under favorable conditions described in [@abmodel], the quantum operator $$\widehat A (\widehat x, \widehat y; q) \; = \; \sum_{m,n}\, a_{m,n}\, q^{c_{m,n}}\, \widehat x^m\, \widehat y^n
\label{Aqnice}$$ can be obtained simply from the data $\{ a_{m,n} \}$ of the original polynomial $A(x,y) = \sum a_{m,n} x^m y^n$ and from the data $\{ c_{m,n} \}$ of the Bergman kernel $B(u_1,u_2)$ which, for curves of arbitrary genus, is given by a derivative of the logarithm of the odd characteristic theta function. Specifically, given the Bergman kernel $B(u_1,u_2)$ for the classical curve [\[Acurve\]](#Acurve){reference-type="eqref" reference="Acurve"}, one can first compute the "torsion" $T(u)$, $$\log T (u) \; = \; \lim_{u_1 \to u_2=u} \int
\left( \frac{du_1 \, du_2}{(u_1 - u_2)^2} - B(u_1,u_2) \right) \,,$$ and then find the exponents $\{ c_{m,n} \}$ by solving $$\sum_{m,n}\, a_{m,n}\, c_{m,n}\, x^m y^n \; = \;
\frac{1}{2} \left( \frac{\partial_u A}{\partial_v A} \partial_v^2 + \frac{\partial_u T}{T} \partial_v \right) \; A$$ together with $A(x,y) = 0$. Substituting the resulting data $\{ c_{m,n} \}$ into [\[Aqnice\]](#Aqnice){reference-type="eqref" reference="Aqnice"} gives the quantization of $A(x,y)$. In the above equations we used the relations $$x = e^u, \qquad  \qquad y = e^v \,.  \label{xuyv}$$

In this paper, our main focus will be the deformation in the other direction, associated with the parameter $t$. Some prominent examples of classical $A$-polynomials and their $t$-deformations which we find are given in table [1](#table){reference-type="ref" reference="table"}. Important examples of quantum refined $A$-polynomials, which we will derive in this paper, are revealed in table [2](#table-qt){reference-type="ref" reference="table-qt"}.

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

# The new conjectures: incorporating $t$

In this section we describe general aspects of the mathematical structure shared by a wide variety of examples, ranging from the counting of refined BPS invariants to categorification of quantum group invariants. Then, in later sections we focus on each class of examples separately.

In particular, one of our goals is to promote the volume conjectures [\[VCparam\]](#VCparam){reference-type="eqref" reference="VCparam"} and [\[VCquant\]](#VCquant){reference-type="eqref" reference="VCquant"} to the corresponding refined / categorified versions, both for knots and for the refined BPS invariants.

## Quantum volume conjecture: refined

The fact that a $q$-difference operator $\widehat A (\widehat x, \widehat y; q)$ annihilates the partition function of Chern-Simons theory / matrix model / B-model / instanton partition function is easy to refine. Just like each of these partition functions becomes $t$-dependent, so does the operator $\widehat A (\widehat x, \widehat y; q,t)$ that annihilates it. The commutation relations [\[xycomm\]](#xycomm){reference-type="eqref" reference="xycomm"} do not change and, therefore, our proposal for the refinement of [\[VCquant\]](#VCquant){reference-type="eqref" reference="VCquant"} is easy to state: $$\label{VCquantref}
\begin{equation}
\widehat A^{\text{ref}} (\widehat x, \widehat y; q, t) \; P_* (K;q,t) \; \simeq \; 0 \qquad \qquad \text{(knots)}
\end{equation}
or
\begin{equation}
\widehat A^{\text{ref}} (\widehat x, \widehat y; q, t) \; Z_{\text{BPS}}^{\text{open}} (u,q,t) \; \simeq \; 0 \qquad \qquad \text{(BPS states)}
\end{equation}$$ While the formulation of this refined / homological version is simple and follows the lines of the ordinary quantum volume conjecture [\[VCquant\]](#VCquant){reference-type="eqref" reference="VCquant"}, its interpretation is rather deep and non-trivial. It involves details of the framework in which [\[VCquantref\]](#VCquantref){reference-type="eqref" reference="VCquantref"} arises and will be given a proper treatment in the following sections. Here, we only remark that polynomials $P_n (K;q,t)$ which appear in ([\[VCquantref\]](#VCquantref){reference-type="ref" reference="VCquantref"}a) as $t$-dependent analogs of the colored Jones polynomials $J_n (K;q)$ are Poincaré polynomials of the $n$-colored $sl(2)$ knot homology groups ${\cal H }^{sl(2),V_n} (K)$: $$P_n (K;q,t) \; = \; \sum_{i,j} q^i t^j \dim {\cal H }_{i,j}^{sl(2),V_n} (K) \,,
\label{Pnoptimistic}$$ such that $$J_n (K;q) \; = \; P_n (K;q,t=-1) \,.$$ Because the $t$-deformation does not affect the commutation relation [\[xycomm\]](#xycomm){reference-type="eqref" reference="xycomm"}, the operators $\widehat x$ and $\widehat y$ act on $P_n$ exactly as in [\[xyactionJ\]](#xyactionJ){reference-type="eqref" reference="xyactionJ"}: $$\begin{aligned}
& \widehat x P_n \; = \; q^n P_n \label{xyactionP} \\
& \widehat y P_n \; = \; P_{n+1} \notag
\end{aligned}$$

::: {#table-qt}
    **Model**                                           $\widehat{A}^{\text{ref}} (\widehat{x},\widehat{y};q,t)$
  ------------- ----------------------------------------------------------------------------------------------------------------------------------------
     unknot                                 $(1 + t^3 q \widehat{x}) ( - q^{-1} t^{-3})^{1/2} - (1 - \widehat{x})\widehat y$
                                                         $\frac{1}{q + \widehat{x}^2 q^{2} t^3} \; \widehat{y}
                              + \frac{\widehat{x}^3 (x - q) t^4}{q (q + \widehat{x}^2 t^3) (1 + \widehat{x} q t^3)} \; \widehat{y}^{-1} +$
                                                        $-   \frac{t^2 \widehat{x}^2}{1 + \widehat{x}^2 q t^3} -
                                                          \frac{ q - \widehat{x} q t^2 + \widehat{x}^{4} t^6 +
                                          \widehat{x}^{2} t^2 (1 + t + q t)}{(q + \widehat{x}^{2} t^3) (1 + \widehat{x} q t^3)}$
   tetrahedron                            $1 + t \widehat{y} - t \sqrt{q} \, \widehat{x}(-\widehat{y})^f  \; \simeq  \; 1 + t$
    conifold     $1 + t \widehat{y} - t \sqrt{q} \, \widehat{x}(-\widehat{y})^f  + Q \sqrt{-tq} \, \widehat{x}(-\widehat{y})^{f+1} \; \simeq \; 1 + t$ 

  : Refined quantum curves derived in this paper. The notation "$\ldots \simeq 1 + t$" should be understood as $\widehat{A}^{\text{ref}} Z_{\text{BPS}}^{\text{open}} = 1 + t$. Note that in section [\[sec:Bmodel\]](#sec:Bmodel){reference-type="ref" reference="sec:Bmodel"} the quantization parameter $q$ is identified with $q_2$, and the deformation parameter is $t= - \frac{q_1}{q_2}$.
:::

## Generalized volume conjecture: refined

The refinement / categorification of the generalized volume conjecture [\[VCparam\]](#VCparam){reference-type="eqref" reference="VCparam"} involves taking the limit [\[VClimit\]](#VClimit){reference-type="eqref" reference="VClimit"} while keeping the extra parameter $t$ fixed: $$q = e^{\hbar} \to 1 \,, \qquad t = \text{fixed} \,, \qquad x \equiv e^u = q^n = \text{fixed}
\label{reflimit}$$ We conjecture that, in this limit, the homological (resp. refined) knot (resp. BPS) invariants have the following asymptotic behavior: $$\label{VCparamref}
\begin{equation}
P_n  \; \simeq \;
\exp\left( \frac{1}{\hbar} S_0 (u,t) \,+\,\sum_{n=0}^\infty S_{n+1} (u,t) \, \hbar^{n} \right)
\qquad \qquad \text{(knots)}
\end{equation}
or
\begin{equation}
Z_{\text{BPS}}^{\text{open}} (u,q,t) \; \simeq \;
\exp\left( \frac{1}{\hbar} S_0 (u,t) \,+\,\sum_{n=0}^\infty S_{n+1} (u,t) \, \hbar^{n} \right)
\qquad \qquad \text{(BPS states)}
\end{equation}$$ with the leading term ("classical action") $$S_0 (u,t) \; = \; \int v du \; = \; \int \log y \frac{dx}{x}
\label{S0ref}$$ defined as an integral on a classical curve $${\cal C }^{\text{ref}}: \quad
\left\{(x,y)\in\mathbb{C}^*\times \mathbb{C}^*\Big|
A^{\text{ref}} (x,y;t) \; = \; 0
\right\}\,,$$ which is a deformation of the classical A-polynomial curve $A(x,y)=0$. In writing [\[S0ref\]](#S0ref){reference-type="eqref" reference="S0ref"} we used the same convention as in ([\[xuyv\]](#xuyv){reference-type="ref" reference="xuyv"}).
