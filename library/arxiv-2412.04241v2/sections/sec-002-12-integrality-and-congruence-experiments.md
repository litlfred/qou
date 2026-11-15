---
doc_id: arxiv-2412.04241v2
doc_title: "The Habiro ring of a number field"
section_id: sec-002-12-integrality-and-congruence-experiments
section_title: "Integrality and congruence experiments"
section_number: 1.2
pages: 2-4
source_pdf: 2412.04241v2.pdf
source_sha256: 308d1dd1c42bd979
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.962
doc_brief: "The Habiro ring of a number field — We introduce the Habiro ring of a number field K and modules over it graded by K3(K)."
---
\label{sub.intexp}

Early experiments by two of the authors on perturbative
invariants of Chern--Simons theory revealed unexpected integrality and gluing
properties of functions near roots of unity. The explanation of this phenomenon was
the original motivation for this work.
One of the experiments in question involved the power series $\Phi(h)$ that appear
in the asymptotic expansion of the Kashaev invariant of the $4_1$ knot, whose first
few terms are given (after multiplication by an overall eighth root of unity)
by~\cite[Eqn.(3)]{GZ:kashaev} 
\be
\label{as41}
\Phi(h)\=  \frac1{\sqrt[4]{-3}}\, 
\Bigl(1 + \frac{11}{24 \cdot 3 \sqrt{-3}}\,h + \frac{697}{1152 \cdot
  (3\sqrt{-3})^2}\,h^2
 + \frac{724351}{414720 \cdot (3 \sqrt{-3})^3}\,h^3 +\cdots\Bigr)\,. 
\ee




\noindent
At the time, 100 terms of the series $\Phi(h)$ were known, and the denominator of
the coefficient of $h^{100}$ was given by
\begin{small}
\begin{equation*}
  2^{397}\!\! \cdot 3^{298}\!\! \cdot 5^{40}\!\! \cdot 7^{22}\!\! \cdot 11^{12}\!\!
  \cdot 13^9 \!\cdot 17^6\!\cdot 19^5\!\cdot 23^4\!\cdot 29^3\!\cdot 31^3\!\cdot 37^2
  \!\cdot 41^2\!\cdot 43^2\!\cdot 47^2\!\cdot 53 \cdot 59 \cdot 61 \cdot 67 \cdot 71
  \cdot 73 \cdot 79 \cdot 83 \cdot 89 \cdot 97 \!\cdot\! 101
\end{equation*}
\end{small}

\noindent
in agreement with Theorem 9.1 of~\cite{GZ:kashaev}. 
However, the symmetrised series $\Phi(h)\Phi(-h)$, after a change of variable $q=e^h$
starts with 
\be
\label{Phi41sym}
\Phi(h)\Phi(-h) \= \frac1{\sqrt{-3}}\,
\big(1 - \frac{1}{3^3} (q-1)^2 + \frac{1}{3^3} (q-1)^3 - \frac{4}{3^5} (q-1)^4
- \frac{1}{3^5} (q-1)^5 + O((q-1)^6) \big)\,,



\ee
with all coefficients being integral away from $3$,
e.g. the denominator of the coefficient of $(q-1)^{100}$ being $3^{146}$.

But that's not all. The asymptotics of the Kashaev invariant at other complex roots
of unity $\z$ (other than $1$ discussed above) involve a power series $\Phi_\z(h)$
discussed in~\cite{GZ:kashaev}, whose constant term is in the ring $\BZ[\z_6,\z,1/3]$.
(These series were denoted by $\Phi_\a(h)$ in~\cite{GZ:kashaev}, where
$\z=e^{2 \pi i \a}$, with $\a \in \BQ$ and $\z_6$ a primitive 6th root of unity).
On the other hand the series~\eqref{Phi41sym}, which lies in
$\BZ[1/\sqrt{-3}][\![q-1]\!]$, can be evaluated when $q=\z_p$ is a primitive $p$-th
root of unity (with $p$ a prime $p \neq 3$), the result being a well-defined element
of $\BZ_p[1/\sqrt{-3},\z_p]$, because $\z_p-1$ is $p$-adically small. These two
numbers matched, up to sign, with the constant term
of $\Phi_{\z_p}(h) \Phi_{\z_p}(-h)$. The sign depended on the prime $p$ and
was equal to $1$ when $p=1 \bmod 3$ and $-1$ when $p=2 \bmod 3$. In more invariant
terms, the sign was given by the Legendre symbol $(\tfrac{p}{3})$. 

Both parts of the experiment were reminiscent of properties that elements of the
Habiro ring have, and this was a motivation for the current paper. It turned out that
the symmetrised series considered above are concrete elements of an abstractly defined
Habiro ring of a number field (in this case $\mathbb{Q}(\sqrt{-3})$) whose definition
was originally motivated by the question
whether $q$-de Rham cohomology admits a definition over the Habiro ring. In this
general definition, the unexpected Legendre symbol originates from the $p$-Frobenius
endomorphism of a $p$-completed ring.

This answer pushed the question further to find a home for the unsymmetrised
collections of power series at roots of unity, which after all is the output of
perturbative Chern--Simons theory. It turned out that such collections are elements
of rank one modules over the Habiro ring of the number field indexed by the third
algebraic $K$-group of the number field.

Quite unexpectedly, another source of elements of these modules comes from
the admissible series introduced and studied by
Kontsevich--Soibelman~\cite{KS:cohomological}. These are generating series of
cohomological Hall algebras that appear in enumerative algebraic geometry such
as Donaldson--Thomas theory.

These two sources of elements gave two complementary clues about the definition of
the rank one modules. Combining both views with a correction coming from $p$-adic
analysis gave the definition of the promised modules.

A corollary of our work is that the Donaldson-Thomas invariants have arithmetic
meaning and that the elements of the Habiro ring of a number field have enumerative
meaning, both being related to the comparison of the $K$-theory of local and global
fields and to the ideas of $q$-de Rham cohomology.
