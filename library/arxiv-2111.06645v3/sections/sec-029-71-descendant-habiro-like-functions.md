---
doc_id: arxiv-2111.06645v3
doc_title: "Knots, Perturbative Series and Quantum Modularity"
section_id: sec-029-71-descendant-habiro-like-functions
section_title: "Descendant Habiro-like functions"
section_number: 7.1
pages: 52-54
source_pdf: 2111.06645v3.pdf
source_sha256: 2a4826bd1c2f0823
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.996
doc_brief: "Knots, Perturbative Series and Quantum Modularity — We introduce an invariant of a hyperbolic knot which is a map α 7→Φα(h) from Q/Z to matrices with entries in Q[[h]] and with rows and columns"
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
