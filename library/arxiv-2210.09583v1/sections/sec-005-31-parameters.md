---
doc_id: arxiv-2210.09583v1
doc_title: "A NEW PRESENTATION OF THE osp(1|2)-POLYNOMIAL LINK INVARIANT"
section_id: sec-005-31-parameters
section_title: "Parameters"
section_number: 3.1
pages: 6-7
source_pdf: 2210.09583v1.pdf
source_sha256: 38fc6fa465a06a7b
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.881
doc_brief: "A NEW PRESENTATION OF THE osp(1|2)-POLYNOMIAL LINK INVARIANT — There is a known connection between the osp(1|2n) polynomial knot invariant Jn K and the so(2n + 1) knot invariant soJn K studied by"
---
\label{sec:3.1}

\begin{notation}
  We borrow much of our notation in this section from \cite{C}. Given an element $m$ in some $\Z\times \Z_2$-graded module $M$, we denote $p(m)$ to be the parity of $m$, $|m|$ denotes the $\Z$-degree of $m$ and $||m||=(|m|,p(m))$.
\end{notation}

Let us review some notions from \cite[Section 2.2]{C}.

Let $t\in \C$ such that $t^2=-1$. Let $q$ be a formal parameter, let $\tau$ be a formal parameter such that $\tau^4=1$, and define $\pi:=\tau^2$.
Recall the notation $R^\pi=R[\pi]/(\pi^2-1)$ and $R^\tau = R[\tau]/(\tau^4-1)$ for a commutative ring $R$ with 1.
Our base ring is $\Q(q,t)^\tau$.

For $x\in \{\pm 1, \pm t\}$, let $\Q(q,t)_x:=\Q(q,t)$ viewed as a $\Q(q,t)^\tau$-module where $\tau$ acts by multiplication by $x$.
\begin{definition}
  The specialization of $\Q(q,t)^\tau$-module $M$ at $x$ is the $\Q(q,t)$-module \[M|_{\tau=x}=\Q(q,t)_x\otimes_{\Q(q,t)^\tau}M\]
\end{definition}

$\Q(q,t)^\tau$ has orthogonal idempotents
\begin{align*}
  \varepsilon_{t^k}&=\frac{1+(t^k\tau)+(t^k\tau)^2+(t^k\tau)^3}{4} & 0\leq k\leq 3,
\end{align*}
such that $\Q(q,t)^\tau=\bigoplus_{k\in \Z_4}Q(q,t)\varepsilon_{t^k}$.

Furthermore, since $\tau \varepsilon_x=x\varepsilon_x$, we see that
\[
M|_{\tau=x}=\varepsilon_x M.
\]
