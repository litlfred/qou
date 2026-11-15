---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-003-22-computation-of-twisted-reidemeister-torsion
section_title: "Computation of twisted Reidemeister torsion"
section_number: 2.2
pages: 4-6
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexand er polynomials of a 3–manifold associated to a representation of its fundam ental group."
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.925
---
\label{section:comptau}

Let $N$ be a 3--manifold with empty or toroidal boundary,  $\psi:\pi_1(N)\to F$ a non--trivial homomorphism to a free abelian group $F$
and $\gamma:\pi_1(N)\to \mbox{GL}(k,R)$  a representation.
In this section we will give an algorithm for computing $\tau(N,\gamma \otimes \psi)$ which is based on ideas of Turaev
(cf. in particular \cite[Theorem~2.2]{Tu01}).


We will first consider the case  that $N$ is closed.  We write $\pi=\pi_1(N)$.
We endow $N$ with  a CW--structure with one 0--cell, $n$ 1--cells, $n$ 2--cells and one $3$--cell.
It is well--known that such a CW--structure exists (cf. e.g. \cite[Theorem 5.1]{McM02} or \cite[Proof~of~Theorem~6.1]{FK06}).
Using this CW--structure we have the cellular chain complex
\[
0 \to C_3(\tilde{N}) \xrightarrow{\partial_3} C_2(\tilde{N})
\xrightarrow{\partial_2} C_1(\tilde{N}) \xrightarrow{\partial_1}
C_0(\tilde{N}) \to 0
\]
where $C_i(\tilde{N})\cong \mathbb{Z}[\pi]$ for $i=0,3$ and
$C_i(\tilde{N})\cong \mathbb{Z}[\pi]^n$ for $i=1,2$. Let $A_i,
i=1,2,3$  be the matrices over $\mathbb{Z}[\pi]$ corresponding to
the boundary maps $\partial_i:C_i\to C_{i-1}$  with respect to the
bases given by the lifts of the cells of $N$ to $\tilde{N}$. We can
arrange the lifts such that
 \[ \begin{array}{rcl} A_3 &=&
(1-g_1, 1-g_2, \ldots, 1-g_n)^t,\\
A_1 &=& (1-h_1, 1-h_2, \ldots, 1-h_n) \end{array} \]
with $g_1,\dots,g_n,h_1,\dots,h_n \in \pi$.
Note that $\{g_1,\dots,g_n\}$ and $\{h_1,\dots,h_n\}$
are generating sets for $\pi$ since $N$ is a closed 3--manifold. Since $\psi$ is non--trivial
there exist $r,s$ such that $\psi(g_r)\ne 0$ and $\psi(h_s)\ne 0$. Let $B_3$ be the $r$--th row of
$A_3$. Let $B_2$ be the result of deleting the $r$-th column and the $s$--th row from $A_2$. Let
$B_1$ be the $s$--th column of $A_1$.

Given a $p\times q$ matrix $B = (b_{rs})$  with entries in $\mathbb{Z}[\pi]$ we write $b_{rs}=\sum
b_{rs}^gg$ for $b_{rs}^g\in \mathbb{Z}, g\in \pi$. We then define $(\gamma \otimes \psi)(B)$ to be the $p\times
q$ matrix with entries
\[ \sum b_{rs}^g (\gamma \otimes \psi)(g)=\sum b_{rs}^g
\gamma(g)\cdot {\psi(g)}\in R[F]. \]
Since each such entry  is a $k\times k$ matrix with entries in $R[F]$ we can think of  $(\gamma \otimes \psi)(B)$ as a $pk\times qk$ matrix with entries in $R[F]$.

Now note that
\[ \det((\gamma \otimes \psi)(B_3))=\det(\mbox{id}-\gamma(g_r)\cdot {\psi(g_r)})\ne 0 \]
 since $\psi(g_r)\ne 0$. Similarly $\det((\gamma \otimes \psi)(B_1))\ne 0$.
 The following theorem is an immediate application of \cite[Theorem~2.2]{Tu01}.

