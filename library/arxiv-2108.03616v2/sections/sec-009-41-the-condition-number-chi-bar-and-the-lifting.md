---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-009-41-the-condition-number-chi-bar-and-the-lifting
section_title: "The condition number chi bar and the lifting operator"
section_number: 4.1
pages: 15-16
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
toc_source: outline
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 1.0
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance measures associated with linear spaces."
---
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
