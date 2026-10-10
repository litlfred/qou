---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-008-4-connections-to-other-condition-numbers
section_title: "Connections to other condition numbers"
section_number: 4
pages: 15-18
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.969
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance mea sures associated with linear spaces."
---
\label{sec:connections}
\subsection{The condition number \texorpdfstring{$\bar\chi$}{chi bar} and the lifting operator}
\label{subsec:lifting_operator}

For a full row rank matrix $A\in \R^{m\times n}$, the
 condition number $\bar\chi_A$ can be defined in the following two equivalent ways:
\begin{equation}
\begin{aligned}
\bar\chi_A&=\sup\left\{\left\|A^\top \left(A D A^\top\right)^{-1}AD\right\|\, : D\in
    \bD_n\right\}\\
&=\sup\left\{\frac{\norm{A^\top y}}{\norm{p}} :
\text{$y$ minimizes $\norm{D^{1/2}(A^\top y - p)}$ for some $0 \neq p \in \R^n$ and $D \in \bD_n$}\right\}.
\end{aligned}
\end{equation}
This condition number was first studied by Dikin \cite{dikin}, Stewart \cite{stewart}, and
Todd \cite{todd-90}. There is an
extensive literature on the properties and applications of $\bar\chi_A$,
as well as its
relations to other condition numbers. In particular, it plays 
a key role in layered-least-squares  interior point methods, see Section~\ref{sec:LLS}.  We refer the reader to
the papers \cite{ho2002,Monteiro2003,Vavasis1996} for further results
and references.

It is important to note that---similarly to $\kappa_A$ and $\dot\kappa_A$---$\bar\chi_A$ only depends on the subspace
$W=\ker(A)$. Hence, we can also write $\bar\chi_W$ for a subspace
$W\subseteq \R^n$, defined to be equal to $\bar\chi_A$ for some matrix
$A\in \R^{k\times n}$ with $W=\ker(A)$. We will use the notations $\bar\chi_A$ and
$\bar\chi_W$ interchangeably. The following characterization reveals the connection between $\kappa_A$ and $\bar\chi_A$.

\begin{prop}[\cite{Todd2001}]\label{prop:chibar}~
For a full row rank matrix $A\in \R^{m\times n}$, 
\[\bar\chi_A = \max\{ \|A_B^{-1} A\| : A_B \text{ is a non-singular $m \times m$-submatrix of } A\} \, .\]
\end{prop}
Together with Proposition~\ref{prop:kappa-max}, this shows that the difference between  $\bar\chi_A$ and $\kappa_A$ is in using $\ell_2$ instead of $\ell_\infty$ norm.
This immediately implies the upper bound and a slightly weaker lower bound in the next theorem.

\begin{theorem}[\cite{DHNV20,DadushNV20}]\label{theorem:kappa_chi_bar_approx}
For a matrix $A \in \R^{m \times n}$ we have $\sqrt{1 + \kappa_A^2} \le \bar\chi_A \le n\kappa_A$.
\end{theorem}

Approximating the condition number $\bar\chi_A$ is known to be hard; by the same token, $\bar\kappa_A$ also cannot be approximated by any polynomial factor. The proof relies on the hardness of approximating the minimum subdeterminant by Khachiyan \cite{khachiyan1995}.
\begin{theorem}[{Tun{\c{c}}el \cite{Tuncel1999}}]\label{thm:chi-inapprox}
  Approximating $\bar\chi_A$ up to a factor of $2^{\operatorname{poly}(n)}$ is NP-hard.
\end{theorem}

\medskip

In connection with $\bar\chi_A$, it is worth mentioning the  {\em lifting map}, a key concept in the algorithms presented in Section~\ref{sec:only-A}. The map 
$L_I^W : \pi_{I}(W) \to W$ lifts back a vector from a coordinate projection of $W$ to a minimum-norm vector in $W$:
\[
L_I^W(p) = \arg\min\left\{\|z\| : z_I = p, z \in W\right\}.
\]
Note that $L_I^W$ is the unique linear map from $\pi_{I}(W)$ to $W$ such that
$L_I^W(p)_I = p$ and $L_I^W(p)$ is orthogonal to $W \cap \R^n_{[n] \setminus
I}$. 
The condition number $\bar\chi_W$ can be equivalently defined as the maximum norm of any lifting map for an index subset.  
\begin{prop}[\cite{DHNV20,OLeary1990,stewart}]\label{prop:subspace-chi}
  For a linear subspace $W  \subseteq \R^n$,
  \[
  \bar{\chi}_W =\max\left\{ \|L_I^W\|\, : {I\subseteq [n]}, I\neq\emptyset\right\}\, .
  \]
