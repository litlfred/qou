---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-006-16-the-main-ideas-and-organization-of-the-paper
section_title: "The main ideas and organization of the paper"
section_number: 1.6
pages: 7-8
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
toc_source: outline
text_source: latex
latex_prose_ratio: 0.936
latex_coverage_ratio: 0.971
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent polynomials, whose nth term is the nth colored Jones polynomial."
---
\lbl{sub.ideas}

In section \ref{sub.complex} we show that weak convergence plus
uniform boundedness implies strong convergence. Thus the strong
convergence of
Theorems \ref{thm.11} and \ref{thm.1} follows from the weak
convergence of Theorems \ref{thm.MMR} and \ref{thm.Zrat},
plus uniform bounds.  Uniform bounds for the colored Jones function
require large cancellations. In order to control these cancellations,
we use the cyclotomic expansion of the colored Jones function of a
knot, which is recalled in Section \ref{sec.fti}. An important point
about this expansion is that its kernel can absorb the exponential
bounds of the coefficients of the cyclotomic functions; see Sections
\ref{sec.estimates} and \ref{sec.allorders}.




Using a state-sum formula for the colored Jones function, we give in
Section \ref{sec.boundsJones} bounds for the degrees and
coefficients of the $n$-th colored Jones polynomial. The result is
also of independent interest. The important point is that the local
weights in the state-sum formula (i.e., the entries of the
$R$-matrix) are Laurent polynomials, given by some ratio of
$q$-factorials. A priori, the bounds of the $n$-colored Jones
function are not good enough to deduce the bounds for the $n$-th
cyclotomic function. However, in Section \ref{sec.boundscyclotomic},
we use a lemma on the growth-rate of the number of partitions of an
integer, in order to deduce the desired bounds for the cyclotomic
function. As a corollary, we can deduce the upper bound of Theorem
\ref{thm.up}.

In the independent Section \ref{sec.hypgeom}, we give a better bound
for the growth-rate of the entries of the $R$-matrix. The important
point is that these entries are ratio of $5$ $q$-factorials, and
each $q$-factorial grows exponentially with rate given by the
Lobachevsky function. The $q$-factorials are arranged in such a way
to deduce that the exponential growth-rate of the entries of the
$R$-matrix is given by the volume of an ideal octahedron. Together
with our state-sum formulas for the $n$-th colored Jones polynomial,
it results in the upper bound of Theorem \ref{thm.4}.

We discuss in Section \ref{sec.cyclotomic} the proof of Theorems
\ref{thm.near1} and \ref{thm.near2}.

In Section \ref{sec.qholonomic} we discuss  bounds on the degrees
and coefficients of $q$-holonomic functions. Earlier work of the authors
implies that the colored Jones and the cyclotomic functions of a knot are
$q$-holonomic.

In Section \ref{sec.physics} we discuss some physics ideas related to the
various expansions of the colored Jones function.

Finally, in  the Appendices we establish the Volume Conjecture for the
Borromean rings using estimates obtained in the proofs of the main results.
At the time when the first draft of this paper was written (2004),  this was
the only hyperbolic link for which the volume conjecture is established.
Since then the volume conjecture has been proved for several other hyperbolic
links, see eg. \cite{Veen}.

Note that Theorems \ref{95} and \ref{thm.L1bound} are not used in the
proofs of our results, and are of independent interest.

The logical dependence of the main theorems is as follows:

$$
\divide\dgARROWLENGTH by2
\begin{diagram}
\node{\text{Thm \ref{thm.1alt}}}
\node{\text{Thm \ref{thm.near1}}}
\node{\text{Thm \ref{thm.near2}}}
\\
\node[2]{\text{Thm \ref{thm.11}}}
\arrow{nw}\arrow{n}\arrow{ne}
\node[2]{\text{Thm \ref{thm.1}}}
\\
\node{\text{Thm \ref{thm.MMR}}}
\arrow{ne}
\node{\text{Thm \ref{thm.boundC3}}}
\arrow{n}
\node{\text{Thm \ref{thm.boundC4}}}
\arrow{ne}
\node{\text{Thm \ref{thm.Zrat}}}
\arrow{n}
\\
\node[2]{\text{Thm \ref{thm.boundC}}}
\arrow{n}\arrow{ne}
\node[2]{\text{Thm \ref{thm.up}}}
\node[2]{\text{Thm \ref{thm.4}}}
\\
\node[3]{\text{Thm \ref{thm.3}}}
\arrow{nw}\arrow{ne}
\node[2]{\text{Prop \ref{prop.R+limit}}}
\arrow{ne}
\node[2]{\text{Prop \ref{prop.R}}}
\arrow{nw}
\end{diagram}
$$
