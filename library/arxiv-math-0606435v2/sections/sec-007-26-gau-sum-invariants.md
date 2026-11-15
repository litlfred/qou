---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-007-26-gau-sum-invariants
section_title: "Gau sum invariants"
section_number: 2.6
pages: 10-11
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 1.0
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
We recall briefly the definition of Gau\ss{} sum invariants.
They were introduced first in \cite{Fied} for braids, and later
\cite{Fied2,VirPol} for knots. It is known that all
they give formulas for Vassiliev invariants.

\begin{defi}(\protect\cite{Fied2})\ 
A Gau\ss{} diagram of a knot diagram is an oriented circle with
arrows connecting points on it mapped to a crossing and
oriented from the preimage of the undercrossing (underpass)
to the preimage of the overcrossing (overpass).
\end{defi}

We will call a pair of crossings whose arrows intersect in
the Gau\ss{} diagram a \em{linked} pair.

\begin{exam}
As an example, figure \ref{fig6_2} shows the knot $6_2$ in its
commonly known projection and the corresponding Gau\ss{} diagram.
\end{exam}

\begin{figure}[htb]
{
\[
\begin{array}{c@{\qquad}c}
     \diag{2cm}{2.0}{2.0}{
  \picputtext[dl]{0 0}{\autoepsffalse\epsfs{4cm}{6_2}}
  \picputtext[u]{1.25 1.65}{$1$} 
  \picputtext[u]{0.8 1.65}{$2$} 
  \picputtext[u]{0.6 0.6}{$3$} 
  \picputtext[u]{1.0 0.35}{$4$} 
  \picputtext[u]{1.3 0.9}{$5$} 
  \picputtext[u]{0.9 1.3}{$6$} 
	}
 & 
\diag{1.6cm}{2.4}{2.4}{\pictranslate{1.2 1.2}{
\piclinewidth{60}
\piccircle{0 0}{1}{}
\labar{240}{ 30}{1}
\labar{ 60}{210}{2}
\labar{300}{ 90}{3}
\labar{120}{330}{4}
\labar{  0}{150}{5}
\labar{180}{270}{6}
} 
} 
\end{array}
\]}
\caption{The standard diagram of the knot $6_2$ and its Gau\ss{}
diagram.\label{fig6_2}}
\end{figure}

The simplest (non-trivial) Vassiliev knot invariant is the
\em{Casson invariant} $v_2$, with $v_2=\Dl''(1)/2=-V''(1)/6$,
for which Polyak-Viro
\cite{VirPol,VirPol2} gave the simple Gau\ss{} sum formula
\begin{eqn}\label{pv2_}
v_2\,=\,\GD{\arrow{225}{45}
\arrow{315}{135}
\picfillgraycol{0}\picfilledcircle{1 90 polar}{0.09}{}
}\,.
\end{eqn}
Here the point on the circle corresponds to a point on the
knot diagram, to be placed arbitrarily except on a crossing.
(The expression does not alter with the position of the
basepoint; we will hence have, and need, the freedom to place
it conveniently.)

We will use the symmetrized version of \eqref{pv2_}
w.r.t. taking the mirror image of the knot diagram:
\begin{eqn}\label{pv2}
v_2\,=\,\frac{1}{2}\es\left(
\GD{\arrow{225}{45}
\arrow{315}{135}
\picfillgraycol{0}\picfilledcircle{1 90 polar}{0.09}{}
}+
\GD{\arrow{45}{225}
\arrow{135}{315}
\picfillgraycol{0}\picfilledcircle{1 90 polar}{0.09}{}
}\right)\,.
\end{eqn}