\end{prop}

Even though $L_I^W$ is defined with respect to the $\ell_2$-norm, it can also be used to characterize $\kappa_W$.
\begin{prop}[\cite{DadushNV20}]\label{lem:kappa-lift}
For a linear subspace $W  \subseteq \R^n$,
\[
\kappa_W =\max\left\{ \frac{\|L_I^W(p)\|_\infty}{\|p\|_1}\, : {I\subseteq [n]}, I\neq\emptyset, p\in \pi_I(W)\setminus\{0\}\right\}\, .
\]
\end{prop}

\begin{proof}
We first show that for any $I\neq\emptyset$, and $p\in \pi_I(W)\setminus\{0\}$, $\|L_I^W(p)\|_\infty\le \kappa_W \|p\|_1$ holds. 
Let $z=L_I^W(p)$, and take a conformal decomposition $z=\sum_{k=1}^h g^k$ as in Lemma~\ref{lem:sign-cons}. For each $k\in [h]$, let $C_k=\supp(g^k)$. We claim that all these circuits must intersect $I$. Indeed, assume for a contradiction that one of them, say $C_1$ is disjoint from $I$, and let $z'=\sum_{k=2}^h g^k$. Then, $z'\in W$ and $z'_I=z_I=p$. Thus, $z'$ also lifts $p$ to $W$, but $\|z'\|_2<\|z\|_2$, contradicting the definition of $z=L_I^W(p)$ as the minimum-norm lift of $p$.

By the definition of $\kappa_W$, $\|g^k\|_\infty\le \kappa_W \|g^k_I\|_1$ for each $k\in [h]$. The claim follows since $p=z_I=\sum_{k=1}^h g^k_I$, moreover, conformity guarantees that $\|p\|_1=\sum_{k=1}^h \|g^k_I\|_1$. Therefore,
\[
\|z\|_\infty\le \sum_{k=1}^h \|g^k\|_\infty\le \kappa_W \sum_{k=1}^h \|g^k_I\|_1=\kappa_W\|p\|_1\, .\]
We have thus shown that the maximum value in the statement is at most $\kappa_W$. To show that equality holds, let $C\in\circuits_W$ be the circuit and $g^C\in W$ the corresponding elementary vector and $i,j\in C$ such that $\kappa_W=|g^C_j/g^C_i|$.

Let us set $I=([n]\setminus C)\cup \{i\}$, and define $p_k=0$ if $k\in [n]\setminus C$ and $p_i=g^C_i$. Then  $p\in \pi_I(W)$,  and the unique extension to $W$ is $g^C$; thus, $L_I^W(p)=g^C$. We have $\|L_I^W(p)\|_\infty=|g^C_j|$. Noting that $\|p\|_1=|g^C_i|$, it follows that 
$\kappa_W=\|L_I^W(p)\|_\infty/\|p\|_1$.
\end{proof}

\subsection{The condition number $\delta$ and bounds on diameters of polyhedra}\label{sec:delta}

Another related condition number is $\delta$, defined as follows:
\begin{Def}\label{def:delta}
Let $V\subseteq \R^n$ be a set of vectors. Then
$\delta_V$ is the largest value such that for any set of linearly independent vectors $\{v_i:\,  i\in I\}\subseteq V$ and $\lambda\in \R^I$,
\[
\left\|\sum_{i\in I}\lambda_i v_i\right\|\ge \delta_V \max_{i \in I} |\lambda_i| \cdot\|v_i\|\, .
\]
For a matrix $M\in\R^{m\times n}$, we let $\delta_M$ denote the value associated with the rows $M^1,M^2,\ldots,M^m$ of $M$.
\end{Def}
This can be equivalently characterized as follows: for a subset  $\{v_i:\,  i\in I\}\subseteq V$ and $v_j \in V$,  $v_j\notin W=\spn(\{v_i:\,  i\in I\})$,   the sine of the angle between the vector  $v_j$ and the subspace $W$ is at least $\delta_V$ (see e.g. for the equivalence \cite{Dadush-oracle}).

A line of work studied this condition number in the context of the simplex algorithm and diameter bounds. The \emph{diameter} of a polyhedron $P$ is the diameter of the vertex-edge graph associated with $P$; Hirsch's famous conjecture from 1957 asserted that the diameter of a polytope (a bounded polyhedron) in $n$ dimensions with $m$ facets is at most $m-n$. This was disproved by Santos in 2012 \cite{santos2012}, but the \emph{polynomial Hirsch conjecture}, i.e., a poly$(n,m)$ diameter bound remains wide open.

