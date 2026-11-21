---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-022-822-convergence-bounds
section_title: "Convergence bounds"
section_number: 8.2.2
pages: 31-32
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.995
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance measures associated with linear spaces."
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
