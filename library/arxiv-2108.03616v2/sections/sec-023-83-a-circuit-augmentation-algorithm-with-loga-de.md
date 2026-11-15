---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-023-83-a-circuit-augmentation-algorithm-with-loga-de
section_title: "A circuit augmentation algorithm with logA dependence"
section_number: 8.3
pages: 32-33
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.995
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance measures associated with linear spaces."
---
\label{sec:log-kappa}
Recall that the diameter bound Theorem~\ref{thm:diam-augment} is non-algorithmic in the sense that the augmentation steps rely on knowing the optimal solution $x^*$.
Dadush et al.~\cite{dadush2021circuit} complemented this with an efficient circuit augmentation algorithm, assuming oracles are provided for certain circuit directions.

\begin{theorem}[\cite{dadush2021circuit}]\label{thm:opt-augment}
    Consider the primal of \ref{LP_primal_dual}. Given a feasible solution, there exists a circuit augmentation algorithm that finds an optimal solution or concludes unboundedness using $O(n^3\log(n+\kappa_A))$ circuit augmentations.
\end{theorem}
	The main circuit augmentation direction used in the paper for optimization is a step defined as \textsc{Ratio-Circuit}, a generalisation of the previously mentioned augmentation step by Wallacher \cite{Wallacher} for minimum cost flows.
It finds a circuit that is a basic optimal solution to the following linear system:
\begin{equation}
    \label{sys:minratio-i}
    \min \; \pr{c}{z}\, \quad \mathrm{s.t.}\quad
    Az =0\, , \, 
    \pr{w}{z^-}  \leq 1\, .
\end{equation}
Equivalently, the goal is to minimize the cost to weight ratio of a circuit, where the unit weight of increasing a variable $x_i$ is $0$ and decreasing it is $w_i$. This can be seen as an efficiently implementable relaxation of the  deepest-descent direction: for suitable weights, it achieves a geometric decrease in the objective value. For a vector $x\in\R^n_+$, we let $1/x\in(\R\cup\{\infty\})^n$ denote the vector $w$ with $w_i=1/x_i$ (in particular, $w_i=\infty$ if $x_i=0$).

\begin{lemma}[{\cite{mccormick-shioura-not-strongly}}]
    Let $\OPT$ denote the optimum value of \ref{LP_primal_dual}.
    Given a feasible solution $x$ to \ref{LP_primal_dual}, let 
        $g$ be the elementary vector returned by {\sc Ratio-Circuit}$(A,c,1/x)$, and $x'$ the next iterate. Then,
    \[\pr{c}{x'}-\OPT\le \left(1-\frac{1}{n}\right)\left(\pr{c}{x}-\OPT\right)\, .\]
\end{lemma}
\begin{proof}
Let $x^*$ be an optimal solution to \ref{LP_primal_dual}, and let $z=(x^*-x)/n$. Then, $z$ is feasible to 
\eqref{sys:minratio-i} for $w=1/x$. The claim easily follows by noting that $\pr{c}{g}\le \pr{c}{z}=(\OPT-\pr{c}{x})/n$, and noting that $x+g$ is feasible since  $\pr{1/x}{g^-}\le 1$.
\end{proof}

Repeated application of a \textsc{Ratio-Circuit} step thus provide an iterate whose optimality gap decreases by a constant factor within $O(n)$ iterations. However, as noted in \cite{mccormick-shioura-not-strongly}, using only this rule does not even finitely terminate already for minimum cost flows.

\paragraph{Support Circuits}
For this reason,
\cite{dadush2021circuit} occasionally uses a second
circuit augmentation step called {\sc Support-Circuit}. Roughly speaking, when given a non-basic feasible point in the system \ref{LP_primal_dual}, one can efficiently augment around a circuit $g$ such that $\pr{c}{g} \le 0$ and thereby reduce its support while maintaining the objective. 

On a high level, the need for such an operation becomes clear when considering following example. Assume $c \equiv 1$ and further assume that we are given an iterate $x$ with $\|x\| \gg \kappa_A \|y\|$ for some basic solution $y$. Then geometric progress in the objective $\pr{c}{x}$ can be achieved by just reducing the norm of $x$, but just geometric progress would not give the desired bound in the number of circuit augmentations. Note that the norm of all basic solutions lies within a factor of $\operatorname{poly}(n) \kappa_A\|y\|$ by Proposition~\ref{prop:kappa-max}. Therefore, it is helpful to reduce the support through at most $n$ \textsc{Support-Circuit} operations until a basic solution is reached instead of applying \textsc{Ratio-Circuit}. Subsequent applications of \textsc{Ratio-Circuit} will now, again due to Proposition~\ref{prop:kappa-max}, not be able to reduce the norm of $x$ by more than a factor of $\operatorname{poly}(n)\kappa_A$, a fact that will be exploited in the proximity arguments. 

\medskip
The main progress in the algorithm in Theorem~\ref{thm:opt-augment} is identifying a new index $i$  such that  $x_i=0$ in the current solution and $x_i^* = 0$ in any optimal solution $x^*$. Such a conclusion derives using a variant of the proximity theorem Theorem~\ref{thm:primal-fixing-upper}.
To implement the main subroutine that fixes a variable to $x_i=0$, a careful combination of \textsc{Ratio-Circuit}  and \textsc{Support-Circuit}  iterations is used.
Interestingly, the \textsc{Ratio-Circuit} iterations do not use the original cost function $c$, but a perturbed objective function $c'$. The main progress in the subroutine is identifying new `large' variables, similarly to the proof of Theorem~\ref{thm:diam-augment}. Perturbations are performed whenever a new large variable $x_j$ is identified.
