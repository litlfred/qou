---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q -HOLONOMIC MODULES"
section_id: sec-004-14-the-generalised-q-hypergeometric-equation-is
section_title: "The generalised q-hypergeometric equation is modular"
section_number: 1.4
pages: 5-7
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
toc_source: outline
text_source: latex
latex_prose_ratio: 0.921
latex_coverage_ratio: 0.977
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
\label{sub.qhyper}

Contrary to what one might expect, modular $q$-holonomic modules are abundant.
This section concerns the generalised $q$-hypergeometric equation

\be
\label{gener.qhyper}
\left(\prod_{j=0}^{r-1}(1-q^{-1}b_{j}\sigma)-t\prod_{j=1}^{r}(1-a_{j}\sigma)\right)f
=0
\ee
for a function $f=f(t,a,b,q)$ where $a=(a_1,\dots,a_r)$ and $b=(b_0,\dots,b_{r-1})$
with $b_0=q$, where $\s$ is the operator that shifts $t$ to $qt$. This equation
is a $q$-deformation of the hypergeometric equation (a regular singular linear
differential equations with singularities at $0,1,\infty$), itself a generalisation
of the Gauss hypergeometric equation. The hypergeometric equation has a rich history
related to, among other things, periods in algebraic geometry and the
in the Gauss-Manin connection of the middle cohomology of the Dwork family of
smooth hypersurfaces; see for example~\cite{Beukers,Katz:another} and references
therein. 

The generalised $q$-hypergeometric equation~\eqref{gener.qhyper} was
introduced and studied by Heine, who shows that this equation has a solution the
function, analytic at $t=0$, given by the $q$-hypergeometric series
\be
\label{phirr}
{}_{r}\phi_{r-1}(a;b;q,t) =
\sum_{k=0}^{\infty}
\frac{(a_{1};q)_{k}\dots(a_{r};q)_{k}}{(b_{1};q)_{k}\dots(b_{r-1};q)_{k}(q;q)_{k}}t^{k}
\,.
\ee
The generalised $q$-hypergeometric equation and the $q$-hypergeometric series
are classical examples of functions that appear in many areas of research, and
for a comprehensive treatment, we refer the reader to the book of Gasper--Rahman
~\cite{Gasper} and references therein. 

Consider the matrices 
\be
\label{UVheine}
  U=W(f^{(1)},f^{(qb_{1}^{-1})},\dots,f^{(qb_{r-1}^{-1})}), \qquad
  V=W(g^{(a_{1}^{-1})},\dots,f^{(a_{r}^{-1})})
\ee
where $W$ denotes the Wronskian of
$r$ functions $f_1,\dots,f_r$, which is an $r \times r$ matrix defined by
$W(f_1,\dots,f_r)_{ij}=(\s^{i-1} f_j)$ for $i,j=1,\dots,r$ and
\be
\label{heine.bjsols}
  f^{(q^{-1}b_{j})}(t,a,b,q)
  =
  B_{j}(a,b,q)\frac{\theta(q^{-1}b_{j}t;q)}{\theta(t;q)}
  {}_{r}\phi_{r-1}(qa/b_{j};qb/b_j;q,t)
\ee
for $j=0,\dots,r-1$ with $B_{0}=1$ and, for $j>0$,
\be
\label{Bjabq}
B_{j}(a,b,q) =
\left(\prod_{i=1}^{r}\frac{(a_{i};q)_{\infty}(qb_{i-1}/b_{j};q)_{\infty}}{
    (qa_{i}/b_{j};q)_{\infty}(b_{i-1};q)_{\infty}}\right)
\frac{(q;q)_{\infty}^{3}}{\theta(q^{-1}b_{j};q)} \,,
\ee
and 
\be
\label{heine.ajsols}
g^{(a_{j}^{-1})}(t,a,b,q) =
A_{j}(a,b,q)\frac{\theta(q^{-1}a_{j}t;q)}{\theta(q^{-1}t;q)}
{}_{r}\phi_{r-1}(qa_{i}/b;qa_{i}/a;q,qb_{1}\dots b_{r-1}a_{1}^{-1}
\dots a_{r}^{-1}t^{-1})
\ee
for $j=1,\dots,r$ with
\be
A_{j}(a,b,q) =
\frac{(q;q)_{\infty}^2}{\theta(q^{-1}a_{j};q)
  \prod_{i=1,i\neq j}^{r}(a_{i}/a_{j};q)_{\infty}}
