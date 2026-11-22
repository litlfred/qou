---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-019-81-an-improved-circuit-diameter-bound
section_title: "An improved circuit diameter bound"
section_number: 8.1
pages: 29-29
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.985
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance measures associated with linear spaces."
---
In a recent paper Dadush et al. \cite{dadush2021circuit} gave the following bound on the circuit diameter:

\begin{theorem}[\cite{dadush2021circuit}]\label{thm:diam-augment} An LP of the form \ref{LP-augment} has circuit diameter bound
$O(m^2 \log(m + \kappa_A) + n \log n)$.
\end{theorem}

Let us highlight the main ideas to prove Theorem~\ref{thm:diam-augment}. The argument is constructive but non algorithmic in the sense that the augmentation steps are defined using the optimal solution.
We first show the bound in Theorem~\ref{thm:diam-augment} for \ref{LP_primal_dual} (i.e., without upper bounds $u$) and then extend the argument to systems of form \ref{LP-augment}. Let $x^*$ be a basic optimal solution to \ref{LP_primal_dual} corresponding to basis $B$, and let $N = [n]\setminus B$. Thus, $x^*$ is the unique optimal solution with respect to the cost vector $c=(0_B,\1_N)$.

For the current iterate $x^{(t)}$, consider a conformal circuit decomposition $h^1, \ldots, h^k$ of $x^* - x^{(t)}$, and select a circuit $h^i, i \in [k]$ such that $\|h_N^i\|_1$ is maximized.
We find the next iterate $x^{(t+1)}=x^{(t)}+\alpha h^i$ for the maximal stepsize $\alpha>0$.
 Note that the existence of such a decomposition \emph{does not} yield a circuit diameter bound $n$ due to the maximality requirement in the definition of circuit walks. 
Nonetheless, it can be shown that we will not overshoot $h^i$ by too much. More precisely, one can show that the step length will be $\alpha\in [1,n]$. Further, the choice of $h^i$ guarantees that $\|x^{(t)}_N\|_1$ decreases geometrically.

The analysis focuses on the index sets $L_t=\{i\in [n]:\, x^*_i>n\kappa_A\|x^{(t)}_N\|_1\}$ and $R_t=\{i\in [n]:\, x^{(t)}_i\le nx^*_i\}$. For every $i\in L_t$, $x_i$ must already be `large' and cannot be set to zero later in the algorithm; $R_t$ is the set of indices that have essentially `converged' to the final value $x^*_i$. Since $\|x^{(t)}_N\|_1$ is decreasing, once an index enters $L_t$, it can never leave again. The same property can be shown for $R_t$. Moreover, a new index is added to either set $R_t$ or $L_t$ every $O(m\log(m+\kappa_A))$ iterations, leading to the
 overall bound $O(m^2 \log(m + \kappa_A))$. 

For a system \ref{LP-augment} with upper bounds $u$, the above argument yields a bound $O(n^2\log(n + \kappa))$ using a simple reduction. To achieve a better bound, \cite{dadush2021circuit} gives a preprocessing sequence of $O(n \log n)$  circuit augmentations that reduces the number of variables to $\le 2m$.
This preprocessing terminates once the set of columns in $A_D$ are linearly independent for $D=\{i \in [n] : x_i^* \neq x_i \text{ and } x_i^* \in \{0, u_i\} \}$. Since a basic solution $x^*$ may have $\le m$ entries not equal to the lower or upper bound, at this point there are $\le 2m$ variables $x_i\neq x_i^*$. This leads to a circuit diameter bound of $O(m^2 \log(m + \kappa_A) + n \log n)$.
