---
doc_id: arxiv-1501.01574v3
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL"
section_id: sec-008-31-the-colored-jones-polynomial
section_title: "The colored Jones polynomial"
section_number: 3.1
pages: 9-10
source_pdf: 1501.01574v3.pdf
source_sha256: 8af5d6264a0ad5e0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 1.0
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL — We study the behavior of the degree of the colored Jones polynomial and the boundary slopes of knots under the operation of cabling."
---
To define the colored Jones polynomial, we first recall the definition of the Chebyshev polynomials of the second kind. For $n \ge 0$, the polynomial $S_n(x)$ is defined recursively as follows:
\begin{equation}
\label{chev}
S_{n+2}(x)=xS_{n+1}(x)-S_{n}(x), \quad S_1(x)=x, \quad S_0(x)=1.
\end{equation}

Let $D$ be a diagram of a knot $K$. For an integer $m>0$, let $D^m$ denote the diagram obtained from $D$ by taking $m$ parallels copies of $K$. This is the $m$-cable of $D$ using the blackboard framing; if $m=1$ then $D^1=D$. Let $\la D^m \ra$ denote the Kauffman bracket of $D^m$: this is a Laurent polynomial over the integers in a variable $v^{-1/4}$ normalized so that $\la \text{unknot} \ra = -(v^{1/2}+v^{-1/2})$. Let $c=c(D)=c_+ + c_-$ denote the crossing number and $w=w(D)=c_+ - c_-$ denote the writhe of $D$. 

For $n>0$, we define 
$$J_K(n):=  ( (-1)^{n-1} v^{(n^2-1)/4} )^w (-1)^{n-1}  \la S_{n-1}(D)\ra$$
where $S_{n-1}(D)$ is a linear combination of blackboard cablings of $D$, obtained via equation \eqref{chev}, and the notation $\la S_{n-1}(D) \ra$ means extend the Kauffman bracket linearly. That is, for diagrams $D_1$ and $D_2$ and scalars $a_1$ and $a_2$, $\la a_1 D_1 + a_2 D_2 \ra = a_1 \la D_1 \ra + a_2 \la D_2 \ra$.


For a Laurent polynomial $f(v) \in \BC[v^{\pm 1/4}]$, let $d_+[f]$ and $d_-[f]$ be respectively the maximal and minimal degree of $f$ in $v$.


\begin{define}
A \emph{quasi-polynomial} is a function $$f:\BN \to \BC, \quad f(n)=\sum_{i=0}^d c_i(n)n^i$$
for some $d \in \BN$, where $c_i(n)$ is a periodic function with integral period for $i=1, \cdots, d$. If $c_d(n)$ is not identically zero, then the degree of $f(n)$ is $d$. 

The \emph{period} $\pi$ of a quasi-polynomial $f(n)$ as above is the common period of $c_i(n)$.
\end{define}

Garoufalidis \cite{ga-quasi} showed that for any knot $K\subset S^3$
the degrees $ d_+[J_{K}(n)] $ and $ d_-[J_{K}(n)] $ are quadratic quasi-polynomials.
The common period  of $ d_+[J_{K}(n)] $ and $ d_-[J_{K}(n)]$ is called \emph{the period of $K$}, denoted  by $\pi(K)$. 
\medskip
