---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-022-9-recovering-a-representation-from-its-ptolemy-c
section_title: "Recovering a representation from its Ptolemy coordinates"
section_number: 9
pages: 26-34
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
toc_source: outline
text_source: latex
latex_prose_ratio: 0.879
latex_coverage_ratio: 0.951
doc_brief: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — For a compact 3-manifold M with arbitrary (possibly empty) boundary, we give a parametrization of the set of conjugacy classes of"
---
\lbl{proofsection}


We now show that a Ptolemy assignment on $K$ determines a
generically decorated
boundary-unipotent representation, which is given explicitly in terms of the Ptolemy coordinates. 
The idea is that a Ptolemy assignment 
canonically determines a $(G,N)$-cocycle on $M$. 


\begin{definition} 
An $n\times n$ matrix $A$ is \emph{counter diagonal} if the only non-zero 
entries of $A$ are on the lower left to upper right diagonal, i.e.~$A_{ij}=0$ 
unless $j=n-i+1$. If $A_{ij}=0$ for $j>n-i+1$ (resp.~$j<n-i+1$), $A$ is 
\emph{upper} (resp.~\emph{lower}) \emph{counter triangular}.
\end{definition}

Given subsets $I,J$ of $\{1,\dots,n\}$, let $A_{I,J}$ denote the submatrix 
of $A$ whose rows and columns are indexed by $I$ and $J$, respectively. If 
$\Norm{I}=\Norm{J}$, let $\Norm A_{I,J}$ denote the minor $\det(A_{I,J})$.
Let $I^c$ denote $\{1,\dots,n\}\setminus I$. 




Recall that the adjugate $\Adj(A)$ of a matrix $A$ is the matrix whose 
$ij$th entry is $(-1)^{i+j}\Norm{A}_{\{j\}^c,\{i\}^c}$. It is well known that 
$\Adj(A)=\det(A)A^{-1}$. The following result by Jacobi 
(see e.g.~\cite[Section~42]{DeterminantBook}) expresses the minors of 
$\Adj(A)$ in terms of the minors of $A$.


\begin{lemma} 
Let $I,J$ be subsets of $\{1,\dots,n\}$ with $\Norm{I}=\Norm{J}=r$. We have
\begin{equation}\lbl{Jacobi}
\Norm{\Adj(A)}_{I,J}=(-1)^{\sum(I,J)}\det(A)^{r-1}\Norm{A}_{J^c,I^c},
\end{equation}

where $\sum(I,J)$ is the sum of the indices occurring  in $I$ and~$J$.\qed
\end{lemma}

\begin{definition} 
A matrix $A\in\GL_n(\C)$ is \emph{generic} if 
$\Norm{A}_{\{k,\dots,n\},\{1,\dots,n-k+1\}}\neq 0$ for all $k\in\{1,\dots,n\}$.
\end{definition}

Note that $A$ is generic if and only if the Ptolemy coordinates of $(N,AN)$ 
are non-zero. The following is a generalization of 
Zickert~\cite[Lemma~3.5]{ZickertDuke}.

\begin{proposition}
\lbl{xyqExistence} 
Let $A\in \GL_n(\C)$ be generic. There exist unique $x\in N$ and $y\in N$ 
such that $q=x^{-1}Ay$ is counter diagonal. The entries of $x$, $y$ and $q$ 
are given by
\begin{gather} 
q_{n,1}=A_{n,1}, \quad q_{n-j+1,j}=(-1)^{j-1}
\frac{\Norm{A}_{\{n-j+1,\dots,n\},\{1,\dots, j\}}}{\Norm{A}_{\{n-j+2,\dots,n\},\{1,\dots,j-1\}}} 
\text{ for }1<j\leq n\lbl{q}\\
x_{ij}=\frac{\Norm{A}_{\{i,j+1,\dots,n\},\{1,\dots,n-j+1\}}}{
\Norm{A}_{\{j,\dots,n\},\{1,\dots,n-j+1\}}} \text{ for $j>i$}\lbl{x}\\
y_{ij}=(-1)^{i+j}\frac{\Norm{A}_{\{n-j+2,\dots,n\},\{1,\dots,\widehat i,\dots,j\}}}{
\Norm{A}_{\{n-j+2,\dots,n\},\{1,\dots,j-1\}}} \text{ for $j>i$}\lbl{y}.
\end{gather}
\end{proposition}

\begin{proof}
It is enough to prove existence and uniqueness of $x$ and $y$ in $N$ such 
that $Ay$ and $x^{-1}A$ are upper and lower counter triangular, respectively. 
Suppose $Ay$ is upper counter triangular. Then the vector $y_{\{1,\dots,j-1\},\{j\}}$ 
consisting of the part above the counter diagonal of the $j$th column vector 
of $y$ must satisfy 
\begin{equation}A_{\{n-j+2,\dots,n\},\{1,\dots,j-1\}}y_{\{1,\dots, j-1\},\{j\}}
+A_{\{n-j+2,\dots,n\},\{j\}}=0.
\end{equation}





