---
doc_id: arxiv-1106.6298v1
doc_title: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS"
section_id: sec-002-unified-invariants-of-integral-homology-3spheres
section_title: "Unified invariants of integral homology 3–spheres"
section_number: null
pages: 3-4
source_pdf: 1106.6298v1.pdf
source_sha256: 23b0754067873a04
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.976
doc_brief: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS — In 2006 Habiro initiated a construction of generating functions for Witten– Reshetikhin–Turaev (WRT) invariants known as uniﬁed WRT invariants."
---
The unification of the WRT invariants was initiated  in 2006 by Habiro.
For any  integral homology
3--sphere $M$,
Habiro \cite{Ha} constructed a {\em unified invariant} $J_M$
 whose evaluation  at any root of unity coincides with
the value of the  WRT
invariant at that root.
Habiro's unified invariant $J_M$ is an element of the following
ring (Habiro's ring)
\[
\Habiro:=\lim_{\overleftarrow{\hspace{2mm}k\hspace{2mm}}}
\frac{\Z[q]}{
((q;q)_k)},  \qquad \text{ where} \quad (q;q)_k = \prod_{j=1}^k (1-q^j).
\]
Every element $f(q)\in \Habiro$ can be written (non--uniquely) as an infinite sum
\[
f(q)= \sum_{k\ge 0} f_k(q)\, (1-q)(1-q^2)...(1-q^k),
\]
with $f_k(q)\in \Z[q]$. When $q=\xi$, a root of unity,
 only a finite number of terms on the right hand side are not zero,
hence  the evaluation
$\ev_\xi(f(q))$ is well--defined and is an algebraic integer.
However,  the fact that the unified invariant belongs to the Habiro ring
is stronger than just integrality of $\tau_M(\xi)$.





The Habiro ring has beautiful
arithmetic properties.
Every element $f(q) \in \Habiro$ can be considered
 as a function whose domain is the set
 of roots of unity.


Moreover, there is a natural Taylor series for $f$ at every root
of unity.
In \cite{Ha} it is shown that two elements $f,g \in \Habiro$ are the same if and
only if their Taylor series at a root of unity coincide.
In addition, each function $f(q) \in \Habiro$ is totally determined
by its values at, say,
infinitely many  roots of order $3^n,\, n\in \N$.
Due to these properties the Habiro ring is also called
a ring of ``analytic functions at roots of unity''. Thus belonging to $\Habiro$ means that the
collection of the  WRT invariants is far from a random
collection of algebraic integers; together they form a nice function.


General properties of the Habiro ring imply that for any integral homology
3--sphere $M$,
the Taylor expansion of the unified invariant $J_M$
at $q= 1$ coincides with the Ohtsuki series
and dominates WRT invariants of $M$ at all roots
of unity (not only of prime order). This is summarized in the following
commutative diagram.

\begin{diagram}
                &                   &\BC             &                                           &\\
                &\ruTo^{\tau_M(\xi)}&\uTo_{q=\xi}    &                                 &\\
\{\BZ\text{HS}\}&\rTo^{J_M(q)}      &\widehat{\BZ[q]}&\rInto                                     &\BZ[[1-q]] \\
                &\rdTo_{\text{LMO}} &                &                                           &\dInto_{h=1-q} \\
				&                   &\A              &\rTo^{\frak {sl}_2\text{--weight}}_{\text{system}} &\BQ[[h]]
\end{diagram}
By $\BZ\text{HS}$ we denoted here the set of integral homology 3--spheres.
In particular, this shows that Ohtsuki series has integral coefficients (which was conjectured by Lawrence and first proved by Rozansky).


Recently, Habiro ring found  applications in algebraic geometry
for  constructing
varieties over the non--existing field of one element \cite{Ma}.
