---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-003-31-bounds-on-subdeterminants
section_title: "Bounds on subdeterminants"
section_number: 3.1
pages: 7-9
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.994
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance measures associated with linear spaces."
---
\label{sec:subdet}
For an integer matrix $A\in \Z^{m\times n}$, we define 
\begin{equation}
\begin{aligned}
  \Delta_A &:= \max \{|\det(B)|: B \text{ is a  nonsingular submatrix of } A\},\mbox{ and}\\
  \dot\Delta_A &:=\lcm \{|\det(B)|: B \text{ is a nonsingular submatrix of } A\}.\\
  \end{aligned}
\end{equation} 
The matrix is \emph{totally unimodular (TU)}, if $\Delta_A=1$: thus, all subdeterminants are $0$ or $\pm 1$. This class of matrices plays a foundational role in combinatorial optimization,  see e.g., \cite[Chapters 19-20]{SchrijverLPIP}. A significant example is the node-arc incidence matrix of a directed graph. A key property is that they define integer polyhedra, see Theorem~\ref{thm:HK} below.
A polynomial-time algorithm is known to decide whether a matrix is TU, 
based on the deep decomposition theorem by Seymour from 1980 \cite{Seymour1980}.

The next statement is implicit in \cite[Proposition 5.3]{Lee89}. 
\begin{prop}
  \label{prop:kappa-delta}
  For every integer matrix $A\in \Z^{m\times n}$, $\bar\Le_A\le \Delta_A$ and $\kd_A\le\dot\Delta_A$.
\end{prop}
\begin{proof}
Let  $C\in\circuits_A$ be a circuit, and select a submatrix $\hat A\in \Z^{(|C|-1)\times |C|}$ of $A$ where the columns are indexed by $C$, and the rows are linearly independent. 
Let $\hat A_{-i}$ be the square submatrix resulting from deleting the column corresponding to $i$ from $\hat A$.
From Cramer's rule, we see that $|g^C_i|=|\det(\hat A_{-i})|/\alpha$ for some $\alpha\in\Q$, $\alpha \ge 1$. This implies both claims $\bar\Le_A\le \Delta_A$ and $\kd_A\le\dot\Delta_A$.
\end{proof}

In Propositions~\ref{prop:B_inverse} and \ref{prop:B_inverse_General}, 
we show that for any matrix $A \in \Q^{m \times n}$ there exists a matrix $\tilde A \in \Z^{m \times n}$ such that $\ker(A) = \ker(\tilde A)$ and $\dot\Delta_{\tilde A} \le (\kd_A)^{m}$.

To see an example where $\Delta_A$ can be much larger than $\kappa_A$, let $A\in \Z^{n\times \binom{n}{2}}$ be the node-edge incidence matrix of a complete undirected graph on $n$ nodes; assume $n$ is divisible by $3$. The determinant corresponding to any submatrix corresponding to an odd cycle is $\pm 2$. Let $H$ be an edge set of $\frac{n}3$ node-disjoint triangles. Then $A_H$ is a square submatrix with determinant $\pm 2^{n/3}$. In fact, $\Delta_A=2^{n/3}$ in this case, since $\Delta_A$ for a node-edge incidence matrix equals the maximum number of node disjoint odd cycles, see  \cite{grossmanMinorsIncidenceMatrix1995}.
On the other hand, $\kappa_A=\bar\kappa_A=\kd_A\in \{1,2\}$ for the incidence matrix $A$ of any undirected graph; see Section~\ref{sec:HK}.

\medskip

For TU-matrices, the converse of Proposition~\ref{prop:kappa-delta}  is also true. In 1956, Heller and Tompkins \cite{heller1957,heller1956} introduced the \emph{Dantzig property}. A matrix $A\in\R^{m\times n}$ has the Dantzig property if $A^{-1}_B A$ is a $0,\pm 1$-matrix for every nonsingular $m\times m$ submatrix $A_B$. According to Proposition~\ref{prop:kappa-max}, this is equivalent to $\kappa_A=1$. Theorem~\ref{thm:tu_iff_kappa_1} below can be attributed to Cederbaum \cite[Proposition (v)]{Cederbaum57}; see also Camion's PhD thesis \cite[Theorem 2.4.5(f)]{camion1964}.
The key is the following lemma that we formulate for general $1/\kd_A$ for later use.

