---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-006-34-matrix-representations
section_title: "Matrix representations"
section_number: 3.4
pages: 12-13
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.989
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance measures associated with linear spaces."
---
\label{sec:matrix}

Proposition~\ref{prop:kappa-max} already tells us that  any rational matrix of the form $A=(I_m|A')$ is $1/\kd_A$-integral, and according to Lemma~\ref{lem:sub-inverse}, the inverse of every non-singular square submatrix of $A$ is also $1/\kd_A$-integral. It is natural to ask whether every linear subspace $W$ can be represented as $W=\ker(A)$ for an 
\emph{integer} matrix $A$ with the same property on the inverse matrices. 

We show that this is true if the dual space is \emph{anchored} but false in general. Recall that this means that every elementary vector $g^C$, $C\in\circuits_{W^\perp}$ has a $\pm 1$ entry. In particular, $\kd_W = p^\alpha$ for some prime number $p \in \primes$ implies that both $W$ and $W^\perp$ are anchored; in this case we also have $\kappa_W=\kd_W$. 

In \cite[Section 7]{Lee89}, it is shown that if $B$ is a basis minimizing $|\det(A_B)|$ for a full rank $A\in \R^{m\times n}$, then every nonzero entry in $A_B^{-1} A$ is at least 1 in absolute value. Moreover, a simple greedy algorithm is proposed (called \textsc{1-OPT}) that finds such a basis within $m$ pivots for $k$-adic spaces. Our next statement can be seen as the variant of this for anchored-spaces, using the lcm-circuit imbalance $\kd_A$.
We note that finding a basis minimizing $|\det(A_B)|$ is computationally hard in general \cite{khachiyan1995}.

\begin{prop} \label{prop:B_inverse}
  Let $W \subseteq \R^n, \dim(W) = n - m$ be a rational subspace such that $W^\perp$ is an  anchored space. Then there exists an integer matrix $A\in \Z^{m\times n}$ such that $\ker(A) = W$, and
  \begin{enumerate}[(i)]
    \item\label{part:norm-bound-p} All entries of $A$ divide $\kd_W$.
    \item\label{part:inverse-p} For all non-singular submatrices $M$ of $A$, $M^{-1}$ is $\frac{1}{\kd_W}$-integral.
    \item\label{part:subdet-p} $\dot\Delta_A$ is an integer divisor of $(\kd_W)^m$.
  \end{enumerate}
\end{prop}
\begin{proof}
  Let $\bar A \in \Q^{m\times n}$ be an arbitrary matrix with $\ker(\bar A) = W$. By performing row operations we can convert $\tilde A$ into $A = (D | A') \in \Z^{m \times n}$ where $D \in \bD_m$ is positive diagonal and $A' \in \Z^{m \times (n-m)}$ (after possibly permuting the columns). If $D=I_m$, then we are already done. Property~\ref{part:norm-bound-p} follows by Proposition~\ref{prop:kappa-max}; property~\ref{part:inverse-p}
 follows by Lemma~\ref{lem:sub-inverse}, and property~\ref{part:subdet-p} holds since $\det(M)\cdot\det(M^{-1})=1$, $\det(M)\in\Z$, and $\det(M^{-1})$ is $\frac{1}{(\kd_W)^m}$-integral.

  If $D$ is not the identity matrix, then we show that $A$ can be brought to the form $(I_m | A'')$ with an integer $A''$ by performing further basis exchanges. 
  Let  us assume that $\gcd(A^i) = 1$ for all rows $A^i$, $i \in [m]$.
By Lemma~\ref{lem:dual-circuit}, $A^i\in \EE(W^\perp)$.
Assume $D_{ii}=A_{ii}> 1$ for some $i\in [m]$.
  As $A^i$ is a circuit and $W^\perp$ is anchored, there exists an index $k \in [n]$ such that $|A_{ik}| = 1$.

Let us perform a basis exchange between columns $i$ and $k$. That is, 
subtract integer multiples of row $i$ from the other rows to turn column $k$ into $e_i$. We then swap columns $i$ and $k$ and obtain the matrix again in the form $(D'|A'')$. 
Notice that the matrix remains integral,  $D'_{ii}=1$, and $D'_{jj}=D_{jj}$ for $j\in [m]$, $j\neq i$. Hence, repeating this procedure at most $n$ times, we can convert the matrix to the integer form $(I_m|A')$, completing the proof.
\end{proof}
Note that the proof gives an algorithm to find such a basis representation using a Gaussian elimination and at most $m$ additional pivot operations.
If $W^\perp$ is not anchored, we show the following weaker statement.
\begin{prop} \label{prop:B_inverse_General}
  Let $W \subseteq \R^n, \dim(W) = n - m$ be a rational subspace. Then there exists an integer matrix $A\in\Z^{m\times n}$ with $\ker(A) = W$ such that
  \begin{enumerate}[(i)]
    \item\label{part:norm-bound} All entries of $A$ divide $\kd_W$;
    \item\label{part:inverse} For all non-singular submatrices $M$ of $A$, $M^{-1}$ is $\frac{1}{(\kd_W)^2}$-integral.
    \item\label{part:subdet} $\dot\Delta_A$ is an integer divisor of $(\kd_W)^{m}$.
  \end{enumerate}
\end{prop}
\begin{proof}
The proof is an easy consequence of Proposition~\ref{prop:kappa-max} and Lemma~\ref{lem:sub-inverse}. Consider any basis form $A=(I_m|A')$ with  $\ker(A)=W$ (after possibly permuting the columns). According to Proposition~\ref{prop:kappa-max},  all entries of $A$ are $1/\dot\kappa_W$ integral.
By Lemma~\ref{lem:dual-circuit}, the rows $A^i\in\EE(W^\perp)$ for $i\in [m]$. We can write $A^i=g^i/d_i$ for some  $g^i\in \EE(W^\perp)\cap \Z^m$ and $d_i\in \Q$ such that $\gcd(g^i)=1$ for each $i\in [m]$. By the definition of $\kd_A$, the entries of each $g^i$ are divisors of $\kd_A$. Since $A_{ii}=1$ it follows that $d_i\in \Z$ and $d_i\divides \kd_A$. Let $D\in\bD_m$ be the diagonal matrix with entries $D_{ii}=d_i$. Then, $\bar A=DA$ is an integer matrix where all entries divide $\kd_A$, proving \ref{part:norm-bound}.
Part~\ref{part:inverse} follows  by Lemma~\ref{lem:sub-inverse} and noting that the subdeterminants get multiplied by a submatrix $D^{-1}$.

For part~\ref{part:subdet}, let us start use a basis $B$ such that $|\det(A_B)|$ is \emph{maximal}; w.l.o.g. assume $B=[m]$. 
Then, in the basis form $(I_m|A')$ for $B$, all subdeterminants are $\le 1$. This holds as for any submatrix $M \in \Q^{k \times k}$ of $A'$ with $\det(M) \neq 0$ we have that augmenting the columns of $M$ by the columns $i \in B$ such that $i$ is not a row of $M$ results in a basis $B_M$ with $|\det(M)| = |\det\big((I_m | A')_{B_M}\big)| \le \det(I_m) = 1$ by assumption on $B$. After multiplying by $D$ as above, $\bar A=DA$, all subdeterminants will be $\le \det(D)\le (\kd_A)^m$.
\end{proof}
Note that parts~\ref{part:norm-bound} and \ref{part:inverse} are true for any choice of the basis form, whereas \ref{part:subdet} requires one to select $A_B$ with maximum determinant. The maximum subdeterminant is NP-hard even to approximate better than $c^m$ for some $c>1$ \cite{DiSumma2014}. However,
it is easy to see that even if we start with an arbitrary basis, then $\dot\Delta_A\divides(\kd_W)^{2m}$, since every subdeterminant of $A_B^{-1} A$ is at most $(\kd_W)^m$ follows by Lemma~\ref{lem:sub-inverse}.

We now give an example to illustrate why Proposition~\ref{prop:B_inverse}\ref{part:inverse-p} cannot hold for arbitrary values of $\kd_W$. The proof is given in the Appendix.
\begin{restatable}{prop}{counterex}\label{prop:counterexample}
Consider the matrix 
$$A = \begin{bmatrix} 1 & 3 & 4 & 3 \\ 0 & 13 & 9 & 10 \end{bmatrix}\, .$$
For this matrix
$\dot{\kappa}_A = 5850 = 2 \times 3^2 \times 5^2 \times 13$ holds, and 
there exists no $\tilde A\in\Z^{2\times 4}$ such that $\ker(\tilde A)=\ker(A)$ and the inverse of every nonsingular $2\times 2$ submatrix of $\tilde A$ is $1/5850$-integral.
\end{restatable}
