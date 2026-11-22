---
doc_id: arxiv-math-0309426v2
doc_title: "ELEMENTARY DIVISORS OF SPECHT MODULES"
section_id: sec-004-5-elementary-divisors-for-conjugate-partitions
section_title: "Elementary divisors for conjugate partitions"
section_number: 5
pages: 5-9
source_pdf: 0309426v2.pdf
source_sha256: f2aa01164d9f243c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.852
doc_brief: "ELEMENTARY DIVISORS OF SPECHT MODULES — 9 sections: Front matter; Introduction and statement of main; The Hecke algebra and permutation"
---
\label{SecConj}

Let $R = \Z[q,q^{-1}]$. Let $\lambda$ be a partition of $n$. In this
section we relate the Gram matrices $G(\lambda)$ and $G(\lambda')$. We
start with some mild generalizations of some results about Specht
modules which were proved by Dipper and James~\cite{DJ:reps} over a
field.

Recall that if $Y$ is a submodule of an $R$--free module $X$ then $Y$
is \textsf{pure} if the quotient module $X/Y$ is $R$-free.

\begin{Lemma}
\label{LemTr1}
Suppose that $\lambda$ is a partition. Then the Specht module
$S(\lambda)$ is a pure submodule of $M(\lambda)$. 
\end{Lemma}

\begin{proof}
Using the Dipper--James basis of $S(\lambda)$, and the basis
$\set{x_\lambda T_d|d\in\D_\lambda}$ of $M(\lambda)$, suitably ordered,
the matrix representing the embedding $S(\lambda)\lra M(\lambda)$
$\Z[q,q^{-1}]$-linearly becomes triangular with $1$s on the diagonal
\cite[Theorem~5.8]{DJ:reps}. 
\end{proof}

\begin{Corollary}
The map $M(\lambda)\lraa{\delta_\lambda}S(\lambda)^*$ is surjective.
\end{Corollary}

\begin{proof}
The map $\delta_\lambda$ is the composition of the map
$$M(\lambda)\; \lraiso \; M(\lambda)^*\; ;\;\;\; \xi\;\lramaps \;\<\xi, -\>_\lambda$$ 
with the dual of the inclusion map $S(\lambda)\lra M(\lambda)$. This
is surjective by (\ref{LemTr1}).
\end{proof}

Let $\alpha(\lambda) = \sum_{i\geq 1} (i-1)\lambda_i 
                     = \sum_{i\geq 1} \binom{\lambda'_i}{2}$. 
Note that $\alpha(\lambda)=\len(w_{0,\lambda'})$, where
$w_{0,\lambda'}$ is the unique length of longest element in
$\Sym_{\lambda'}$. The next lemma is well known; see, for example,
\cite[Prop.~2.2]{Takeuchi}. We include a proof for completeness.

Recall that automorphism $\#$, and the corresponding operation on the
module category of $\H$, were defined at the end of section~2.

\begin{Lemma}\label{hash}
We have $x_\lambda^\# = q^{\alpha(\lambda')} y_\lambda$ and 
$y_\lambda^\# = q^{-\alpha(\lambda')} x_\lambda$.
\end{Lemma}

\begin{proof}
As $\#$ is an involution the two equalities are equivalent, so we
prove only the first.  For any integer $i$, with $1\le i < n$, we have
$x_\lambda^\# T_i=(x_\lambda T_i^\#)^\# = -x_\lambda^\#$. Write
$x_\lambda^\# = \sum_{w\in \Sym_\lambda} a_w T_w$, for some
$a_w\in\Z[q,q^{-1}]$.  Comparing coefficients on both sides of the
equation $x_\lambda^\# T_i=-x_\lambda^\#$ shows that $a_{wr_i} = (-q)
a_w$ for each $w$ that has a reduced expression ending in $r_i$;
compare \cite[Cor.~1.7]{M:IHA}. Hence, $x_\lambda^\#$ is a scalar multiple of
$y_\lambda$. Then
$T_{w_{0,\lambda}}^\#=(-1)^{\len(w_{0,\lambda})}T_{w_{0,\lambda}}$
plus a linear combination of $T_v$ where $v\in\Sym_\lambda$ and
$\len(v)<\len(w_{0,\lambda})$. Therefore, comparing the coefficient of
$T_{w_{0,\lambda}}$ in $x_\lambda^\#$ and $y_\lambda$ gives the
result.
\end{proof}

Recall that $S(\lambda)=z_\lambda\H$, where 
$z_\lambda=x_\lambda T_{w_\lambda} y_{\lambda'}$. The importance of
$z_\lambda$, and the irreducibility of $S(\lambda)$ in the semisimple
case, follow from the following simple fact.

\begin{Point}\it{(Dipper--James~\cite[Lemma~4.1]{DJ:reps})}\label{vanishing}
Suppose that $w\in\Sym_n$. Then 
$$x_\lambda T_w y_{\lambda'}=\begin{cases}
       \pm q^a z_\lambda,&\If w\in\Sym_\lambda w_\lambda\Sym_{\lambda'},\\
                       0,&\Otherwise,
\end{cases}$$
for some integer $a$.
\end{Point}

The proof of this result amounts to the observation that
$\Sym_\lambda\cap w\Sym_{\lambda'}w^{-1}=\{1\}$ if and only if
$w\in\Sym_\lambda w_\lambda\Sym_{\lambda'}$. 

\begin{Lemma}[The Submodule Theorem]
\label{LemJST}
If $U$ is a pure submodule of $M(\lambda)$, then $S(\lambda)\ss U$ or $U\ss S(\lambda)^\perp$.
\end{Lemma}

\begin{proof}
For all $u\in U$, we have $u y_{\lambda'} = \alpha_u z_\lambda$ for some $\alpha_u\in\Z[q,q^{-1}]$ by (\ref{vanishing}). 

{\it Case $1$}: $\alpha_u = 0$ for all $u\in U$. Therefore, if $u\in U$ and
$h\in\H$ then we have $\<u,z_\lambda h\>_\lambda = \<u h^*
y_{\lambda'},x_\lambda T_{w_\lambda}\>_\lambda$, since $y_{\lambda'}^*
= y_{\lambda'}$. But $u h^*\in U$, so $u h^* y_{\lambda'}
= 0$ and $u\in S(\lambda)^\perp$. Hence, $U\ss S(\lambda)^\perp$.

{\it Case $2$}: $\alpha_u \neq 0$ for some $u\in U$. Now $U\ni u
y_{\lambda'} = \alpha_u z_\lambda$ implies $z_\lambda\in U$ since
$U\ss M^\lambda$ is a pure submodule. Therefore, $S(\lambda)\ss U$.
\end{proof}

Note that the right ideal $y_{\lambda'} T_{w_\lambda}^{-1} x_\lambda\H$ is isomorphic to $S(\lambda)^\#$ via $\xi\lramaps\xi^\#$. Composing left multiplication
by $y_{\lambda'} T_{w_\lambda}^{-1}$ with this isomorphism, and using
Lemma~\ref{hash}, we obtain a surjective $\H$-linear map
$$
M(\lambda)\; =\; x_\lambda \H \; \lraa{\theta_\lambda} \; S(\lambda')^\# \; ; \;\; x_\lambda h \; \lramaps \; z_{\lambda'}\,\cdot_\#\, h\; , 
$$
where $h\in\H$.

\begin{Lemma}
We have $\Kern\theta_\lambda = S(\lambda)^\perp$. This induces an isomorphism
$$
S(\lambda')^\#\;\lraisoa{\psi_\lambda}\;S(\lambda)^* \; ;\;\;\; z_{\lambda'}\,\cdot_\#\, h \;\lramaps\;\< x_\lambda h , -\>_\lambda \; ,
$$
where $h\in\H$.
\end{Lemma}

\begin{proof}
Both $\Kern\theta_\lambda$ and $S(\lambda)^\perp$ are pure submodules
of $M(\lambda)$.  Over $\Z[q,q^{-1}]$, both $S(\lambda')^\#$ and
$S(\lambda)^*$ are free of rank $n_\lambda$, so it suffices to prove
that $\Kern\theta_\lambda\ss S(\lambda)^\perp$. By (\ref{LemJST}) this
is equivalent to showing that $S(\lambda)\not\ss \Kern\theta_\lambda$.
So it is enough to show that $z_\lambda \theta_\lambda \neq 0$. 
The bilinear form $\<\ ,\ \>_{\lambda'}$ is associative, so
\begin{align*}
\<z_\lambda \theta_\lambda, x_{\lambda'}\>_{\lambda'}
& =  q^{-\alpha(\lambda)}\< z_{\lambda'} T_{w_{\lambda'}}^{-1} x_{\lambda'} , x_{\lambda'}\>_{\lambda'} \\
& =  q^{-\alpha(\lambda')}(\Sum_{w\in\Sym_{\lambda'}} q^{\len(w)})\<z_{\lambda'}, x_{\lambda'} T_{w_\lambda}^{-1}\>_{\lambda'}\; . \\
\end{align*}
Now, 
$z_{\lambda'} = \sum_{v\in\Sym_\lambda}(-q)^{-\len(v)} x_{\lambda'} T_{w_{\lambda'} v}$, where each $w_{\lambda'} v$ is a distinguished coset representative for 
$\Sym_{\lambda'}$. In contrast, $T_{w_\lambda}^{-1}$ is equal to
$T_{w_{\lambda'}}$ plus a linear combination of terms $T_u$, where
$u\in\Sym_n$ with $\len(u) < \len(w_{\lambda'})$. Thus
$\<z_{\lambda'}, x_{\lambda'} T_{w_\lambda}^{-1}\>_{\lambda'} 
       =\<x_{\lambda'} T_{w_{\lambda'}}, x_{\lambda'} T_{w_{\lambda'}}\>_\lambda 
       = q^{\len(w_{\lambda'})}$. 
Hence, $\<z_\lambda \theta_\lambda, x_{\lambda'}\>_{\lambda'} \neq 0$.

A comparison of the short exact sequences
$$
0\;\lra\;\Kern\theta_\lambda\;\lra\; M(\lambda) \;\lraa{\theta_\lambda}\; S(\lambda')^\# \;\lra\; 0 
$$
and 
$$
0\;\lra\; S(\lambda)^\perp\;\lra\; M(\lambda) \;\lraa{\delta_\lambda}\; S(\lambda)^*\;\lra\; 0
$$
yields the isomorphism $\psi_\lambda$.
\end{proof}

For each node $(i,j)\in [\lambda]$, we let 
$h_{i,j} = (\lambda_i - j) + (\lambda'_j - i)+1$ be the corresponding
hook length and set 
$h_{\lambda}(q) = \prod_{(i,j)\in [\lambda]} [h_{i,j}]_q$. The next
lemma follows from results of {Murphy} \cite{murphy:hecke}.

\begin{Lemma}\label{scalar}
We have $z_\lambda T_{w_\lambda}^{-1} z_\lambda = q^{n - \alpha(\lambda)} h_\lambda(q) z_\lambda$. 
\end{Lemma}

\begin{proof} For the purpose of this proof, we may assume $R = \Q(q)$. By 
\cite[p.~510--511]{murphy:hecke}, there exists an element 
$\Psi^*_{\t_\lambda}=T_{w_{\lambda'}}+\sum_{\len(v)<\len(w_{\lambda'})}r_v T_v\in\H$, 
for some $r_v\in R$, such that
\[
z_\lambda\Psi^*_{\t_\lambda}\; =\; q^{n - \alpha(\lambda) + \len(w_{\lambda'})} h_\lambda(q) E_\lambda\; ,
\]
where $E_\lambda$ is a primitive idempotent such that
$E_\lambda \H = z_\lambda\H = S(\lambda)$.  In particular 
$E_\lambda z_\lambda=z_\lambda$. (Note that $z_\lambda=z_{\lambda t}$ 
in Murphy's notation; see \cite[p.~496, p.~498]{murphy:hecke}.)

Note that $T_{w_\lambda}^{-1} = q^{-\len(w_\lambda)}T_{w_{\lambda'}} +
\sum_{\len(v) < \len(w_{\lambda'})} r_v T_v$, for some $r_v\in R$.
Now, if $\len(v)<\len(w_{\lambda'})$ then 
$v \not\in \Sym_{\lambda'} w_{\lambda'} \Sym_\lambda$, so
$y_{\lambda'} T_v x_\lambda =(x_{\lambda} T_v^* y_{\lambda'})^*= 0$ by
(\ref{vanishing}). Consequently,  $z_\lambda T_v z_\lambda = 0$.
Therefore,
\begin{xalignat*}{2}
z_\lambda T_{w_\lambda}^{-1}z_\lambda
   &= q^{-\len(w_\lambda)} z_\lambda T_{w_{\lambda'}} z_\lambda \\
   &= q^{-\len(w_\lambda)} z_\lambda \Psi^*_{\t_\lambda} z_\lambda \\
   &= q^{n - \alpha(\lambda)} h_\lambda(q) E_\lambda z_\lambda \\
   &= q^{n - \alpha(\lambda)} h_\lambda(q)  z_\lambda\; .
\end{xalignat*}
  
\end{proof}

Consider the $\H$-linear map
\[
S(\lambda)\;\lraa{\gamma_\lambda}\;S(\lambda)^\ast \; ;\;\;\; \xi\;\lramaps\;\< \xi , -\>_\lambda\; .
\]

\begin{Lemma}
\label{PropComp}
The composition
\[
S(\lambda)\;\lraa{\gamma_\lambda}\; S(\lambda)^\ast \;\lraisoa{\psi_\lambda^{-1}}\; S(\lambda')^\# \;\lraa{\gamma_{\lambda'}^\#}\; S(\lambda')^{\ast,\#} 
\;\;\lraisoa{(\psi_{\lambda'}^\#)^{-1}}\;\; S(\lambda)
\]
is equal to scalar multiplication by $(-q)^{\len(w_{\lambda'})} q^{n - \alpha(\lambda) - \alpha(\lambda')} h_\lambda(q)$.
\end{Lemma}

\begin{proof}
The element $z_\lambda$ is mapped via $\gamma_\lambda$ to $\< z_\lambda , -\>_\lambda$, which is mapped via 
$\psi_\lambda^{-1}$ to $z_{\lambda'}\,\cdot_\#\, T_{w_\lambda} y_{\lambda'} = z_{\lambda'} T_{w_\lambda}^\# y_{\lambda'}^\#$, which in turn
goes to $\< z_{\lambda'} T_{w_\lambda}^\# y_{\lambda'}^\# , -\>_\lambda$ via $\gamma_{\lambda'}^\#$, and finally to 
\[
\begin{array}{rcl}
z_\lambda\,\cdot_\#\, T_{w_{\lambda'}} y_\lambda T_{w_\lambda}^\# y_{\lambda'}^\#  
& = & (-q)^{\len(w_{\lambda'})} q^{-\alpha(\lambda')} z_\lambda T_{w_\lambda}^{-1} z_\lambda \vspace{1mm}\\
& = & (-q)^{\len(w_{\lambda'})} q^{n - \alpha(\lambda) - \alpha(\lambda')} h_\lambda(q) z_\lambda \\
\end{array}
\]
via $(\psi_{\lambda'}^\#)^{-1}$, by Lemma~\ref{scalar}.
\end{proof}

Let $I_m$ be the $m\times m$ identity matrix. Recall that
$n_\lambda=\#\Std(\lambda)$ is the dimension of the Specht module
$S(\lambda)$.

\begin{Proposition} 
\label{CorDiagbar}
Suppose that $\lambda$ is a partition of $n$.
\\\vspace*{-4mm}
\begin{itemize}
\item[(1)] There exist invertible matrices $A,B\in\GL_{n_\lambda}(\Z[q,q^{-1}])$ 
such that 
\[
G(\lambda)\cdot A \cdot G(\lambda')\cdot  B \; =\; h_\lambda(q)\cdot I_{n_{\lambda}}\; .
\] 
\item[(2)] $G(\lambda)$ is diagonalizable to the diagonal matrix $D$ if and only if $G(\lambda')$ is diagonalizable to the diagonal matrix $h_\lambda(q) D^{-1}$.
\item[(3)] $G(\lambda)$ is divisibly diagonalizable if and only if $G(\lambda')$ is divisibly diagonalizable. In this case, the product of the $i^\th$ 
elementary divisor of $G(\lambda)$ and the $(n_\lambda + 1 - i)^\th$ elementary divisor of $G(\lambda')$ is equal to $h_\lambda(q)$.
\end{itemize}
\end{Proposition}

Recall that elementary divisors are only well defined up to a unit in
$\Z[q,q^{-1}]$; the same is true of their product in (3).

\begin{proof}
(1) The $R$-linear map $\gamma_\lambda$ is represented by the matrix $G(\lambda)$ with respect to the Dipper--James basis and its dual basis. Thus
the assertion follows by (\ref{PropComp}).

(2) If $G(\lambda) = SDT$ with $S,T\in\GL_{n_\lambda}(\Z[q,q^{-1}])$ and $D\in\Z[q,q^{-1}]^{n_\lambda\times n_\lambda}$ is a diagonal matrix, then 
$G(\lambda') = A^{-1}T^{-1}(h_\lambda(q) D^{-1})S^{-1}B^{-1}$. Since $G(\lambda')$ has coefficients in $\Z[q,q^{-1}]$, so does $h_\lambda(q) D^{-1}$.

(3) Repeat the argument of (2). 
\end{proof}

We remark that all of the results in this section hold more generally
when the Hecke algebra $\H$ is defined over an integral domain $R$
such that $\H\otimes_R Q$ is semisimple, where $Q$ is the field of
fractions of $R$. (We need semisimplicity over~$Q$ only when we apply
Murphy's results in the proof of Lemma~\ref{scalar}.) In particular,
Proposition~\ref{CorDiagbar} holds when $R=F[q,q^{-1}]$ and $F$ is any
field. Notice that $G(\lambda)$ is always diagonalizable in this case
because $F[q,q^{-1}]$ is a principle ideal domain.
