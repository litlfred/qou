---
doc_id: arxiv-math-0612592v1
doc_title: "Analytic q -diﬀerence equations"
section_id: sec-000-difference-equations-in-general
section_title: "Difference equations in general"
section_number: null
pages: 2-3
source_pdf: 0612592v1.pdf
source_sha256: a5d29fa15a0b74ff
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.994
doc_brief: "Analytic q -diﬀerence equations — 7 sections: Front matter; Difference equations in general; First examples of q-difference equ"
---
A difference field $F$ is a field provided with an automorphism $\phi$ of infinite order. A scalar linear difference equation is an equation of the form $$\phi ^n(y)+a_{n-1}\phi ^{n-1}(y)+\cdots +a_1\phi (y) +a_0y=0\,$$ with given $a_i\in F$ and, say, $a_0\neq 0$. As in the case of linear differential equations, one can transform this equation into a matrix difference equation, i.e., an equation of the form $Y=A\phi (Y)$, where $A$ is a given invertible $n\times n$-matrix with coefficients in $F$ and $Y$ denotes a vector of length $n$. On the vector space $M=F^n$ one considers the operator $\Phi : Y\mapsto A\phi (Y)$. The bijective map $\Phi :M\rightarrow M$ is additive and $\Phi (f\cdot m)=\phi (f)\cdot \Phi (m)$ for $m\in M$ and $f\in F$. This leads to the following definition of a *difference module $M=(M,\Phi )$ over $F$*:\
$M$ is a finite dimensional vector space over $F$ and $\Phi :M\rightarrow M$ is an additive, bijective map satisfying $\Phi (f\cdot m)=\phi (f)\cdot \Phi (m)$ for $m\in M$ and $f\in F$. The equation, corresponding to a difference module is $Y=\Phi (Y)$. In general this equation has few solutions in $M$ itself. Like ordinary polynomial equations over fields, one has to construct extensions of $F$ in order to have sufficiently many solutions.

We will now assume that $F$ has *characteristic zero* and that its field of constants $C: =\{f\in F|\ \phi (f)=f\}$ is *algebraically closed*. A *Picard-Vessiot ring (or extension) $R$ for a difference module $M$*, say, represented by the matrix equation $Y=A\phi (Y)$ is defined by:\
(i) $R$ is an $F$-algebra (commutative and with a $1$),\
(ii) $R$ is provided with an automorphism $\phi$ extending $\phi$ on $F$,\
(iii) $R$ has only trivial $\phi$-invariant ideals,\
(iv) there exists an invertible matrix $U$ (called fundamental matrix) with coefficients in $R$ such that $U=A\phi (U)$,\
(v) $R$ is generated over $F$ by the coefficients of $U$ and $\frac{1}{\det U}$.\
Property (iii) translates in terms of $M$ into $V:=\{a\in R\otimes _FM|\ \Phi (a)=a\}$ is a vector space over $C$ and the natural map $R\otimes _CV\rightarrow R\otimes _FM$ is an isomorphisms.

One constructs $R$ as follows. Let $X$ denote a matrix $(X_{i,j})$ of indeterminates and put $D:=\det X$. The $F$-algebra $R_0:=F[X,\frac{1}{D}]$ is provided with a $\phi$-action, extending the one on $F$, by the formula $(\phi X_{i,j} )=A^{-1}(X_{i,j})$. Let $I\subset R_0$ denote an ideal maximal among the ideals invariant under $\phi$. Then $R=R_0/I$ is a Picard-Vessiot ring for the given equation.

The basic results of difference Galois theory are:\
(1) A Picard-Vessiot ring $R$ exists and is unique up to a, non unique, isomorphism.\
(2) $R$ is reduced (i.e., has no nilpotent elements).\
(3) The set constants of the ring of total fractions of $R$ is $C$.\
(4) Let $G$ be the group of the $F$-linear automorphism of $R$, commuting with $\phi$. The natural action of $G$ on $R\otimes _FM$ induces a faithful action of $G$ on $V$, the solution space. The image of $G$ in ${\rm GL}(V)$ is a linear algebraic subgroup of the latter. This makes $G$ into a linear algebraic group over $C$.\
(5) The action of $G$ on $Spec(R)$ makes the latter into an $G$-torsor over $F$. In other words, there exists a finite extension $F^+\supset F$ and a $G$-equivariant isomorphism $F^+\otimes _CC[G]\rightarrow F^+ \otimes _FR$, where $C[G]$ is the coordinate ring of $G$.\
Most of the notions and 'operations of linear algebra', such as morphisms, kernels, cokernels, direct sums have an obvious equivalent for difference modules. Let $(M_1,\Phi _1),\ (M_2,\Phi _2)$ denote two difference modules. The tensor product of the two modules is defined as $M_1\otimes _FM_2$ with $\Phi$ given by $\Phi (m_1\otimes m_2)=(\Phi _1m_1)\otimes (\Phi _2m_2)$. The internal hom of the two modules is ${\rm Hom}_F(M_1,M_2)$ with $\Phi$ defined by $(\Phi (L))(m_1)=\Phi _2^{-1}(L(\Phi _1m_1))$ for $L\in {\rm Hom}_F(M_1,M_2)$ and $m_1\in M_1$.

This leads to another, more abstract but very useful, formulation of the above Picard-Vessiot theory, namely that of (neutral) Tannakian categories. The category of all difference modules over $F$ is a neutral Tannakian category. We will return to this in section 6. For a specific difference field $F$ one can say much more than the above formalism (analogous to the case of ordinary Galois theory for specific fields).
