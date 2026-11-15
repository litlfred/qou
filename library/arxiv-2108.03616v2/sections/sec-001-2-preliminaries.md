---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-001-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 5-6
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.985
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance measures associated with linear spaces."
---
\label{sec:prelim}

We let $[n] := \{1, \ldots, n\}$. For $k\in\N$, a number $q\in\Q$ is \emph{$1/k$-integral} if it is an integer multiple of $1/k$. Let $\primes\subseteq\N$ denote the set of primes.
Let $\R_{++}$ denote the set of positive reals, and $\R_+$ the set of nonnegative reals. 
  

For a prime number $p\in \primes$, the $p$-\emph{adic valuation} for $\mathbb{Z}$ is the function $\nu_p\colon \Z \to \N$ defined by
\begin{equation}\label{eq:p-adic}
  \nu_p(n) =
  \begin{cases}
      \max \{v \in \N : p^v \divides n\} & \text{if } n \neq 0\\
      \infty & \text{if } n=0.
  \end{cases}
\end{equation}

We denote the support of a vector $x \in \R^n$ by $\supp(x) = \{i\in [n]: x_i \neq 0\}$.  We let ${\1}_n$ denote the $n$-dimensional all-ones vector, or simply $\1$, whenever the dimension is clear from the context. Let $e_i$ denote the $i$-th unit vector.

For vectors $v, w \in \R^n$ we denote by $\min\{v,w\}$ the vector $z \in \R^n$ with $z_i = \min\{v_i, w_i\}, i \in [n]$; analogously for $\max\{v,w\}$. Further, we use the notation $v^+ = \max\{v, 0_n\}$ and $v^- = \max\{-v, 0_n\}$ 
; note that both $v^+$ and $v^-$ are nonnegative vectors. 
For two vectors $x, y \in \R^n$, we let $\pr{x}{y}=x^\top y$ denote their scalar product. For sets $S, T \subseteq \R$ we let $S \cdot T = \{st | s \in S, t \in T\}$.

We let $I_n\in \R^{n\times n}$ denote the $n$-dimensional identity matrix.  We let $\bD_n$ denote the set of all positive definite $n\times n$
diagonal matrices. 
For a vector $v \in \R^n$, we denote by $\Diag(v)$ the diagonal matrix whose $i$-th diagonal entry is $v_i$ and for a matrix $A\in\R^{m\times n}$, let $A_1,A_2,\ldots,A_n\in \R^n$ denote the column vectors, and $A^1,A^2,\ldots,A^m\in\R^m$ denote the row vectors, transposed. For $S\subseteq [n]$, let $A_S$ denote the submatrix formed by the columns of $A$ and for $B\subseteq [n]$, $|B|=m$, we say that $A$ is in \emph{basis form} for $B$ if $A_B=I_m$.

We will use $\ell_1,\ell_2$ and $\ell_\infty$ vector norms, denoted as $\|.\|_1,\|.\|_2$, and $\|.\|_\infty$, respectively. By $\|v\|$, we always mean the 2-norm $\|v\|_2$. Further, for a matrix $A\in\R^{m\times n}$, $\|A\|$ will refer to the $\ell_2\to\ell_2$ operator norm, 
and $\|A\|_{\max}=\max_{i,j}|A_{ij}|$ to the max-norm.

For an index subset $I\subseteq [n]$, we use $\pi_I: \R^n \rightarrow \R^I$ for the coordinate
projection. That is, $\pi_I(x)=x_I$, and for a subset $S\subseteq
\R^n$, $\pi_I(S)=\{x_I:\, x\in S\}$.
We let $\R^n_I = \{x \in \R^n : x_{[n]\setminus I} = 0\}$.

For a subspace $W\subseteq \R^n$, we let $W_I=\pi_I(W\cap \R^n_I)$. It is easy to see that $\pi_I(W)^\perp = (W^\perp)_I$. 
Assume we are given a matrix $A\in \R^{m\times n}$ such that $W=\ker(A)$. Then, $W_I=\ker(A_I)$, and we can obtain a matrix $A'$ from $A$ such that $\pi_I(W)=\ker(A')$ by performing a Gaussian elimination of the variables in $[n]\setminus I$.

For a subspace $W \subseteq \R^n$, we define by $\Pi_W\colon \R^n \to \R^n$ the orthogonal projection onto $W$.

For a set of vectors $V=\{v_i:\,  i\in I\}$ we let $\spn(V)$ denote the linear space spanned by the vectors in $V$. For a matrix $A\in\R^{m\times n}$, $\spn(A)\subseteq\R^{m}$ is the subspace spanned by the columns of $A$.
A \emph{circuit basis} of a subspace $W\subseteq \R^n$ is a set ${\cal F}\subseteq {\EE}(W)$ of $\rk(W)$ linearly independent elementary vectors, i.e., $\spn({\cal F})=W$.

\paragraph{Linear Programming (LP) in matrix formulation} We will use LPs in the following standard primal and dual form for $A\in\R^{m\times n}$, $b\in \R^m$, $c\in \R^n$. 