The existence and uniqueness of $y$, as well as the given formula for the entries, now follow from Cramer's rule.
Since $x^{-1}A$ is lower counter-triangular if and only if $A^{-1}x$ is upper counter-triangular, existence and uniqueness of $x$ follows. The explicit formula for the entries follows from Jacobi's identity~\eqref{Jacobi} and the formula for the entries of $y$. To obtain the formula for the entries of $q$, note that $q_{n-j+1,j}=(Ay)_{n-j+1,j}$. Hence, $q_{n,1}=A_{n,1}$, and for $1<j\leq n$,
\begin{align*}
q_{n-j+1,j}&=\sum_{i=1}^{j-1}A_{n-j+1,i}y_{i,j}+A_{n-j+1,j}\\&=\frac{\sum_{i=1}^{j}(-1)^{i+j}A_{n-j+1,i}\Norm{A}_{\{n-j+2,\dots,n\},\{1,\dots\widehat i,\dots,j\}}}{\Norm{A}_{\{n-j+2,\dots,n\},\{1,\dots,j-1\}}}\\&=(-1)^{j-1}\frac{\Norm{A}_{\{n-j+1,\dots,n\},\{1,\dots,j\}}}{\Norm{A}_{\{n-j+2,\dots,n\},\{1,\dots,j-1\}}},
\end{align*}
where the second equality follows from~\eqref{y}.
\end{proof}












For a generic matrix $A$, let $x_A$, $y_A$ and $q_A$ be the unique matrices provided by Proposition~\ref{xyqExistence}. Given cosets $g_{i}N$, $g_jN$, $g_kN$, define
\begin{equation}
\lbl{qandalpha}
q_{ij}=q_{g_i^{-1}g_j},\qquad \alpha^i_{jk}=(x_{g_i^{-1}g_j})^{-1}x_{g_i^{-1}g_k}.
\end{equation}

\begin{corollary}
\lbl{freeaction}
The diagonal left $G$-action on $C_k^{\gen}(G/N)$ is free when $k\geq 1$, and the chain complex $C_{*\geq 1}^{\gen}(G/N)\otimes_{\Z[G]}\Z$ computes relative homology.
\end{corollary}

\begin{proof}
By Proposition~\ref{xyqExistence}, every generic tuple $(g_0N,\dots,g_kN)$ may be uniquely written as
\begin{equation}
g_0x_{g_0^{-1}g_1}(N,q_{01}N,\alpha^0_{12}q_{02}N,\dots,\alpha^0_{1k}q_{0k}N).
\end{equation}
This proves that the $G$-action is free. Also note that for each generic tuple $(g_0N,\dots,g_kN)$, there exists a coset $gN$ such that $(gN,g_0N,\dots,g_kN)$ is generic. Hence, $C_{*\geq 1}^{\gen}(G/N)$ is acyclic, and is thus a free resolution of $\Ker(C_0(G/N)\to\Z$). This proves the result (see e.g.~Zickert~\cite[Theorem~2.1]{ZickertDuke}).
\end{proof}

A generic tuple $(g_0N,\dots,g_kN)$ determines a $(G,N)$-cocycle on a truncated simplex $\overline\Delta$, by labeling the long edges by $q_{ij}$ and the short edges by $\alpha^i_{jk}$ (see Figure~\ref{cocyclefigure}). In particular, a generically decorated representation $\rho$ determines a $(G,N)$-cocycle representing $\rho$. 

\begin{figure}[htpb]
$$
\psdraw{SLrepFigures.8}{2.3in}
$$
\caption{A $(G,N)$-cocycle on a truncated $3$-simplex.}\lbl{cocyclefigure}
\end{figure}

A $(G,N)$-cocycle $\tau$ coming from a generic tuple is called \emph{generic}. 
Letting $\overline B_*^{\gen}(G,N)$ be the subcomplex of $\overline B_*(G,N)$ generated by generic cocycles on a standard simplex, it follows that we have a canonical isomorphism
\begin{equation}
\overline B_*^{\gen}(G,N)=C_*^{\gen}(G/N)\otimes_{\Z[G]}\Z.
\end{equation} 
It now follows from Proposition~\ref{fundclassrepprop}, that the fundamental class can be represented as in \eqref{fundclassrep}. 

We wish to prove that a generic $(G,N)$-cocycle is uniquely determined by the Ptolemy coordinates.
\begin{notation}
Let $k\in\{1,\dots,n-1\}$.
\begin{enumerate}[(i)]
\item For $a_1,\dots,a_n\in\C^*$, let $q(a_1,\dots,a_n)$ be the counter-diagonal matrix whose entries on the counter-diagonal (from lower left to upper right) are $a_1,\dots ,a_n$.
\item For $x\in\C$, let $x_k(x)$ be the elementary matrix whose $(k,k+1)$ entry is $x$. 
\item For $b_1,\dots, b_k\in\C$, let $\pi_k(b_1,\dots,b_k)=x_1(b_1)x_2(b_2)\cdots x_k(b_k)$.
\end{enumerate}
\end{notation}








\begin{proposition}
\lbl{longedges} 
The long edges of a generic $(G,N)$-cocycle are determined by the Ptolemy coordinates as follows:
\begin{equation}
\lbl{qij}
q_{ij}=q(a_1,\dots,a_n),\qquad a_k=(-1)^{k-1}\frac{c_{(n-k)e_i+ke_j}}{c_{(n-k+1)e_i+(k-1)e_j}}.
\end{equation} 
\end{proposition}

