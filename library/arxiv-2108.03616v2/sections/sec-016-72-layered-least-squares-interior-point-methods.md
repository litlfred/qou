---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-016-72-layered-least-squares-interior-point-methods
section_title: "Layered least squares interior point methods"
section_number: 7.2
pages: 26-28
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.994
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance measures associated with linear spaces."
---
\label{sec:LLS}

In this section, we briefly review layered least squares (LLS) interior-point methods, and highlight the role of the circuit imbalance measure $\Le_W$ in this context.
The \emph{central path} for the standard log-barrier function is the  parametrized curve given by the solutions to the system following system for $\mu\in \R_{++}$
\begin{equation}
  \label{sys:central_path}
  \begin{aligned}
  Ax &= b \\
  A^\top y + s & = c\\
  x_is_i &= \mu \;\quad \forall i \in [n]\\
  x, s &>0
  \end{aligned}
\end{equation}
 A unique solution for each $\mu>0$ exist whenever \ref{LP_primal_dual} possesses strictly feasible primal and dual solutions, i.e.\ primal resp.~dual solutions with $x > 0$ resp.~$s > 0$; the duality gap between these solutions is $n\mu$. The limit point at $\mu\to 0$ gives a pair of primal and dual optimal solutions.
At a high level,  interior point methods require an initial solution close to the central path for some large $\mu$ and proceed by following the central path in some proximity towards smaller and smaller $\mu$, which corresponds to converging to an optimal solution. A standard variant is the Mizuno--Todd--Ye \cite{MTY} \emph{predictor-corrector} method. This alternates between \emph{predictor} and \emph{corrector} steps. Each predictor step decreases the parameter $\mu$ at least by a factor $(1-\beta/\sqrt{n})$, but moves further away from the central path. Corrector steps maintain the same $\mu$ but restore better centrality. 

Let us now focus on the predictor step at a given point $(x,s)$; we use the subspace notation $W=\ker(A)$, $W^\top=\operatorname{im}(A^\top)$ as in \ref{LP-subspace-f}. The augmentation direction is computed by the \emph{affine scaling (AS) step}, that can be written as 
weighted least squares problems on the primal and dual sides:
\begin{equation}
  \label{sys:affine_scaling}
  \begin{aligned}
\Delta x &:= \argmin \Big\{\sum_{i \in [n]} \Big(\frac{x_i + \Delta x_i}{x_i}\Big)^2 : \Delta x \in W\Big\} \\
\Delta s &:= \argmin \Big\{\sum_{i \in [n]} \Big(\frac{s_i + \Delta s_i}{s_i}\Big)^2 : \Delta s \in W^\perp\Big\} \\
  \end{aligned}
\end{equation}
The update is then performed by setting $x \gets x + \alpha \Delta x$, $s \gets s + \alpha \Delta s$
for some $\alpha \in [0,1]$. As such, this algorithm can find $\varepsilon$-approximate solutions in weakly polynomial time. However,  it does not even terminate in finitely many iterations,
because using the weighted $\ell_2$-regressions problems \eqref{sys:affine_scaling} will never set variables exactly to 0
as required by complementary slackness. For standard interior point methods, a final rounding step is required.

The layered least squares interior-point method by Vavasis and Ye \cite{Vavasis1996} not only  terminates finitely, but has an iteration bound
of $O(n^{3.5}\log(\bar \chi_W + n))$, depending only on $A$, but independent of $b$ and $c$. We will refer to this as the VY algorithm.

Recall from Theorem~\ref{theorem:kappa_chi_bar_approx} that $\log(\bar \chi_A + n)=\Theta(\log(\kappa_A + n))$.
 For certain predictor iterations, they use a
 \emph{layered least squared (LLS)} step instead of affine scaling.
Variables are split into layers according to the $x_i$ values: we order the variables as $x_1\ge x_2\ge\ldots\ge x_n$, and start a new layer whenever there is a big gap between consecutive variables, i.e. $x_i>O(n^2)\bar\chi_A x_{i+1}$. For a point $(x,s)$ on the central path, the ordering on the $s_i$'s will be approximately reverse.

We illustrate their step based on a partition of the variable set $[n]$ into two layers $B \cup N = [n]$; the general step may use an arbitrary number of layers.
The layered least squared step is given in a 2-stage approach via
\begin{equation}
  \label{sys:lls}
  \begin{aligned}
\Delta x_N^\lal &:= \argmin \Big\{\sum_{i \in N} \Big(\frac{x_i + \Delta x_i}{x_i}\Big)^2 : \Delta x_N \in \pi_N(W)\Big\}, \\
\Delta x_B^\lal &:= \argmin \Big\{\sum_{i \in B} \Big(\frac{x_i + \Delta x_i}{x_i}\Big)^2 : (\Delta x_B, \Delta x_N)\in W\Big\}, \\[10pt]
\Delta s_B^\lal &:= \argmin \Big\{\sum_{i \in B} \Big(\frac{s_i + \Delta s_i}{s_i}\Big)^2 : \Delta s_B \in \pi_B(W^\perp)\Big\}, \\
\Delta s_N^\lal &:= \argmin \Big\{\sum_{i \in N} \Big(\frac{s_i + \Delta s_i}{s_i}\Big)^2 : (\Delta s_B, \Delta s_N)\in W^\perp\Big\}. \\
  \end{aligned}
