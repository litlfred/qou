---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-012-51-perfect-balancing-w1
section_title: "Perfect balancing: *W=1"
section_number: 5.1
pages: 20-22
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
toc_source: outline
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.992
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance measures associated with linear spaces."
---
Let us now show that  $\kappa^*_A=1$ can be efficiently checked.
\begin{theorem}\label{thm:kappa-star-1}
There exists a strongly polynomial algorithm, that given a matrix $A\in\R^{m\times n}$, returns one of the following outcomes:
\begin{enumerate}[(a)]
\item \label{i:outcome_TU} 
A diagonal matrix $D\in{\bD}_n$ such that $\kappa_{AD}=1$ showing that $\kappa^*_A=1$. The algorithm also returns the exact value of $\kappa_A$.
Further, if $\ker(A)$ is a rational linear space, then we can select $D$ with integer diagonal entries that divide $\kd_A$.
\item \label{i:outcome_not_TU} The answer $\kappa^*_A>1$, along with a cycle of circuits $H$ such that $\kappa_A(H) > 1$.
\end{enumerate}
\end{theorem}
\begin{proof}
As noted above, we can assume without loss of generality that the matroid ${\cal M}(W)$ is non-separable, as we can reduce the problem to solving on all connected components separately.

We obtain estimates $\hat\Le_{ij}$ for every edge $(i,j)$ of the circuit ratio graph  using a circuit $C\in\circuits_W$ with $i,j\in C$. Assuming that $\Le^*_W=1$, \eqref{eq:hat-sandwich} implies that $\hat\kappa_{ij}=\kappa_{ij}$ holds and the rescaling factors $d_i$ must satisfy 
\begin{equation}\label{eq:kappa-d}
\hat\kappa_{ij}d_j=d_i\quad \forall i,j\in [n]\, . 
\end{equation}
If this system is infeasible, then using the circuits that provided the estimates $\hat\kappa_{ij}$, we can 
obtain a cycle  $H$ such that $\kappa_A(H)>1$, that is, outcome \ref{i:outcome_not_TU}. Let us now assume that \eqref{eq:kappa-d} is feasible; then it has a unique solution $d$ up to scalar multiplication.
We define $D\in\bD_n$ with diagonal entries $D_{ii}=d_i$. 

Since ${\cal M}(W)$ is non-separable, we can conclude that $\kappa^*_A=1$ if and only if $\kappa_{AD}=1$. By Theorem~\ref{thm:tu_iff_kappa_1}, this holds if and only if $A'=A_B^{-1} AD$ is a TU-matrix for any basis $B$.

We run Seymour's algorithm \cite{Seymour1980} for $A'$. If it confirms that $A$ is TU (certified by a construction sequence), then we return outcome \ref{i:outcome_TU}. In this case, $|g^C_j/g^C_i|$ is the same for any circuit $C$ with $i,j\in C$; therefore $\Le_{ij}=\hat\Le_{ij}$, and we can return $\Le_A=\max_{(i,j)\in E}\hat\Le_{ij}$.