\begin{proof} 
Let $(g_0N,\dots,g_kN)$ be a generic tuple, and let $A=g_i^{-1}g_j$. 
Then $q_{ij}=q_A$. Since 
\begin{equation}
\Norm{A}_{\{n-j+1,\dots,n\},\{1,j\}}=\det(\{g_i\}_{n-k},\{g_j\}_k)=c_{(n-k)e_i+ke_j},
\end{equation} 
the result follows from~\eqref{q}.
\end{proof}

The corresponding formula for the short edges requires considerable more work, and is given in Proposition~\ref{shortedgeformula} below. 

\begin{lemma} 
Let $A$ be generic, and let $L=x_A^{-1}A$.
The entries $L_{i,n-i+2}$ right below the counter diagonal are given by
\begin{equation}\lbl{belowcounterdiag}L_{i,n-i+2}=(-1)^{n-i}\frac{\Norm{A}_{\{i,\dots,n\},\{1,\dots,\widehat{n-i+1},n-i+2\}}}{\Norm{A}_{\{i+1,\dots,n\},\{1,\dots,n-i\}}}.
\end{equation}
\end{lemma}

\begin{proof}
We proceed as in the proof of Proposition~\ref{xyqExistence}. Let $x=x_A^{-1}$. Since $L$ is lower counter-triangular, we must have
\begin{equation}
x_{\{i\},\{i+1,\dots,n\}}A_{\{i+1,\dots,n\},\{1,\dots,n-i\}}+A_{\{i\},\{1,\dots,n-i\}}=0,
\end{equation}
so by Cramer's rule,
\begin{equation}
x_{ij}=(-1)^{i+j}\frac{\Norm{A}_{\{i,\dots,\widehat j,\dots,n\},\{1,\dots,n-i\}}}{\Norm{A}_{\{i+1,\dots,n\},\{1,\dots,n-i\}}}\text{ for }j>i.
\end{equation}
We thus have
\begin{align*}
\Norm{A}_{\{i+1,\dots,n\},\{1,\dots,n-i\}}L_{i,n-i+2}&=A_{i,n-i+2}\Norm{A}_{\{i+1,\dots,n\},\{1,\dots,n-i\}}\\&\hphantom{==}+\sum_{k=i+i}^n(-1)^{i+k}\Norm{A}_{\{j,\dots,\widehat k,\dots,n\},\{1,\dots,n-j\}}A_{k,n-i+2}\\&=\sum_{k=j}^n(-1)^{i+k}\Norm{A}_{\{j,\dots,\widehat k,\dots,n\},\{1,\dots,n-i\}}A_{k,n-i+2}\\&=(-1)^{n-i}\Norm{A}_{\{i,\dots,n\},\{1,\dots,\widehat{n-i+1},\dots,n-i+2\}},
\end{align*}
which proves the result.
\end{proof}

\begin{definition} 
Let $A,B\in\GL(n,\C)$. 
\begin{enumerate}[(i)]
\item $A$ and $B$ are related by a \emph{type $0$ move} if all but the last column of $A$ and $B$ are equal.
\item $A$ and $B$ are related by a \emph{type $1$ move} if all but the second last column of $A$ and $B$ are equal.
\item $A$ and $B$ are related by a \emph{type $2$ move} if for some $j<n-1$, $B$ is obtained from $A$ by switching columns $j$ and $j+1$. 
\end{enumerate}
\end{definition}




\begin{proposition}
\lbl{moveeffectonx} 
Let $A$ and $B$ be generic, and let $A_i$ and $B_i$ denote the $i$th column of $A$, resp.~$B$.
\begin{enumerate}[(i)]
\item If $A$ and $B$ are related by a type $0$ move, $x_B=x_A$.
\item If $A$ and $B$ are related by a type $1$ move, $x_B=x_Ax_1(x)$, where
\begin{equation}

x=-\frac{\det(A_1,\dots,A_{n-1},B_{n-1})\det(e_1,e_2,A_1,\dots,A_{n-2})}{\det(e_1,A_1,\dots,A_{n-1})\det(e_1,A_1,\dots,A_{n-2},B_{n-1})}.
\end{equation}
\item If $A$ and $B$ are related by a type $2$ move switching columns $j$ and $j+1$, $x_B=x_Ax_{n-j}(x)$, where
\begin{equation}
x=-\frac{\det(e_1,\dots,e_{n-j-1},A_1,\dots,A_{j+1})\det(e_1,\dots,e_{n-j+1},A_1,\dots,A_{j-1})}{\det(e_1,\dots,e_{n-j},A_1,\dots,A_j)\det(e_1,\dots,e_{n-j},A_1,\dots,A_{j-1},B_j)}.
\end{equation}
\end{enumerate}
\end{proposition}

