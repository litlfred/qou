---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-017-822-convergence-bounds
section_title: "Convergence bounds"
section_number: 8.2.2
pages: 31-33
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance mea sures associated with linear spaces."
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.994
---
We now state the convergence bounds from \cite{DHL15}. The original statement refers to subdeterminant bounds; we paraphrase them in terms of finding approximately optimal solutions.

\begin{theorem}[{De Loera, Hemmecke, Lee \cite{DHL15}}]\label{thm:DLHL}
Consider a linear program in the form \ref{LP-augment}. 
Assume we are given an initial feasible solution $x^{(0)}$, and let $\OPT$ denote the optimum value. By an $\varepsilon$-
 optimal solution we mean an iterate $x^{(t)}$ such that $\pr{c}{x^{(t)}}\le \OPT+\varepsilon$.
\begin{enumerate}[(a)]
	\item \label{i:deepest}For given $\varepsilon>0$, one can find an $\varepsilon$-optimal solution in
	$2n\log_2\left(\frac{\pr{c}{x^{(0)}}-\OPT}{\varepsilon}\right)$ deepest-descent augmentations.
	\item\label{i:dantzig} For given $\varepsilon>0$, one can find an $\varepsilon$-optimal solution in
	$\frac{2n^2\gamma}{\varepsilon}\log_2\left(\frac{\pr{c}{x^{(0)}}-\OPT}{\varepsilon}\right)$  Dantzig-descent augmentations, where $\gamma$ is an upper bound on the maximum entry in any feasible solution.
	\item\label{i:steepest} One can find an exact optimal solution in $\min\{n|\circuits_A|,\ell_A\}$ steepest-descent augmentations, 
	 where $\ell_A$ denotes the number of distinct values of $\pr{c}{g}/\|g\|_1$ over $g\in \EE(A)$.
\end{enumerate}
\end{theorem}

In general, circuit augmentation algorithms may not even finitely terminate; see \cite{mccormick-shioura-not-strongly} for an example on Wallacher's rule for minimum cost flows.
In parts \ref{i:deepest} and \ref{i:dantzig}, assume that all basic solutions are $1/k$-integral for some $k\in \mathbb{Z}$ and cost function is $c\in \Z^n$. If $x^{(t)}$ is a $\varepsilon$-optimal solution for $\varepsilon<1/k$, then we can identify an optimal vertex of the face containing $x^{(t)}$ using 
a Carath\'eodory decomposition argument,
this can be implemented by a sequence of $\le n$ circuit augmentations (see \cite[Lemma 5]{DHL15}).

According to part \ref{i:steepest}, steepest descent terminates with  an optimal solution in a finite number of iterations; moreover,  the bound only depends on the linear space $\ker(A)$ and $c$, and not on the parameters $b$ and $u$. However, the bound can be exponentially large.

Bland's original observation was that $\ell_A$ is strongly polynomially bounded for the maximum flow problem. Recall that all elementary vectors $g$ correspond to cycles in the auxiliary graph. Normalizing such that $g_i\in \{0,\pm 1\}$,  $-\pr{c}{g}=1$ for every augmenting cycle (as these must use the $(t,s)$ arc), and $\|g\|_1$ is between 1 and $|E|$. In fact, the crucial argument by Edmonds and Karp \cite{Edmonds72} and Dinic \cite{dinic1970algorithm}  is showing that the length of the shortest augmenting path is non-decreasing, and must strictly increase within $|E|$ consecutive iterations.

For an integer cost function $c\in \Z^n$, Lee~\cite[Proposition 3.2]{Lee89}  gave the following upper bound on $\ell_A$:
\begin{prop}\label{prop:l-a} If $\|c\|_1\le (n-m+1)\|c\|_\infty$, then 
\[
\ell_A\le\frac12 {\|c\|_\infty} (n-m+1)\bar\Le_A((n-m+1)\bar\Le_A +1)\, .
\]
\end{prop}

 In order to bound the circuit distance between vertices $x$ and $y$ let us use the following cost function. For the basis $B$ defining $y$, let 
\begin{equation}
\label{eq:c-u}
c_i=\begin{cases}0&\mbox{if }i\in B\, ,\\
1& \mbox{if }i\in [n]\setminus B, y_i=0\, ,\\
-1&\mbox{if }i\in [n]\setminus B, y_i=u_i\, .
\end{cases}
\end{equation}
With this cost function, Theorem~\ref{thm:DLHL}\ref{i:steepest} and Proposition~\ref{prop:l-a} yield  a bound $O((n-m)^2 \bar\Le_A^2)$ on the circuit diameter using the steepest descent algorithm.

Extending the analysis of the Goldberg-Tarjan algorithm \cite{Goldberg89}, we present a new bound that only depends on the fractional circuit imbalance $\kappa_A$, and is independent of $c$.
The same bound was independently obtained by Gauthier and Derosiers \cite{Gauthier2021}. The proof is given in Section~\ref{sec:steepest-improved}.

\begin{theorem}\label{thm:steepest-main} For the problem \ref{LP-augment} with constraint matrix $A\in\R^{m\times n}$, the steepest-descent algorithm terminates within $O(n^2m\kappa_A \log(\kappa_A+n))$ augmentations starting from any feasible solution $x^{(0)}$.
\end{theorem} 
This improves on the above bound $O((n-m)^2 \bar\Le_A^2)$ for most values of the parameters (recall that $\kappa_A\le\bar\kappa_A^2$). Moreover, this bounds the running time for steepest descent for an arbitrary cost function $c$, not necessarily of the form \eqref{eq:c-u}.

Both these bounds are independent of $b$, however, $\kappa_A$ and $\bar\kappa_A$ may be exponentially large in the encoding length $L_A$ of the matrix $A$. In contrast, Theorem~\ref{thm:DLHL}\ref{i:deepest} yields a polynomial bound $O(n L_{A,b})$ on the number of deepest-descent iterations, where $L_{A,b}$ is the encoding length of $(A,b)$. In what follows, we review a new circuit augmentation algorithm from \cite{dadush2021circuit} that achieves a $\log\kappa_A$ dependence; the running time is bounded as $O(n^3 L_A)$, independently from $b$.


\subsection{A circuit augmentation algorithm with $\log\kappa_A$ dependence}\label{sec:log-kappa}
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
