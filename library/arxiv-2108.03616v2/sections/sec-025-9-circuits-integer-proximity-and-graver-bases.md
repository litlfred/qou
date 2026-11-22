---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-025-9-circuits-integer-proximity-and-graver-bases
section_title: "Circuits, integer proximity, and Graver bases"
section_number: 9
pages: 36-37
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.975
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance measures associated with linear spaces."
---
\label{sec:graver}
We now briefly discuss implications of circuit imbalances to the integer program (IP) of the form
\begin{equation}
\label{eq:IP} \tag{IP}
\begin{aligned}
\min \; &\pr{c}{x} \quad \\
Ax& =b \\
x &\geq 0, \\
x &\in \Z^n.
\end{aligned}
\end{equation}

Many algorithms for \eqref{eq:IP} solve the LP-relaxation first and deduce from the optimal solution of the relaxation information about the IP itself. The following proximity lemma shows that in case that \eqref{eq:IP} is feasible, the distance of an optimal integral solution to the optimal solution of the relaxation can be bounded in terms of max-circuit imbalance $\bar\kappa_A$. So, a local search within a radius of this guaranteed proximity will provide the optimal solution for the IP; see \cite[Proposition 4.1]{Lee89}.
\begin{lemma}\label{opt:IP}
Let $x^*$ be an optimal solution to \ref{LP_primal_dual}. Then there exists an optimal solution $\hat x$ to \eqref{eq:IP} such that $\|\hat x - x\|_1 \le n \bar\kappa_W$.
\end{lemma}
\begin{proof}
  Let $\hat x$ be an optimal solution to \eqref{eq:IP} that minimizes $\|\hat x - x^*\|_1$ and consider $w = x^* - \hat x \in W$ and a conformal circuit decomposition $w = \sum_{i = 1}^k \lambda_i g^{C_i}$ for some $k \le n$ and circuits $C_1, \ldots, C_k$ and $\lambda_1, \ldots, \lambda_k \ge 0$. Then, $\pr{c}{g^{C_i}} \le 0$ for all $i \in [k]$ as otherwise $x^* - \lambda_i g^{C_i}$ would be a feasible solution to the primal of \ref{LP_primal_dual} with strictly better objective than $x^*$. Further, note that $\lambda_i \le 1$ for all $i \in [k]$ as otherwise $\hat x - g^{C_i}$ is a feasible solution to \eqref{eq:IP} that has an objective as least as good as $\hat x$ and would in $\ell_1$ norm be strictly closer to $x^*$ than $\hat x$.   
  Therefore, 
  \[\|\hat x - x^*\|_\infty \leq \sum_{i = 1}^k \|g^{C_i}\|_\infty \le n\bar \kappa_W. \]
\end{proof}
Another popular and well-studied quantity in integer programming is the \emph{Graver basis}, defined as follows.
\begin{Def}[Graver basis]
The \emph{Graver basis} of a matrix $A$, denoted by $\mathcal{G}(A)$, consists of all $g \in \ker(A) \cap \Z^n$ such that there exists no $h \in (\ker(A) \cap \Z^n)\setminus \set{g}$ such that $g$ and $h$ are conformal and $|h_i| \le |g_i|$ for all $i \in [n]$. 
We can further define  
\begin{equation}
  \mathfrak g_1(A) := \max_{v \in \mathcal{G}(A)} \|v\|_1, \qquad
  \mathfrak g_\infty(A) := \max_{v \in \mathcal{G}(A)} \|v\|_\infty.
\end{equation}
\end{Def}
See \cite{bookDeLoera} for extensive treatment of the Graver basis and \cite{eisenbrand2019algorithmic} for more recent developments.  
Clearly, elementary vectors, scaled such that its entries have greatest common divisor equal to one belong to the Graver basis: $\set{g \in \EE(W) \cap \Z^n: \gcd(g) = 1} \subseteq \mathcal{G}(A)$. 

We will furthermore see how the max-circuit imbalance measure and Graver basis are related.

\begin{lemma} $\bar \kappa_A \le \mathfrak g_\infty(A) \le n\bar\kappa_A$.
\end{lemma}
\begin{proof}
The first inequality follows from the paragraph above, noting that 
  $$\set{g^C : C\in \circuits(W)} \subseteq \mathcal{G}(A),$$
for the normalized elementary vectors $g^C$ with $\lcm(g^C)=1$.
  For the second inequality, let $g \in \mathcal{G}(A)$ and $g = \sum_{i = 1}^k{\lambda_i g^{C_i}}$ be  a conformal circuit decomposition where $k \le n $. Note that $\lambda_i < 1$ for all $i \in [k]$ as otherwise $h^i$ would contradict that $g \in \mathcal{G}(A)$. Therefore, 
  \begin{equation}
    \|g\|_\infty \le \sum_{i = 1}^k \lambda_i \|g^{C_i}\|_\infty \le n \bar \kappa_A. 
  \end{equation} 
\end{proof}

Using the Steinitz lemma, Eisenbrand and Weismantel  \cite[Lemma 2]{eisenbrand2018blockstructure} gave a bound on $\mathfrak g_1(A)$ that only depends on $m$ but is independent of $n$:

\begin{theorem}
  Let $A \in \Z^{m \times n}$. Then $\mathfrak g_1(A) \le (2 m \|A\|_{\max} + 1)^m$.
\end{theorem}
