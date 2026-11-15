---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q -HOLONOMIC MODULES"
section_id: sec-001-11-summary
section_title: "Summary"
section_number: 1.1
pages: 2-3
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
toc_source: outline
text_source: latex
latex_prose_ratio: 0.939
latex_coverage_ratio: 1.0
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
We introduce a new class of linear $q$-difference equations and (corresponding
$q$-holonomic modules) which we call \emph{modular}, with several key features.

\begin{itemize}
  \item
 Their fundamental solutions at 0 and infinity have explicitly
  computable monodromy.
\item
  A natural $\SL_2(\BZ)$-cocycle constructed from a fundamental
  solution extends from $\BC\setminus\BR$ to the complex plane minus a ray in
  the real numbers.
\item
  Their fundamental solutions are meromorphic and their residues are
  expressed in terms of the solutions themselves (kind of 'resurgence').
\end{itemize}
Modular $q$-holonomic modules are abundant. We show that the generalised
$q$-hypergeometric equation ~\eqref{gener.qhyper} (and in particular
the $q$-hypergeometric equation) is modular and self-dual; see
Theorem~\ref{thm.heine} below. Among other things, this implies an improved
analyticity for the $q$-hypergeometric function
\be
\label{2phi1}
  {}_{2}\phi_{1}(a,b;c;q,t) =
  \sum_{k=0}^{\infty}\frac{(a;q)_{k}(b;q)_{k}}{(c;q)_{k}(q;q)_{k}}t^{k} \,,
\ee
namely, that the bilinear combination
\be
\begin{aligned}
  &\frac{(q;q)_{\infty}(c;q)_{\infty}}{(a;q)_{\infty}(b;q)_{\infty}}
  \frac{(\tq\tilde{a};\tq)_{\infty}(\tq\tilde{b};\tq)_{\infty}}{
    (\tq;\tq)_{\infty}(\tq\tilde{c};\tq)_{\infty}}{}_{2}\phi_{1}(a,b;c;q,t)
  {}_{2}\phi_{1}(\tilde{a}^{-1},\tilde{b}^{-1};\tilde{c}^{-1};\tq,\tq\tilde{a}
  \tilde{b}\tilde{c}^{-1}\tilde{t})\\
  &+\tau\frac{\theta(q^{-1}ct;q)(q;q)_{\infty}^{3}}{\theta(t;q)\theta(q^{-1}c;q)}
  \frac{(q^{2}c^{-1};q)_{\infty}(q;q)_{\infty}}{
    (qac^{-1};q)_{\infty}(qbc^{-1};q)_{\infty}}
  \frac{\theta(\tq\tilde{c};\tq)\theta(\tilde{t};\tq)}{
    \theta(\tq\tilde{c}\tilde{t};\tq)
    (\tq;\tq)_{\infty}^3}\frac{(\tilde{a}\tilde{c}^{-1};\tq)_{\infty}
    (\tilde{b}\tilde{c}^{-1};\tq)_{\infty}}{(\tq^{-1}\tilde{c}^{-1};\tq)_{\infty}
    (\tq;\tq)_{\infty}}\\
  &\quad\times{}_{2}\phi_{1}(qac^{-1},qbc^{-1};q^2c^{-1};q,t)
  {}_{2}\phi_{1}(\tq\tilde{a}^{-1}\tilde{c},
  \tq\tilde{b}^{-1}\tilde{c};\tq^2\tilde{c};
  \tq,\tq\tilde{a}\tilde{b}\tilde{c}^{-1}\tilde{t})
\end{aligned}
\ee
(which a priori is a meromorphic function of $\tau \in \BC\setminus\BR$)
extends to $\tau\in\BC\setminus(-\infty,0]$.
We also show that modular linear $q$-difference equations and the corresponding
$q$-holonomic modules appear naturally in complex Chern-Simons theory. We illustrate
with three examples (Theorems~\ref{thm.ex1}, ~\ref{thm.ex2} and ~\ref{thm.41} below)
whose corresponding cocycles are the Faddeev quantum dilogarithm, the Appell-Lerch
sums, and the Andersen--Kashaev state integrals of the $4_1$ knot.

We expect that all proper (i.e., basic) $q$-hypergeometric modules are modular, and
in particular the ones that appear in the quantum differential equation in Quantum
Cohomology, or the linear q-difference equation for the small J-function of
Quantum K-Theory.
