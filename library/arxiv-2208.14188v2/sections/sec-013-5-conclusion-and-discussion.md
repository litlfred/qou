---
doc_id: arxiv-2208.14188v2
doc_title: "Resurgence in complex Chern-Simons theory at generic levels"
section_id: sec-013-5-conclusion-and-discussion
section_title: "Conclusion and discussion"
section_number: 5
pages: 34-38
source_pdf: 2208.14188v2.pdf
source_sha256: 92a7651c81b799b3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.902
doc_brief: "Resurgence in complex Chern-Simons theory at generic levels — In this note we study the resurgent structure of sl(2, C) Chern-Simons state integral model on knot complements S3\41, S3\52 with generic"
---
\label{sc:con}

In this short note we study the resurgent properties of the
$sl(2,\IC)$ Chern-Simons state integral model on knot complemnets
$S^3\backslash \knot{4}_1$, $S^3\backslash \knot{5}_2$ at generic
level $k\geq 1$.

When the level $k$ increases, the saddle point expansion of the $sl(2,\IC)$
Chern-Simons state integral becomes
increasingly more complicated.
But there are several interesting universal featrues.

First of all, the coefficients of the power series always live in the
trace field of the knot extended by the holonomy paramter $x$.

Second, these power series enjoy universal resurgent properies.  When
the holonomy deformed is weak so that $|\log x^k|\ll 1$, the
distribution of the singularities of the Borel transform is the same
and they are all related to the level $k=1$ singularites by a factor
of $1/k$.  In addition, the Stokes constants associated to these
singularities are independent of the level $k$.  We speculate that
this is related to the fact the Hilbert space of the quantum
Chern-Simons theory at level $k$ is simply a $k$ copy of the level one
theory, and that they all coincide with the same BPS invariants of the
dual 3d SCFT.

Some interesting questions remain unanswered following this work.
Both this work and its predecessor \cite{Garoufalidis:2020xec} focus
on the case when the holonomy is weak\footnote{There are some limited
  but unsystematic discussion for large holonomy in
  \cite{Garoufalidis:2020xec}.}.  It will be interesting to understand
the resurgent structure of the Chern-Simons theory in the entire
holonomy space.  Due to the identification of the Stokes constants
with the BPS invariants in the dual 3d SCFT
\cite{Garoufalidis:2020xec,Garoufalidis:2020nut}, the evolution of the
resurgent structure as the holonomy changes may enjoy features similar
to the Wall Crossing Formulas of Kontsevich and Soibelman
\cite{Kontsevich:2008fj}.

Second, it was shown in \cite{Garoufalidis:2021osl} that the resurgent
structures presented in
\cite{Garoufalidis:2020xec,Garoufalidis:2020nut} are not complete:
They involve only asymptotic series $\varphi^{(k=1,\s_j)}(x;\tau)$
($j\geq 1$) associated to non-Abelian flat connections, while there
still remains the asymptotic series $\varphi^{(k=1,\s_0)}(x;\tau)$
associated to the Abelian flat connection.  It was revealed in
\cite{Garoufalidis:2021osl} with examples of $\knot{4}_1$ and
$\knot{5}_2$ that there are non-trivial Stokes automorphisms that
relate $\varphi^{(k=1,\s_0)}(x;\tau)$ to
$\varphi^{(k=1,\s_j)}(x;\tau)$ ($j\geq 1$) but not the other way
around.  This is similar to the discovery in the case of compact three
manifolds in \cite{Gukov2016}.  It would be interesting to also
generalise this connection to generic levels.

In fact, the power series $\varphi^{(k=1,\s_0)}(x;\tau)$ were computed
by expanding colored Jones polynomial near $q\rightarrow 1$.  Both
$\varphi^{(k=1,\s_0)}(1;\tau)$ and $\varphi^{(k=1,\s_j)}(1;\tau)$ with
holonomy turned off appear in the Refined Quantum Modularity
Conjecture \cite{Zagier:2010qmf,Garoufalidis:2021lcp} in the case of
S-transformation (see also \cite{Dimofte:2015kkp,Dimofte:2012qj}).
For a generic $sl(2,\IZ)$ transformation
$(\begin{smallmatrix} a&b\\c&d\end{smallmatrix})$, the power series
should be replaced by $\varphi^{(k=c,\s_0)}(1;\tau)$ and
$\varphi^{(k=c,\s_j)}(1;\tau)$ or their Galois transformation in the
trace field.  The power series $\varphi^{(k=c,\s_0)}(x;\tau)$ can be
computed by expanding colored Jones polynomial near
$q\rightarrow \exp2\pi\ri/c$.  We conjecture then that
$\varphi^{(k,\s_0)}(x;\tau)$ constructed this way is also related to
$\varphi^{(k,\s_j)}(x;\tau)$ ($j\geq 1$) computed in this work by
non-trivial Stokes automorphisms, where the Stokes constants coincide
with those in \cite{Garoufalidis:2021osl}.

We have been focusing on the generalisation of
\cite{Garoufalidis:2020xec,Garoufalidis:2020nut} to $sl(2,\IC)$
Chern-Simons theory with higher levels $k\geq 1$.  Other directions of
generalisation are also possible.  For instance one can consider
$sl(N,\IC)$ Chern-Simons theory with $N\geq 2$.  State integral models
have also been written down in \cite{Dimofte:2013iv}.

Alternatively, one can also study the resurgent structures of the
Chern-Simons theory at level $k=0$.  This is a special case, and by
the 3d-3d correspondence, it is dual to the 3d SCFT on $S^2\times S^1$
\cite{Dimofte:2011py}, whose partition function is nothing else but
the supersymmetric indices of the 3d SCFT.  In other words, one could
study the saddle point expansion of the indices and their resurgent
structures. See related work in
\cite{Garoufalids:2022pmi}. Furthermore, three manifolds obtained from
Dehn filling of hyperbolic knot complements are also interesting
objects to study \cite{Gang:2017cwq,Choi:2022dju}.

Finally, following the arguments in \cite{Gaiotto2008cd} (see a
similar application of the same idea \cite{Ito:2018eon}), the Stokes
automorphism together with the asymptotic behavior define for us a
Riemann-Hilbert problem for the Borel resummed asymptotic series.  The
latter may be solved by a TBA-like equation.  It is interesting to
explore if such a TBA-like equation can be written down for Borel
resummed asymptotic series in complex Chern-Simons theory.  As
showcased in \cite{Ito:2018eon}, such an equation could help answer
the question of the evolution of the resurgent structure as we change
the moduli of the system, which are the holonomy parameter $x$ here.


\section{Acknowledgements}

We thank Sunjin Choi, Dongmin Gang, Stavros Garoufalidis, Kimyeong Lee, Sungjay Lee, Marcos Mari\~no for stimulating
discussions. Main results of this work have been presented by ZD in Incheon workshop "New Frontiers in Quantum Field Theory and String Theory" and string theory seminar at LPENS. ZD would like to thank the audience for suggestions and feedback. ZD is supported by KIAS Grant PG076902. JG is supported by the Startup Funding no.~3207022203A1 and no.~4060692201/011 of the Southeast University.
