---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-005-33-self-duality
section_title: "Self-duality"
section_number: 3.3
pages: 10-12
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.921
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance measures associated with linear spaces."
---
\label{sec:self-dual}
We next show that both $\Le_W$ and $\kd_W$ are self-dual.
These rely on the following duality property of circuits.
We introduce the following more refined quantities that will also come useful later on.

\begin{Def}[Pairwise Circuit Imbalances] \label{def:pairwise circuit_imbalances} For a space $W \subseteq \R^n$ and variables $i,j \in [n]$ we define 
\[
\begin{aligned}\KK_{ij}^W &:= \set{\left|\frac{g_j}{g_i}\right|:\,  \{i,j\} \subseteq \supp(g), g \in \EE(W)}\, ,\quad \Le_{ij}^W := \max \KK_{ij}^W\, ,\\
\dot \KK_{ij}^W &:= \left\{\lcm(p,q) : p,q \in \N, \gcd(p,q) = 1, \frac{p}{q} \in \KK_{ij}^W\right\}\, .
\end{aligned}\]
We call $\Le_{ij}^W $ the \emph{pairwise imbalance between $i$ and $j$}.
\end{Def}
Cleary, $\Le_W=\max_{i,j\in [n]} \Le_{ij}^W$ for a nontrivial linear space $W$.
We use the following simple lemma.
\begin{lemma}\label{lem:basis_circuits}
Consider a matrix $A\in\R^{m\times n}$ in basis form for $B\subseteq[n]$, i.e., $A_B=I_m$. Let $W=\ker(A)$; thus, $W^\perp=\spn(A^\top)$. The following hold.
\begin{enumerate}[(i)]
\item \label{i:basis_circuits-i} The rows of $A$ form a circuit basis of $W^\perp$, denoted as $\EE_B(W^\perp)$.
\item \label{i:basis_circuits-ii} For any two rows $A^i,A^j$, $i,j\in B$, $i\neq j$, and $k\in[n]\setminus B$, the vector $h=A_{jk} A^i-A_{ik} A^j$ fulfills $h \in\EE(W^\perp)$.
\end{enumerate}
\end{lemma}
\begin{proof}
For part \ref{i:basis_circuits-i}, the rows are clearly linearly independent and span $W^\perp$. Therefore,  every $g\in W^\perp$ must have $\supp(g)\cap B\neq\emptyset$, and if $\supp(g)\cap B=\{i\}$ then $g=g_i A^i$. These two facts imply that each $A^i$ is support minimal in $W^\perp$, that is, $A^i\in\EE(W^\perp)$.

For part \ref{i:basis_circuits-ii}, there is nothing to prove if $A_{ik}=0$ or $A_{jk}=0$; for the rest, assume both are nonzero. Assume for a contradiction $h\notin\EE(W^\perp)$; thus, there exists a $g\in W^\perp$, $g\neq 0$ and $\supp(g)\subsetneq \supp(h)$. We have $\supp(h)\cap B=\{i,j\}$. If $\supp(g)\cap B\subsetneq \{i,j\}$, as above we get that $g=g_i A^i$ or $g=g_j A^j$, a contradiction since $h_k=0$ but $A_{ik}, A_{jk}\neq 0$. Hence, $\supp(g)\cap B=\{i,j\}$. By part \ref{i:basis_circuits-i}, we have $g=g_i A^i+g_j A^j$; and since $h_k=0$ it follows that $g_i/g_j=-A_{jk}/A_{ik}$; thus, $g$ is a scalar multiple of $h$, a contradiction.
\end{proof}

\begin{lemma}\label{lem:dual-circuit}
For any $i,j \in [n]$ we have $\KK_{ij}^W = \set{\alpha^{-1} : \alpha \in \KK_{ji}^{W^\perp}}$. Equivalently: for every elementary vector $g \in \EE(W)$ with indices $i,j \in \supp(g)$ there exists an elementary vector $h\in \EE(W^\perp)$  such that $|h_i/h_j| = |g_j/ g_i|$.
\end{lemma}
\begin{proof}
Let $g \in \EE(W)$ such that $i,j \in \supp(g)$. If $\supp(g) = \{i,j\}$ then any $h \in \EE(W^\perp)$ with $i \in \supp(h)$ fulfills $g_ih_i + g_jh_j = \pr{g}{h} = 0$, so $j \in \supp(h)$ and $|h_i/h_j| = |g_j/g_i|$.