\end{equation}
Whereas the  predictor-corrector algorithm---as most standard interior point variants---is invariant under rescaling the columns of the constraint matrix, the VY algorithm is \emph{not}: the layers are chosen by comparing the $x_i$ values. For this reason, it was long sought to find a scaling-invariant version of \cite{Vavasis1996}, that would automatically improve the running time dependence from $\bar\chi_W$ to the best possible value $\bar\chi^*_W$ achievable under column rescaling. In this line of work fall the results of \cite{Monteiro2008,Monteiro2003,MonteiroT05}, but none of them achieving dependence on the constraint matrix only while being scaling-invariant. 

This question was finally settled in \cite{DHNV20} in the affirmative. A key ingredient is revealing the connection between $\bar\chi_W$ and $\Le_W$. Preprocessing the instance via  the algorithm in Theorem~\ref{thm:bar-chi-star} to find a nearly optimal rescaling for $\Le_W$ (and thus for $\bar\chi_W$), and then using the VY algorithm already achieves $O(n^{3.5}\log(\bar \chi^*_W + n))$.
Beyond this, \cite{DHNV20} also presents a new LLS interior point method based on the pairwise circuit imbalances $\Le_{ij}$ that is inherently scaling invariant, as well as an improved analysis of $O(n^{2.5}\log(n)\log(\bar \chi^*_W + n))$ iterations.
 We give an outline next. Details are omitted here, a self-contained 
 overview  can be found in \cite{DHNV20}.

\paragraph{What determines a good layering?}
We illustrate the LLS step in the following hypothetical situation. Assume that the partition $B \cup N$ is such that $x_N^* = 0$ and $s_B^*=0$ for  optimal primal and dual solution $(x^*,s^*)$ to \ref{LP-subspace-f}. 
In particular, the LLS direction in \eqref{sys:lls} will set $\Delta x_N^\lal = -x_N$. Note that this does not hold for the AS direction $\Delta x_N$ that solves \eqref{sys:affine_scaling}. This benefit of the LLS direction over the AS direction will result in us being able to choose $\alpha$ larger for the LLS step compared to the AS step. 

To terminate with an optimal solution in a single step, we need to be able to select the step size $\alpha=1$, which requires that $x_B+\Delta_B^\lal\ge 0$.
But as in the computation of $\Delta x_N^\lal$ the components in $B$ are ignored we need to ensure the choice of $\Delta x_N^\lal$ does not impact $\Delta x_B^\lal$ by too much. By that we mean that there is a vector $z \in \R^B$ such that $|z_i/x_i| \ll 1$ for all $i \in B$ and $(z, \Delta x_N) \in W$. The norm of this $z$ is exactly governed by the lifting operator we introduced in Section~\ref{subsec:lifting_operator}. Let $W^x=\operatorname{diag}(x)^{-1}W= \{(w_i/x_i)_{i \in [n]} : w \in W\}$ denote the space $W$ rescaled by the $1/x_i$ values. Then,
\begin{equation}
\Big\|\Big(\frac{z_i}{x_i}\Big)_{i \in B}\Big\| = \Big\|L_N^{W^x}\Big(\Big(\frac{\Delta x_i^\lal}{x_i}\Big)_{i \in N}\Big)\Big\| \le \|L_N^{W^x}\| \cdot \Big\|\Big(\frac{\Delta x_i^\lal}{x_i}\Big)_{i \in N}\Big\|\, .
\end{equation}
By Lemma~\ref{lem:kappa-lift}, note that
\begin{equation}
  \Big\|\Big(\frac{z_i}{x_i}\Big)_{i \in B}\Big\| \le n\kappa_{W^x} \Big\|\Big(\frac{\Delta x_i}{x_i}\Big)_{i \in N}\Big\|\, .
\end{equation}
Further, notice that the lifting cost imposed on variables in $B$ by $\Delta x_N^\lal$ are given by the circuit imbalances in the rescaled space $W^x$: For $i \in B$ and $j \in N$ we are interested in $\kappa^{W^x}_{ji} = \kappa_{ji}{x_j}/{x_i}$.
In particular, if these quantities are small for all $i\in B$ and $j\in N$, then the \emph{low lifting cost} discussed above is achieved and we can select stepsize $\alpha=1$.

\paragraph{The choice of layers}
The Vavasis-Ye algorithm defines the layering based on the magnitude of the elements $x_i$. This guarantees that  $\kappa_{ji}{x_j}/{x_i}$ is small since 
$x_i>O(n^2)\kappa_A x_{j}$ if $i$ is on a higher layer than $j$. However, this choice is inherently not scaling-invariant.

The LLS algorithm in \cite{DHNV20} directly uses the scaling invariant quantities $\kappa_{ji}{x_j}/{x_i}$ to define the layering. In the ideal version of the algorithm, the layers are selected as the strongly connected components of the directed graph formed by the edges where this value is large. Hence, $\kappa_{ji}{x_j}/{x_i}$ is small whenever $i$ is on a higher layer than $j$.

This ideal version cannot be implemented since the pairwise imbalances $\kappa_{ji}$ are hard to compute or even approximate. The actual algorithm instead works with lower estimates $\hat\kappa_{ji}$. Thus, we may miss some edges from the directed graph, in which case the lifting may fail. Such failure will be detected in the algorithm, and in turn reveals better estimates for some pairs $(i,j)$.
