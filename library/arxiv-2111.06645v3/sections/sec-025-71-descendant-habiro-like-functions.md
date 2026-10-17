---
doc_id: arxiv-2111.06645v3
doc_title: "Part 0: Introduction and overview"
section_id: sec-025-71-descendant-habiro-like-functions
section_title: "Descendant Habiro-like functions"
section_number: 7.1
pages: 52-55
source_pdf: 2111.06645v3.pdf
source_sha256: 2a4826bd1c2f0823
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.984
---
[]{#sub.qholo label="sub.qholo"}

It turns out that the first row of $\mathbf{J}$ and the first row of $\mathbf{\widehat\Phi}$ are basis elements of the span of an inhomogeneous recursion, and the same holds (but now with the corresponding homogeneous recursion) for each of the remaining rows of $\mathbf{J}$ and of $\mathbf{\widehat\Phi}$ as well as for the matrix of $q$-series of [@GZ:qseries]. To illustrate how this works, we give the complete formulas for the matrix for the $4_1$ knot. The corresponding formulas for the $5_2$ knot, which are considerably more complicated and illustrate several further refinements (like the appearance of Dedekind sums), will be given in Section [\[sub.statesum\]](#sub.statesum){reference-type="ref" reference="sub.statesum"}.

Collecting together our previous results for the $4_1$ knot for the reader's convenience, we obtain that the matrix $\mathbf{J}=\mathbf{J}^{(4_1)}$ of periodic functions on $\mathbb Q$ has the form $$\mathbf{J}(x) = \begin{pmatrix}
 1 & J^{(0,1)}(x) & J^{(0,2)}(x) \\
 0 & J^{(1,1)}(x) & J^{(1,2)}(x) \\
 0 & J^{(2,1)}(x) & J^{(2,2)}(x)
\end{pmatrix}
 =\mathcal{J}(q) = \begin{pmatrix}
 1 & \mathcal{J}^{(0,1)}(q) & \mathcal{J}^{(0,2)}(q) \\
 0 & \mathcal{J}^{(1,1)}(q) & \mathcal{J}^{(1,2)}(q) \\
 0 & \mathcal{J}^{(2,1)}(q) & \mathcal{J}^{(2,2)}(q)
\end{pmatrix}$$ (with $q=\mathbf{e}(x)$ and omitting $K$ as usual), where the elements of the first row are given by $$\begin{gathered}
 \mathcal{J}^{(0,1)}(q) =\mathcal{Q}^{(4_1)}_1(q)=\mathcal{J}^{(4_1)}(q)
 = \sum_{n=0}^\infty (q;q)_n \big(q^{-1};q^{-1}\big)_n ,\nonumber\\
 \mathcal{J}^{(0,2)}(q) =\mathcal{Q}^{(4_1)}_2(q)
 =\frac{1}{2}\sum_{n=0}^\infty \big(q^{n+1}-q^{-n-1}\big) (q;q)_n \big(q^{-1};q^{-1}\big)_n\label{Q41J0Q0}
\end{gathered}$$ (equations [\[Hab41\]](#Hab41){reference-type="eqref" reference="Hab41"} and [\[Q0for41\]](#Q0for41){reference-type="eqref" reference="Q0for41"}), with $\mathcal{Q}^{(4_1)}_i(q)$ being the elements of the Habiro ring defined and tabulated in Section [\[sub.4.3\]](#sub.4.3){reference-type="ref" reference="sub.4.3"}, and that the elements of the other two rows are given by $$\begin{aligned}
\mathcal{J}^{(1,1)}(q) &= \frac{1}{\sqrt{c}\sqrt[4]{3}} \sum_{Z^c = \zeta_6}
 \prod_{j=1}^c \bigl|1 - q^jZ\bigr|^{2j/c} ,\nonumber\\
\mathcal{J}^{(2,1)}(q) &= \frac{\rm i}{\sqrt{c}\sqrt[4]{3}}  \sum_{Z^c = \zeta_6^{-1}}
 \prod_{j=1}^c \bigl|1 - q^jZ\bigr|^{2j/c} ,\nonumber\\
\mathcal{J}^{(1,2)}(q) &= \frac{1}{2\sqrt{c} \sqrt[4]{3}}
\sum_{Z^c = \zeta_6} \bigl(Zq - Z^{-1}q^{-1}\bigr) \prod_{j=1}^c \bigl|1 - q^jZ\bigr|^{2j/c},\nonumber
\\
\mathcal{J}^{(2,2)}(q) &= \frac{\rm i}{2\sqrt c \sqrt[4]{3}}
\sum_{Z^c = \zeta_6^{-1}} \bigl(Zq - Z^{-1}q^{-1}\bigr)
\prod_{j=1}^c \bigl|1 - q^jZ\bigr|^{2j/c}\label{Q41abcd}
\end{aligned}$$ (equations [\[Def41J1\]](#Def41J1){reference-type="eqref" reference="Def41J1"}, [\[Q1for41\]](#Q1for41){reference-type="eqref" reference="Q1for41"} and the accompanying text). The syntactical similarity between equations [\[Q41J0Q0\]](#Q41J0Q0){reference-type="eqref" reference="Q41J0Q0"} and equations [\[Q41abcd\]](#Q41abcd){reference-type="eqref" reference="Q41abcd"} is striking, and leads directly to the $q$-holonomy.

To see this, we rewrite the two formulas in [\[Def41J1\]](#Def41J1){reference-type="eqref" reference="Def41J1"} as $$\label{41holonomy0}
\mathcal{J}^{(0,1)}(q)=\mathcal H^{(0)}_0(q) ,\qquad
\mathcal{J}^{(0,2)}(q)=\frac12\bigl(q\mathcal H^{(0)}_1(q)-q^{-1}\mathcal H^{(0)}_{-1}(q)\bigr) ,$$ where is the sequence of elements of the Habiro ring defined by $$\label{qHol41}
\mathcal H^{(0)}_m(q) = \sum_{n=0}^\infty (q;q)_n \big(q^{-1};q^{-1}\big)_n q^{m n},
\qquad m\in\mathbb Z.$$ It is easy to see that this sequence satisfies the recursion relation $$\label{rec41}
q^{m+1} \mathcal H^{(0)}_{m+1}(q) + (1-2 q^m) \mathcal H^{(0)}_{m}(q)
+ q^{m-1} \mathcal H^{(0)}_{m-1}(q) = 1,
\qquad m \in \mathbb Z$$ (a similar, but homogeneous, recursion relation for the descendants of certain $q$-series associated to the $4_1$ knot was given in [@GGM equation (14)] and used in [@GZ:qseries]) and also that the $\mathbb Q\big[q^\pm\big]$-module they span is free of rank 3 with the top row of the matrix $\mathbf{J}$ as a basis. If we now introduce two further sequences of functions of $q$ (or periodic functions of $x$, where $q=\mathbf{e}(x)$) by $$\begin{aligned}
\mathcal H^{(1)}_m(q) &= \frac{1}{\sqrt c \sqrt[4]{3}}
\sum_{Z^c = \zeta_6} Z^m \prod_{j=1}^c \bigl|1 - q^jZ\bigr|^{2j/c} ,\nonumber
\\
\mathcal H^{(2)}_m(q) &= \frac{\rm i}{\sqrt c \sqrt[4]{3}}
 \sum_{Z^c = \zeta_6^{-1}} Z^m \prod_{j=1}^c \bigl|1 - q^jZ\bigr|^{2j/c} ,\label{41holonomy12}
\end{aligned}$$ then [\[Q41abcd\]](#Q41abcd){reference-type="eqref" reference="Q41abcd"} says that the non-trivial elements of the second and third rows of $\mathbf{J}$ are given by $$\mathcal{J}^{(i,1)}(q)=\mathcal H_0^{(i)}(q) ,\qquad
\mathcal{J}^{(i,2)}(q)=\frac12\bigl(q\mathcal H^{(i)}_1(q)-q^{-1}\mathcal H^{(i)}_{-1}(q)\bigr),
\qquad i=1,2 .$$ Furthermore, we see that the first column of the matrix $\mathbf{J}$, trivial though it is, nevertheless belongs to the same $q$-holonomic module as the other columns, since as well as equations [\[41holonomy0\]](#41holonomy0){reference-type="eqref" reference="41holonomy0"} and [\[41holonomy12\]](#41holonomy12){reference-type="eqref" reference="41holonomy12"} we also have the relation $$\label{41holonomy1stcol}
\mathcal{J}^{(i,0)}(q)=
q \mathcal H^{(i)}_1(q) + \mathcal H^{(i)}_0(q) + q^{-1}\mathcal H^{(i)}_{-1}(q), \qquad i=0,1,2 ,$$ as we see by specializing the recursion [\[rec41\]](#rec41){reference-type="eqref" reference="rec41"} and its counterparts for $\mathcal H^{(1)}_m$ and $\mathcal H^{(2)}_m$ to $m=0$. Then the quantitative version of the "syntactical similarity" noted above is that we can write the formulas [\[Q41J0Q0\]](#Q41J0Q0){reference-type="eqref" reference="Q41J0Q0"} and [\[Q41abcd\]](#Q41abcd){reference-type="eqref" reference="Q41abcd"} or [\[41holonomy12\]](#41holonomy12){reference-type="eqref" reference="41holonomy12"} and [\[41holonomy1stcol\]](#41holonomy1stcol){reference-type="eqref" reference="41holonomy1stcol"} uniformly and more compactly in matrix form as $$\begin{gathered}
\label{41matrixholonomy}
\mathcal{J}^{(4_1)}(q) =
\begin{pmatrix} \mathcal H^{(0)}_{-1}(q) & \mathcal H^{(0)}_0(q) &\mathcal H^{(0)}_1(q) \\
 \mathcal H^{(1)}_{-1}(q) & \mathcal H^{(1)}_0(q) &\mathcal H^{(1)}_1(q) \\
 \mathcal H^{(2)}_{-1}(q) & \mathcal H^{(2)}_0(q) &\mathcal H^{(2)}_1(q) \end{pmatrix}
\begin{pmatrix} q^{-1} & 0 & \frac12 q \\ 1 & 1 & 0 \\ q & 0 & -\frac12 q^{-1}
\end{pmatrix} .
\end{gathered}$$ Note that none of these equations are unique, since any one of them could be written in infinitely many other ways by using the $q$-holonomy property, e.g., we could specialize the recursions to any value of $m$ other than 0 to get formulas for $\mathcal{J}^{(i,0)}(q)$ different from [\[41holonomy1stcol\]](#41holonomy1stcol){reference-type="eqref" reference="41holonomy1stcol"}. Similarly, we could rewrite [\[41matrixholonomy\]](#41matrixholonomy){reference-type="eqref" reference="41matrixholonomy"} by taking three other columns (or linear combinations of columns) of the $\mathcal H$-matrix for the first factor on the right, with the corresponding new matrix of Laurent polynomials in the second factor.

More interesting is that there is also nothing sacred about the particular collection $\mathcal H^{(i)}(q)$ of functions of $q$ that we chose to define our $q$-holonomic system, and that there infinitely many other collections, even with completely different indexing sets (e.g., $\mathbb Z^2$ instead of $\mathbb Z$) that could be used instead and that might have been found it we had given a different combinatorial description of knot. However, the module over $\mathbb Q\big[q,q^{-1}\big]$ that they generate is at least conjecturally intrinsic to the knot and is simply the span of the columns of , which therefore constitute a canonical basis indexed by $\mathcal P$. This is one of the most mysterious aspects of our matrix invariants. We will return to it in at the end of this section in connection with other possible representations of the same abstract $q$-holonomic module.

We end the subsection with a final remark. Despite the apparent similarity in the formulas for the elements of the first row and all other rows of the matrix $\mathbf{J}$, there is a crucial difference between formulas like [\[Q41J0Q0\]](#Q41J0Q0){reference-type="eqref" reference="Q41J0Q0"} or [\[qHol41\]](#qHol41){reference-type="eqref" reference="qHol41"}

for the top rows of our matrix and formulas like [\[Q41abcd\]](#Q41abcd){reference-type="eqref" reference="Q41abcd"} or [\[41holonomy12\]](#41holonomy12){reference-type="eqref" reference="41holonomy12"}

for the other rows: the former are sums over the lattice points of a cone and hence satisfy an inhomogeneous linear $q$-difference equation, whereas the latter are sums over periodic groups $\mathbb Z/c\mathbb Z$ and hence have no boundary terms and satisfy a homogeneous equation. Another difference, to which we hope to return in [@GSZ:habiro] in the context of Habiro rings for general number fields, is that [\[Q41J0Q0\]](#Q41J0Q0){reference-type="eqref" reference="Q41J0Q0"} and [\[qHol41\]](#qHol41){reference-type="eqref" reference="qHol41"} obviously give algebraic integers when $q$ is a root of unity, whereas [\[Q41abcd\]](#Q41abcd){reference-type="eqref" reference="Q41abcd"} or [\[41holonomy12\]](#41holonomy12){reference-type="eqref" reference="41holonomy12"} give algebraic integers in some non-evident way, since it is not obvious (but in fact true) that the sums in these formulas are divisible by $\sqrt c$. We will find exactly the same behavior for the elements of the $\mathbf{J}$-matrix for the $5_2$ knot in the next subsection.

## The $\mathbf{J}$-matrix for the $\boldsymbol{5_2}$ knot {#sub.52statesum}

In this subsection, we describe that analogues of the formulas just given for our second standard knot $5_2$, because as usual the figure 8 knot has such special properties that some of the interesting features are obscured.

The Kashaev invariant of the $5_2$ knot is given by $$\label{Kashaev.52}
 \mathcal J^{(5_2)}(q) =\sum_{m=0}^{\infty} \sum_{k=0}^m
q^{-(m+1)k} \frac{(q;q)_m^2}{\big(q^{-1};q^{-1}\big)_k} .$$ (See [@K97 equation 2.3].) This is manifestly an element of the Habiro ring. We generalize it to the two-parameter family of elements of the Habiro ring given by $$\label{52desc}
\mathcal H^{(0)}_{a,b}(q) =\sum_{m=0}^{\infty} \sum_{k=0}^m
q^{-(m+1)k + am+bk} \frac{(q;q)_m^2}{\big(q^{-1};q^{-1}\big)_k}, \qquad a,b \in \mathbb Z.$$ These again form a $q$-holonomic module in the sense of [@WZ], meaning that they satisfy recursions like [\[rec41\]](#rec41){reference-type="eqref" reference="rec41"} (though in this case more complicated, and omitted here) and hence generate a $\mathbb Q\big[q,q^{-1}\big]$-module of finite rank. Here the rank is 4 and the $q$-holonomic module is generated (as we expect to hold for every knot) by the first row of the matrix $\mathbf{J}$ of the knot, $$\begin{aligned}
 \mathcal{J}^{(0,0)}(q) &
 =- \mathcal H^{(0)}_{0,0}(q)+q^{-1} \mathcal H^{(0)}_{-1,0}(q)+\mathcal H^{(0)}_{0,-1}(q)=1 , \qquad
\mathcal{J}^{(0,1)}(q) =\mathcal H^{(0)}_{0,0}(q) , \\
\mathcal{J}^{(0,2)}(q) & =\mathcal H^{(0)}_{0,0}(q)  - q^{-1}\mathcal H^{(0)}_{-1,0}(q) , \qquad
\mathcal{J}^{(0,3)}(q) = 2\mathcal H^{(0)}_{0,0}(q)  - q^{-1} \mathcal H^{(0)}_{-1,0}(q)
+ \mathcal H^{(0)}_{-1,1}(q) .
\end{aligned}$$

Just as in the case of the $4_1$ knot, we find that the further three rows are given by the *same* linear combinations of three other two-parameter families $\mathcal H^{(i)}_{a,b}$ ($1\le i\le3$) of functions, i.e., we have $$\begin{aligned}
 \mathcal{J}^{(i,0)}(q) &
 = - \mathcal H^{(i)}_{0,0}(q)+ q^{-1}\mathcal H^{(i)}_{-1,0}(q) - \mathcal H^{(i)}_{0,-1}(q) ,\qquad
\mathcal{J}^{(i,1)}(q) =\mathcal H^{(i)}_{0,0}(q) , \\
\mathcal{J}^{(i,2)}(q) & =\mathcal H^{(i)}_{0,0}(q)  - q^{-1}\mathcal H^{(i)}_{-1,0}(q) , \qquad
\mathcal{J}^{(i,3)}(q) = 2\mathcal H^{(i)}_{0,0}(q)  - q^{-1} \mathcal H^{(i)}_{-1,0}(q)
+ \mathcal H^{(i)}_{-1,1}(q)
\end{aligned}$$ for $i=0,1,2,3$. The formulas for the functions for $i\ne0$, whose origin will be indicated in Section [\[sub.statesum\]](#sub.statesum){reference-type="ref" reference="sub.statesum"}, are of the same type as the corresponding ones for the $4_1$ knot (equation [\[Q41abcd\]](#Q41abcd){reference-type="eqref" reference="Q41abcd"}), though considerably more complicated, but are completely different from [\[52desc\]](#52desc){reference-type="eqref" reference="52desc"}, namely $$\label{52H}
\mathcal H_{a,b}^{(i)}(x) = \frac 1{c \sqrt{3\xi_i-2}}  \frac{\theta_{1,i}^{c-1}
 \mathcal D_{\zeta}(\zeta\theta_{1,i})^2}{\mathcal D_{\zeta}\big(\zeta^{-1} \theta_{2,i}^{-1}\big)}
\sum_{k,m \bmod c} \zeta^{-(k+1)m} \theta_{1,i}^{-m} \theta_{2,i}^{-k}
\frac{(\zeta \theta_{1,i};\zeta)_k^2 }{\big(\zeta^{-1}\theta_{2,i}^{-1};\zeta^{-1}\big)_m} ,$$ where $c=\mathrm{den}(x)$, $\zeta=\mathbf{e}(-x)$ and and are any choice of $c$-th roots of  and $\xi_{i}^{-2}$ and $\xi_1$ (resp., $\xi_2$, $\xi_3$) the complex root of the equation $\xi^3-\xi^2+1=0$ (as in Section [\[sub.p\]](#sub.p){reference-type="ref" reference="sub.p"}) with negative (resp., positive, zero) imaginary part. Here $\mathcal D_\zeta(x)$ is the renormalized version of the cyclic quantum dilogarithm $D_\zeta(x)$ defined for $q=\mathbf{e}(a/c)$ by $$\label{Dm}
\mathcal D_q(x) = {\rm e}^{-2 \pi {\rm i} s(a,c)/2} D_q(x)
= {\rm e}^{-2 \pi {\rm i} s(a,c)/2}
\exp \Biggl(\sum_{j=1}^{c-1} \frac{j}{c} \log\big(1-q^j x\big) \Biggr) ,$$ where $s(a,c)$ is the Dedekind sum (cf. [@HZ; @Rademacher]) and where the logarithm is the principal one away from the cut at the negative real axis and is defined on the cut as the average of the principal branches just above and just below. The cyclic quantum dilogarithm appears in the expansion of Faddeev's quantum dilogarithm at roots of unity (see, for example, [@GK:evaluation; @Kashaev:star]) and plays a key role in the definition of the near units associated to elements of the Bloch group [@CGZ].

It is worth mentioning that the formulas [\[Q41abcd\]](#Q41abcd){reference-type="eqref" reference="Q41abcd"} and [\[41holonomy12\]](#41holonomy12){reference-type="eqref" reference="41holonomy12"} for the $4_1$ knot can also be written in terms of the modified cyclic quantum dilogarithm $\mathcal D_q$, because can be rewritten as $\mathcal D_q(Z) \mathcal D_{q^{-1}}\big(Z^{-1}\big)$. In fact, we expect formulas of this type, involving multiplicative combinations of the $\mathcal D_q$'s corresponding to the combinations defining the element of the Bloch group of $F$ corresponding to the knot, to exist for all knots.