Else, there exists $k \in \supp(g) \setminus \{i,j\}$. Let us select a basis $B$  of $\mathcal{M}(W)$ with $\supp(g) \setminus B=\{k\}$. Let $A\in\R^{m\times n}$ be a matrix in basis form for $B$ with $\ker(A)=W$, and let  $h=A_{jk} A^i-A_{ik} A^j$, an elementary vector in $\EE(W^\perp)$
by  Lemma~\ref{lem:basis_circuits}\ref{i:basis_circuits-ii}.

By the construction, $|h_i/h_j|=|A_{jk}/A_{ik}|$. On the other hand,
$\pr{g}{A^i} = 0$ and $\supp(g) \setminus B=\{k\}$ implies $g_i=-g_k A_{ik}$ and similarly $\pr{g}{A^j} = 0$ implies $g_j=-g_k A_{jk}$. The claim follows.
\end{proof}

For $\Le_W$, duality is immediate from the above:
\begin{prop}[\cite{DHNV20}]\label{prop:kappa-dual}
For any linear subspace $W\subseteq \R^n$, we have
$\Le_W=\Le_{W^\perp}$.
\end{prop}

Let us now show duality also for $\kd_W$; this was  shown in \cite[Lemma 2.1]{Lee89} in a slightly different form.
\begin{prop}\label{prop:kappadot-dual}
For any rational linear subspace $W\subseteq \R^n$, we have $\kd_W=\kd_{W^\perp}$.
\end{prop}

\begin{proof}
Recall the $p$-adic valuation $\nu_p(n)$ defined in \eqref{eq:p-adic}.
It suffices to show that $\nu_p(\dot \kappa_W) = \nu_p(\dot \kappa_{W^\perp})$ for any prime $p \in \primes$.
We can reformulate as
\begin{eqnarray*}
\nu_p(\dot \kappa_W) &=& \nu_p(\lcm\left\{\lcm(g^C):\,C\in\circuits_W\right\})\\
&=&\max\left\{\nu_p(\lcm(g^C)):\,C\in\circuits_W\right\}\\
&=& \max \left\{ \nu_p(\alpha) :\,  i,j \in [n], \alpha \in \dot\KK_{ij}^W\right\}. \, 
\end{eqnarray*}
Lemma~\ref{lem:dual-circuit} implies that the last expression is the same for $W$ and $W^\perp$.
\end{proof}

We next show that $\kappa_W$ and $\kd_W$ are monotone under projections and restrictions of the subspace.
\begin{lemma}\label{lem:circuit_minors}
For any linear subspace $W\subseteq \R^n$, $J\subseteq[n]$ and $i,j\in J$, we have 
\[
\KK_{ij}^{\pi_J(W)} \subseteq \KK_{ij}^W\, ,\quad \KK_{ij}^{W_J} \subseteq \KK_{ij}^W\, , \quad \dot\KK_{ij}^{\pi_J(W)} \subseteq \dot\KK_{ij}^W\, ,\quad   \mbox{and}\quad \dot\KK_{ij}^{W_J} \subseteq \dot\KK_{ij}^W\, .
\]
\end{lemma}
\begin{proof}
Let $g \in \EE(W_J)$. Then $(g, 0_{[n]\setminus J} )\in \EE(W)$ and so $\KK_{ij}^{W_J} \subseteq \KK_{ij}^W$. Note that $\pi_J(W) = ((W^\perp)_J)^\perp$ and so by Proposition~\ref{lem:dual-circuit},
\begin{equation}\KK_{ij}^{\pi_J(W)} = \set{\alpha^{-1} : \alpha \in \KK_{ji}^{(W^\perp)_J}} \subseteq \set{\alpha^{-1} : \alpha \in \KK_{ji}^{W^\perp}} = \KK_{ij}^{W}. 
\end{equation} 
The same arguments extend to $\dot\KK_{ij}$.
\end{proof}
\begin{prop}\label{prop:proj-fix}
For any linear subspace $W\subseteq \R^n$ and $J\subseteq[n]$, we have 
\[
\Le_{W_J}\le\Le_W\, ,\quad  \Le_{\pi_J(W)}\le\Le_W\, , \quad \kd_{W_J}\le\kd_W\, ,\quad  \mbox{and}\quad \kd_{\pi_J(W)}\le\kd_W\, .
\]
\end{prop}