\begin{proof}
The first statement follows from the fact that $x_A$ is independent of the last column of $A$.
Suppose $A$ and $B$ are related by a type $1$ move. Using \eqref{x}, one sees that $(x_A)_{ij}=(x_B)_{ij}$ except when $i=1$ and $j=2$. It thus follows that $x_B=x_Ax_1(x)$, where $x=(x_B)_{12}-(x_A)_{12}$. Letting $C$ be the matrix obtained from $A$ by replacing the $n$th column by the $(n-1)$th column of $B$, one has 
\begin{equation*}
\begin{gathered}
\Norm{A}_{\{1,3,\dots,n\},\{1,\dots,n-1\}}=\Adj(C)_{n,2},\quad \Norm{B}_{\{1,3,\dots,n\},\{1,\dots,n-1\}}=\Adj(C)_{n-1,2},\\
\Norm{A}_{\{2,\dots,n\},\{1,\dots,n-1\}}=\Adj(C)_{n,1},\quad \Norm{B}_{\{2,\dots,n\},\{1,\dots,n-1\}}=\Adj(C)_{n-1,1},
\end{gathered}
\end{equation*}
and it follows from~\eqref{x} that 
\begin{equation}\lbl{type1eq} x=(x_B)_{12}-(x_A)_{12}=\frac{\Adj(C)_{n-1,2}}{\Adj(C)_{n-1,1}}-\frac{\Adj(C)_{n,2}}{\Adj(C)_{n,1}}.
\end{equation}

We then have
\begin{align*}
x\Adj(C)_{n,1}\Adj(C)_{n-1,1}&=\Adj(C)_{n-1,2}\Adj(C)_{n,1}-\Adj(C)_{n-1,1}\Adj(C)_{n,2}\\&=-\Norm{\Adj(C)}_{\{n-1,n\},\{1,2\}}\\&=
-\det(C)\Norm{C}_{\{3,\dots,n\},\{1,\dots,n-2\}}\\&=-\det(A_1,\dots,A_{n-1},B_{n-1})\det(e_1,e_2,A_1,\dots,A_{n-2}),
\end{align*}
where the third equality follows from Jacobi's identity~\eqref{Jacobi}.
Since \begin{equation*}\Adj(C)_{n,1}\Adj(C)_{n-1,1}=\det(e_1,A_1,\dots,A_{n-1})\det(e_1,A_1,\dots,A_{n-2},B_{n-1}),\end{equation*} this proves the second statement. 

Now suppose $A$ and $B$ are related by a type $2$ move. Let $E_{j,j+1}$ be the elementary matrix obtained from the identity matrix by switching the $j$th and $(j+1)$th columns. Then $B=AE_{j,j+1}$. Since $L=x_A^{-1}A$ is lower counter triangular, $x_{n-j}(-\frac{L_{n-j,j+1}}{L_{n-j+1,j+1}})LE_{j,j+1}$ must also be lower counter triangular. We thus have
\begin{equation}
x_B=x_Ax_{n-j}(-\frac{L_{n-j,j+1}}{L_{n-j+1,j+1}})^{-1}=x_Ax_{n-j}(\frac{L_{n-j,j+1}}{L_{n-j+1,j+1}}).
\end{equation}
By \eqref{belowcounterdiag} and \eqref{q}, we have
\begin{equation}
\begin{aligned}
L_{n-j+1,j+1}&=(-1)^{j-1}\frac{\Norm{A}_{\{n-j+1,\dots,n\},\{1,\dots,\widehat j,j+1\}}}{\Norm{A}_{\{n-j+2,\dots,n\},\{1,\dots,j-1\}}}\\
L_{n-j,j+1}&=(-1)^j\frac{\Norm{A}_{\{n-j,\dots,n\},\{1,\dots,j+1\}}}{\Norm{A}_{\{n-j+1,\dots,n\},\{1,\dots,j\}}}.
\end{aligned}
\end{equation}
Hence,
\begin{align*}
\frac{L_{n-j,j+1}}{L_{n-j+1,j+1}}&=-\frac{\Norm{A}_{\{n-j,\dots,n\},\{1,\dots,j+1\}}\Norm{A}_{\{n-j+2,\dots,n\},\{1,\dots,j-1\}}}{\Norm{A}_{\{n-j+1,\dots,n\},\{1,\dots,j\}}\Norm{A}_{\{n-j+1,\dots,n\},\{1,\dots,\widehat j,j+1\}}}\\&=-
\frac{\det(e_1,\dots,e_{n-j-1},A_1,\dots,A_{j+1})\det(e_1,\dots,e_{n-j+1},A_1,\dots,A_{j-1})}{\det(e_1,\dots,e_{n-j},A_1,\dots,A_j)\det(e_1,\dots,e_{n-j},A_1,\dots,A_{j-1},B_j)},
\end{align*} 
proving the third statement.
\end{proof}

Note that any two matrices $A,B\in\GL(n,\C)$ are related by a sequence of moves of type $1$, $2$ and $0$ as follows:
\begin{equation}\lbl{movestring}
\begin{aligned}A\xrightarrow{1}&[A_1,\dots,A_{n-2},B_1,A_n]\xrightarrow{2}[A_1,\dots,A_{n-3},B_1,A_{n-2},A_n]\xrightarrow
{2}\dots\xrightarrow{2}\\&[B_1,A_1,\dots,A_{n-2},A_n]\xrightarrow{1}[B_1,A_1,\dots,A_{n-3},B_2,A_n]\xrightarrow{2}\dots\xrightarrow{2}\\&[B_1,B_2,A_1,\dots,A_{n-3},A_n]\xrightarrow{1,2}\dots\xrightarrow{1,2}[B_1,\dots,B_{n-1},A_n]\xrightarrow{0}B.
\end{aligned}
\end{equation}


