---
doc_id: arxiv-2507.19896v1
doc_title: "Generalized Markov traces and Jucys-Murphy elements"
section_id: sec-009-markov-traces-via-jucys-murphy-elements
section_title: "Markov traces via Jucys-Murphy elements."
section_number: null
pages: 5-7
source_pdf: 2507.19896v1.pdf
source_sha256: a3f23d5a08b397ee
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 1.0
doc_brief: "Generalized Markov traces and Jucys-Murphy elements — We give a simple construction of Markov traces for Iwahori-Hecke algebras associated with infinite series of crystallographic Coxeter groups."
---
\label{sec:markov-traces-via-1}
\begin{definition}
\label{sec:markov-traces}  
Let $\mathcal{R}$ be a commutative $\mathcal{A}$-algebra. A family $(\phi_n)$ of $\mathcal{A}$-linear functionals $\phi_n: \He(X_n),$ where $X$ is $A_{-1}, B$ or $D$ and $n \in \mathbb{Z}_{\geq 1}$ ($n \in \mathbb{Z}_{\geq 2}$ in type $D$) is called a Markov trace if there are elements $\mu, \rho \in \mathcal{R}$ such that the following conditions are satisfied.
\begin{enumerate}
\myitem[.]{(M1)}\label{item:4} $\phi_n$ is a trace function, i.e. $\phi_n(hh') = \phi_n(h'h)$. This property is a generalization of the first Markov move from the theory of link invariants. 

  Recall the embedding $ \iota = \iota_{n-1}:\He(X_{n-1}) \to \He(X_n)$ defined in Section \ref{sec:full-twist-jucys}. The functionals $\phi_{n-1}$ and $\phi_n$, $n \geq 2$ must satisfy 
\myitem[.]{(U1)}\label{item:5} 
  \(   \phi_n(\iota(h)) = \rho \phi_{n-1}(h). \) This property is a generalization of a rule for removing an unlinked circle in the theory of link invariants.
\myitem[.]{(M2)}\label{item:6} 
  \(   \phi_n(\iota(h)t_n) = \mu \phi_{n-1}(h). \)
This property is a generalization of the second Markov move from the theory of link invariants.
\end{enumerate}

Note that if $(\phi_n)$ is a Markov trace with constants $\rho, \mu$,  then, for arbitrary $\lambda_1, \lambda_2 \in \mathcal{R}$, $(\lambda_1\lambda_2^n\phi_n)$ is again a Markov trace with constants $\lambda_2\rho, \lambda_2\mu$.

\begin{remark}
  We exclude small $n$ in our definition of the Markov trace because some special treatment is needed for the embeddings $B_0 \to B_1, D_0 \to D_1 \to D_2$. For the geometric traces these properties are extended to small $n$, see Section \ref{sec:geom-mark-trac}.
\end{remark}



\end{definition}
\begin{definition}
  Assume that the involution $v \mapsto v^{-1}$ is extended to $\mathcal{R}$. We say that an element $z \in \He(W,S) \otimes_\mathcal{A}\mathcal{R}$ represents a functional $\phi:\He(W,S) \to \mathcal{R}$ if $\phi(h) = \langle z, h\rangle$ for any $h \in \He(W,S)$. It is easy to see that $\phi$ satisfies the property \ref{item:4} if and only if $z$ is in the center of $\He(W,S)$. In this case we write $\phi = \tr_z$.
\end{definition}

Let $\mathcal{R} = \mathcal{A}(a)$ and let $\overline{a} = a^{-1}$. Define
\[
  \zeta_n = \prod_{i = 1}^{n} (1 + a^{-1}J^X_i), \zeta_0 = 1,
\]
an element in $\He(X_n)$ when $X = A_{-1}, B$ or $D$. By Corollary \ref{sec:jucys-murphy-central}, elements $\zeta_n$ are central in the corresponding Iwahori-Hecke algebras.  We prove 
\begin{theorem}
  \label{sec:markov-traces-via}
  The family of functionals $(\tr_{\zeta_n})$ is a Markov trace with constants $\rho = 1 + a, \mu = v-v^{-1}.$
\end{theorem}
\begin{proof}
  We first check the property \ref{item:5}. We have
  \[
    \langle \zeta_n, \iota(h)\rangle = \langle\zeta_{n-1}(1+a^{-1}J^X_n), \iota(h) \rangle = \langle \zeta_{n-1}, \iota(h)\rangle + a\langle\zeta_{n-1}J_n^X, \iota(h)\rangle. 
  \]
  Applying Proposition~\ref{sec:full-twist-jucys-1} twice --- recall that $J_n^X = \Se(X_n)^{-1}\Se(X_{n-1})$ --- we get the equality \(\langle\zeta_{n-1}J_n^X, \iota(h)\rangle = \langle\zeta_{n-1}, \iota(h)\rangle\) and \ref{item:5} follows.

  We now check the property \ref{item:6}. We have
   \begin{multline}
\label{eq:1}
\langle \zeta_n, \iota(h)t_n\rangle = \langle\zeta_{n-1}(1+a^{-1}J^X_n), \iota(h)t_n \rangle = \langle \zeta_{n-1}, \iota(h)t_n\rangle + a\langle\zeta_{n-1}J_n^X, \iota(h)t_n\rangle = \\
= \langle \zeta_{n-1}, \iota(h)t_n^{-1}\rangle +(v-v^{-1}) \langle \zeta_{n-1}, \iota(h)\rangle + a\langle\zeta_{n-1}J_n^X, \iota(h)t_n\rangle. 
\end{multline}
From Corollary \ref{sec:trace-funct-pair-1}, we get that
\(\langle\zeta_{n-1},\iota(h)t_n^{-1}\rangle = 0.\)

  For the third summand in the last expression in \eqref{eq:1}, applying Proposition \ref{sec:full-twist-jucys-1}, we have
  \[
    \langle\zeta_{n-1}J_n^X, \iota(h)t_n\rangle = \overline{\langle \iota(h)t_n,\zeta_{n-1}\Se(X_{n-1})\rangle} = 0,\]
with the last equality again following from Corollary \ref{sec:trace-funct-pair-1}. We obtain \ref{item:6}.
\end{proof}
\begin{remark}
 We will show below that, in types $A$ and $B$ (but not in type $D$), the traces $\tr_{\zeta_n}$ coincide with the traces coming from geometry. See Section \ref{sec:geom-mark-trac}.
\end{remark}
