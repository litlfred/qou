---
doc_id: arxiv-2412.04241v2
doc_title: "The Habiro ring of a number field"
section_id: sec-009-19-future-extensions
section_title: "Future extensions"
section_number: 1.9
pages: 17-17
source_pdf: 2412.04241v2.pdf
source_sha256: 308d1dd1c42bd979
toc_source: outline
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 0.986
doc_brief: "The Habiro ring of a number field — We introduce the Habiro ring of a number field K and modules over it graded by K3(K)."
---
\label{sub.further}

We conclude this introduction by discussing several natural extensions of
our paper that we hope to come back to.

\noindent $\bullet$ {\bf Bad primes.}
The current definition of $\calH_R$ is a collection of power series associated to
all roots of unity that satisfies the gluing condition~\eqref{gluef}, which allows
to re-expand the series at $\z_{pm}$ from the series at $\z_m$ as long as the prime
$p$ is prime to $\Delta$. In other words, the series at $\z_1$ does not determine
the series at any $\z_m$ when $m$ is not prime to $\Delta$. This implies that
$\calH_R$ is not an integral domain, but instead a product of integral domains,
see the remark

of Section~\ref{sub.hab}. On the other hand, the collections $\Phitof_{A,z}(q)$ of
power series associated to a symmetric matrix $A$ together with a non-degenerate
solution $z$ to the Nahm equations assigns a collection of power series
$\Phitof_{A,z,m}(x)$ at all roots of unity, not just those that are prime to an
integer $\Delta$; see Theorem~\ref{thm.2} of Section~\ref{sub.results}. Understanding
how these series at
the bad primes determine the series at the remaining primes is an interesting
question whose answer could potentially improve the current definition of $\calH_R$.

\noindent $\bullet$ {\bf Relative Bloch group.}
The Habiro ring of the \'etale map $\BZ[t]\to S$
(with $S$ given in~\eqref{Sdef}) can be defined and
is being studied in the upcoming thesis of Ferdinand Wagner. With additional work,
one can define modules over this Habiro ring that are graded by a relative Bloch group
(defined like the usual Bloch group with $t \wedge S = 0$)
that ought to be identified with some relative $K$-theory group, and that the
collection of series $\Phitof_{A}(t,q)$ is an element of such a module.

\noindent $\bullet$ {\bf Higher weight modules.}
One can define higher weight modules over the Habiro ring of a number field,
indexed by the odd $K$ groups of a number field, which we hope to discuss in a
subsequent publication.

\noindent $\bullet$ {\bf Line bundles on $A_{\mathrm{inf}}$.}
The line bundles defined in the present paper can also be defined over
the period ring $A_{\mathrm{inf}}$ of $p$-adic Hodge theory, for all elements
of $K_3^{\mathrm{cont}}(\mathbb C_p)$. In this picture, the functions $\Phitof_A$
define sections of this line bundle on $\mathrm{Spa}(A_{\mathrm{inf}})$ away
from a disc around $\{q^{1/p}=1\}$.

\noindent $\bullet$ {\bf Relation with holomorphic quantum modular forms.}
A fifth extension concerns the quantum modularity properties
of the collection of the series associated to knots over $\BC$, and especially
the extension of matrices of holomorphic functions on $\BC\smallsetminus\BR$ to the
cut plane $\BC'=\BC\smallsetminus (-\infty,0]$, or more generally
$\BC_\gamma=\BC\smallsetminus \{\tau \in \BR \,| c \,\tau+d \leq 0\}$ for an element
$\gamma=\sma abcd \in \SL_2(\BZ)$; see~\cite[Sec.5]{GZ:kashaev}
and~\cite[Sec.5]{GZ:qseries}. There are some tantalising parallels between the
$p$-adic picture of the preceding bullet and this complex picture, similar to the
parallels between the Fargues-Fontaine curve and the so called twistor-$\mathbb P^1$.