Consider the tilings of a face ${ijk}$, $i<j<k$, of $\Delta^2_n$ by \emph{diamonds} shown in Figure~\ref{diamondfigure}. We refer to the diamonds as being of type $i$, $j$ and $k$, respectively. 
\begin{definition}\lbl{diamondcoordinates}
The \emph{diamond coordinate} $d^k_{r,s}$ of a diamond $(r,s)$ of type $k$ is the alternating product of the Ptolemy coordinates assigned to its vertices, see Figure~\ref{diamondfigure}.
\end{definition}
\begin{figure}[ht]
$$
\psdraw{SLrepFigures.9}{2in} \quad
\psdraw{SLrepFigures.10}{2in} \quad
\psdraw{SLrepFigures.11}{2in} 
$$
\caption{Diamonds of type $i$, $j$ and $k$. The diamond coordinates are $d^i_{r,s}=d^k_{r,s}=\frac{-ab}{cd}$, and $d^j_{r,s}=\frac{ab}{cd}$, where $a$, $b$, $c$, and $d$ are Ptolemy coordinates.}\lbl{diamondfigure}
\end{figure}














\begin{proposition}
\lbl{shortedgeformula} 
The short edges $\alpha^i_{jk}$, $j<k$, of a generic $(G,N)$-cocycle are determined by the Ptolemy coordinates as follows:
\begin{equation}\lbl{alphaijk}
\alpha^i_{jk}=\pi_{n-1}(d^i_{1,1},\dots,d^i_{1,n-1})\pi_{n-2}(d^i_{2,1},\dots,d^i_{2,n-2})\cdots \pi_1(d^i_{n-1,1}),
\end{equation}
where the $d^i_{j,k}$'s are the type $i$ diamond coordinates on the face $ijk$.
\end{proposition}

\begin{proof} 
Let $(g_0N,\dots,g_lN)$ be a generic tuple, and let $A=g_i^{-1}g_j$ and $B=g_i^{-1}g_k$.
We assume that $i<j<k$, the other cases being similar. Note that the Ptolemy coordinates on the $ijk$ face are given by 
\begin{equation}
c_{t_ie_i+t_je_k+t_ke_k}=\det(e_1,\dots,e_{t_i},A_1,\dots,A_{t_j},B_1,\dots,B_{t_k}).
\end{equation}
Performing the sequence of moves in \eqref{movestring}, the result follows from Proposition~\ref{moveeffectonx}. 
\end{proof}


\begin{corollary}
A generic tuple is determined up to the diagonal $G$-action by its Ptolemy coordinates.\qed
\end{corollary}

This result together with Proposition~\ref{longedges} shows that there is at most one generic $(G,N)$-cocycle with a given collection of Ptolemy coordinates. We now prove that the Ptolemy relations are the only relations among the Ptolemy coordinates when $k\leq 3$.

\begin{example} 
Suppose Ptolemy assignments on $\Delta^2_n$, $n\in\{2,3\}$, are given as in Figure~\ref{Ptolemyandassignment}. Using~\eqref{qij} and \eqref{alphaijk}, we obtain that the corresponding $(G,N)$-cocycle is given by


\begin{equation}
\begin{gathered}
q_{01}=q(a,-1/a),\quad q_{12}=q(b,-1/b),\quad q_{02}=q(c,-1/c),\\
\alpha^0_{12}=x_1\Bigl(\frac{-b}{ac}\Bigr),\quad \alpha^1_{02}=x_1\Bigl(\frac{c}{ab}\Bigr),\quad \alpha^2_{01}=x_1\Bigl(\frac{-a}{cb}\Bigr)
\end{gathered}
\end{equation}
when $n=2$, and
\begin{equation}
\begin{gathered}
q_{01}=q(c,-a/c,1/a),\quad q_{12}-q(b,-e/b,1/e),\quad q_{02}=q(f,-g/f,1/g),\\
\alpha_{02}^1=x_1\Bigl(\frac{fa}{cd}\Bigr)x_2\Bigl(\frac{d}{ab}\Bigr)x_1\Bigl(\frac{gb}{de}\Bigr),\\
\alpha^0_{12}=x_1\Bigl(\frac{-bc}{ad}\Bigr)x_2\Bigl(\frac{-d}{cf}\Bigr)x_1\Bigl(\frac{-ef}{dg}\Bigr),\quad \alpha_{01}^2=x_1\Bigl(\frac{-cg}{fd}\Bigr)x_2\Bigl(\frac{-d}{ge}\Bigr)x_1\Bigl(\frac{-ae}{db}\Bigr)
\end{gathered}
\end{equation}
when $n=3$.


\begin{figure}[ht]
$$
\psdraw{SLrepFigures.23}{1.4in}\hspace{2cm}
\psdraw{SLrepFigures.19}{1.4in}\hspace{2cm}
\psdraw{SLrepFigures.20}{1.4in}
$$
\caption{Ptolemy assignments and the corresponding cocycle for $n=2$ and $n=3$.}\lbl{Ptolemyandassignment}
\end{figure}
\end{example}




\begin{lemma}
\lbl{uniquefactorization}
Let $a_{i,j}$ and $b_{i,j}$ be non-zero complex numbers. The equality 
\begin{equation} \pi_{n-1}(a_{1,1},\dots,a_{1,n-1})\cdots \pi_1(a_{n-1,1})=\pi_{n-1}(b_{1,1},\dots,b_{1,n-1})\cdots \pi_1(b_{n-1,1})
\end{equation}
holds if and only if $a_{i,j}=b_{i,j}$ for all $i,j$.
\end{lemma}

