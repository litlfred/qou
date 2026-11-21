---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-002-3-properties-of-the-imbalance-measures
section_title: "Properties of the imbalance measures"
section_number: 3
pages: 6-7
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.993
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance measures associated with linear spaces."
---
\label{sec:basic}

\paragraph{Comparison to well-scaled frames}
Lee's work ~\cite{Lee89} on \emph{`well-scaled frames'},
investigated the following closely related concepts. For a set $S\subseteq \Q$ the rational linear space $W$ is \emph{$S$-regular} if for every elementary vector $g\in \EE(F)$, there exists a $\lambda\neq 0$ such that all nonzero entries of $\lambda g$ are in $S$. For $S=\{-k,\ldots,k\}$, the subspace is called \emph{$k$-regular}. 
For $k,\Omega\in \N$, a subspace is \emph{$k$-adic of order $\Omega$} if it is $S$-regular for $S=\{\pm 1,\pm k,\ldots,\pm k^\Omega\}$. The \emph{frame} of the subspace $W$ refers to the set of elementary vectors $\EE(W)$.

Using our terminology, 
a subspace is $k$-regular if and only if $\bar\kappa_W=k$, and every $k$-adic subspace is anchored. Many of the properties in this section were explicitly or implicitly shown in Lee~\cite{Lee89}. However, it turns out that many  properties are simpler and more natural to state in terms of either $\kappa_W$ and $\dot\kappa_W$. Roughly speaking, the fractional circuit imbalance $\kappa_W$ is the key quantity of interest for continuous properties, particularly relevant for proximity results in linear programming. On the other hand, the lcm-circuit imbalance $\dot\kappa_W$ captures most clearly the integrality properties. The max-circuit imbalance $\bar\kappa_W$ interpolates between these two, although, as already noted by Lee, it is the right quantity for proximity results in integer programming (see Section~\ref{sec:graver}).

Appa and Kotnyek \cite{Appa04} also use the term $k$-regularity in a different sense, as a natural extension of unimodularity. This turns out to be strongly related to $\kd_W$; see Lemma~\ref{lem:sub-inverse} and Corollary~\ref{cor:HK-kappa}.

\paragraph{The key lemma on basis forms}
The following simple proposition turns out to be extremely useful in deriving properties of $\Le_W$ and $\kd_W$. The first statement is from \cite{DadushNV20}.
\begin{prop}\label{prop:kappa-max}
For every matrix $A\in \R^{m\times n}$ with $\rk(A) = m$,
\[
    \Le_A = \max\left\{ \|A_B^{-1} A\|_{\max} : A_B \text{ non-singular $m \times m$-submatrix of } A\right\}\, .
\]
Moreover, for each nonsingular $A_B$, all nonzero entries of $A_B^{-1} A$ have absolute values between $1/\Le_A$ and $\Le_A$ and are $1/\kd_A$-integral.
\end{prop} 
\begin{proof}
Consider the matrix $A'=A_B^{-1}A$ for any non-singular $m\times m$ submatrix $A_B$. Let us renumber the columns such that $B$ corresponds to the first $m$ columns. 
Then, for every $m+1\le j\le n$, the $j$th column of $A'$ corresponds to an elementary vector $g$ where $g_j=1$, and $g_i=-A'_{ij}$ for $i\in [m]$. Hence, $\|A'\|_{\max}$ gives a lower bound on $\Le_A$. This also implies that all nonzero entries are between $1/\Le_A$ and $\Le_A$. To see that all entries of $A'$ are $1/\kd_A$-integral, note that $g=g'/\alpha$ for a vector $g'$ where all entries are integer divisors of $\dot\kappa_A$. Since $g_j=1$, it follows that $\alpha$ itself is an integer divisor of $\kd_A$.

To see that the maximum in the first statement is achieved, take the elementary vector $g^C$ that attains the maximum in the definition of $\Le_A$; let $g_j^C$ be the minimum absolute value element.
Let us select a basis $B$ such that $C\setminus \{j\}\subseteq B$. Then, the largest absolute value in the $j$-th column of $A_B^{-1}A$ will be $\Le_A$.
\end{proof}
