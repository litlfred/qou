---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q -HOLONOMIC MODULES"
section_id: sec-017-34-resonance
section_title: "Resonance"
section_number: 3.4
pages: 29-30
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
toc_source: outline
text_source: latex
latex_prose_ratio: 0.884
latex_coverage_ratio: 0.96
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
In this section we discuss in detail the resonant generalised $q$-hypergeometric
equation~\eqref{gener.qhyper}, i.e., the case where at least one of the ratios
$a_i/a_j$ (for $i \neq j$), $b_i/b_j$ (for $i \neq j$) or $a_i/b_j$ (for some $i$
and $j$) is an integer power of $q$. For simplicity, we will 
consider only the case of $r=2$, although our arguments remain valid for all
$r$. When $r=2$, the system of equations ~\eqref{heine.equs} is given by
{\small
\be
\label{2phi1equs}
\begin{aligned}
  (1-t)f(t,a,b,c,q)-(q^{-1}c+1-t(a+b))f(qt,a,b,c,q)+(q^{-1}c-tab)f(q^2t,a,b,c,q)
  &=0\\
  f(t,q^{-1}a,b,c,q)-q^{-1}af(qt,q^{-1}a,b,c,q)-(1-q^{-1}a)f(t,a,b,c,q)
  &=0\\
  f(t,a,q^{-1}b,c,q)-q^{-1}bf(qt,a,q^{-1}b,c,q)-(1-q^{-1}b)f(t,a,b,c,q)
  &=0\\
  f(t,a,b,c,q)-q^{-1}cf(qt,a,b,c,q)-(1-q^{-1}c)f(t,a,b,q^{-1}c,q)
  &=0\,,
\end{aligned}
\ee
}

\noindent
with Equation~\eqref{2phi1} being one such solution. We can specialise $a,b,c$ so
that some of $a$, $b$, $c$, $a/b$, $a/c$ or $b/c$ lies in $q^{\BZ}$. All of these
conditions can be seen to be special
points of the monodromy matrix~\eqref{Mheine} and various special properties of the
equations appear like, for example, submodules. 

We now present two examples of these special points in the simplest case or
$r=2$. These can all be deduced from Theorem~\ref{thm.heine}.

\noindent
$\bullet \,\, b=c$. 
The first Equation~\eqref{2phi1equs} now takes the form
\be
\begin{aligned}
  &(1-q^{-1}b\s_{t})\left((1-\s_{t})-t(1-a\s_{t})\right)\\
  &=\left((1-\s_{t})(1-q^{-1}b\s_{t})-t(1-a\s_{t})(1-b\s_{t})\right)f\\
  &=0\,.
\end{aligned}
\ee
This has normalised solutions
\be
\begin{aligned}
  f^{(1)}(t,a,b,q)
  &=
  \sum_{k=0}^{\infty}\frac{(a;q)_{k}}{(q;q)_{k}}t^{k}\\
  f^{(qb^{-1})}(t,a,b,q)
  &=
  \frac{(a;q)_{\infty}(q^{2}b^{-1};q)_{\infty}
  \theta(q^{-1}bt;q)(q;q)_{\infty}^{2}}{(qab^{-1};q)_{\infty}\theta(q^{-1}b;q)
  \theta(t;q)}\sum_{k=0}^{\infty}\frac{(qab^{-1};q)_{k}}{(q^{2}b^{-1};q)_{k}}t^{k}\,.
\end{aligned}
\ee
Note that the first generates a submodule and indeed satisfies
\be
\left(\left((1-\s_{t})-t(1-a\s_{t})\right)f^{(1)}\right)(t,q)
=(1-t)f^{(1)}(t,a,b,q)-(1-at)f^{(1)}(qt,a,b,q)=0\,.
\ee
We note that for the value at $t=0$ and the $q$-difference equation we see that
\be
  f^{(1)}(t,a,b,q)
  =
  \frac{(at;q)_{\infty}}{(t;q)_{\infty}}
\ee
a classical result known as the $q$-binomial theorem. From Theorem~\ref{thm.ex1} or
even Theorem~\ref{thm.heine} with $r=1$, we then see that this is a modular
$q$-holonomic submodule. Now the second solution satisfies the inhomogeneous equation
\be
(1-t)f^{(qb^{-1})}(t,a,b,q)-(1-at)f^{(qb^{-1})}(qt,a,b,q)
=\frac{(a;q)_{\infty}(q^{2}b^{-1};q)_{\infty}
  \theta(q^{-1}bt;q)(q;q)_{\infty}^{2}}{(qab^{-1};q)_{\infty}
  \theta(q^{-1}b;q)\theta(t;q)}
\ee
where we note that the RHS is of course annihilated by $(1-q^{-1}b\s_{t})$. The full
module can then be shown to be modular using elementary functions holomorphic for
$\tau\in\BC'$ times the state integral









\be
\begin{aligned}
\int_{\calC}
\frac{\Phi_{\sfb}(x)}
{\Phi_{\sfb}(x+i\sfb^{-1}\alpha)}
\frac{\exp\left(-2\pi\frac{zx}{\sfb}\right)}{1+\tq^{1/2}
  \exp\left(-2\pi\frac{x}{\sfb}\right)\e(\beta/\tau)}
dx \,.
\end{aligned}
\ee
Note that this state integral is of course the same as the one in
Equation~\eqref{heine.stateint} where $\beta_{1}=\gamma=\beta+1=\alpha_{2}+1$.

\noindent
$\bullet \,\, c=q$. 
The first Equation~\eqref{2phi1equs} now takes the form
\be
    (1-t)f(t,a,b,q)-(2-t(a+b))f(qt,a,b,q)+(1-tab)f(q^2t,a,b,q)=0\,.
\ee
Notice that this now has indicial polynomial $(1-\rho)^2$. Therefore, we expand
using the Frobenius method to find solutions which are the coefficients of $\ve$
in the expansion to order $O(\ve^2)$ of 
\be
\begin{aligned}
  f^{(1,0)}(t,a,b,q)&=\frac{(qe^{\ve};q)_{\infty}^{2}}{
    (ae^{\ve};q)_{\infty}(be^{\ve};q)_{\infty}}\sum_{k=0}^{\infty}
  \frac{(ae^{\ve};q)_{k}(be^{\ve};q)_{k}}{(qe^{\ve};q)_{k}^{2}}t^{k}
  \frac{\theta(e^{-\ve}t;q)}{\theta(t;q)}\\
  &=f^{(1,0)}(t,a,b,q)+f^{(1,1)}(t,a,b,q)\ve+O(\ve^2)\,.
\end{aligned}
\ee
Then considering the state integral












\be
\begin{aligned}
\int_{\calC}
\frac{\Phi_{\sfb}(x)^2}
{\Phi_{\sfb}(x+i\sfb^{-1}\alpha)\Phi_{\sfb}(x+i\sfb^{-1}\beta)}
\exp\left(-2\pi\frac{zx}{\sfb}\right)
dx \,.
\end{aligned}
\ee
along with Equation~\eqref{S.mod.thd} we can show that the module is modular with
this special value.





\section{Proof of Theorems~\ref{thm.ex1} and~\ref{thm.ex2}}
\label{sec.thm12}