\begin{proof}
For any $c_{i,j}$, the $n$th column of $\pi_{n-1}(c_{1,1},\dots,c_{1,n-1})\cdots \pi_1(c_{n-1,1})$ is equal to the $n$th column of $\pi_{n-1}(c_{1,1},\dots,c_{1,n-1})$, which equals
\[(\prod_{i=1}^{n-1} c_{1,i},\prod_{i=2}^{n-1}c_{1,i},\dots,c_{1,n-1}).\]
This proves that $a_{1,j}=b_{1,j}$ for all $j$. The result now follows by induction.
\end{proof}

\begin{proposition}
\lbl{reconstructtwotuple} 
For any assignment $c\colon\dot\Delta^2_n(\Z)\to\C^*$, there is a unique Ptolemy assignment $c\in Pt_2^n$ whose Ptolemy coordinates are $c_t$.
\end{proposition}

\begin{proof} 
We prove that the Ptolemy coordinates $c_t^\prime$ of $(N,q_{01}N,\alpha^0_{12}q_{02}N)$ equal $c_t$, where $q_{01}$, $q_{02}$ and $\alpha^0_{12}$ are given in terms of the $c_t$'s by \eqref{qij} and \eqref{alphaijk}. First note that $c_t=c^\prime_t$ if either $t_1$ or $t_2$ is $0$, i.e.~if $t$ is on one of the edges of $\Delta^2_n$ containing the $0$th vertex. 
Each of the other integral points $t$ is the upper right vertex of a unique diamond $(r,s)$ of type $0$.
Let $\tau_k$ be the upper right vertex of the $k$th diamond $D_k$ in the sequence
\begin{equation}
\lbl{diamondsequence}
(1,n-1),(1,n-2),\dots(1,1),(2,n-2),\dots,(2,1),\dots,(n-1,1).
\end{equation}
By Lemma~\ref{uniquefactorization}, $d^{0\prime}_{r,s}=d^0_{r,s}$ for all diamonds $(r,s)$ of type $0$. It thus follows that if $c_t=c^\prime_t$ for all but one of the vertices of a diamond $D$, then $c_t=c^\prime_t$ for all vertices of $D$. In particular $c^\prime_{\tau_1}=c_{\tau_1}$.
Suppose by induction that $c^\prime_{\tau_i}=c_{\tau_i}$ for all $i<k$. Then $c^\prime_t=c_t$, for all vertices of $D_k$ except $\tau_k$. Hence, we also have $c^\prime_{\tau_k}=c_{\tau_k}$, completing the induction.
\end{proof}

\begin{proposition}
\lbl{reconstructtriple} 
For any assignment $c\colon\\dot\Delta^3_n(\Z)\to\C^*$ satisfying the Ptolemy relations, there is a unique Ptolemy assignment $c\in Pt_3^n$ whose Ptolemy coordinates are $c_t$.
\end{proposition}

\begin{proof}
Let $c^\prime_t$ be the Ptolemy coordinates of the tuple $(N,q_{01}N,\alpha^0_{12}q_{02}N,\alpha^0_{13}q_{03}N)$ defined from the $c_t$'s by \eqref{qij} and \eqref{alphaijk}. We wish to prove that $c^\prime_t=c_t$ for all $t$. Note that if, for some subsimplex $\Delta^3(\alpha)$, $c^\prime_{\alpha_{ij}}=c_{\alpha_{ij}}$ for all but one of the $6$ $\alpha_{ij}$'s, then $c^\prime_{\alpha_{ij}}=c_{\alpha_{ij}}$ holds for all $\alpha_{ij}$. This is a direct consequence of the Ptolemy relations.
By Proposition~\ref{reconstructtwotuple}, $c^\prime_t=c_t$, when either $t_2$ or $t_3$ is zero.
Hence, for each $\alpha=(a_0,a_1,a_2,a_3)$ with $a_2=a_3=0$, $c^\prime_{\alpha_{ij}}=c_{\alpha_{ij}}$ except possibly when $(i,j)=(2,3)$. As explained above, $c^\prime_{\alpha_{23}}=c_{\alpha_{23}}$ as well. Now suppose by induction that $c^\prime_{\alpha_{ij}}=c_{\alpha_{ij}}$ for all $\alpha$ with $a_2+a_3<k$. Then $c^\prime_{\alpha_{ij}}=c_{\alpha_{ij}}$ holds except possibly when $(i,j)=(2,3)$. Again, $c^\prime_{\alpha_{23}}=c_{\alpha_{23}}$ must also hold, completing the induction. 
\end{proof}

A $(G,N)$-cocycle on $M$ obviously determines a decorated representation (up to conjugation). The main results of this section can thus be summarized by the diagram below.
\begin{equation}\label{summaryof1to1}
\xymatrix{\left\{\txt{Points in $P_n(K)$}\right\}\ar@{<->}[r]&\left\{\txt{Generic
$(G,N)$-cocycles\\on $M$}\right\}\ar@{<->}[r]&\left\{\txt{Generically decorated\\
$(G,N)$-representations}\right\}}
\end{equation}

\begin{remark}
We stress that the Ptolemy variety parametrizes decorated representations and \emph{not} decorated representations up to equivalence. In particular, the dimension of $P(K)$ depends on the triangulation, and may be very large if $K$ has many interior vertices. 
\end{remark}








