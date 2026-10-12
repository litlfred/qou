---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-027-58-an-analytic-lift-of-the-colored-jones-polynom
section_title: "An analytic lift of the colored Jones polynomial"
section_number: 5.8
pages: 62-62
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
text_source: latex
latex_prose_ratio: 0.88
latex_coverage_ratio: 0.987
---
\label{sub.CJ41lift}

We finish this section by giving a proof of Theorem~\ref{thm.CJ41lift}. The
main observation is that when $x=q^N$, the series $\hat{f}^{(0)}(t,q^{N},q)$
terminates to a polynomial of $t$, in which case the $q$-Borel transfrom, followed
by a $q$-Laplace transfrom is the identity. Explicitly, when $x=q^{N}$ for
$N\in\BZ_{\geq1}$ we have
  \be
  \begin{aligned}
\hat{f}^{(0)}(t,q^{N},q)
&=
\sum_{k=0}^{\infty}(-1)^{k}q^{-k(k+1)/2}
(q^{1+N};q)_{k}(q^{1-N};q)_{k}t^{k}\\
&=
\sum_{k=0}^{N-1}(-1)^{k}q^{-k(k+1)/2}
(q^{N+1};q)_{k}(q^{1-N};q)_{k}t^{k}\,.
  \end{aligned}
  \ee
  The theorem then follows from Equation~\eqref{qlapbort}.
\qed


\subsection{Specialisation $t=q^m$}
\label{sub.tqm}

In this short subsection, included for completeness, we briefly comment how
our analytic functions of $t$, specialised to $t=q^m$, become the known sequences
of $q$-series and $(x,q)$-series that have appeared in the literature. 
In~\cite{GZ:qseries} and~\cite{GGM:peacock,GGM,GGMW:trivial} the $q$-holonomic
modules are discrete versions of what we have considered in Section~\ref{sec.41}.
Here we describe how the solutions can be constructed from the ones presented here.
Consider a solution $f(t,q)$ of a $q$-difference equation
$$
a_r(t,q) f(q^r t, q) + a_{r-1}(t,q) f(q^{r-1}t,q) + \dots + a_0(t,q) f(t,q) =0 
$$
corresponding to an edge of slope $\kappa$ on the Newton polygon, and let
\be
\label{fm}
f_{m}(q)=(-1)^{\kappa m}q^{-\kappa m(m+1)/2}
\Res_{z=0}\theta(q^{m}\e(z),q)^{-\kappa}f(q^{m}\e(z),q)\frac{dz}{2\pi iz} \,.
\ee
Then we find that $f_m(q)$ satisfies the linear $q$-difference equation
$$
a_r(q^m,q) f_{r+m}(q) + a_{r-1}(q^m,q) f_{r+m-1}(q) + \dots
  + a_0(q^m,q) f_{m}(q) =0 \,.
$$
This follows from   
\be
\begin{small}
\begin{aligned}
  0=&\Res_{z=0}\left(a_r(q^m\e(z),q) f(q^{r+m}\e(z), q)
    + a_{r-1}(q^m\e(z),q) f(q^{r+m-1}\e(z),q) + \dots \right. \\ & \left.
    + a_0(q^m\e(z),q) f(q^m\e(z),q)\right)
  \frac{\e(\kappa z)dz}{\theta(\e(z);q)^{\kappa}2\pi iz}\\
  =&a_r(q^m,q) f_{r+m}(q) + a_{r-1}(q^m,q) f_{r+m-1}(q) + \dots
  + a_0(q^m,q) f_{m}(q) 
\end{aligned}
\end{small}
\ee
where the equality follows from holomorphicity of $\theta^{-\kappa}f$ or the
higher order of vanishing of the indicial polynomial.

For example, for the Equation~\eqref{41x1}, and its solution
solution $g^{(0,1)}$ defined in Equation~\eqref{ex41.g00}, we obtain that 
\be
    \Res_{z=0}g^{(0,1)}(q^{m}\e(z),q)\frac{dz}{2\pi iz}
    =
    \sum_{k=0}^{\infty}\left(k+\frac{1}{2}-m
  -2E^{(k)}_{1}(q)\right)(-1)^{k}\frac{q^{k(k+1)/2-km-m}}{(q;q)_{k}^{2}} \,,
\ee
a $q$-series that appears in \cite[Equ.13b]{GGM} and \cite[Equ.6]{GGMW:trivial}.
