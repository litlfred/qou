---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-014-34-the-trace-and-categories-of-complexes
section_title: "The trace and categories of complexes"
section_number: 3.4
pages: 16-17
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.971
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a higher categorical level."
---
The trace of a linear category $\C$ gives rise to an interesting variant of Euler characteristic.
Let $\Kom(\C)$ be the category of bounded complexes over $\C$. Recall that the objects of $\Kom(\C)$ are complexes
$$
A_{\bullet}:\quad \quad \dots\longrightarrow A_i \xto{d_i} A_{i-1} \xto{d_{i-1}} \dots \xto{d_2} A_1 \xto{d_1} A_0 \longrightarrow 0,
$$
where $A_i  \in \Ob(\C)$ and
$d_i\in \C(A_i, A_{i-1})$, and the morphisms are chain maps.


The ``traced'' Euler characteristic of a complex $A_{\bullet}$ is
defined by
\[
\chi_{\tr}(A_{\bullet})=\sum_i (-1)^i [1_{A_i}]  \in \Tr(\C),
\]
where $[1_x]$ is the class of $1_x$ in $\Tr(\C)$ for any $x\in \Ob(\C)$.
More generally, to any chain endomorphism $F:A_{\bullet}\to A_{\bullet}$ we can associate its
``traced''  Lefschetz number
$$ \tau(F)=\sum_i (-1)^i [F_i]\, .$$ Then $\chi_{tr} (A_{\bullet})=\tau (1_{A_{\bullet}})$.

\begin{lem}  For any $A_{\bullet} \in \Kom(\C)$ and homotopic chain endomorphisms $F, G: A_{\bullet}\to A_{\bullet}$
we have $\tau(F)=\tau(G)$. Furthermore,
$\chi_{\tr}$ is  homotopy invariant.
\end{lem}

\begin{exercise}
Prove this lemma using the definition of the chain homotopy, i.e.
$F-G=dh+hd$.
\end{exercise}
\nc\Cob{{\rm Cob}}


An interesting application of the traced Euler characteristic was given
 by Bar-Natan~\cite{Dror}. There he defined a quotient $\Cob_/$ of the $\Z[1/2]$-linear category of 2-dimensional cobordisms,
and associated a complex in $\Kom(\Cob^{\oplus}_/)$ to any tangle, which he called a Khovanov bracket. He showed that isotopies of the tangle do not change the homotopy type of this complex.  The following theorem of Bar-Natan shows that the traced Euler characteristic can be used as decategorification map in a categorification of the Jones polynomial.



\begin{thm}[Theorem 6 \cite{Dror}]    \label{Dror}
The traced Euler characteristic of the Khovanov bracket
of a tangle in Bar-Natan's category  is equal to the Jones
polynomial.
\end{thm}