\subsection{Obstruction cocycles and the $p\SL(n,\C)$-Ptolemy varieties}
\lbl{sub.obstruction}
Suppose $n$ is even. The projection $G\to pG$ maps $N$ isomorphically onto its image (also denoted by $N$), and by elementary obstruction theory (see e.g.~Steenrod~\cite{Steenrod}), the obstruction to lifting a $(pG,N)$-representation $\rho$ to a $(G,N)$-representation is a class in 
\begin{equation}
H^2(M,\partial M;\Z/2\Z)=H^2(K;\Z/2\Z).
\end{equation} 
We can represent it by an explicit cocycle in $Z^2(K;\Z/2\Z)$ as follows: Pick any $(p\SL(n,\C),N)$-cocycle $\bar\tau$ on $M$ representing $\rho$ and a lift $\tau$ of $\bar\tau$ to a $(G,N)$-cochain. Each $2$-cell of $K$ corresponds to a hexagonal $2$-cell of $M$, and the $2$-cocycle $\sigma\in Z^2(K;\Z/2\Z)$ taking a $2$-cell to the product of the $\tau$-labelings along the corresponding hexagonal $2$-cell of $M$ represents the obstruction class. 

\begin{proposition} 
Suppose the interior of $M$ is a $1$-cusped hyperbolic $3$-manifold with finite volume. The obstruction class in $H^2(K;\Z/2\Z)$ to lifting the geometric representation is non-trivial.
\end{proposition}

\begin{proof} 
By a result of Calegari~\cite[Corollary~2.4]{Calegari}, any lift of the geometric representation takes a longitude to an element in $\SL(2,\C)$ with trace $-2$. This shows that no lift is boundary-unipotent, so the obstruction class must be non-trivial.
\end{proof}

Proposition~\ref{xyqExistence} also holds in $p\SL(n,\C)$, and we thus have a $1$-$1$ correspondence between generically decorated representations and $(pG,N)$-cocycles on $M$.

\begin{definition} 
Let $\sigma\in Z^2(K;\Z/2\Z)$. A lifted $(pG,N)$ cocycle on $M$ with obstruction cocycle $\sigma$ is a generic $(G,N)$-assignment on $M$ lifting a $(pG,N)$-cocycle on $M$ such that the 2-cocycle on $K$ obtained by taking products along hexagonal faces of $M$ equals $\sigma$.
\end{definition}

A $1$-cochain $\eta\in C^1(K;\Z/2\Z)$ acts on a lifted $(pG,N)$-cocycle $\tau$ by multiplying a long edge $e$ by $\eta(e)$. Note that if $\tau$ has obstruction cocycle $\sigma$, $\eta\tau$ has obstruction cocycle $\delta(\eta)\sigma$, where $\delta$ is the standard coboundary operator.
Recall that there is a $1$-$1$ correspondence between generic $(G,N)$-cocycles on $M$ and points in the Ptolemy-variety.
We shall prove a similar result for $pG$.


We wish to define a coboundary action on $pG$-Ptolemy assignments (see Definition~\ref{pSLPtolemydefn}). Let $c$ be a $pG$-Ptolemy assignment on $\Delta$, and let $\eta_{ij}\in C^1(\Delta;\Z/2\Z)$ be the cochain taking the edge $ij$ to $-1$ and all other edges to $1$. Define
\begin{equation}\lbl{actiononPtolemys}
\eta_{ij} c\colon\dot\Delta^3_n(\Z)\to \C^*,\qquad (\eta_{ij}c)_t=(-1)^{t_it_j}c_t
\end{equation} 
and extend in the natural way to define $\eta c$ for a $pG$-Ptolemy assignment $c$ on $K$ and $\eta\in C^1(K;\Z/2\Z)$. A priori $\eta c$ is only an assignment of complex numbers to the integral points of the simplices of $K$. However, we have:
 
\begin{lemma}
\lbl{boundaryactiononPtolemy} 
If $c$ is a $pG$-Ptolemy assignment on $K$ with obstruction cocycle $\sigma$, $\eta c$ is a $pG$-Ptolemy assignment on $K$ with obstruction cocycle $\delta(\eta)\sigma$.
\end{lemma}

\begin{proof}
It is enough to prove this for a simplex $\Delta$ and for $\eta=\eta_{ij}$. Let $c^\prime=\eta_{ij}c$. We assume for simplicity that $ij=01$; the other cases are proved similarly. For any $\alpha=(a_0,a_1,a_2,a_3)\in \Delta^k_{n-2}(\Z)$, we then have
\begin{equation}\lbl{actionpreservesPtolemy}
c^\prime_{\alpha_{03}}c^\prime_{\alpha_{12}}+c^\prime_{\alpha_{01}}c^\prime_{\alpha_{23}}-c^\prime_{\alpha_{02}}c^\prime_{\alpha_{13}}=
(-1)^{a_0+a_1}(c_{\alpha_{03}}c_{\alpha_{12}}-c_{\alpha_{01}}c_{\alpha_{23}}-c_{\alpha_{02}}c_{\alpha_{13}})
\end{equation}
Let $\tau=\delta(\eta_{01})$. Since $\delta(\eta_{01})_2=\delta(\eta_{01})_3=-1$ and $\delta(\eta_{01})_0=1$, \eqref{actionpreservesPtolemy} implies that
\begin{equation}
\tau_2\tau_3c^\prime_{\alpha_{03}}c^\prime_{\alpha_{12}}+\tau_0\tau_3c^\prime_{\alpha_{03}}c^\prime_{\alpha_{01}}c^\prime_{\alpha_{23}}=c^\prime_{\alpha_{02}}c^\prime_{\alpha_{13}},
\end{equation}
as desired.
\end{proof}