\begin{lemma}\label{lem:sub-inverse}
Let $A=(I_m|A')\in\R^{m\times n}$. Then, for any nonsingular square submatrix $M$ of $A$, the inverse $M^{-1}$ is $1/\kd_A$-integral, with non-zero entries between $1/\Le_A$ and $\Le_A$ in absolute value.
\end{lemma}
\begin{proof}
Let $M$ be any $k \times k$ nonsingular submatrix of $A$; w.l.o.g., let us assume that it uses the first $k$ rows of $A$. Let $B$ be the set of columns of $M$, along with the $m-k$ additional columns $i\in [k+1,m]$, i.e., the last $m-k$ unit vectors from $I_m$. Thus,
$A_B\in \R^{m\times m}$ is also nonsingular. After permuting the columns, this can be written in the form
\[
A_B=\left(\begin{array}{c|c}
M & 0  \\
\hline
L& I_{m-k} 
\end{array}\right)
\]
for some $L\in \Z^{(m-k)\times k}$.
We now use Proposition~\ref{prop:kappa-max}  for $
\tilde A = A_B^{-1} A$. 
Note that the first $m$ columns of $
\tilde A$ correspond to $A_B^{-1}$. Moreover, we see that
\[
A_B^{-1}=\left(\begin{array}{c|c}
 M^{-1} & 0 \\
\hline
-LM^{-1} & I_{m-k} 
\end{array}\right)
\]
Thus, $M^{-1}$ is $1/\dot\kappa_A$-integral, with non-zero entries between $1/\Le_A$ and $\Le_A$ completing the proof.
\end{proof}
Appa and Kotnyek define $k$-regular matrices as follows: a rational matrix $A'\in\R^{m\times n}$ is $k$-regular if and only if the inverse of all nonsingular submatrices is $1/k$-integral. From the above statement, it follows that $A'$ is $k$-regular in this sense for $k=\kappa_{(I_m|A')}$. See also
Corollary~\ref{cor:HK-kappa}.

\begin{theorem}[Cederbaum, 1957]
  \label{thm:tu_iff_kappa_1}
  Let $W \subset \R^n$ be a linear subspace. Then, the following are equivalent.
  \begin{enumerate}[(i)]
  \item\label{Ced:i} $\kappa_W=\bar\kappa_W=\kd_W = 1$.
  \item\label{Ced:ii} There exists a TU matrix $A$, such that $W = \ker(A)$.
  \item\label{Ced:iii} For any matrix $A$ in basis form such that $W=\ker(A)$, $A$ is a TU-matrix.
  \end{enumerate} 
\end{theorem}
\begin{proof}
\ref{Ced:iii} $\Rightarrow$ \ref{Ced:ii} is straightforward, and \ref{Ced:ii} $\Rightarrow$ \ref{Ced:i} follows by  Proposition~\ref{prop:kappa-delta}. It remains to show \ref{Ced:i} $\Rightarrow$ \ref{Ced:iii}. Let $\rk(W)=n-m$, and consider any $A\in \R^{m\times n}$ in basis form such that $W=\ker(A)$. For simplicity of notation, assume the basis is formed by the first $m$ columns, that is, 
 $A=(I_{m} | A')$ for some $A' \in \R^{m \times (n-m)}$.

Proposition~\ref{prop:kappa-max} implies that all entries of $A$ are $0$ and $\pm 1$. Consider any nonsingular square submatrix $M$ of $A$.
By Lemma~\ref{lem:sub-inverse}, $M^{-1}$ is also a $0$, $\pm 1$ matrix.
 Consequently, both $\det(M)$ and $\det(M^{-1})$ are nonzero integers, which implies that $|\det(M)|=1$, as required.
\end{proof}
