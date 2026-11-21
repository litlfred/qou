---
doc_id: arxiv-0707.2340v2
doc_title: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS"
section_id: sec-009-32-hadamard-fischer-inequalities-and-gkk-matrice
section_title: "Hadamard-Fischer Inequalities and GKK-Matrices"
section_number: 3.2
pages: 15-17
source_pdf: 0707.2340v2.pdf
source_sha256: bf0f91277a5874ff
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.984
doc_brief: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS — We introduce the class of strongly Rayleigh probability measures by means of geometric properties of their generating polynomials that amount to"
---
\label{ss-gkk}

Given an $n\times n$ matrix $A$ over $\CC$ and $S\subseteq [n]$ denote
by $A[S]$ the principal submatrix of $A$ with rows
and columns indexed by $S$ and let $A\langle S\rangle=\det(A[S'])$ be the 
principal minor of $A$ with rows
and columns indexed by $S'=[n]\setminus S$, where 
$A\langle [n]\rangle=\det(A[\emptyset]):=1$. The matrix $A$ is called  a
$P$-{\em matrix} if all its principal minors are positive. A much studied 
class of $P$-matrices that unifies several important types of matrices is 
the class of $\GKK$-matrices, see \cite{FJ,HS} and references 
therein. 
A $P$-matrix $A$ is a $\GKK$-{\em matrix} (after Gantmacher-Krein and
Kotelyansky) if it satisfies the {\em
Hadamard-Fischer-Kotelyansky inequalities}, that is,
\begin{equation}\label{eq-HFK}
A\langle S\rangle A\langle T\rangle \ge A\langle S\cup T\rangle A\langle
S\cap T\rangle,\quad S,T\subseteq [n].
\end{equation}
In other words, an $n \times n$ $P$-matrix $A$  is $\GKK$ if and only if
the probability measure $\mu_A$ on $2^{[n]}$ defined by
\begin{equation}\label{meas-matrix} 
\mu_A(S)= A\langle S \rangle\det(A+I)^{-1}
\end{equation}
satisfies the negative lattice condition (NLC). It is not hard to see that the
generating polynomial of such a measure is
$$
g_{\mu_A}(z) = \det(A+I)^{-1}\sum_{S \subseteq [n]} A\langle S \rangle
z^S=\det(A+I)^{-1}\det(A+Z),\quad z^S:= \prod_{i \in S}z_i,
$$
where  $Z=\text{diag}(z_1,\ldots,z_n)$. Examples of $\GKK$-matrices are:
\begin{itemize}
\item[(I)] Positive definite matrices;
\item[(II)] Totally positive matrices, i.e., matrices for which {\em all}
minors are positive;
\item[(III)] Non-singular $M$-matrices; recall that an $M$-{\em matrix}
(named after Minkowski) is a matrix with all non-negative principal minors 
and all non-positive off-diagonal entries.
\end{itemize}

An ambitious project would be to classify $\GKK$-matrices according to
the various negative dependence properties (introduced in \S \ref{s2-plet}) 
that these matrices satisfy. This would take us beyond the scope of this 
paper. In what follows we will only briefly discuss some of these aspects.

\begin{definition}\label{d-mat-ral}
We say that a $P$-matrix $A$ is a {\em Rayleigh matrix} if the associated 
probability measure $\mu_A$ defined in \eqref{meas-matrix} is Rayleigh 
(in the sense of Definition~\ref{d1}).
\end{definition} 

By \cite[Theorem 4.4]{W}, 
Rayleigh matrices are $\GKK$. In fact, the following holds.

\begin{theorem}\label{R-matrix}
Let $A$ be an $n \times n$ matrix over $\CC$. The following are equivalent:
\begin{itemize}
\item[(1)] $A$ is a Rayleigh matrix;
\item[(2)] $A+X$ is a $\GKK$-matrix for all $X=\diag(x_1,\ldots, x_n)$,
where $x_i \geq 0$ for all $1\leq i \leq n$.
\end{itemize}
\end{theorem}

\begin{proof}
(1) $\Rightarrow$ (2): As we already noted, by \cite[Theorem~4.4]{W} 
Rayleigh matrices are $\GKK$ and by definition the set of all Rayleigh 
matrices is obviously closed under adding positive diagonal matrices.

(2) $\Rightarrow$ (1): Let $f=\det(A+Z)$. Then
\begin{eqnarray*}
&& \frac {\partial f} {\partial z_i}(x) \frac {\partial f} {\partial z_j}(x)
- \frac {\partial^2 f} {\partial z_i \partial z_j}(x) f(x) =\\
&& (A+X)\langle i \rangle \cdot (A+X)\langle j \rangle - (A+X)\langle i,j
\rangle \cdot (A+X)\langle\emptyset \rangle.
\end{eqnarray*}
Using the Hadamard-Fischer-Kotelyansky inequalities \eqref{eq-HFK} for $A+X$ 
with $S=\{i\}$ and $T=\{j\}$ one gets the desired conclusion.
\end{proof}

It follows immediately from  Theorem~\ref{R-matrix} that non-singular
$M$-matrices and positive definite matrices are Rayleigh. Now 
for any $s,t\in(0,1)$ one can easily check that the matrix 
\begin{equation}\label{b-mat}
B=
 \left[\begin{array}{ccc}
 1 & 1/2 & s/4 \\
 1/2 & 1 & 1/2 \\
 t/4 & 1/2 & 1 \\ \end{array} \right]
\end{equation}
 is totally positive.
Given an $n\times n$ matrix $A$ and two subsets $S, T \subseteq [n]$ of the
same size we let $A(S,T)$ denote the minor of $A$ lying in rows indexed by 
$S$ and columns indexed by $T$. It was proved by Gantmacher-Krein \cite{GK} 
and Carlson \cite{Ca}
that a  necessary and sufficient condition for a $P$-matrix to be $\GKK$
is that
$$
A(S,T)A(T,S) \geq 0\text{ for any }S,T \subseteq [n]\text{ with } 
|S|=|T|=|S\cup T|-1.
$$
Since
$$
(B+I)(12,23)= ( 1-2s)/4\text{ and } (B+I)(23,12)=(1-2t)/4
$$
we may choose $s,t\in (0,1)$ so that 
$(B+I)(12,23)(B+I)(23,12)<0$. We conclude that
for such values of $s,t$ the matrix  $B+I$ fails to be $\GKK$.

It is easy to see that the measures associated with positive definite and
totally positive matrices have $\ULC$ rank sequences. This follows from
Newton's inequalities and the fact that 
Hermitian matrices and totally positive matrices have real-rooted
characteristic polynomials (in the case of totally positive matrices this
goes back to Gantmacher and Krein \cite{GK}). For $M$-matrices it is not
as obvious but nonetheless true.
In \cite{HS} Holtz and Schneider conjectured that $M$-matrices satisfy the
conclusion of Conjecture~\ref{big}. This was subsequently confirmed by Holtz
in \cite{HM} using a certain monotonicity property for so-called
symmetrized Fischer 
products of $M$-matrices due to James-Johnson-Pierce \cite{JJP} (see 
\cite{BBS1} for further results on Fischer products).

We end this section with some open questions.

\begin{question}
Is $\mu_A$ an $\ULC$ measure whenever $A$ is a Rayleigh matrix?
\end{question}

\begin{question}
For which $\GKK$-matrices $A$ is $\mu_A$ negatively associated?
\end{question}

Again, negative association fails for measures associated with 
totally positive matrices. Indeed,
let $B$ be the totally positive $3\times 3$ matrix defined in \eqref{b-mat} 
and fix $s,t\in (0,1)$ such that $A:=B+I$ is not $\GKK$ (see the above 
discussion). 
It is known \cite{Ca,GK} that an $n \times n$
$P$-matrix $C$ is $\GKK$ if and only if
\begin{equation}\label{w-kot}
C\langle S \cup\{i\} \rangle \cdot C\langle S \cup\{j\} \rangle \geq
C\langle S \cup\{i,j\} \rangle \cdot C\langle S  \rangle
\end{equation}
for all $S \subseteq [n]$ and $i,j\in [n]\setminus S$ with $i\neq j$.  
Hence, since
$A$ fails to be $\GKK$ it follows that
\eqref{w-kot} fails for $A$ and some $S, i,j$. Unraveling the definitions 
this means that for some principal submatrix $B'$ of
$B$ the corresponding measure $\mu_{B'}$ will fail to have pairwise negatively
correlated variables (cf.~Definition~\ref{d-pnc}). In particular, since
NA $\Rightarrow$ p-NC, the measure $\mu_{B'}$ cannot be negatively 
associated. 

\begin{question}
Describe all $n\times n$ Rayleigh  matrices.
\end{question}

\begin{question}
Characterize the class of all real stable $n\times n$
matrices, that is,
$n\times n$ matrices $A$ such that $\det(A+Z)$ is real stable.
\end{question}