\prod_{i=1}^{r}
\frac{(a_{i};q)_{\infty}(b_{i-1}/a_{j};q)_{\infty}}{(b_{i-1};q)_{\infty}}\,.
\ee
The calculation of the monodromy is a classical result and follows from
~\cite[Eq.(4.5.2)]{Gasper}. The monodromy
$\vM(t,a,b,q) = V(t,a,b,q)^{-1}U(t,a,b,q)$ is given explicitly by
\be
\label{Mheine}
\vM(t,a,b,q) =
\begin{pmatrix}
  1 & \frac{(q;q)_{\infty}^{3}\theta(b_{1}t;q)\theta(a_{1}/b_{1}t;q)
  \theta(a_{1};q)}{\theta(t;q)\theta(a_{1}t;q)\theta(b_{1};q)\theta(a_{1}/b_{1};q)}
  & \dots & \frac{(q;q)_{\infty}^{3}\theta(b_{r-1}t;q)\theta(a_{1}/b_{r-1}t;q)
  \theta(a_{1};q)}{\theta(t;q)\theta(a_{1}t;q)\theta(b_{r-1};q)\theta(a_{1}/b_{r-1};q)}
  \\
1 & \frac{(q;q)_{\infty}^{3}\theta(b_{1}t;q)\theta(a_{2}/b_{1}t;q)
  \theta(a_{2};q)}{\theta(t;q)\theta(a_{2}t;q)\theta(b_{1};q)\theta(a_{2}/b_{1};q)}
& \dots & \frac{(q;q)_{\infty}^{3}\theta(b_{r-1}t;q)\theta(a_{2}/b_{r-1}t;q)
  \theta(a_{2};q)}{\theta(t;q)\theta(a_{2}t;q)\theta(b_{r-1};q)\theta(a_{2}/b_{r-1};q)}
\\
: & : & : & \dots
\\
1 & \frac{(q;q)_{\infty}^{3}\theta(b_{1}t;q)\theta(a_{r}/b_{1}t;q)
  \theta(a_{r};q)}{\theta(t;q)\theta(a_{r}t;q)\theta(b_{1};q)\theta(a_{r}/b_{1};q)}
& \dots & \frac{(q;q)_{\infty}^{3}\theta(b_{r-1}t;q)\theta(a_{r}/b_{r-1}t;q)
  \theta(a_{r};q)}{\theta(t;q)\theta(a_{r}t;q)\theta(b_{r-1};q)\theta(a_{r}/b_{r-1};q)}
\end{pmatrix} \,.
\ee
Then from the modularity of the Dedekind $\eta$-function and the Jacobi
$\theta$-function the matrix $\vM$ satisfies the modular transformation~\eqref{Mmod}
with weights $\kappa_{U}=(0,1,\dots,1)$ and $\kappa_{V}=(0,\dots,0)$.

When $a,b$ are specialised at points where there are singularities, one can take
coefficients of the expansion around these points to define $U,V$.

Theorem~\ref{thm.heine} states that the generalised $q$-hypergeometric equation in
modular. The theorem will also hold when we specialise the values of $a,b$. This is
because the integral representations of the cocycle will be regular at these
specialisations and the factorisation of the integral will similarly involve the
expansion around these points as it will involve computation of residues of higher
order.

\begin{theorem}
\label{thm.heine}
The two cocycles~\eqref{Om} $\Om_{U}$ and $\Om_{V}$ are equal and modular.
















\end{theorem}

The proof of the above theorem is given in Section~\ref{sec.heine} and uses an
integral representation of the solutions of Equation~\eqref{gener.qhyper} in
terms of a special function, the Faddeev quantum dilogarithm~\cite{Faddeev,FK-QDL},
the factorisation of the corresponding integrals (so-called state integrals)
as a bilinear combination functions of $z,\tau$ and $(z/\tau,-1/\tau)$ along the
lines of~\cite{GK:qseries}, combined with an explicit description of the
self-duality of the corresponding $q$-holonomic module. What is more, the $U$ and the
$V$ cocycles are obtained by moving the contour of integration of the state integral
upwards or downwards, respectively, and this is one explanation of their
equality. We also remark that the above theorem is valid for $r=1$,
where the corresponding cocycle is none other than a ratio of two Faddeev
quantum dilogarithms.
