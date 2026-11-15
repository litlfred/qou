---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-046-101-a-bound-on-cumulants
section_title: "A bound on cumulants"
section_number: 10.1
pages: 81-83
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.955
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
\subsubsection{Subgraph count statistics}
In the following we denote $\arr(n,k)$ the set of \emph{arrangements} in $[n]$ of length $k$, \emph{i.e.}, lists of $k$ distinct elements in $[n]$. 
The cardinality of $\arr(n,k)$ is  the falling factorial 
$n\fall{k}=n(n-1) \cdots (n-k+1)$.
Let $A=(a_1,\dots,a_k)$ be an arrangement in $[n]$ of length $k$, and $\gamma$ be a fixed graph with vertex set $[k]$. Recall that $\Gamma=\Gamma(n,p_{n})$ is a random Erd\"os-R\'enyi graph on $[n]$. We denote $\delta_\gamma(A)$ the following random variable:
\begin{equation}\delta_\gamma(A) = \begin{cases}
     1 & \text{ if }\gamma \subseteq \Gamma[a_1,\dots,a_k];\\
     0 & \text{ else.}
\end{cases}\label{eq:deltadef}
\end{equation}
Here $\Gamma[a_1,\dots,a_k]$ denotes the graph induced by $\Gamma$ on vertex set $\{a_1,\dots,a_k\}$.
As our data is an {\em ordered} list $(a_1,\dots,a_k)$, this graph can canonically be seen as a graph on vertex set $[k]$, that is the same vertex set as $\gamma$. Then the inclusion should be understood as inclusion of edge sets.\medskip

\noindent For any graph $\gamma$ with $k$ vertices
and any integer $n \ge 1$, we then define the random variable $\SubGraph_{\gamma}$ by
$$\SubGraph_{\gamma} = \sum_{A \in \arr(n,k)} \delta_\gamma(A).$$

\begin{remark}
It would also be natural to replace in Definition \eqref{eq:deltadef} the inclusion by an equality $\gamma = \Gamma[a_1,\dots,a_k]$. This would lead to other random variables $Y_\gamma^{(n)}$, called {\em induced} subgraph count statistics. Their asymptotic behavior is harder to study (in particular, fluctuations are not always Gaussian; see \cite[Theorem 6.52]{JLR00}). Notice that if $\gamma$ is a complete graph, then both definitions coincide.
\end{remark}\medskip



\subsubsection{A dependency graph of the subgraph count statistics}
Fix some graph $\gamma$ with vertex set $[k]$. By definition, the variable we are interested in writes as a sum
$$\SubGraph_{\gamma} = \sum_{A \in \arr(n,k)} \delta_\gamma(A).$$
We shall describe a dependency graph for the variables $\{\delta_\gamma(A)\}_{A \in \arr(n,k)}$.\bigskip

For each pair $e=\{v,v'\} \subset [n]$, denote $I_e$ the indicator function of the event: {\em $e$ is in the graph $\Gamma(n,p)$}. By definition of the model $\Gamma(n,p)$, the random variables $I_e$ are independent Bernouilli variables of parameter $p$. Then, for an arrangement $A$, denote $E(A)$ the set of pairs $\{v,v'\}$ where $v$ and $v'$ appear in the arrangement $A$. One has
\[\delta_\gamma(A) = \prod_{e \in E'(A)} I_e, \]
where $E'(A)$ is a subset of $E(A)$ determined by the graph $\gamma$. In particular, if, for two arrangements $A$ and $A'$, one has $|E(A) \cap E(A')| =\emptyset$ (equivalently, $|A \cap A'| \le 1$), then the variables $\delta_\gamma(A)$ and $\delta_\gamma(A')$ are defined using different variables $I_e$ (and, hence, are independent). This implies that the following graph denoted $\B$ is a dependency graph for the family of variables $\{\delta_\gamma(A)\}_{A \in \arr(n,k)}$:\vspace{2mm}
\begin{itemize}
    \item its vertex set is $\arr(n,k)$;\vspace{2mm}
    \item there is an edge between $A$ and $A'$ if  $|A \cap A'| \ge 2$.\vspace{2mm}
\end{itemize}
Considering this dependency graph is quite classical --- see, {\em e.g.}, \cite[Example 1.6]{JLR00}.\bigskip

All variables in this graph are Bernoulli variables and, hence, bounded by $1$. Besides the graph $\B$ has $N=n\fall{ k}$ vertices, and is regular of degree $D$ smaller than 
$$\binom{k}{2}^2  \,2\,  (n-2)(n-3)\cdots(n-k+1) < k^4 \,n^{k-2}.$$ 
Indeed, a neighbour $A'$ of a fixed arrangement $A \in \arr(n,k)$ is given as follows:\vspace{2mm}
\begin{itemize}
    \item choose a pair $\{a_i,a_j\}$ in $A$ that will appear in $A'$;\vspace{2mm}
    \item choose indices $i'$ and $j'$ such that $a'_{i'}=a_i$ and $a'_{j'}=a_j$
        (these indices are different but their order matters);\vspace{2mm}
    \item choose the other values in the arrangement $A'$.\vspace{2mm}
\end{itemize}
So, we may apply Theorem \ref{thm:dependencygraphsrefined} and we get:
\begin{proposition} \label{prop:boundcumulantsubgraph}
Fix a graph $\gamma$ of vertex set $[k]$. For any $r\le 1$, one has
$$ \big| \kappa^{(r)}(\SubGraph_\gamma) \big| \le 2^{r-1} r^{r-2}\,  n^k\, (k^4 \,n^{k-2})^{r-1}. $$
\end{proposition}
\bigskip
