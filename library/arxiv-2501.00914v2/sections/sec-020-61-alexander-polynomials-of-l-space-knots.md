---
doc_id: arxiv-2501.00914v2
doc_title: "L-spaces and knot traces"
section_id: sec-020-61-alexander-polynomials-of-l-space-knots
section_title: "Alexander polynomials of L-space knots"
section_number: 6.1
pages: 28-30
source_pdf: 2501.00914v2.pdf
source_sha256: d94bd6edf8544d4a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.955
doc_brief: "L-spaces and knot traces — There has been a great deal of interest in understanding which knots are characterized by which of their Dehn surgeries."
---
We begin with a computation that follows from useful restrictions found by Krcatovich \cite{krcatovich} on the Alexander polynomials of L-space knots.

\begin{theorem}[{\cite[Theorem~1.6]{krcatovich}}] \label{thm:krcatovich}
If $K \subset S^3$ is an L-space knot of genus $g \geq 1$, then its Alexander polynomial has the form
\begin{equation} \label{eq:krcatovich-lspace}
\Delta_K(t) = (1-t^{-1})\sum_{i=0}^\infty t^{a_i},
\end{equation}
where $\{a_i\}$ is a strictly decreasing sequence with $a_0 = g$ and $a_i=-i$ for all $i \geq g$, and moreover
\[ a_i \leq g-2i \]
for $0 \leq i \leq g$.
\end{theorem}

It will be convenient for us to rewrite \eqref{eq:krcatovich-lspace} slightly, using 
\[ (1-t^{-1})\sum_{i=g}^\infty t^{a_i} = (1-t^{-1})\sum_{i=g}^\infty t^{-i} = t^{-g} \]
to say that
\begin{equation} \label{eq:krcatovich-finite}
\Delta_K(t) = (1-t^{-1}) \left(\sum_{i=0}^{g-1} t^{a_i}\right) + t^{-g}.
\end{equation}

\begin{lemma} \label{lem:other-alexander-restrictions}
Under the hypotheses of Theorem~\ref{thm:krcatovich}, we have $a_{g-1} = 2-g$, and if $g \geq 2$ then the remaining exponents
\[ a_1 > a_2 > \dots > a_{g-2} \]
contain exactly one element from each pair $\{g-2,3-g\},\ \{g-3,4-g\},\ \{g-4,5-g\},\ \dots,\ \{1,0\}$.
\end{lemma}

\begin{proof}
We use \eqref{eq:krcatovich-finite} to write
\begin{align*}
\Delta_K(t^{-1}) &= t^g + (1-t)\sum_{i=0}^{g-1} t^{-a_i} \\
&= \left( (1-t^{-1})(t^g + t^{g-1} + \dots + t^{1-g}) + t^{-g} \right) - (1-t^{-1})\sum_{i=0}^{g-1} t^{1-a_i} \\
&= (1-t^{-1})\left(\sum_{\substack{1-g \leq b \leq g \\ b \neq 1-a_i\ \forall i}} t^b\right) + t^{-g}.
\end{align*}
Since $\Delta_K(t) = \Delta_K(t^{-1})$, we conclude that the $g$-element sets
\[ \{a_0,\dots,a_{g-1}\} \quad\text{and}\quad \{1-a_0,\dots,1-a_{g-1}\} \]
are disjoint and thus partition the $2g$-element set $\{g,g-1,\dots,1-g\}$.  In other words, no two elements of $\{a_0,\dots,a_{1-g}\}$ can sum to $1$.

This last condition implies that $a_{g-1} \neq 1-a_0 = 1-g$, and we have $a_{g-1} > a_g = -g$, so in fact $a_{g-1} \geq 2-g$.  At the same time, Theorem~\ref{thm:krcatovich} says that $a_{g-1} \leq g-2(g-1) = 2-g$, so equality must hold.  Then the remaining $g-2$ exponents $a_1 > a_2 > \dots > a_{g-2}$ contain at most one element from each pair $\{g-2,3-g\}, \{g-3,4-g\}, \dots, \{1,0\}$, since otherwise two of them would sum to $1$, but there are exactly $g-2$ such pairs so each must contain one of the $a_i$ as claimed.
\end{proof}

We will eventually be interested in the Casson--Walker invariants \cite{walker} of Dehn surgeries on L-space knots, so the following lemma will allow us to compute them in terms of the coefficients $a_i$.

\begin{lemma} \label{lem:lspace-casson}
If $K \subset S^3$ is an L-space knot of genus $g \geq 1$, and we write $\Delta_K(t)$ in the form \eqref{eq:krcatovich-lspace}, then
\[ \frac{\Delta''_K(1)}{2} = \sum_{i=0}^{g-1} a_i + \frac{g(g-1)}{2}. \]
\end{lemma}

