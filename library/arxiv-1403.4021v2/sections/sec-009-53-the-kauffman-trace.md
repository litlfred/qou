---
doc_id: arxiv-1403.4021v2
doc_title: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS"
section_id: sec-009-53-the-kauffman-trace
section_title: "The Kauffman trace"
section_number: 5.3
pages: 22-23
source_pdf: 1403.4021v2.pdf
source_sha256: 046d02411e0dc086
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.989
doc_brief: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS — We classify the Markov traces factoring through the Birman-Wenzl-Murakami (BMW) algebras."
---
Recall that we defined in \S \ref{secttwobmwagebras} two Markov traces $t_n^{\pm} : BMW_n^{\pm} \to S_{\pm}$. Using the Chinese
Remainder Theorem isomorphism $\overline{S} \simeq S_+ \oplus S_-$ they
can be patched together into a Markov trace $\overline{BMW}_n \otimes_{\overline{R}}  \overline{S} \to
\overline{S}$, which extends to a Markov trace $t_n^K : \WBMW_n \to \overline{S}$.


$$
\xymatrix{
  &\overline{BMW}_n\otimes_{\overline{R}}S_+ \ar[r]&  BMW_n^+ \ar[r]^{t_n^+} & S_+ \ar[dr] & \\
 \overline{BMW}_n\otimes_{\overline{R}} \overline{S} \ar[ur] \ar[dr] \ar@{.>}[rrrr]^{t_n^K}& & & & \overline{S} \\
  & \overline{BMW}_n\otimes_{\overline{R}}S_- \ar[r]& BMW_n^- \ar[r]_{t_n^-} & S_- \ar[ur] & \\
}
$$

Note that the value of $t_3^K((s_1 s_2^{-1})^2)$ define before indeed matches
this new definition, because of the
computation of the Kauffman invariant of the figure-eight knot we did in section \ref{secttwobmwagebras}.

\begin{prop} Let $t'_n$ be the composite of $t_n$ with $M \to M \otimes_R \overline{S}[ (a^2-y)^{-1}]$.
 Then $(t'_n)$ is a linear combination of the composites of $t_n^H$ and $t_n^K$ with some morphism $\overline{S} \to M \otimes_R \overline{S}[ (a^2-y)^{-1}]$.
\end{prop}
\begin{proof}
By proposition \ref{prop:unicitetracegen} we know that $t'_n$ is uniquely determined by $t'_1(1) = t'_3(s_1s_2)$ and $t'_2(1) = t'_3(s_1)$. It is thus
sufficient to show that $t_3^H$ and $t_3^K$ induce a basis of $( \overline{S}[ (a^2-y)^{-1}])^2$ under $t'_3 \mapsto (t'_3(s_1s_2),t'_3(s_1))$.
The corresponding $2 \times 2$ matrix has for determinant
$$
\left| \begin{array}{cc} \delta_H & 1 \\ \delta_K & 1 \end{array} \right| = \delta_H - \delta_K = \frac{a}{y} \in ( \overline{S}[ (a^2-y)^{-1}])^{\times}
$$
with $\delta_H = \frac{y+1}{x}$, and this concludes the proof.
\end{proof}


\begin{remark} It is well-known that both the Kauffman polynomial and
the HOMFLYPT polynomial both specialize to the Jones polynomial
(see e.g. \cite{LICKO} p. 180). It could have been expected that this coincidence would have appeared in the previous proposition.
It clearly does not, since any specialized value of the invariants defined by our
traces $t_n^H$ and $t_n^K$
cannot coincide on the 2-components unlink (we always have $\delta_H \neq \delta_K$).
What happens is that, according to \cite{LICKO} proposition 16.6, the trace $t_n^K$ provides the Jones
polynomial when specialized to $\alpha = -t^{\frac{-3}{4}}$, $q = t^{\frac{1}{4}}$, that
is $a = q^{-6}$, $b = -q^{-2} = -t^{\frac{-1}{2}}$, $c = -q^{-4} = -t^{-1}$ while, according to \cite{LICKO} proposition 16.5, $t_n^H$
provides the Jones polynomial when $\{b,c \}$ is specialized to $\{ - t^{\frac{1}{2}}, t^{\frac{3}{2}} \}$, and the
only value of $t$ for which these two parametrizations coincide is $t^{\frac{1}{2}} = -1$, in which
case we get $b+c = 0$, which is forbidden here.
\end{remark}