\begin{definition}
\lbl{pSLdiamondcoordinates}
The diamond coordinates of a $p\SL(n,\C)$-Ptolemy assignment with obstruction cocycle $\sigma$ are defined as in Definition~\ref{diamondcoordinates}, but multiplied by the sign (provided by $\sigma$) of the face.
\end{definition}

Note that for $\eta\in C^1(K;\Z/2/\Z)$, the diamond coordinates of $c$ and $\eta c$ are identical.

\begin{proposition}
\lbl{pGcocyclesandPtolemy} 
For any $\sigma\in Z^2(K;\Z/2\Z)$, there is a $1$-$1$ correspondence between $p\SL(n,\C)$-Ptolemy assignments on $K$ with obstruction cocycle $\sigma$, and lifted $(p\SL(n,\C),N)$-cocycles on $M$ with obstruction cocycle $\sigma$. The correspondence preserves the coboundary actions.
\end{proposition}

\begin{proof}
It is enough to prove this for a simplex $\Delta$. For a $pG$-Ptolemy assignment $c$ on $\Delta$ with obstruction cocycle $\sigma\in Z^2(\Delta;\Z/2\Z)$, define a cochain $\tau$ on $\overline\Delta$ by the formulas~\eqref{qij} and \eqref{alphaijk} using the $\sigma$-modified diamond coordinates (Definition~\ref{pSLdiamondcoordinates}). Let $\eta\in C^1(\Delta;\Z/2\Z)$ be such that $\delta\eta=\sigma$, where $\delta$ is the standard coboundary map. By Lemma~\ref{boundaryactiononPtolemy} $\eta c$ satisfies the $\SL(n,\C)$ Ptolemy relations~\eqref{Ptolemyrelation}, and hence corresponds to an $(\SL(n,\C),N)$-cocycle $\tau^{\prime}$. Since the diamond coordinates of $c$ and $\eta c$ are the same, the short edges of $\tau^\prime$ agree with those of $\tau$ and the long edges differ from those of $\tau$ by $\eta$. This proves that $\tau$ is a lifted $(pG,N)$-cocycle with obstruction cocycle $\sigma$. The inductive arguments of Propositions~\ref{reconstructtwotuple} and \ref{reconstructtriple} show that this is a $1$-$1$ correspondence. The fact that the actions by coboundaries correspond is immediate from the construction.
\end{proof}

\begin{corollary}
\lbl{pGvariety}

Let $\sigma\in Z^2(K;\Z/2\Z)$. There is an algebraic variety
$P_n^\sigma(K)$ of generically decorated boundary-unipotent
representations $\rho\colon\pi_1(M)\to p\SL(n,\C)$ whose obstruction
class to lifting to $\SL(n,\C)$ is represented by~$\sigma$. Up to canonical
isomorphism, the variety
$P_n^\sigma(K)$ only depends on the cohomology class of~$\sigma$.
\end{corollary}

\begin{proof}
This follows immediately from Proposition~\ref{pGcocyclesandPtolemy}.
\end{proof}

Note that the canonical isomorphisms in Corollary~\ref{pGvariety} respect the extended Bloch group element. This follows from the $pG$ variant of Proposition~\ref{independenceoflog}. The analogue of~\eqref{summaryof1to1} is
\begin{equation}
\xymatrix{\left\{\txt{Points in $P^\sigma_n(K)$}\right\}\ar@{<->}[r]&\left\{\txt{Lifted
$(pG,N)$-cocycles on $M$\\with obstruction cocycle $\sigma$}\right\}\ar@{->>}[r]^{k:1}&\left\{\txt{Generically decorated\\
$(pG,N)$-representations\\with obstruction cocycle $\sigma$}\right\},}
\end{equation}
where $k$ is the number of lifts, i.e.~$k=\vert Z^1(K;\Z/2\Z)\vert$.


\subsection{Proof of Theorem~\ref{mainthmintro} and Theorem~\ref{mainthmpSLintro}}\label{Proofofmainthm}
Let $\rho\colon P_n(K)\to R_{G,N}(M)\big/\Conj$ be the composition of the map in~\eqref{summaryof1to1} with the forgetful map ignoring the decoration.  Let $c\in P_n(K)$. By Proposition~\ref{lambdaimageinBhat}, $\lambda(c)$ is in $\widehat\B(\C)$ and by Proposition~\ref{independenceofdec}, $\lambda(c)$ only depends on $\rho(c)$.  Commutativity of diagram~\eqref{mainthmdiag} follows from Remark~\ref{extensionremark}, and the fact that $\rho$ is surjective if $K$ is sufficiently fine follows from Proposition~\ref{barycentric}.
This concludes the proof of Theorem~\ref{mainthmintro}. The first part of Theorem~\ref{mainthmpSLintro} is proved similarly, and the last part follows from Theorem~\ref{Ptolemydetectsrhogeoproof} below.
