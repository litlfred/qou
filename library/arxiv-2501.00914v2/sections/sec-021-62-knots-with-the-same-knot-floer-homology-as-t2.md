---
doc_id: arxiv-2501.00914v2
doc_title: "L-spaces and knot traces"
section_id: sec-021-62-knots-with-the-same-knot-floer-homology-as-t2
section_title: "Knots with the same knot Floer homology as T2,2g+1"
section_number: 6.2
pages: 30-31
source_pdf: 2501.00914v2.pdf
source_sha256: d94bd6edf8544d4a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.988
doc_brief: "L-spaces and knot traces — There has been a great deal of interest in understanding which knots are characterized by which of their Dehn surgeries."
---
We know that $\hfkhat(K)$ detects the trefoil $T_{2,3}$ \cite{ghiggini} and the cinquefoil $T_{2,5}$ \cite{frw-cinquefoil}, but not whether it detects other knots $T_{2,2g+1}$ with $g \geq 3$.  However, we can combine Proposition~\ref{prop:casson-t2n} with work of Baker--Motegi \cite{baker-motegi-twist} on L-space satellites to show that any other knot whose knot Floer homology agrees with that of $T_{2,2g+1}$ must be hyperbolic.

\begin{proposition} \label{prop:satellite-t2n}
Let $K$ be an L-space knot of genus $g \geq 1$, and suppose that $\Delta_K(t) = \Delta_{T_{2,2g+1}}(t)$.  Then $K$ is not a satellite knot.
\end{proposition}

\begin{proof}
Suppose that $K$ is a satellite knot, say $K=P(C)$ where $P \subset S^1\times D^2$ is the pattern and $C \subset S^3$ the companion.  Since $K$ is an L-space knot, the pattern $P$ is braided by \cite[Theorem~1.17]{baker-motegi-twist}, so since $P$ is a nontrivial satellite pattern it must have winding number $w \geq 2$.

Since $K$ is a satellite L-space knot, we appeal to \cite[Theorem~1.15]{hrw} to see that $P(U)$ and $C$ are both L-space knots as well.  Writing $h=g(P(U))$ and $k = g(C) \geq 1$, so that $g = h+wk$, we apply Proposition~\ref{prop:casson-t2n} and Lemma~\ref{lem:casson-satellite} to get
\begin{align*}
g(g+1) = \Delta''_K(1) &= \Delta''_{P(U)}(1) + w^2 \Delta''_C(1) \\
&\leq h(h+1) + w^2k(k+1) \\
&= (h^2 + (wk)^2) + (h+w^2k) \\
&= (h+wk)^2 + (h+wk) + (w^2k - 2hwk - wk) \\
&= g^2+g + wk(w-(2h+1))
\end{align*}
which can only be true if $w \geq 2h+1$.

If we had a strict inequality $w > 2h+1$, then the first few terms of $\Delta_K(t)$ would have the form
\begin{align*}
\Delta_K(t) = \Delta_{P(U)}(t) \cdot \Delta_C(t^w) &= (t^h - \dots + t^{-h}) (t^{wk} + O(t^{w(k-1)})) \\
&= (t^h - \dots + t^{-h})t^{wk} + O(t^{wk-w+h}) \\
&= t^{wk+h} - \dots + t^{wk-h} + O(t^{wk-w+h}).
\end{align*}
But $w > 2h+1$ is equivalent to $wk-w+h < wk-h-1$, so then the $t^{wk-h-1}$-coefficient of $\Delta_K(t)$ is zero.  Since $\Delta_K(t)$ has nonzero terms of strictly lower degree -- the lowest-degree term is $t^{-g} = t^{-wk-h}$ -- this contradicts our assumption that $\Delta_K(t)$ is equal to $\Delta_{T_{2,2g+1}}(t)$, all of whose $t^i$-coefficients for $-g \leq i \leq g$ are nonzero.  We must therefore have $w=2h+1$.  (Note that since $w \geq 2$, this means in particular that $h \geq 1$.)

Finally, Baker--Motegi \cite[Theorem~7.3]{baker-motegi-twist} proved that since $K$ is a satellite L-space knot, it satisfies
\[ w(2k-1) < \frac{2h-1 + w}{w-1}. \]
Using $w=2h+1$, this inequality simplifies to
\[ (2h+1)(2k-1) < \frac{4h}{2h} = 2. \]
Since the left side is at least $3\cdot 1 = 3$, we have a contradiction.
\end{proof}
