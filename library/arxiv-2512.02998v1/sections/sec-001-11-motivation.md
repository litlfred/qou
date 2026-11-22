---
doc_id: arxiv-2512.02998v1
doc_title: "Stability of knot equivalence at low regularity, and symmetric critical knots for the M\'obius energy"
section_id: sec-001-11-motivation
section_title: "Motivation"
section_number: 1.1
pages: 1-2
source_pdf: 2512.02998v1.pdf
source_sha256: 146ff93cd70baad4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.909
latex_coverage_ratio: 0.861
doc_brief: "Stability of knot equivalence at low regularity, and symmetric critical knots for the M\'obius energy — We present sufficient criteria for the equivalence of tame knots at low regularity."
---
The notion of \emph{ambient isotopy} is used in classical knot theory
to distinguish between different knot classes. It follows from a result
of Fisher \cite[Theorem~15]{fisher_1960} that 
two knots $\g_1,\g_2\in C^0(\R/\Z,\R^3)$
are ambiently isotopic if there exists an orientation preserving
homeomorphism $h:\R^3\to\R^3$ such that $h\circ\g_1=\g_2$. In concrete applications
it might be hard to come up with such a homeomorphism, but in the smooth category one
has the following useful stability theorem which to the best of our knowledge
has first been explicitly stated and proven by Diao et al.\@ who give also credit
to Ken Millet.
\begin{externaltheorem}[$C^1$-isotopy stability {\cite[Lemma 3$\cdot$2]{diao-etal_1999},
\cite{reiter_2005}, \cite[Proposition 3.1]{denne-sullivan_2008}}]
\label{thm:C1-stability}
For any immersed embedded curve $\g\in C^1(\R/\Z,\R^3)$ there is some number
$\epsilon_\g>0$ such that all curves $\eta\in C^1(\R/\Z,\R^3)$ with 
$\|\g-\eta\|_{C^1} < \epsilon_\g$ are embedded and ambiently isotopic to $\g$.
\end{externaltheorem}
This result also follows from the fact that any $C^1$-isotopy can be extended
to an ambient isotopy in arbitrary dimensions and co-dimensions which was proven\footnote{
For a proof in the simpler setting of the $C^2$-category see 
\cite[Chapter 8]{hirsch_1994}.}
by the first author in \cite{blatt_2009a}. The $C^1$-stability of isotopy is used
quite frequently in \emph{geometric knot theory} where one produces and investigates
specific knot representatives as minimizers or critical points of so-called
knot energies, 
to obtain more information about their knot classes; see, e.g., the
surveys 
\cite{strzelecki-vdm_2013a,strzelecki-etal_2013a,strzelecki-vdm_2014,blatt-reiter_2014,strzelecki-vdm_2018}  
and the many references therein. 
However, for the most interesting and mathematically more challenging
scale-invariant knot energies such as the M\"obius energy\footnote{In addition to 
scale-invariance the M\"obius energy is also invariant under M\"obius transformations
of the ambient Euclidean space \cite[Theorem~2.1]{freedman-etal_1994}, which lent
this energy that name.}
introduced by O'Hara \cite{ohara_1991a}
the underlying energy spaces do \emph{not} embed into $C^1$. Therefore,
one cannot expect, e.g., that minimizing sequences for these energies subconverge
in $C^1$, so that it is a priori not clear if the limit curves still belong to the
prescribed knot class. One of our goals in the present paper is therefore
to develop criteria
for stability of knot classes at low regularity.

For that we consider the slightly weaker notion
of \emph{knot equivalence} instead of ambient isotopy. Two knots $\g_1,\g_2\in
C^0(\R/\Z,\R^3)$ are said to be \emph{equivalent}, denoted by $\g_1\sim\g_2$, if and
only if there is a homeomorphism $h:\R^3\to\R^3$ such that $h(\g_1(\R/\Z))=\g_2(\R/\Z)$;
cf.\@ \cite[p. 4]{crowell-fox_1977}. It is known, e.g., that the trefoil knot is not
ambiently isotopic to its mirror image; see \cite[Theorem~3.39 (b)]{burde-zieschang_2014}. The corresponding reflection, however,
is an orientation reversing homeomorphism of $\R^3$ mapping the image of the trefoil
knot onto its mirror image, so that the two knots are equivalent.  So, there are
more (ambient) isotopy types than knot equivalence classes in knot space. On the other
hand, if two tame
arclength parametrized knots are equivalent, then one
can show that they are either ambiently
isotopic, or one is ambiently isotopic to the other one's mirror image. 

Gordon and Luecke studied in \cite{gordon-luecke_1989}
the fundamental groups of the knots' complements, also 
called \emph{knot groups}, and their peripheral subgroups. Combining their work
with results of Waldhausen \cite{waldhausen_1968} yields the following sufficient
criteria for knot equivalence.
\begin{externaltheorem}[Knot equivalence via knot complements
{\cite{waldhausen_1968,gordon-luecke_1989}}]\label{thm:gordon-luecke}
Let  $\g_1,\g_2\in C^0(\R/\Z,\R^3)$ be two tame knots.
\begin{enumerate}
\item[\rm (i)] If their complements $\R^3\setminus\g_i(\R/\Z)$, $i=1,2$, are homeomorphic,
then $\g_1\sim\g_2$.
\item[\rm (ii)] If $\g_1,\g_2$ are prime and their knot groups 
$\pi_1(\R^3\setminus\g_i(\R/\Z))$, $i=1,2,$ are isomorphic,  then $\g_1\sim\g_2$. 
\item[\rm (iii)] If the knot groups $\pi_1(\R^3\setminus\g_i(\R/\Z))$, $i=1,2,$ 
are isomorphic and if this isomorphism induces isomorphic peripheral subgroups $P_{\g_i}$, $i=1,2,$
then $\g_1\sim\g_2$ even if the $\g_i$ are composite knots.
\end{enumerate}
\end{externaltheorem}


Recall that for a set $M\subset\R^n$ with path-connected complement $\R^n\setminus M$
two closed loops $c_1,c_2\in C^0(\R/\Z,\R^n\setminus M)$ are equivalent if they are
homotopic, and that the fundamental group $\pi_1(\R^n\setminus M)$ consists of
the  respective equivalence classes. The group  structure is induced by concatenation
of closed loops containing a fixed base point in $\R^n\setminus M$. The peripheral
subgroup $P_M\subset\pi_1(\R^n\setminus M)$ then consists of all equivalence classes that
possess representative loops arbitrarily close to $M$.