Otherwise, Seymour's algorithm finds a $k\times k$ submatrix $T$ of $A'$ with $\det(T)\notin\{0,\pm1\}$. As in the proof of Proposition~\ref{prop:kappa-delta}, we can recover a circuit $C$ in $\circuits_{A'}=\circuits_{AD}$ with two entries $i,j\in C$ such that $|\bar g_j|\neq |\bar g_i|$ for the corresponding elementary vector $\bar g\in {\EE}(AD)$. Note that $\hat \Le_{ij} d_j=d_i$ for the rescaled estimates. Hence, the circuit $C'$ with $i,j\in C'$ used to obtain the estimate $\Le_{ij}$, together with $C$ certifies that $\Le^*_A>1$ as required for outcome \ref{i:outcome_not_TU}.

Finally, if $\ker(A)$ is a rational linear space and we concluded $\Le^*_A=1$, then let us select the solution $d_i$ to \eqref{eq:kappa-d} such that $d\in \Z^n$ and $\gcd(d)=1$. We claim that $d_i\divides\dot\kappa_W$ for all $i$. Indeed, let $k=\lcm(d)$. For each pair $i,j\in [n]$, $d_j/d_i = r/q$ for two integers $r,q\divides \kd_A$.
Hence, for any prime $p\in\primes$, $\nu_p(k)\le \nu_p(\kd_A)$, implying $k\divides\kd_A$. 
\end{proof}

Let $W\subseteq \R^n$ be a linear space such that ${\cal M}(W)$ is non-separable.
Recall from Theorem~\ref{thm:imbalance_triangle_inequality} that 
$\KK_{ij}^W\subseteq \KK_{ik}^W \cdot \KK_{kj}^W$ for all $i,j,k\in [n]$. We now characterize when equality holds for all triples.
\begin{prop}
\label{prop:reverse-kappa-1}
Let $W\subseteq \R^n$ be a linear space such that ${\cal M}(W)$ is non-separable. Then, the following are equivalent:
\begin{enumerate}[(i)]
\item\label{i:TU_equiv_i} $\Le^*_W=1$,
\item\label{i:TU_equiv_ii} $|\KK_{ij}^W|=1$ for all $i,j\in [n]$, 
\item\label{i:TU_equiv_iii}  $\KK_{ij}^W= \KK_{ik}^W \cdot \KK_{kj}^W$ holds for all distinct $i,j,k\in [n]$.
\end{enumerate}
\end{prop}
\begin{proof} 
\ref{i:TU_equiv_i} $\Leftrightarrow$ \ref{i:TU_equiv_ii}:
Consider any  rescaling  $D\in\bD_n$ with diagonal entries $d_i=D_{ii}$.
Then,  $\KK_{ij}^{DW}=\{1\}$, and $\KK_{ij}^{DW}=\frac{d_j}{d_i}\KK_{ij}^{W}$. Hence, if $\Le_{DW}=1$ for some $D\in\bD_n$, then  $\KK_{ij}^{DW}=\{1\}$ implying $|\KK_{ij}^W|=1$  for every $i,j\in [n]$. If $|\KK_{ij}^{W}|>1$ for some $i,j$, it follows that $\Le_{DW}\neq 1$ for any diagonal rescaling. 

\noindent \ref{i:TU_equiv_ii} $\Rightarrow$ \ref{i:TU_equiv_iii}: 
 We have $\KK_{ij}^W\subseteq \KK_{ik}^W \cdot \KK_{kj}^W$ by Theorem~\ref{thm:imbalance_triangle_inequality}. If all three sets are of size one, then equality must hold.

\noindent \ref{i:TU_equiv_iii} $\Rightarrow$ \ref{i:TU_equiv_i}: 
Let $i,j \in [n]$ arbitrary but distinct and let us define
 $$\Gamma_{ij} := \{\kappa(H) |\, \text{$H$ closed walk in $G$, $(i,j) \in E(H)$}\}\, .$$
 Note that either $\Gamma_{ij} = \{1\}$ or $\Gamma_{ij}$ is infinite as any cycle $H$ can be traversed multiple times to form a closed walk. Note that by (iii) we have for any $i,j \in [n]$ that
\begin{equation}
  \Gamma_{ij} \subseteq \bigcup  \Big\{\Pi_{(k,\ell) \in E(H)} \mathcal K_{k,\ell} |\, \text{$H$ closed walk in $G$, $(i,j) \in E(H)$}\Big\}
  = \mathcal K_{ij} \cdot\mathcal K_{ji}. 
\end{equation}
The set $\mathcal K_{ij} \cdot\mathcal K_{ji}$ is finite, implying that $\Gamma_{ij} = \{1\}$. This, together with Theorem~\ref{thm:circuit-min-max} gives \ref{i:TU_equiv_i}.
\end{proof}

A surprising finding by Lee \cite{Lee89,Lee90} is that if $\dot\kappa_W$ is an odd prime power, then $\kappa^*_W=1$ holds.\footnote{The statement in the paper is slightly more general, for $k$-adic subspaces with $k>2$; the proof is essentially the same.}
We first present a proof sketch following the lines of the one in \cite{Lee89,Lee90}.
We also present a second, almost self-contained proof,  relying only on basic results on TU matrices. \begin{theorem}[{Lee~\cite{Lee89,Lee90}}]\label{thm:kappa-star}
Each $W$ for which $\dot{\kappa}_W = p^\alpha$ where $p\in\primes$, $p>2$,  $\alpha\in \N$, then  $\kappa^*_W = 1$.
\end{theorem}

\begin{proof}
A theorem by Tutte \cite{Tutte1965} asserts that $W$ can be represented as the kernel of a unimodular matrix, i.e.\ $\kappa^*_W = 1$ or $W$ has a minor $W'$ such that $\circuits(W') \cong \circuits(U_2^4)$ where $U_2^4$ is the uniform matroid on four elements such that the independent sets are the sets of cardinality at most two. Here, a matroid minor corresponds to iteratively either deleting variables or projecting variables out. In the first case we are done, so let us consider the second case. Note that $W' \subset \R^4$ and by Lemma~\ref{lem:circuit_minors} we have that for all $i,j \in [4]$ we have that $\mathcal K_{ij}^{W'} \subseteq \mathcal K_{ij}^W$ and so in particular $\dot \kappa_{W'} = p^\beta$ for some $\beta \le \alpha$. An easy consequence of the proof of Proposition~\ref{prop:B_inverse} and the congruence $\circuits(W') \cong \circuits(U_2^4)$ is that $W'$ can be represented by $A'$, i.e.\ $\ker(A') = W'$ such that 
\begin{equation}
  A' = 
  \begin{bmatrix}
    1 & 0 & p^{\gamma_1} & p^{\gamma_2} \\
    0 & 1 & p^{\gamma_3} & p^{\gamma_4}
  \end{bmatrix}
\end{equation}  
for $\gamma_i \in \N \cup \{0\}$ and $i \in [4]$. Further, by $\circuits(W') \cong \circuits(U_2^4)$ and $\Delta_{A'} \divides \dot \kappa_{W'}$ (Proposition~\ref{prop:B_inverse}) we have that 
\begin{equation}
  \label{eq:p_alpha_contradiction}
  0 \neq \det\begin{pmatrix}
     p^{\gamma_1} & p^{\gamma_2} \\
     p^{\gamma_3} & p^{\gamma_4}
  \end{pmatrix} = p^{\gamma_1 + \gamma_4} - p^{\gamma_2 + \gamma_3} \divides p^\beta.
\end{equation}
It is immediate that \eqref{eq:p_alpha_contradiction} cannot be fulfilled for $p > 2$. 
\end{proof}

\begin{proof}[Alternative Proof of Theorem~\ref{thm:kappa-star}]
  Let $A \in \R^{m \times n}$ be such that $A = \ker(W)$ satisfying the properties in Proposition~\ref{prop:B_inverse} in basis form $A=(I_m|A')$; for simplicity, assume the identity matrix is in the first $m$ columns.
Let $G = \big([n], E(G)\big)$ be a directed multigraph associated with $A$ with edge set $E(G) = \bigcup_{k \in [m]} E_k(G)$ where $E_k(G) = \{(i,j) : A_{ki}A_{kj} \neq 0\}$. Further, define $\gamma\colon E(G) \to \R_+$ where for $e \in E_k$ we let $\gamma(e) = |A_{kj}/A_{ki}|$. For a directed cycle $C$ in $G$ we define $\gamma(C) := \prod_{e \in E(C)} \gamma(e)$.
\begin{claim}
All cycles $C$ in $G$ fulfill $\gamma(C) = 1$.
\end{claim}
\begin{proof}
For a contradiction, assume that there exists a cycle $C$ such that $\gamma(C) \neq 1$ and let $C$ be a shortest cycle with this property. Then $C$ has no chord $f \in E(G)$, as otherwise $C \cup \{f\}$ contains two shorter cycles $C_1, C_2$ such that $\gamma(C_1) \gamma(C_2) = \gamma(C) \neq 1$ and so in particular $\gamma(C_1) \neq 1$ or $\gamma(C_2) \neq 1$. This also means that the support of the corresponding submatrix $A_{I,J}$ of $A$ where $I := \{i \in [m] : E_i(G) \cap E(C) \neq 0\}$ and $J := V(C)$ is exactly the set of non-zeros of an incidence matrix of a cycle. We have that $\det(A_{I,J}) \neq 0$ as the corresponding cycle $C$ has $\gamma(C) \neq 1$. 
Recall the Leibniz determinant formula. As $A_{I,J}$ is supported on the incidence matrix of a cycle there exist only two bijective maps $\phi, \psi: I \to J$, $\phi \neq \psi$ such that $\prod_{i\in I}A_{i,\phi(i)} \neq 0 \neq \prod_{i \in I} A_{i, \psi(i)}$ is non-vanishing. One of the maps corresponds to traversing the cycle forward, the other corresponds to traversing it backwards. As all the entries of $A$ are powers of $p$ we therefore have that $0 \neq \det(A_{I,J}) = \pm p^\alpha \pm p^\beta $ for some $\alpha, \beta \in \N$. This contradicts Proposition~\ref{prop:B_inverse}\ref{part:subdet-p} for $p > 2$.
\end{proof}

The above claim implies the existence of a rescaling of rows and columns $\tilde A:= LAR$ where $L\in \bD_n$, $R \in \bD_m$ such that $\tilde A \in \{-1,0,1\}^{m \times n}$. If $\tilde A$ is TU, then we are done by Proposition~\ref{prop:kappa-delta} as now $\kappa_W^* =1$. Otherwise, we use a result by Gomory (see \cite{Camion1965} and \cite[Theorem 19.3]{SchrijverLPIP}) that states that any matrix $B$ with entries in $\{-1,0,1\}$ that is not totally unimodular has a submatrix $B'$ with $|\det(B')| = 2$. 
Let $I \subseteq [m]$ and $J \subseteq [n]$ such that $|\det(\tilde A_{I,J})| = 2$. Note that w.l.o.g.\ the diagonal entries of $L$ and $R$ are of the form $p^\alpha$ for some $\alpha \in \Z$. Therefore, $|\det(A_{I,J})| = \prod_{i \in I}L_{ii} \prod_{j \in J} R_{jj} |\det (\tilde A_{I,J})| = 2p^\beta$ for some $\beta \in \Z$. As $|\det(A_{I,J})| \in \N$ we must have $\beta \ge 0$ and  $2 \divides |\det(A_{I,J})|$. This again contradicts Proposition~\ref{prop:B_inverse}\ref{part:subdet-p} for $p > 2$.
\end{proof}