\begin{equation}
  \label{LP_primal_dual} \tag{LP$(A,b,c)$}
  \begin{aligned}
  \min \; &\pr{c}{x} \quad \\
  Ax& =b \\
  x &\geq 0. \\
  \end{aligned}
  \quad\quad\quad
  \begin{aligned}
  \max \; & \pr{y}{b} \\
  A^\top y + s &= c \\
  s & \geq 0. \\
  \end{aligned}
\end{equation}

\paragraph{Linear Programming  in subspace formulation}
Since our main focus is on properties of subspaces, it will be more natural to think about linear programming in the following \emph{subspace formulation}.
For $A$, $b$ and $c$ as above,  let $W=\ker(A)\subseteq \R^n$ and $d\in \R^n$ such that $Ad=b$. We assume the existence of such a vector $d$ as otherwise the primal program is trivially infeasible. We can write \ref{LP_primal_dual}  in the following equivalent form:
\begin{equation}
\tag{LP$(W,d,c)$}
\label{LP-subspace-f}
\begin{aligned}
\min \; & \pr{c}{x} \\ 
x &\in W + d \\
x &\geq 0.\,
\end{aligned}
\quad\quad\quad
\begin{aligned}
\max \; & \pr{c - s}{d} \\
s &\in W^\perp + c \\
s & \geq 0.
\end{aligned}
\end{equation}

\paragraph{Conformal circuit decompositions}
\label{par:sign_consistent}
We say that the vector $y \in \R^n$ \emph{conforms to}
$x\in\R^n$ if $x_iy_i > 0$ whenever $y_i\neq 0$. 
Given a subspace $W\subseteq \R^n$, a \emph{conformal circuit decomposition} of a vector $z\in W$ is a decomposition
\[
z=\sum_{k=1}^h  g^k,
\]
where
$h\le n$ and  $g^1,g^2,\ldots,g^h\in \EE(W)$ are elementary vectors that are conformal with
$z$. A fundamental result on elementary vectors asserts the existence of a conformal circuit decomposition, see e.g. \cite{Fulkerson1968,RockafellarTheEV}.

\begin{lemma} \label{lem:sign-cons}
For every subspace $W\subseteq \R^n$,  every $z\in W$ admits a conformal circuit decomposition. 
\end{lemma}
\begin{proof}
Let $F \subseteq W$ be the set of vectors conformal with $z$. $F$ is a polyhedral cone; its
 faces  correspond to inequalities of the form $y_k \geq 0$, $y_k\leq 0$,
or $y_k = 0$.
The rays (edges) of $F$ are of the form $\{\alpha g:\,  \alpha\ge 0\}$  for $g\in\EE(W)$. Clearly, $z\in F$, and thus, $z$ can be written as a conic combination of at most $n$ rays by the Minkowski--Weyl theorem. Such a decomposition yields a conformal circuit decomposition.
\end{proof}

\paragraph{Linear matroids}
For a linear subspace $W\subseteq\R^n$, let ${\cal M}(W)=([n],{\cal I})$ denote the associated linear matroid, i.e. the matroid defined by the set of circuits $\circuits_W$. Here, ${\cal I}$ denotes the set of independent sets; $S\in {\cal I}$ if and only if there exists no $z\in W\setminus \{0\}$ with $\supp(z)\subseteq S$; the maximal independent sets are the \emph{bases}.
We refer
the reader to \cite[Chapter 39]{schrijver} or \cite[Chapter
5]{frankbook} for relevant definitions and background on matroid theory.

 Assume $\rk(W)=m$ and $W=\ker(A)$ for $A\in\R^{m\times n}$. Then $B\subseteq [n]$, $|B|=m$ is a basis in ${\cal M}(A):={\cal M}(W)$ if and only if $A_B$ is nonsingular; then, $A'=A_B^{-1}A$ is in basis form for $B$ 
such that $\ker(A')=W$. 

The matroid $\cal M$ is \emph{separable}, if the ground set $[n]$ can be
partitioned into two nonempty subsets $[n]=S\cup T$ such that $I\in
{\cal I}$ if and only if $I\cap S,I\cap T\in {\cal I}$. In this case, the matroid is the direct sum of its
restrictions to $S$ and $T$. In particular, every circuit is fully
contained in $S$ or in $T$. For the linear matroid ${\cal M}(A)$, separability means that $\ker(A)=\ker(A_S)\oplus \ker(A_T)$. 
 In this case, we have $\kappa_A=\max\{\kappa_{A_S},\kappa_{A_T}\}$ and  $\kd_A=\lcm\{\kd_{A_S},\kd_{A_T}\}$; 
solving \ref{LP_primal_dual} can be decomposed into two
subproblems, restricted to the columns in $A_S$ and in $A_T$.

Thus, for most concepts and problems considered in this paper, we can focus on the \emph{non-separable} components of ${\cal M}(W)$.
The following characterization will turn out to be very useful, see e.g.
\cite[Theorem 5.2.5]{frankbook}.

\begin{prop}\label{prop:conn}
A matroid ${\cal M}=([n],{\cal I})$ is non-separable if and only if for 
any $i,j\in [n]$, there exists a circuit containing $i$ and $j$.
\end{prop}
