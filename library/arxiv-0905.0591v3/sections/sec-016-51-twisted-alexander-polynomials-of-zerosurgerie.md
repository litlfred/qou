---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-016-51-twisted-alexander-polynomials-of-zerosurgerie
section_title: "Twisted Alexander polynomials of zero–surgeries"
section_number: 5.1
pages: 13-14
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.944
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
\label{section:zerosurgery}

Given a knot $K\subset S^3$ the zero--framed surgery $N_K$ of $S^3$ along $K$ is defined to be
\[ N_K =S^3\setminus \nu K \cup_{T} S^1\times D^2\]
where $T=\partial (S^3\setminus \nu K)$ and $T$ is glued to $S^1\times D^2$ by gluing the meridian to $S^1\times \mbox{pt}$.
The inclusion map induces an isomorphism $\mathbb{Z}\cong H_1(S^3\setminus \nu K;\mathbb{Z})\xrightarrow{\cong} H_1(N_K;\mathbb{Z})$.
It is well--known that understanding the zero--framed surgery $N_K$
is the key to determining whether $K$ is slice or not
(cf. e.g. \cite{COT03}, \cite[Proposition~3.1]{FT05}, \cite[Proposition~2.1]{CFT09}).
We therefore prefer to formulate the sliceness obstructions in terms of the twisted Alexander polynomials of the zero--framed surgery.
The following lemma, together with Proposition \ref{prop:taudelta}, relates the twisted invariants of the zero--framed surgery with the twisted invariants of the knot complement.
We refer to \cite[Lemma~6.3]{KL99a} and \cite[Section~VII]{Tu02a} for very similar statements.


\begin{lemma}\label{lem:zerosurgery}
Let $K \subset S^3$ be a knot. Denote its meridian by $\mu$.
Let  $\alpha:\pi_1(N_K)\to \mbox{GL}(k,R[t^{\pm 1}])$ be a representation
such that $\det(\alpha(\mu)-\mbox{id})\ne 0$.
We denote the inclusion induced representation $\alpha:\pi_1(S^3\setminus \nu K)\to \pi_1(N_K)\to \mbox{GL}(k,R[t^{\pm 1}])$ by $\alpha$ as well.
Then
\[ \tau(S^3\setminus \nu K,\alpha)=\tau(N_K,\alpha) \cdot \det(\alpha(\mu)-\mbox{id}).\]
\end{lemma}

\begin{proof}
The proof of the lemma is standard and well--known. We therefore give just a quick summary.
Consider the decomposition $ N_K = S^3\setminus \nu K \cup_{T} S$ as above, where $S = S^1 \times D^2$.


Using the Mayer--Vietoris theorem for torsion we obtain that
\[ \tau(N_K,\alpha) =\frac{\tau(S^3\setminus \nu K,\alpha)\cdot \tau(S,\alpha)} { \tau( T,\alpha)}.\]
It is well--known that the torsion of the torus is trivial (c.f. e.g \cite{KL99a})
and that the torsion of $S$ is given by
\[ \tau(S,\alpha) = \frac{1}{ \det(\alpha(\mu)-\mbox{id})}.\]
The lemma now follows immediately.
\end{proof}
