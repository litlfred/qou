---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-030-81-a-partial-order-on-knots
section_title: "A Partial order on knots"
section_number: 8.1
pages: 26-26
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 1.0
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
\label{section:po}

Given a knot $K$ we write $\pi_1(S^3\sm \nu K)\mathrel{\mathop:}=\pi_1(S^3\setminus K)$.
 For two prime
knots $K_1$ and $K_2$ one defines $K_1 \geq K_2$ if there exists a surjective group homomorphism
$\varphi:\pi_1(K_1)\to \pi_1(K_2)$.
The relation $``\geq"$ defines a partial order on the set of prime knots (cf. \cite{KS05a}). Its study is often related to a well--known conjecture of J. Simon, that posits that for a given $K_1$, the set of knots $K_2$ s.t. $K_1 \geq K_2$ is finite.

Kitano, Suzuki and Wada \cite{KSW05} prove the following theorem
which generalizes a result of Murasugi \cite{Mu03}.

\begin{theorem}\label{thm:epi}
Let $K_1$ and $K_2$ be two knots in $S^3$ and let $\varphi:\pi_1(K_1)\to \pi_1(K_2)$ an epimorphism.
Let $\gamma:\pi_1(K_2)\to \mbox{GL}(k,R)$ a representation with $R$ a Noetherian UFD. Then
\[ \frac{\tau(K_1,\gamma\circ \varphi)}{\tau(K_2,\gamma )} \]
is an element in $R[t^{\pm 1}]$.
\end{theorem}

This theorem plays a crucial role in determining the partial order on the set of knots with up to eleven crossings.
We refer to \cite{KS05a}, \cite{KS05b}, \cite{KS08} and \cite{HKMS09} for details.
