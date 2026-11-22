---
doc_id: arxiv-2007.13108v1
doc_title: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube"
section_id: sec-001-11-a-lower-bound-on-the-entropy
section_title: "A lower bound on the entropy"
section_number: 1.1
pages: 3-3
source_pdf: 2007.13108v1.pdf
source_sha256: b298478f5f5b948d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.982
doc_brief: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube — It is well-known that measures whose density is the form e−V where V is a uniformly convex potential on Rn attain"
---
Our second result addresses the question of finding conditions under which the entropy of the measure $\nu$ is close to that of the corresponding product measure, having the same marginals as $\nu$. This result is inspired by a corresponding bound due to Anari, Oveis-Gharan and Vinzant \cite[Theorem 5.2]{AOV1}, see the discussion below.

Given a measure $\nu$ on $\DC$, we define,
$$
\mathcal{H}(\nu) := \int_{\DC} \log \frac{1}{\nu(\{y\})} d\nu(y),
$$
the entropy of $\nu$. Moreover, for all $i$ let $\pi_i(\nu)$ be the marginal of $\nu$ onto the $i$-th coordinate, and define
$$
\tilde {\mathcal{H}}(\nu) := \sum_{i \in [n]} \mathcal{H}(\pi_i(\nu)).
$$
A well-known fact is that $\mathcal{H}(\nu) \leq \tilde {\mathcal{H}}(\nu)$. We show that under a log-concavity-type condition, this inequality can be reversed. 
\begin{theorem} \label{thm:entropy}
Let $\nu$ be a probability measure on $\DC$. Suppose that, for some $\beta \geq 1$, $\nu$ satisfies the condition
\begin{equation}\label{eq:semilc2}
\nabla^2 \mathcal{L}[\nu](x) \preceq \beta \mathrm{diag}\left ( \nabla^2 \mathcal{L}[\nu](x) \right) , ~~ \forall x \in \RR^n.
\end{equation}
Then one has
$$
\tilde {\mathcal{H}}(\nu) \leq \beta \mathcal{H}(\nu).
$$
\end{theorem}
\begin{remark}
Condition \eqref{eq:semilc2} is stronger than condition \eqref{eq:semilc}. Indeed, it is not hard to check that $\mathrm{diag}\left ( \nabla^2 \mathcal{L}[\nu](x) \right) \preceq \Id$ (see formula \eqref{eq:momentgenerating} below).
\end{remark}