\begin{proof}
Differentiating \eqref{eq:krcatovich-finite} twice yields
\begin{multline*}
\Delta''_K(t) = (1-t^{-1})\left(\sum_{i=0}^{g-1} a_i(a_i-1)t^{a_i-2}\right) \\
+ 2t^{-2}\left(\sum_{i=0}^{g-1} a_it^{a_i-1}\right) - 2t^{-3}\left(\sum_{i=0}^{g-1} t^{a_i}\right) + g(g+1)t^{-g-2},
\end{multline*}
and then we set $t=1$ and divide by $2$ to get the desired expression.
\end{proof}

We can now prove that the Alexander polynomial of $T_{2,2g+1}$ is uniquely identified among all Alexander polynomials of genus-$g$ L-space knots by its second derivative at $t=1$.

\begin{proposition} \label{prop:casson-t2n}
Let $K \subset S^3$ be an L-space knot of genus $g \geq 1$.  Then its Alexander polynomial satisfies
\[ \frac{\Delta''_K(1)}{2} \leq \frac{g(g+1)}{2}, \]
with equality if and only if $\Delta_K(t) = \Delta_{T_{2,2g+1}}(t)$.
\end{proposition}

\begin{proof}
We combine Lemma~\ref{lem:lspace-casson} with Krcatovich's inequality $a_i \leq g - 2i$ for $0 \leq i \leq g$ from Theorem~\ref{thm:krcatovich} to write
\begin{align*}
\frac{\Delta''_K(1)}{2} &\leq \sum_{i=0}^{g-1} (g-2i) + \frac{g(g-1)}{2} \\
&= \left(g^2 - g(g-1)\right) + \frac{g(g-1)}{2} = \frac{g(g+1)}{2},
\end{align*}
where equality holds if and only if $a_i = g-2i$ for each $i=0,1,\dots,g-1$.  But this is the case precisely when
\begin{align*}
\Delta_K(t) &= (1-t^{-1})(t^g + t^{g-2} + t^{g-4} + \dots + t^{2-g}) + t^{-g} \\
&= t^g - t^{g-1} + t^{g-2} - t^{g-3} + t^{g-4} - \dots + t^{2-g} - t^{1-g} + t^{-g} \\
&= \Delta_{T_{2,2g+1}}(t),
\end{align*}
as claimed.
\end{proof}

\begin{remark}
There are other cases where knowing the value of $\frac{1}{2}\Delta''_K(1)$ for some L-space knot $K$ is enough to recover $\Delta_K(t)$, even though it does not work in general.  For example, using Lemmas~\ref{lem:other-alexander-restrictions} and \ref{lem:lspace-casson}, one can directly check that if $J$ and $K$ are L-space knots of the same genus $g \leq 5$ satisfying $\frac{1}{2}\Delta''_J(1) = \frac{1}{2}\Delta''_K(1)$, then $\Delta_J(t) = \Delta_K(t)$, since each possible choice of $a_1>\dots>a_{g-2}$ leads to a different value of $\sum_i a_i$.
\end{remark}

In the next subsection, we will classify the non-hyperbolic L-space knots whose Alexander polynomials achieve equality in Proposition~\ref{prop:casson-t2n}.  Such knots must be either torus knots or satellite knots \cite[Corollary~2.5]{thurston-kleinian}, so it will also be helpful to compute $\frac{1}{2}\Delta''_K(1)$ for satellite knots $K$ in terms of the pattern and companion knots.

\begin{lemma} \label{lem:casson-satellite}
Suppose that $K \subset S^3$ is a nontrivial satellite knot, and $K = P(C)$ where $P \subset S^1\times D^2$ is the pattern and $C \subset S^3$ the companion.  Then
\[ \Delta''_K(1) = \Delta''_{P(U)}(1) + w^2\Delta''_C(1). \]
\end{lemma}

\begin{proof}
Let $w \geq 0$ be the winding number of $K$.  We differentiate the relation
\[ \Delta_K(t) = \Delta_{P(U)}(t) \cdot \Delta_C(t^w) \]
twice to get
\begin{multline*}
\Delta''_K(t) = \Delta''_{P(U)}(t)\Delta_C(t^w) + 2\Delta'_{P(U)}(t) \cdot wt^{w-1}\Delta'_C(t^w) \\
+ \Delta_{P(U)}(t)\left( w(w-1)t^{w-2}\Delta'_C(t^w) + w^2t^{2w-2}\Delta''_C(t^w) \right).
\end{multline*}
The desired relation follows from setting $t=1$ and noting that $\Delta_{P(U)}(1) = \Delta_C(1) = 1$ while $\Delta'_{P(U)}(1) = \Delta'_C(1) = 0$.
\end{proof}
