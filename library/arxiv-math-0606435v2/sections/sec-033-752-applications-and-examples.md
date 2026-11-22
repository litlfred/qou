---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-033-752-applications-and-examples
section_title: "Applications and examples"
section_number: 7.5.2
pages: 55-56
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.985
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
The image of the r.h.s. of \eqref{qw0} under \eqref{qw}
will be some curve in $\bC$ that generically intersects
$S^1$ in a finite number of points. This parametric
equality can be examined numerically and allows to recover
$A=\tr \psi_3$ up to finite indeterminacy. In particular,
we have

\begin{prop}\label{4brt}
Assume for some $t\in S^1$ with $|\arg t|\le \pi/2$ we
cannot find $y$ as in \eqref{qw0}, such that $\lm_1$
given by \eqref{qw} has norm 1 and \eqref{qw2} holds. Then
there is no $\bt\in B_4$ with the given $e$ whose closure has
the given Alexander and Jones polynomial. \qed
\end{prop}

\begin{rem}
To apply the test in practice, one chooses a small stepwidth $s$
for $y$ in the interval \eqref{qw0}, and calculates the derivative
of the r.h.s. of \eqref{qw} in $y$ to have an error bound on
$||\lm_1|-1|$ in terms of $s$. When some of the radicands in \eqref{Gm}
becomes close to $0$, some care is needed. One situation where
such degeneracy occurs are the knots $15_{144634}$, $15_{144635}$,
and $15_{145731}$. They have representations $\bt\in B_4$, whose
Burau matrix is trivial for $t=e^{\pi i/3}$. This may be noteworthy
on its own in relation to the problem whether $\psi_3$ is faithful. 
(Clearly $\psi_3$ is unfaithful at any root of unity on the
center of $B_4$, but here $\bt$ is not even a pure braid.)
\end{rem}

\begin{exam}
Applying proposition \reference{4brt} we can exclude $11_{387}$, one
of the 7 prime 11 crossing knots with $b=5$ but $MWF\le 4$. Eleven
prime knots with 12 crossings, and 63 of 13 crossings where braid
index 4 is not prohibited by MWF can be ruled out. The correctness
of these examples was later verified by the 2-cabled MWF. Up to 16
crossings more than 4000 examples were obtained. (Let us note that
from them only about 100 can be identified using the norm estimates.)
\end{exam}

\begin{exam}
The check of prime 14 crossing knots to which our criterion applied,
revealed 6 knots with 2-cable MWF bound 8. One, $14_{22691}$,
can be excluded from braid index 4 (as done with $14_{45759}$ 
in \cite{posex_bcr}), by making the $v$-degrees of the
polynomial of the 2-cable contradict the exponent sum of its
possible 8-braid representation. However, for the other 5
knots, $14_{28220}$, $14_{30960}$, $14_{41334}$, $14_{41703}$,
and $14_{44371}$, the argument fails, and so our condition
seems the only applicable one. (Clearly a 3-cable polynomial
is not a computationally reasonable option, and even the 2-cable
requires up to several hours, while our test lasts a few seconds.)
\end{exam}

Still our criterion leaves open several interesting examples
of (apparent) failure of the 2-cable MWF inequality, among
them the knot $13_{9684}$ encountered with M.~Hirasawa. A more
general, and important, possible application is as follows.

\begin{rem}\label{rJC}
In relation to Jones's conjecture \reference{jcc}, we
already quoted (in the proof of theorem \ref{thJC})
the observation in \cite{posex_bcr} that counterexamples
to the conjecture would make MWF and \em{all} of its cabled
versions unsharp. In that sense, our 4-braid test may be
the first possible approach toward identifying such a
counterexample. Birman-Menasco claimed indeed a family
of 6-string potential counterexamples, and K.~Kawamuro
gave later a simpler family on 5 strings. Extensive
checks with our test of Kawamuro's knots failed to turn up
successful cases. This puzzled us a while, until Kawamuro
reported recently that in fact H.~Matsuda falsified all
Birman-Menasco (and hence also Kawamuro's) candidates.
\end{rem}