Consider the LP in standard inequality form with $n$ variables and $m$ constraints as 
\begin{equation}\label{LP:ineq}
\max \pr{c}{x}\, \st\,  x\in P\, ,\quad P=\{x\in \R^n:\, Ax\le b\}\, ,
\end{equation}
for $A\in \R^{m\times n}$, $b\in \R^m$.
Using a randomized dual simplex algorithm, Dyer and Frieze \cite{Dyer1994} showed the polynomial Hirsch conjecture for TU matrices. Bonifas et al.~\cite{Bonifas2014} strengthened and extended this to the bounded subdeterminant case, showing a diameter bound of $O(n^4\Delta_A^2 \log(n\Delta_A))$ for integer constraint matrices $A\in\Z^{m\times n}$. Note that this is independent of the number of constraints $m$.

Brunsch and R\"oglin \cite{brunsch2013} analyzed the shadow vertex simplex algorithm in terms of the condition number $\delta_A$, noting that for integer matrices $\delta_A\ge 1/(n\Delta_A^2)$. They gave a diameter bound $O(mn^2/\delta^2_A)$.
 Eisenbrand and Vempala \cite{eisenbrand2017} used a different approach to derive a bound poly$(n,1/\delta_A)$ that is independent of $m$.  Dadush and H\"ahnle \cite{dadush2016shadow} further improved these bounds to $O(n^3\log(n/\delta_A)/\delta_A)$.

 In recent work, Dadush et al.~\cite{Dadush-oracle} considered \eqref{LP:ineq} in the oracle model, where for each point $x\in \R^n$, the oracle returns $x\in P$ or a violated inequality $\pr{a_i}{x}\le b_i$ from the system $Ax\le b$. Their algorithm finds exact primal and dual solutions using $O(n^2\log(n/\delta_M))$ oracle calls, where 
 $M=\begin{pmatrix}\mathbf{0}& 1\\
A & b
\end{pmatrix}$; the running time is independent of the cost function $c$. They also show the following relation between $\kappa$ and $\delta$:

\begin{lemma}[{\cite{Dadush-oracle}}]\label{lem:delta-kappa}
\begin{enumerate}[(i)]
\item \label{i:delta-kappa-part-i} Let $A\in\R^{m\times n}$ be a matrix with full row rank and $m<n$, 
with $\|a_i\|=1$ for all columns $i\in[n]$. Then, $\kappa_A\le{1}/{\delta_{A^\top}}$. 
\item \label{i:delta-kappa-part-ii}Let $A\in\R^{m\times n}$ be in basis form  $A=(I_m|A')$. Then,
${1}/{\delta_{A^\top}}\le m\kappa_A^2$.
\item\label{i:m-kappa} If $B$ is the basis maximizing $|\det(A_B)|$, then  for $\bar A=A_B^{-1}A$, it holds that ${1}/{\delta_{\bar A^\top}}\le m\kappa_A$.
\end{enumerate}
\end{lemma}
\begin{proof}
{\bf Part \ref{i:delta-kappa-part-i}:} Let  $g\in\EE(A)$ be an elementary vector. Select an arbitrary $i\in \supp(g)$, and let $J=\supp(g)\setminus \{i\}$. Then, the columns $\{g_i:\,  i\in J\}$ are linearly independent, and $-g_i a_i=\sum_{j\in J} g_j a_j$. Thus,
\[
|g_i|\cdot\|a_i\|=\left\|\sum_{j\in J} g_j a_j\right\|\ge \delta_{A^\top} \max_{j\in J} |g_j|\cdot\|a_j\|\, ,
\]
and using that all columns have unit norm, we get $|g_j/g_i|\le 1/\delta_{A^\top}$ for all $j\in J$. This shows that $\kappa_{A}\le 1/\delta_{A^\top}$.

\paragraph{Parts \ref{i:delta-kappa-part-ii} and \ref{i:m-kappa}:} Let $A=(I_m|A')$ in basis form, and let $\alpha=\max_{i\in [n]} \|A_i\|$. Let us first show 
\begin{equation}\label{eq:delta-kappa-alpha}
{1}/{\delta_{A^\top}}\le \sqrt{m}\alpha \kappa_A\, .\end{equation}
 Take any set $\{A_i:\, i\in I\}$ of linearly independent columns of $A$, along with coefficients $\lambda\in \R^I$. Without loss of generality, assume $|I|=m$, i.e., $I$ is a basis, by allowing $\lambda_i=0$ for some coefficients. Let $z=\sum_{i\in I}\lambda_i A_i$. Then, $\lambda=A_I^{-1} z$. Lemma~\ref{lem:sub-inverse} implies that every column of $A_I^{-1}$ has 2-norm at most $\sqrt{m}\kappa_A$. Hence, $|\lambda_i|\le \sqrt{m}\kappa_A \|z\|$ holds for all $i\in I$, implying \eqref{eq:delta-kappa-alpha}.

 Then, part \ref{i:delta-kappa-part-ii} follows since $\|A_i\|\le \sqrt{m}\kappa_A$ by Proposition~\ref{prop:kappa-max}. For part \ref{i:m-kappa}, let  $B$ be a basis maximizing $|\det(A_B)|$. Then, $\|A_B^{-1} A\|_\infty\le 1$. Indeed, if there is an entry $|A_{ij}|>1$, then we can obtain a larger determinant by exchanging $i$ for $j$. This implies $\alpha\le \sqrt{m}$.
\end{proof}

Using this correspondence between $\delta$ and $\Le$, we can derive the following bound on the diameter of polyhedra in standard form from \cite{dadush2016shadow}. This verifies the polynomial Hirsch-conjecture whenever $\kappa_A$ is polynomially bounded.

\begin{theorem}\label{thm:kappa-diameter}
Consider a polyhedron in the standard equality form 
\[P=\{x\in\R^n:\, Ax=b, x\ge 0\}\]
for $A\in\R^{m\times n}$ and $b\in \R^m$. Then, the diameter of $P$ is at most  $O((n-m)^{3} m \kappa_{A}$ $\log(\kappa_{A}+n))$.
\end{theorem}
\begin{proof}
Without loss of generality, we can assume that $A$ has full row rank. Changing to a standard basis representation does neither change the geometry (in particular, the diameter) of $P$, nor the value of $\kappa_A$.
Let $B$ be the basis maximizing $\det(A_B)$, and let us replace $A$ by $A_B^{-1} A$; w.l.o.g. assume that $B$ is the set of the last $m$ columns.
 Hence, $A=(A'|I_m)$ for $A'\in \R^{m\times (n-m)}$. 
According to Lemma~\ref{lem:P-project}, $P$ has the same diameter as $P'$ defined as
\[P'=\{x'\in\R^{n-m}:\, A'x'\le b, x'\ge 0\}\, ,\]
in other words, $P'=\{x'\in\R^{n-m}:\, Cx'\le d\}$, where $C={-I_{n-m}\choose A'}$ and $d={0 \choose b}$. There is a one-to-one correspondence between the vertices and edges of $P$ and $P'$, and hence, the two polyhedra have the same diameter.
Thus, \cite{dadush2016shadow} gives a bound $O((n-m)^3\log(n/\delta_C)/\delta_C)$ on the diameter of $P'$.
By the choice of $B$, from Lemma~\ref{lem:delta-kappa}\ref{i:m-kappa}, we obtain the diameter bound
 $O((n-m)^{3}m\kappa_{C^\top}$ $\log(\kappa_{C^\top}+n))$.
We claim that $\kappa_{C^\top}=\kappa_A$. Indeed, the kernels of $A=(A'|I_m)$ and $C^\top=(-I_{n-m}|(A')^\top)$ represent orthogonal complements, thus $\kappa_{C^\top}=\kappa_A$ by Proposition~\ref{prop:kappa-dual}. This completes the proof.
\end{proof}

The diameter bound in \cite{dadush2016shadow} is proved constructively, using the shadow simplex method. However, in the proof we choose $B$ maximizing $|\det(A_B)|$, a hard computational problem to solve even approximately \cite{DiSumma2014}. 
However, we do not actually require a (near) maximizing subdeterminant. For the argument, we only need to find a basis $B\subseteq [n]$ such that for $\bar A=A_B^{-1}A$, $\|\bar A\|_\infty\le \mu$ for some constant $\mu>1$. 
Then,  \eqref{eq:delta-kappa-alpha}, gives $1/\delta_{\bar A^\top}\le m\mu\kappa_A$.

Such a basis $B$ corresponds to  approximate local subdeterminant maximization, and 
 can be found using the following simple algorithm proposed by Knuth \cite{Knuth1985}. As long as there is an entry $|A_{ij}|>\mu$, then swapping $i$ for $j$ increases $|\det(A_B)|$ by a factor $|A_{ij}|>\mu$. 
Using that $|\det(A_B)|\le (\kd_W)^m$ by Proposition~\ref{prop:B_inverse_General}, the algorithm terminates in $O(m\log(\kd_W/\mu))$ iterations.

We also note that $\delta_A$ was also studied  for lattice basis reduction by Seysen \cite{seysen1993}. A related quantity has been used to characterize Hoffman constants (introduced in Section~\ref{sec:hoffman}), see \cite{Guler1995,Klatte1995,Pena2020}.
