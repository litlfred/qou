---
doc_id: arxiv-1308.2499v1
doc_title: "Towards a regularity theory for integral Menger curvature"
section_id: sec-005-a-product-and-chain-rule
section_title: "A Product and chain rule"
section_number: null
pages: 26-27
source_pdf: 1308.2499v1.pdf
source_sha256: 3b20abdc0e1b0ba9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.892
latex_coverage_ratio: 1.0
doc_brief: "Towards a regularity theory for integral Menger curvature — We generalize the notion of integral Menger curvature introduced by Gonzalez and Maddocks [14] by decoupling the powers in the integrand."
---
\label{sect:fractional}

As in~\cite{blatt-reiter2}, we make use of the following results which
we briefly state for the readers' convenience.

\begin{lemma}[Product rule]\label{lem:product}
  Let $q_1,\dots,q_{k} \in (1,\infty)$ with $\sum_{i=1}^{k}\frac1{q_{k}}=\frac1r\in(1,\infty)$ and 
  $s > 0$.
  Then, for $f_{i}\in\W[s,q_{i}]\rzd$, $i=1,\dots,k$,
 \begin{equation*}
  \norm{\prod_{i=1}^{k} f_{i}}_{\W[s,r]} \leq C_{k,s} \prod_{i=1}^{k}\norm{f_{i}}_{\W[s,q_{i}]}.
 \end{equation*}
\end{lemma}

We also refer to Runst and Sickel~{\cite[Lem.~5.3.7/1~(i)]{RS}}. ---
For the following statement, one mainly has to treat $\norm{(D^k\psi)\circ f}_{\W[\s,p]}$ for $k\in\N\cup\set0$ and $\s\in(0,1)$
which is e.g.\@ covered by~\cite[Thm.~5.3.6/1~(i)]{RS}.

\begin{lemma}[Chain rule]\label{lem:chain}
 Let $f\in\W[s,p](\mathbb R / \mathbb Z, \mathbb R^n)$, $s > 0$, $p \in (1,\infty)$.
 If $\psi\in C^\infty(\R)$ is globally Lipschitz continuous and $\psi$ and all its derivatives vanish at~$0$ then $\psi\circ f\in\W[s,p]$ and
 \[ \|\psi \circ f\|_{\W[s,p]} \le C\|\psi\|_{C^{\scriptstyle k}}\|f\|_{\W[s,p]} \]
 where $k$ is the smallest integer greater than or equal to $s$.
\end{lemma}