\begin{theorem}\label{thm:Tu22}
We have
\[ \tau(N,\gamma \otimes \psi) \doteq \prod\limits_{i=1}^3 \det((\gamma \otimes \psi)(B_i))^{(-1)^{i}}.
\]
In particular, $H_*(N;Q(R[F])^k)=0$ if and only if
$\det((\gamma \otimes \psi)(B_2))\ne 0$.

\end{theorem}


We now consider the case  that $N$ has non--empty toroidal boundary.
Let $X$ be a CW--complex with the following two properties:
\begin{enumerate}
\item $X$ is simple homotopy equivalent to a CW--complex of $N$,
\item $X$ has one 0--cell, $n$ 1--cells and  $n-1$ 2--cells.
\end{enumerate}
It is well--known that such a CW--structure exists.
For example, if $N$ is the complement of a non--split link $L\subset S^3$, then we can take $X$
to be the 2--complex corresponding to a Wirtinger presentation of $\pi_1(S^3\setminus \nu L)$.

We now consider
\[
0 \to  C_2(\tilde{X})
\xrightarrow{\partial_2} C_1(\tilde{X}) \xrightarrow{\partial_1}
C_0(\tilde{X}) \to 0
\]
where $C_0(\tilde{X})\cong \mathbb{Z}[\pi]$,
$C_i(\tilde{X})\cong \mathbb{Z}[\pi]^n$ and $C_i(\tilde{X})\cong \mathbb{Z}[\pi]^{n-1}$.
Let $A_i, i=1,2$ over $\mathbb{Z}[\pi]$ be the matrices corresponding to
the boundary maps $\partial_i:C_i\to C_{i-1}$. As above we can arrange that
 \[
A_1 = (1-h_1, 1-h_2, \ldots, 1-h_n)  \] where $\{h_1,\dots,h_n\}$
is a  generating set for $\pi$. Since $\psi$ is non--trivial
there exists an $s$ such that $\psi(h_s)\ne 0$.  Let $B_2$ be the result of deleting the $s$--th row from $A_2$. Let
$B_1$ be the $s$--th column of $A_1$.
As above we have $\det((\gamma \otimes \psi)(B_1))\ne 0$.
 The following theorem is again an immediate application of \cite[Theorem~2.2]{Tu01}.

\begin{theorem}\label{thm:Tu22boundary}
We have \[ \tau(N,\gamma \otimes \psi) \doteq \prod\limits_{i=1}^2 \det((\gamma \otimes \psi)(B_i))^{(-1)^{i}}.
\]
In particular, we have $H_*(N;Q(R[F])^k)=0$ if and only if
$\det((\gamma \otimes \psi)(B_2))\ne 0$.

\end{theorem}



\subsection{Torsion invariants}\label{section:torsioninvariants}
Let $S$ be a Noetherian unique factorization domain
(henceforth UFD). Examples of Noetherian UFD's are given by $\mathbb{Z}$ and by fields,
furthermore if $R$ is a Noetherian UFD and $F$ a free abelian group, then $R[F]$ is again a Noetherian UFD.

For a finitely generated
$S$-module $A$ we can find a presentation
$$
S^r \xrightarrow{P} S^s \to A \to 0
$$
since $S$ is Noetherian. Let $i\ge 0$ and suppose $s-i\le r$. We
define $E_i(A)$, \emph{the $i$-th elementary ideal} of $A$, to be
the ideal in $S$ generated by all $(s-i)\times (s-i)$ minors of
$P$ if $s-i>0$ and to be $S$ if $s-i\le 0$. If $s-i > r$, we
define $E_i(A)= 0$. It is known that $E_i(A)$ does not depend on
the choice of a presentation of $A$ (cf. \cite{CF77}).


Since $S$ is a UFD there exists a unique smallest principal ideal
of $S$ that contains $E_0(A)$. A generator of this principal ideal
is defined to be the \emph{order of $A$} and denoted by $\mbox{ord}
(A)\in S$. The order is well-defined up to multiplication by a
unit in $S$. Note that  $A$ is  $S$-torsion if and only if
$\mbox{ord} (A) \ne 0$. For more details, we refer to \cite{Tu01}.
