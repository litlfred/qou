---
doc_id: arxiv-1403.4021v2
doc_title: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS"
section_id: sec-015-64-computations-inside-fn
section_title: "Computations inside Fn"
section_number: 6.4
pages: 32-32
source_pdf: 1403.4021v2.pdf
source_sha256: 046d02411e0dc086
toc_source: outline
text_source: latex
latex_prose_ratio: 0.844
latex_coverage_ratio: 0.587
doc_brief: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS — We classify the Markov traces factoring through the Birman-Wenzl-Murakami (BMW) algebras."
---
Following the arguments of Wenzl in \cite{WENZL} p. 400 we can derive additional useful relations
inside $F_n$.

\begin{lemma} \label{lemformulesFsee}Assume $|j-i| = 1$. Then we have
\begin{enumerate}
\item $s_j s_i e_j = e_i s_j s_i$
\item $s_i e_j e_i = a s_j^{-1} e_i + C$, $e_i e_j s_i = a e_i s_j^{-1} + C$
\item $e_i e_j e_i = e_i + \frac{2a}{x} C$
\item $e_i s_j s_i = a e_i e_j -C$
\end{enumerate}
\end{lemma}
\begin{proof}
By the braid relations, we have $s_j s_i s_j^{\alpha} = s_i^{\alpha} s_j s_i$ whenever $\alpha \in \{ -1,0,1 \}$.
Since $e_k = a ((s_k^{-1} + s_k)/x-1)$ we get (i).
Using the defining relations of $F_n$ and (i) we get
$s_i e_j e_i  = s_j^{-1} (s_j s_i e_j) e_i = s_j^{-1}  e_i s_j (s_i e_i) = a s_j^{-1}  (e_i s_j  e_i) = 
a s_j^{-1}  (C+e_i) = a s_j^{-1}  C+a s_j^{-1} e_i =   C+a s_j^{-1} e_i$ hence the first part of (ii). The
second part is similar. Now $e_i e_j e_i$ is equal to
$$a e_i \left( \frac{s_j + s_j^{-1}}{x}-1 \right) e_i
= a  \left( \frac{1}{x} e_is_je_i + \frac{1}{x} e_is_j^{-1}e_i-e_i^2 \right) 
= a  \left( \frac{1}{x} (e_i + C) + \frac{1}{x} (e_i + C)-\frac{\tilde{\delta}}{x} e_i \right) $$
hence $e_i e_j e_i = 
 a  \left( \frac{ax}{x}e_i + \frac{2}{x}C  \right) $ which proves (iii).
 In order to prove (iv), we use that, because of (iii),
 $e_i s_j s_i = (e_i e_j e_i - \frac{2a}{x} C) s_j s_i =
 e_i (e_j e_i s_j) s_i- \frac{2a}{x} Cs_j s_i =
 e_i (a e_j s_i^{-1} + C) s_i- \frac{2a}{x} C =
  a e_ie_j s_i^{-1}s_i + e_iCs_i - \frac{2a}{x} C =
  a e_ie_j  + \frac{\tilde{\delta}}{x} a C - \frac{2a}{x} C =
  a e_ie_j  + \frac{2-ax-2}{x} a C $ which proves (iv).
 
\end{proof}
