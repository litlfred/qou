---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-004-32-fractional-integrality-characterization
section_title: "Fractional integrality characterization"
section_number: 3.2
pages: 9-10
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.974
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance measures associated with linear spaces."
---
\label{sec:HK}

Hoffman and Kruskal \cite{Hoffman56} gave the following characterization of TU matrices. A polyhedron $P\subseteq \R^n$ is \emph{integral}, if all vertices (=basic feasible solutions) are integer.
\begin{theorem}[Hoffman and Kruskal, 1956]\label{thm:HK}
An integer matrix $A\in\Z^{m\times n}$ is totally unimodular if and only if for every $b\in\Z^m$
, the polyhedron $\{x\in \R^n:\, Ax\le b,x\ge 0\}$
 is integral.
\end{theorem}

Since $\kd$ is a property of the subspace, it will be more convenient to work with the standard equality form of an LP. Here as well as in Section~\ref{sec:delta}, we use the following straightforward correspondence between the two forms. Recall that an \emph{edge} of a polyhedron is a bounded one dimensional face; every edge is incident to exactly two vertices. The following statement is standard and easy to verify.

\begin{lemma}\label{lem:P-project}
Let $ A\in \R^{m\times n}$ be of the form $A=(A'|I_m)$ for $A'=\R^{m\times (n-m)}$. For a vector $b\in\R^m$, let 
\[P_b=\{x\in\R^n:\, Ax=b, x\ge 0\}\quad\mbox{and}\quad P'_b=\{x'\in\R^{n-m}:\, A'x'\le b, x'\ge 0\}\, .\]
 Let $I=[n-m]$ denote the index set of $A'$. Then,  $P'_b=\pi_I(P_b)$, i.e., $P'_b$ is the projection of $P_b$ to the coordinates in $I$.
For every vertex $x$ of $P_b$,  $x'=x_I$ is a vertex of $P'_b$, and conversely, for every vertex $x'$ of $P'_b$, there exists a unique vertex $x$ of $P$ such that $x_I=x'$. There is a one-to-one correspondence between the edges of $P_b$ and $P'_b$.
Further, if $b\in\Z^m$, then $P_b$ is $1/k$-integral if and only if $P'_b$ is $1/k$-integral.
\end{lemma}

Using Theorem~\ref{thm:tu_iff_kappa_1} and Lemma~\ref{lem:P-project}, we can formulate Theorem~\ref{thm:HK} in subspace language.
\begin{cor}
Let $W\subseteq\R^n$ be a linear space. Then, $\kappa_W=1$ if and only if for every $d\in \Z^n$, the polyhedron $\{x\in\R^n:\, x\in W+d, x\ge 0\}$ is integral.
\end{cor}
\begin{proof}
Let $n'=n-m=\dim(W)$.  W.l.o.g., assume the last  $m$ variables form a basis, and 
let us represent $W$ in a basis form as $W=\ker(A)$ for $A=(A'|I_m)$, where $A'\in\R^{m\times n'}$. It follows by Theorem~\ref{thm:tu_iff_kappa_1} that $\kappa_W=1$ if and only if $A$ is TU, which is further equivalent to $A'$ being TU.

Further, note that the system $\{x\in\R^n:\, x\in W+d, x\ge 0\}$  coincides with  $P_b=\{x\in\R^n:\, (A'|I_m)x=b, x\ge 0\}$, where $b=Ad$.

Note that  $b=Ad$ is integer whenever $d\in\Z^m$. Moreover, we can obtain every integer vector in $b\in\Z^m$ this way, since $A$ contains an identity matrix.
According to Lemma~\ref{lem:P-project}, $P_b$ is integral if and only if $P'_b=\{x\in \R^{n-m}:\, A'x'\le b, x'\ge 0\}$ is integral. The claim follows by Theorem~\ref{thm:HK}.
\end{proof}

We provide the following natural generalization. Related statements, although in substantially more complicated forms, were given in \cite[{Proposition 6.1 and 6.2}]{Lee89}.

\begin{theorem}\label{thm:kappa-HK}
Let $W\subseteq\R^n$ be a linear space. Then, $\dot\kappa_W$ is the smallest integer $k\in\Z$ such that for every $d\in \Z^n$,
the polyhedron $\{x\in\R^n:\, x\in W+d, x\ge 0\}$ is $1/k$-integral.
\end{theorem}
\begin{proof}  Let $\dim(W)=n-m$, and let us represent $W=\ker(A)$ for $A\in\R^{m\times n}$. Then, $x\in W+d$, $x\ge 0$ can be written as $Ax=Ad$, $x\ge 0$. 
Let $x$ be a basic feasible solution (i.e. vertex) of this system. Then, $x=A_B^{-1}Ad$. By Proposition~\ref{prop:kappa-max}, $A_B^{-1}A$ is $1/\kd_W$-integral. Thus, if $d\in \Z^n$ then $x$ must be also $1/\kd_W$-integral.

Let us now show the converse direction. Assume $\{x\in\R^n:\, x\in W+d, x\ge 0\}$ is $1/k$-integral for every $d\in\Z^n$. For a contradiction, assume there exists a circuit $C\in\circuits_W$ such that the entries of the elementary vector  are not all divisors of $k$ (or that $g^C$ is not even a rational vector if $W$ is not a rational space). In particular, select an index $\ell\in C$ such that $g^C_\ell\nmid k$, or such that $(1/g^C_\ell)g^C$is not rational.

 Let us select a basis $B\subseteq [n]$ such that $C\setminus B=\{\ell\}$. For simplicity of notation, let $B=[m]$. We can represent $W=\ker(A)$ in a basis form as $A=(I_m|A')$. Let $g\in\R^n$ be defined by $g_{\ell}=1$, $g_j=-A_{j\ell}$ for $j\in B$ and $g_j=0$ otherwise; thus, $g=(1/g^C_\ell)g^C$. 

Let us pick an integer $t\in\N$, $t\ge \|g\|_\infty$, and define $d\in\Z^n$ by $d_j=t$ for $j\in B$, $d_\ell=-1$, and $d_j=0$ otherwise. Then, the basic solution of $x\in W+d$, $x\ge 0$ corresponding to the basis $B$ is obtained as $x_j=t+g_j$ for $j\in B$ and $x_j=0$ for $j\in [n]\setminus B$. The choice of $t$ guarantees  $x\ge 0$. By the assumption, $x$ is $1/k$-integer, and therefore $g$ is also $1/k$-integer. Recall that $g=(1/g^C_\ell)g^C$, where either $g^C\in\Z^n$ with $\lcm(g^C)=1$ and $g^C_\ell\nmid k$, or $g$ is not rational. Both cases give a contradiction.
\end{proof}

Using again Lemma~\ref{lem:P-project}, we can write this theorem in a form similar to the Hoffman-Kruskal theorem. 

\begin{cor}\label{cor:HK-kappa}
Let $A=(A'|I_m)\in\R^{m\times n}$. Then, $\kd_A$ is the smallest value $k$ such that for 
 every $b\in\Z^m$, the polyhedron $\{x'\in \R^{n-m}:\, A'x'\le b,x'\ge 0\}$
 is $1/k$-integral.
\end{cor} 
Appa and Kotnyek \cite[Theorem 17]{Appa04} show that $k$-regularity of $A'$ (in the sense that the inverse of every square submatrix is $1/k$-integral) is equivalent to the property above. 

\paragraph{Subspaces with $\dot\kappa_A=2$}The case $\kd_W=2$ is a particularly interesting class. As already noted, it includes incidence matrices of undirected graphs, and according to Theorem~\ref{thm:kappa-HK}, it corresponds to half-integer polytopes. This class includes the following matrices, first studied by Edmonds and Johnson \cite{Edmonds1970}; the following result follows e.g. from \cite{Appa04,Gerards1986,Hochbaum1993}.
\begin{theorem}\label{thm:edmonds-johnson}
Let $A\in\Z^{m\times n}$ such that for each column $j\in [n]$, $\sum_{i=1}^m|A_{ij}| \leq 2$. Then $\dot{\kappa}_A\in \{1,2\}$. 
\end{theorem}

Appa and Kotnyek \cite{Appa04} define \emph{binet matrices} as $A'=A_B^{-1} A$ for a matrix $A$ as in Theorem~\ref{thm:edmonds-johnson} for a basis $B$. Clearly, these matrices have $\kd_{A'}\in \{1,2\}$ since they define the same subspace. 

Deciding whether a matrix has $\kd_A=2$ (or more generally, $\kd_A=k$ for a fixed constant $k$) is an interesting open question: is it possible to extend Seymour's decomposition~\cite{Seymour1980} from TU matrices? The matrices in Theorem~\ref{thm:edmonds-johnson} could be a natural building block of such a decomposition.
