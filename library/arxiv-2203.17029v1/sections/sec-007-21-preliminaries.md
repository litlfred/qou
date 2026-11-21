---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q -HOLONOMIC MODULES"
section_id: sec-007-21-preliminaries
section_title: "Preliminaries"
section_number: 2.1
pages: 12-13
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
toc_source: outline
text_source: latex
latex_prose_ratio: 0.844
latex_coverage_ratio: 0.976
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
\label{sub.prelim}

It is well-known that formal power series solutions to linear difference equations
with a small parameter are typically factorially divergent series,
which lead to analytic solutions to the difference equation after applying the
process of a Borel transformation, followed by a Laplace transformation. This
subject is classical and well-studied, see for example~\cite{Bender,
  Costin:asymptotics,Miller:applied,Sauzin:divergent}.

A corresponding theory for linear $q$-difference equations was developed recently
by di Vizio, Sauloy, Ramis and others~\cite{Dreyfus:building,Hardouin,Ramis},
with particular emphasis given on the arithmetic and the Galois theoretic aspects
of the theory. A $q$-holonomic module has two canonical filtrations, one from $t=0$
and another from $t=\infty$. These filtrations can be computed concretely choosing
a cyclic vector which converts the $q$-holonomic module into a linear
$q$-difference equation.

To explain the solutions of linear $q$-difference equations, let us recall
 the Jacobi theta function which is given by a one dimensional
lattice sum, and by an infinite product (known as the Jacobi triple product identity)
by
\be
\label{theta}
\theta(t;q)
=
\sum_{k\in\BZ}(-1)^{k}q^{k(k+1)/2}t^{k}
=
(qt;q)_{\infty}(t^{-1};q)_{\infty}(q;q)_{\infty} \,.
\ee
From the above representation, it is easy to see that it satisfies the functional
equations
\be
\label{theta.fun}
\theta(t^{-1};q)
=

\theta(q^{-1}t;q)
=
-t\theta(t;q)
\ee
which imply that
\be
\label{theta.fun2}
\theta(q^{\ell}t;q)
=
(-1)^{\ell}q^{-\ell(\ell+1)/2}t^{-\ell}\theta(t;q),
\qquad (\ell \in \BZ) \,.
\ee
The Jacobi theta function is modular. Its transformation under the element
$S$ of $\SL_2(\BZ)$ is given by
\be
\label{thetaS}
\theta(\tilde{t};\tilde{q})
= \e(-3/8)
\e\left(\frac{z^{2}}{2\tau}\right)t^{\frac{1}{2}}
\tilde{t}^{-\frac{1}{2}}q^{\frac{1}{8}}\tq^{-\frac{1}{8}}\sqrt{\tau} \,
\theta(t;q)\,.
\ee
The derivative of $\theta$ with respect to $t d/dt=1/(2 \pi  i) d/dz$,
\be
\theta'(t;q)
=
\sum_{k}(-1)^{k}kq^{k(k+1)/2}t^{k}
\ee
satisfies the $q$-difference equation
\be
\label{thetader}
\frac{\theta'(q^{\ell}t;q)}{\theta(q^{\ell}t;q)}
=
\frac{\theta'(t;q)}{\theta(t;q)}-\ell \,.
\ee





It has transformation under the element $S$ of $\SL_2(\BZ)$ given by
\be
\label{S.mod.thd}
\begin{aligned}
  \frac{\theta'(t;q)}{\theta(t;q)} \Big|_{1} S
  :=\frac{1}{\tau}\frac{\theta'(\tilde{t};\tq)}{\theta(\tilde{t};\tq)}










&=
\frac{\theta'(t;q)}{\theta(t;q)}+\frac{z}{\tau}+\frac{1}{2}-\frac{1}{2\tau}\,.
\end{aligned}
\ee
