---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-038-112-the-wkb-method
section_title: "The WKB method"
section_number: 11.2
pages: 25-25
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 1.0
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent polynomials, whose nth term is the nth colored Jones polynomial."
---
\lbl{sec.WKB}

Since we are discussing physics interpretations of Theorem \ref{thm.1}
let us make some more comments. Obviously, when the angle
$\a$ is sufficiently big, the asymptotic expansion of Equation \eqref{eq.thm1}
may break down. For example, when $e^{\a}$ is a complex root of the Alexander
polynomial, then the right hand side of \eqref{eq.thm1} does not make sense,
even to leading order. In fact, when $\a$ is near $2 \pi i$, then the solutions
are expected to grow exponentially, and not polynomially, according to the
Volume Conjecture.

The breakdown and change of rate of asymptotics is
a well-documented phenomenon well-known in physics, associated with WKB
analysis, after Wentzel-Krammer-Brillouin; see for example \cite{O}.
 In fact, one may obtain an independent proof of Theorem \ref{thm.1}
using {\em WKB analysis}, that is, the study of asymptotics of solutions of
difference equations with a small parameter.
The key idea is that the sequence of colored Jones
functions is a solution of a linear $q$-difference equation, as was
established in \cite{GL}. A discussion on WKB analysis of $q$-difference
equations was given by Geronimo and the first author in \cite{GG}.

The WKB analysis can, in particular, determine {\em small exponential
corrections} of the form $e^{-c_{\a} n}$ to the asymptotic expansion of
Theorem \ref{thm.1}, where $c_{\a}$ depends on $\a$, with $\text{Re}(c_{\a})
<0$ for $\a$ sufficiently small. These small exponential corrections
(often associated with instantons)
cannot be captured by classical asymptotic analysis (since they vanish
to all orders in $n$), but they are important and dominant (i.e.,
$\text{Re}(c_{\a})>0)$ when $\a$ is
near $2 \pi i$, according to the volume conjecture. Understanding the change of
sign of $\text{Re}(c_{\a})$ past certain so-called Stokes directions
is an important question that WKB addresses.

We will not elaborate or use the WKB analysis in the present paper.
Let us only mention that the loop expansion of the colored Jones function
can be interpreted as WKB asymptotics on a $q$-difference equation satisfied
by the colored Jones function.
