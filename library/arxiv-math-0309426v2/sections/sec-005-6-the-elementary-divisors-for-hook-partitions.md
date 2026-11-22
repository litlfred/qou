---
doc_id: arxiv-math-0309426v2
doc_title: "ELEMENTARY DIVISORS OF SPECHT MODULES"
section_id: sec-005-6-the-elementary-divisors-for-hook-partitions
section_title: "The elementary divisors for hook partitions"
section_number: 6
pages: 9-17
source_pdf: 0309426v2.pdf
source_sha256: f2aa01164d9f243c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.928
doc_brief: "ELEMENTARY DIVISORS OF SPECHT MODULES — 9 sections: Front matter; Introduction and statement of main; The Hecke algebra and permutation"
---
Throughout this section we fix an integer $k$, with $0\le k<n$, and
consider the Specht module $S(\lambda)$, where $\lambda=(n-k,1^k)$. We
will show that $G(\lambda)$ is divisibly diagonalizable by explicitly
constructing two bases of $S(\lambda)$ which transform $G(\lambda)$
into the form of the matrix in Lemma~\ref{diag}. In particular, this
will allow us to determine the elementary divisors of $S(\lambda)$.

The Specht module $S(\lambda)$ is defined as a submodule of the
permutation module $M(\lambda)$; however, to compute the elementary
divisors we will work inside a different permutation module.

By definition,
$S(\lambda)=x_\lambda T_{w_\lambda}y_{\lambda'}\H
           =x_{(n-k,1^k)}T_{w_{(n-k,1^k)}}y_{(k+1,1^{n-k-1})}$.
We first need to understand the permutation $w_\lambda=w_{(n-k,1^k)}$
a little better. This requires some new notation. For integers
non--negative $i$ and $j$ define
$$r_{i,j}=\begin{cases}1,                   &\If i=0\Or j=0,\\
                       r_ir_{i+1}\dots r_j, &\If 0<i\le j,\\
                       r_ir_{i-1}\dots r_j, &\If i>j>0,
\end{cases}$$
and set $T_{i,j}=T_{r_{i,j}}$.  Next, let $a$ and $b$ be non--negative
integers such $a+b\le n$. If either $a=0$ or $b=0$ then set
$w_{a,b}=1$. If both $a$ and $b$ are non--zero then define
$w_{a,b}=(r_{a+b-1,1})^b$; then one can check that, in two--line
notation,
$$w_{a,b}=\Big(\begin{array}{cccc|cccc}
                 1&2&\dots&a&a+1&a+2&\dots&a+b\\
              b+1&b+2&\dots&a+b&1&2&\dots&b
\end{array}\Big).$$
It is not hard to see that $w_{b,a}=w_{a,b}^{-1}$
and that $w_{a,b}=r_{a,a+b-1}w_{a-1,b}$ and 
$\len(w_{a,b})=\len(r_{a,a+b-1})+\len(w_{a-1,b})$; see \cite{DJ:B}. 
Consequently,
$$w_{a,b}=r_{a,a+b-1}r_{a-1,a+b-2}\dots r_{1,b}
         =r_{1,a}r_{2,a+2}\dots r_{b,a+b-1}$$
with the lengths adding in both cases. Hence, $\len(w_{a,b})=ab$.

The permutation $w_{(n-k,1^k)}$ is essentially one of these
permutations because
$$w_{(n-k,1^k)}=\Big(\begin{array}[c]{*7c}
           1&2&\cdots&n-k&n-k+1&\cdots&n\\
           1&k+2&\cdots&n&2&\cdots&k+1
\end{array}\Big).$$
Hence, $w_{(n-k,1^k)}=r_{n-k,n-1}r_{n-k-1,n-2}\dots r_{2,k+1}$, with
the lengths adding. So
$$T_{w_{(n-k,1^k)}}=T_{n-k,n-1}\dots T_{2,k+1},$$ 
Notice also that $T_{w_{n-k.k}}=T_{w_{(n-k,1^k)}}T_{1,k}$.

If $w\in\Sym_{(k,n-k)}\cong\Sym_k\times\Sym_{n-k}$
then we write $w=(u,v)$, where $u\in\Sym_k$ and $v\in\Sym_{(1^k,n-k)}$
are the unique permutations such that $w=uv=vu$. Set 
$$x_{(k|n{-}k)}=y_{(k,1^{n-k})}x_{(1^k,n-k)}
       =\sum_{(u,v)\in\Sym_{(k,n-k)}}(-q)^{-\len(u)}T_{uv}.$$
Then it is easy to see that $Rx_{(k|n-k)}$ is an $\H(\Sym_\mu)$--module on
which the subalgebras $\H(\Sym_k)$ and $\H(\Sym_{(1^k,n-k)})$ act via
their sign and trivial representations, respectively. Let
$$M(k|n{-}k)=\Ind_{\H(\Sym_{(k,n-k)})}^{\H(\Sym_n)}\big(Rx_{(k|n{-}k)}\big)
              \cong x_{(k|n{-}k)}\H.$$ 
As in section~2, the induced module $M(k|n{-}k)$ is free as an $R$--module with
basis $\set{x_{(k{\mid}n-k)}T_d|d\in\D_{(k,n-k)}}$. Furthermore,
$M(k|n{-}k)$ possesses a natural non--degenerate associative bilinear form 
$\<\ ,\ \>_{(k|n{-}k)}$ which is determined by 
$$\<x_{(k|n{-}k)} T_u,x_{(k|n{-}k)} T_v\>_{(k|n{-}k)}
  =\begin{cases}
                  q^{\len(u)}, & \If u=v,\\
                  0,&\Otherwise,
   \end{cases}
$$
for $u,v\in\D_{(k,n-k)}$. Donkin~\cite{D:super} calls $M(k|n{-}k)$ a
{\sf trivial source module}.

Let $y_{k+1}'=1+\sum_{j=1}^k(-q)^{j-k-1}T_{k,j}
        =1-q^{-1}T_k+q^{-2}T_{k,k-1} +\dots+(-q)^{-k}T_{k,1}$. This is
a sum over the right coset representatives of $\Sym_k$ in
$\Sym_{k+1}$. Consequently, it follows that
$y_{(k+1,1^{n-k-1})}=y_{(k,1^{n-k})}y_{k+1}'$.
The reason for introducing the module $M(k|n{-}k)$ is the following
result.

Given a non--negative integer $k>1$ let $[k]_q =1+q+\dots+q^{k-1}$ and
$[k]_q^! = [1]_q [2]_q \cdots [k]_q$. Notice that if $q=1$ then
$[k]_1=k$ and $[k]_1^!=k!$.

\begin{Proposition}
Let $\lambda = (n-k,1^k)$. The map 
$$\pi_k\;\map{\; S(\lambda)\;}\; M(k|n{-}k)\; ;\;\; 
    z_\lambda h\;\mapsto\; x_{(k|n{-}k)}y_{k+1}'h$$
is an injective $\H$--module homomorphism. Moreover, 
$$\<x,y\>_\lambda 
   =q^{\frac k2(2n-3k-1)}[k]_q^!\<\pi(x),\pi(y)\>_{(k|n{-}k)},$$
for all $x,y\in S(\lambda)$.
\label{changing}
\end{Proposition}

\begin{proof}
By definition, 
$S(\lambda)=x_{(n-k,1^k)}T_{w_\lambda} y_{(k+1,1^{n-k-1})}\H$.
As remarked above, $w_{n-k,k}=w_{(n-k,1^k)}r_{1,k}$ with
the lengths adding. Therefore, since $r_{1,k}\in\Sym_{\lambda'}$, 
\begin{align*}
x_{(n-k,1^k)}T_{w_{(n-k,1^k)}} y_{(k+1,1^{n-k-1})}
          &=(-1)^kx_{(n-k,1^k)}T_{w_{(n-k,1^k)}}T_{1,k}y_{(k+1,1^{n-k-1})}\\
          &=(-1)^kx_{(n-k,1^k)}T_{w_{n-k,k}}y_{(k+1,1^{n-k-1})}\\
          &=(-1)^kT_{w_{n-k,k}}x_{(1^k,n-k)}y_{(k+1,1^{n-k-1})}\\
          &=(-1)^kT_{w_{n-k,k}}x_{(1^k,n-k)}y_{(k,1^{n-k})}y_{k+1}'\\
          &=(-1)^kT_{w_{n-k,k}}x_{(k|n{-}k)}y_{k+1}'.
\end{align*}
Therefore, $\pi(x)=(-1)^kT_{w_{n-k,k}}^{-1}x$, for all $x\in S(\lambda)$. As
$T_{w_{n-k,k}}$ is invertible, the first claim now follows.

To prove the second claim we first suppose that $R=\ZZ$. If $x,y\in
S(\lambda)$ then, by extending scalars, we may assume that $x$ and $y$
are elements of $S(\lambda)_{\Q(q)}=S(\lambda)_\ZZ\otimes\Q(q)$. Now
$S(\lambda)_{\Q(q)}\cong\pi\big(S(\lambda)_{\Q(q)}\big)$ is
irreducible so, up to a scalar, there is a unique associative bilinear form on
$S(\lambda)_{\Q(q)}$. To determine this scalar it is enough to compare
the two inner products
on $z_\lambda$ and $\pi(z_\lambda)$. Using associativity,
\begin{align*}
\<z_\lambda,z_\lambda\>_\lambda
     &=\<x_\lambda T_{w_\lambda} y_{\lambda'},
         x_\lambda T_{w_\lambda} y_{\lambda'}\>_\lambda
      =\<x_\lambda T_{w_\lambda} y_{\lambda'}^2,
           x_\lambda T_{w_\lambda}\>_\lambda\\
     &=q^{-\binom{k+1}2} [k+1]_q^!\<x_\lambda T_{w_\lambda} y_{\lambda'},
                         x_\lambda T_{w_\lambda}\>_\lambda\\
     &=q^{-\binom{k+1}2}[k+1]_q^!\sum_{v\in\Sym_{\lambda'}}(-q)^{-\len(v)}
        \<x_\lambda T_{w_\lambda v},x_\lambda T_{w_\lambda}\>_\lambda\\
     &=q^{\len(w_\lambda)-\binom{k+1}2}[k+1]_q^!\\
     &=q^{\frac k2(2n-3k-3)}[k+1]_q^!.
\intertext{Similarly,}
\big\<\pi(z_\lambda),\pi(z_\lambda)\big\>_{(k|n{-}k)}
     &=\<x_{(k|n{-}k)}y_{k+1}',x_{(k|n{-}k)}y_{k+1}'\>_{(k|n{-}k)}
      =q^{-k}[k+1]_q
\end{align*}
This proves that 
$\<x,y\>_\lambda=q^{\frac k2(2n-3k-1)}[k]_q^!\<\pi(x),\pi(y)\>_{(k|n{-}k)}$, for all 
$x,y\in S(\lambda)$ when $R=\ZZ$. The general case now follows by
specialization.
\end{proof}

\begin{Corollary}
Suppose that $\lambda=(n-k,1^k)$. Then $[k]_q^!$ divides
$\<x,y\>_\lambda$, for all $x,y\in S(\lambda)$.
\end{Corollary}

Let $S'(\lambda)=\pi\(S(\lambda)\)=x_{(k|n{-}k)}y_{k+1}'\H$. Then
$S'(\lambda)\cong S(\lambda)$ by the Proposition. We will work with
$S'(\lambda)$ in what follows rather than working
with $S(\lambda)$ directly. 

As a first step we need a basis of $S'(\lambda)$. For \textit{any}
$\lambda$-tableau $\t$ define
$$v_\t'=\pi(v_\t)=x_{(k|n{-}k)}y_{k+1}'T_{d(\t')}.$$

The Dipper--James basis of $S(\lambda)$, (\ref{DJ_basis}), combined
with Proposition~\ref{changing}, give us the following.

\begin{Corollary}
The module $S'(\lambda)$ is $R$--free with basis 
$\set{v_\t'|\t\in\Std(\lambda)}$.
\end{Corollary}























In order to exploit this basis we introduce another type of tableaux.
For our purposes we could get by using $(k,n-k)$--tableaux; however,
we use the notation from the theory of trivial source modules.

The {\sf diagram} of $(k|n{-}k)$ is the ordered pair of diagrams
$[k|n-k]=([k], [n-k])$.  A $(k|n{-}k)$--tableau is a bijection from
$[k|n-k]$ to $\{1,2,\dots,n\}$. Once again, we will think of a
$(k|n{-}k)$--tableau as being a labelling of $[k|n-k]$. Accordingly, we
will write a $(k|n{-}k)$--tableau as an ordered pair $(\a|\b)$, where
$\a$ and $\b$ are suitable labellings of the diagrams of the
partitions $(k)$ and $(n-k)$ respectively. We refer to $\a$ and $\b$
as the first and second components of $(\a|\b)$.

A $(k|n{-}k)$--tableau $(\a|\b)$ is {\sf (row) standard} if the
entries in $\a$ increase from left to right and the entries in $\b$
increase from left to right.  Let $\Std(k|n-k)$ be the set of standard
$(k|n{-}k)$--tableaux. For example, the standard $(1|3)$--tableaux are
$$\tab(1|234),\quad\tab(2|134),\quad\tab(3|124)\quad\And\quad
\tab(4|123).$$ Let $\t^{(k|n{-}k)}$ be the standard
$(k|n{-}k)$--tableau with $1,\dots,k$ entered in order, from left to
right, in the first omponent and the numbers $k+1,\dots,n$ in the
second. The first of the tableaux above is $\t^{(1|3)}$.

Two $(k|n-k)$--tableaux $(\a|\b)$ and $(\s|\t)$ are {\sf row
equivalent} if $\a$ and $\s$ contain the same entries up to reordering
(in which case, $\b$ and $\t$ also contain the same set of entries).
As with ordinary tableaux, the symmetric group acts from the right on
the set of $(k|n{-}k)$--tableaux. If $(\a|\b)$ is
a $(k|n{-}k)$--tableau we define $d(\a|\b)$ to be the unique
permutation such that $(\a|\b)=\t^{(k|n{-}k)}d(\a|\b)$. Then $(\a|\b)$
and $(\s|\t)$ are row equivalent if and only if $d(\a|\b)=wd(\s|\t)$
for some $w\in\Sym_{(k,n-k)}$. Consequently,
$$\D_{(k,n-k)}=\{\,d(\a|\b)\mid(\a|\b)\in\Std(k|n{-}k)\}.$$
So the standard $(k|n-k)$--tableaux index a basis of
$M(k|n{-}k)$. 

For furture reference, notice that if $(\a|\b)$ is a standard
$(k|n-k)$--tableau then $\len(d(\a|\b))$ is equal to the number of
pairs of integers $(i,j)$ where $i$ appears in $\a$, $j$ appears in
$\b$ and $i>j$. This follows because if $w\in\Sym_n$ then $\len(w)$ is
equal to the number of pairs $a<b$ with $i=a^w>j=b^w$, and the entries
in $\a$ are the images of $1,\dots,k$ under $d(\a|\b)$, whereas the
entries in $\b$ are the images of $k+1,\dots,n$.

For any $(k|n{-}k)$--tableau $(\a|\b)$ define
$x_{(\a|\b)}=x_{(k|n{-}k)}T_{d(\a|\b)}$. Here we do not assume that
$(\a|\b)$ is standard.  The following lemma is easily verified.

\begin{Lemma}\label{signed} Suppose that $0\le k<n$. 
\begin{enumerate}
\item $M(k|n{-}k)$ is free as an $R$--module with basis
$\{\,x_{(\a|\b)}\mid(\a|\b)\in\Std(k|n{-}k)\,\}$.
\item Suppose that $(\a|\b)\in\Std(k|n{-}k)$ and $1\le i<n$. Then
$$x_{(\a|\b)}T_i=\begin{cases}
  -x_{(\a|\b)},&\text{if $i$ and $i+1$ are both contained in $\a$,}\\
  qx_{(\a|\b)},&\text{if $i$ and $i+1$ are both contained in $\b$,}\\
  x_{(\a_i|\b_i)},&\text{if $i$ is in $\a$ and $i+1$ is in $\b$},\\
  qx_{(\a_i|\b_i)}+(q-1)x_{(\a|\b)},&\text{otherwise,}
\end{cases}$$
where $(\a_i|\b_i)=(\a|\b)r_i$.
\end{enumerate}
\end{Lemma}

The action of $\H$ on $M(k|n-k)$ is completely determined by (ii).

We now show how to write the basis $\{v_\t'\}$ of $S'(\lambda)$ in
terms of this basis of $M(k|n-k)$. To do this, if $\t$ is a
$\lambda$--tableau and $(\a|\b)$ is a $(k|n{-}k)$--tableau write
$(\a|\b)\prec\t$ if $(\a|\b)$ is standard and all of the entries in
$\a$ are contained in the first column of $\t$. Finally, if
$(\a|\b)\prec\t$ we set $I_\t(\a|\b)=i$, the index of $(\a|\b)$ in
$\t$, if the number in row $i$ of $\t$ does not appear in $\a$.

\begin{Lemma}\label{+lot}
Suppose that $\t$ is a standard $\lambda$--tableau. Then
$$v_\t'=\sum_{(\a|\b)\prec\t}
   (-1)^{k+1-I_\t(\a|\b)}q^{\len(d(\t'))-\len(d(\a|\b))}x_{(\a|\b)}.$$
\end{Lemma}

\begin{proof}
First consider $v_{\t_\lambda}$. Looking at the definitions we see
that
\begin{align*}
v_{\t_\lambda}'&=x_{(k|n-k)}y_{k+1}'
     =x_{\t^{(k|n-k)}}\Big(1-q^{-1}T_k+q^{-2}T_{k,k-1}
                 -\dots+(-q)^{-k}T_{k,1}\Big)\\
    &=\sum_{(\a|\b)\prec\t_\lambda}(-q)^{-\len(d(\a|\b))} x_{(\a|\b)}.
\end{align*}
As $\len(d(\t_\lambda)')=\len(d(\t^{\lambda'}))=0$ and
$\len(d(\a|\b))=k+1-I_{\t_\lambda}(\a|\b)$, when
$(\a|\b)\prec\t_\lambda$, the Lemma follows in this case.

Now suppose that $\t$ is an arbitrary standard $\lambda$--tableaux.
If $\t\ne\t_\lambda$ then we can find another standard
$\lambda$--tableau $\s$ and an integer $i$ in the first column of $\s$
such that~$\t=\s r_i$ and $\len(d(\t))=\len(d(\s))-1$. (That is,
$\t\gedom\s$ where $\gedom$ is the dominance order on tableaux; see,
for example,~\cite{M:IHA}.) Therefore, by induction,  
$$v_\t'=v_\s'T_i=\sum_{(\a|\b)\prec\s}
   (-1)^{k+1-I_\s(\a|\b)}q^{\len(d(\s'))-\len(d(\a|\b))}x_{(\a|\b)}T_i.$$
Since $\s$ and $\t$ are standard, $i$ is in the first column of $\s$
and the first row of $\t$ and~$i+1$ is in the first row of $\s$ and
the first column of $\t$.  Therefore, if $(\a|\b)\prec\s$ then the
entries in the first component of $(\a|\b)r_i$ are still in increasing
order and the entries in the second component are in increasing order
unless $i$ and~$i+1$ both appear in~$\b$. So,
$\len(d(\a|\b)r_i)=\len(d(\a|\b))+1$ and by Lemma \ref{signed}(ii) we
have
$$x_{(\a|\b)}T_i=\begin{cases}
      qx_{(\a|\b)},&\If i\And i+1\text{ both appear in $\b$},\\
       x_{(\a|\b)r_i},&\Otherwise.
\end{cases}$$
In the first case, when $i$ and $i+1$ both appear in $\b$, we have
that $(\a|\b)\prec\t$. Also, that
$\len(d(\t'))-\len(d(\a|\b))=\len(d(\s'))-\len(d(\a|\b))+1$ and
$I_\t(\a|\b)=I_\s(\a|\b)$ so $x_{(\a|\b)}$ has the required
coefficient in $v_\t'$.

In the second case, $i$ appears in $\a$ and $i+1$ appears in $\b$, so 
$(\a r_i|\b r_i)=(\a|\b)r_i\prec\t$, $I_\t(\a r_i|\b r_i)=I_\s(\a|\b)$
and $\len(d(\t'))-\len(d(\a|\b))=\len(d(\s'))-\len(d(\a|\b))+1$.
Hence, once again, $x_{(\a|\b)r_i}$ has the predicted coefficient in $v_\t'$.

As there are exactly $k$ standard $(k|n-k)$--tableaux $(\a|\b)$ 
satisfying $(\a|\b)\prec\t$, this completes the proof.
\end{proof}

In order to compute the elementary divisors of $S(\lambda)$ we need a
second basis of~$S'(\lambda)$. Let
$$x_{n-k}=1+T_1+\dots+T_{1,n-k-1}=\sum_{j=0}^{n-k-1}T_{1,j}.$$
(Note that $r_{1,0}=1$.) As with $y_{k+1}'$, we have
$x_{(n-k,1^k)}=x_{(1,n-k-1,1^{k-1})}x_{n-k}$. Now, for any standard
$(n-k,1^k)$--tableau $\t$ we define
$$w_\t'=\begin{cases}
          v_{\t(1,n)}',&\text{\ if $n$ appears in row 1 of $\t$},\\
          v_{\t^\lambda}'x_{n-k}T_{d(\t)},&\Otherwise.
\end{cases}$$
We remark that it is not obvious that the set of elements
$\set{w_\t'|\t\in\Std(\lambda)}$ is a basis of $S'(\lambda)$. We will
prove this below.

Lemma~\ref{+lot} gives an explicit description of the basis
$\{v_\t'\}$. We need to do the same for the basis $\{w_\t'\}$, and for
this we need some more notation. If $\t$ is a standard
$\lambda$--tableau let $\t^*=\t(1,n)$. If $(\a|\b)$ is a
$(k|n-k)$--tableau write $(\a|\b)\prec_n\t$ if $(\a|\b)\prec\t$ and
$n$ is contained in $\b$. Finally, if $n$ appears in the first row of
$\t$ then we define $(\a_\t^*|\b_\t^*)$ to be the unique standard
$(k|n-k)$--tableau such that $\(\a_\t^*|\b_\t^*)\prec\t^*$ and $n$
appears in $\b_\t^*$. So $\(\a_\t^*|\b_\t^*)\prec\t^*$ and
$\(\a_\t^*|\b_\t^*)\prec\t$.

\begin{Lemma}
Suppose that $\t$ is a standard $\lambda$--tableau and that $n$
appears in the first row of~$\t$.  Then
$$w_\t'=(-1)^kq^{2n-2k-3}x_{(\a_\t^*|\b_\t^*)}
        +\sum_{(\a|\b)\prec_n\t^*}r_{\a\b}x_{(\a|\b)},$$
for some scalars $r_{\a\b}\in\ZZ$. 
\label{+hot}
\end{Lemma}

\begin{proof}
We now argue by downwards induction on $\t$ beginning with
$\t=\t_\lambda$, this is an unpleasant calculation. Now, 
\begin{align*}
w_{\t_\lambda}'&=x_{(k|n{-}k)}y_{k+1}'T_{1,n-1}T_{n-2,1}
               =(-1)^kx_{(k|n{-}k)}y_{k+1}'T_{k+1,n-1}T_{n-2,1}\\
\intertext{since $x_{(k|n{-}k)}y_{k+1}'=x_{(1^k,n-k)}y_{(k+1,1^{n-k-1})}$.
Therefore, using the definitions together with the braid relations,}
w_{\t_\lambda}'
           &=(-1)^kx_{(k|n{-}k)}y_{k+1}'T_{n-1}\dots T_{k+2}T_{k+1,n-1}T_{k,1}\\
           &=(-1)^kx_{(k|n{-}k)}T_{n-1}\dots T_{k+2}y_{k+1}'T_{k+1,n-1}T_{k,1}\\
           &=(-1)^kq^{n-k-2}x_{(k|n{-}k)}y_{k+1}'T_{k+1,n-1}T_{k,1}\\
\end{align*}
\begin{align*}
           &=(-1)^kq^{n-k-2}x_{(k|n{-}k)}\Big\{1
             +\sum_{j=1}^k(-q)^{j-k-1}T_{k,j}\Big\}T_{k+1,n-1}T_{k,1}\\
           &=(-1)^kq^{n-k-2}x_{(k|n-k)}\Big\{q^{n-k-1}
             +\sum_{j=1}^k(-q)^{j-k-1}T_{k,j}T_{k+1,n-1}\Big\}T_{k,1}\\
           &=(-1)^kq^{n-2k-3}x_{(k|n-k)}\Big\{q^{n}T_{k,1}
             +\sum_{j=1}^k(-q)^{j}T_{k,j}T_{k+1,1}T_{k+2,n-1}\Big\}\\
           &=(-1)^kq^{n-2k-3}x_{(k|n-k)}\Big\{q^{n}T_{k,1}
           +\sum_{j=1}^k(-q)^{j}T_{k+1,1}T_{k+1,j+1}T_{k+2,n-1}\Big\}\\
           &=(-1)^kq^{n-2k-3}x_{(k|n-k)}\Big\{q^{n}T_{k,1}
           -\sum_{j=1}^k(-q)^{j+1}T_{k,1}T_{k+1,j+1}T_{k+2,n-1}\Big\}\\
           &=(-1)^kq^{n-2k-3}x_{(k|n-k)}T_{k,1}\Big\{q^{n}
             -\sum_{j=2}^{k+1}(-q)^{j}T_{k+1,j}T_{k+2,n-1}\Big\}.
\end{align*}
Now, 
$\t^{(k|n-k)}r_{k,1}=\big(\,\widetab(2&&\cdots&&k+1)\,\big|\,
                            \widetab(1&&k+2&&\cdots&&n)\,\big)
                    =(\a_{\t_\lambda}^*|\b_{\t_\lambda}^*)$ and,
consequently,
$\t^{(k|n-k)}r_{k,1}r_{k+1,j}r_{k+2,n-1}
    =\big(\,\widetab(2&&\cdots&&j-1&&j+1&&\cdots&&k+1&&n)\,\big|\,
            \widetab(1&&j&&k+2&&\cdots&&n-1)\,\big),$
for $j=2,\dots,k+1$. This completes the proof for $w_{\t_\lambda}'$. 

Now suppose that $\t$ is an arbitrary standard $\lambda$--tableau
which has $n$ in its first row. Then $d(\t')\in\Sym_{(1,n-2,1)}$ so
$d(\t')$ and $(1,n)$ commute and
$\len(d(\t')(1,n))=\len(d(\t'))+\len(1,n)$.  Therefore,
$w_\t'=w_{t_\lambda}'T_{d(\t')}$. To complete the proof now argue by
induction, as in the proof of Lemma~\ref{+lot}; we leave the details
to the reader. (Indeed, this shows that $r_{\a\b}=\pm q^a$ for some
integer $a$.)
\end{proof}

For convenience we now write $\<\ ,\ \>=\<\ ,\ \>_{(k|n{-}k)}$. In
terms of the standard basis of $M(k|n-k)$, the bilinear form 
$\<\ ,\ \>$ on $M(k|n-k)$ is determined by
$$
\<x_{(\a|\b)}, x_{(\s|\t)}\> \; =\; 
\begin{cases}
q^{\len(d(\a|\b))},& \If (\a|\b)=(\s|\t),\\
0,                 & \Otherwise,
\end{cases}
$$
for standard $(k|n-k)$--tableaux $(\a|\b)$ and $(\s|\t)$.

\begin{Corollary}\label{top half}
Suppose that $\s$ and $\t$ are standard $\lambda$--tableaux which have
$n$ in their first row. Then
$$\<w_\s',v_\t'\>=\begin{cases}q^{2n-2k-3+\len(d(\t'))},&\If\s=\t,\\
                               0,&\Otherwise.
\end{cases}$$
\end{Corollary}

\begin{proof}By Lemma~\ref{+lot} and Lemma~\ref{+hot} we have
\begin{align*}
v_\s'&=\sum_{(\a_s|\b_s)\prec\s}
    (-1)^{k+1-I_\s(\a_s|\b_s)}q^{\len(d(\s'))-\len(d(\a_s|\b_s))}
              x_{(\a_s|\b_s)}\\
\intertext{and, by Lemma \ref{+hot},} 
w_\t'&=(-1)^kq^{2n-2k-3}x_{(\a_\t^*|\b_\t^*)}
        +\sum_{(\a_t|\b_t)\prec_n\t^*}r_{\a_t\b_t}x_{(\a_t|\b_t)}.
\end{align*}
Now, all of the tableaux appearing in $w_\t'$ have $1$
appearing in their second component. In contrast, the only tableau in
$v_\s'$ which has $1$ in its second component is the tableau
$(\a_\s^*|\b_\s^*)$. Therefore,
\begin{align*}
\<w_\s',v_\t'\>
    &=(-1)^{2k+1-I_\s(\a_s^*|\b_s^*)}
      q^{2n-2k-3+\len(d(\s'))-\len(d(\a_\s^*|\b_\s^*))}
             \<x_{(\a_\s^*|\b_\s^*)},x_{(\a_\t^*|\b_\t^*)}\>\\
    &=\begin{cases}
          (-1)^{1+I_\t(\a_\t^*|\b_\t^*)}
           q^{2n-2k-3+\len(d(\t'))},&\If\s=\t,\\  
           0,&\Otherwise.
      \end{cases}
\end{align*}
Finally, the sign vanishes when $\s=\t$ because $I_\t(\a_\t^*|\b_\t^*)=1$ .
\end{proof}

We need one more result before we can produce the elementary divisors
of $S(\lambda)$.

\begin{Lemma}Let $(\a_\lambda^+|\b_\lambda^+)$ be the unique standard
$(k|n-k)$--tableau which has the numbers $n-k+1,\dots,n$ in
$\a_\lambda^+$. Then
\begin{align*} w_{\t^\lambda}'
=(-1)^kq^{\len(w_{\lambda'})}\Big\{&
        q^{-\len(d(\a_\lambda^+|\b_\lambda^+))}[n-k]_q 
             x_{(\a_\lambda^+|\b_\lambda^+)}\\
  &\quad +\sum_{\substack{(\a|\b)\prec\t^\lambda\\
                         (\a|\b)\ne(\a_\lambda^+|\b_\lambda^+)}}
        (-1)^{1-I_{\t^\lambda}(\a|\b)}q^{-\len(d(\a|\b))}
        \sum_{j=0}^{n-k-1}x_{(\a|\b)r_{1,j}}\Big\}.
\end{align*}
\label{w_t}\end{Lemma}

\begin{proof}
By definition $w_{\t^\lambda}'=v_{\t^\lambda}'x_{n-k}$. Also,
$d((\t^\lambda)')=d(\t_{\lambda'})=w_{\lambda'}$ so, by 
Lemma~\ref{+lot},
\begin{align*}w_{\t^\lambda}'
 &=v_{\t^\lambda}'x_{n-k}=\sum_{(\a|\b)\prec\t^\lambda}
               (-1)^{k+1-I_{\t^\lambda}(\a|\b)}
               q^{\len(w_{\lambda'})-\len(d(\a|\b))}x_{(\a|\b)}x_{n-k}\\
 &=\sum_{(\a|\b)\prec\t^\lambda}
    (-1)^{k+1-I_{\t^\lambda}(\a|\b)}q^{\len(w_{\lambda'})-\len(d(\a|\b))}
        x_{(\a|\b)}\Big(1+T_1+\dots+T_{1,n-k-1}\Big).
\end{align*}
Let $(\a|\b)$ be one of the tableaux appearing in this sum. If
$(\a|\b)\ne(\a_\lambda^+|\b_\lambda^+)$ then $1$ is contained in $\a$
and all of the numbers $2,3,\dots,n-k$ are contained in $\b$.
Therefore, $(\a|\b)r_{1,j}$ is standard and
$x_{(\a|\b)}T_{1,j}=x_{(\a|\b)r_{1,j}}$, for $0\le j\le n-k-1$. On the
other hand,
$x_{(\a_\lambda^+|\b_\lambda^+)}T_{1,j}=q^jx_{(\a_\lambda^+|\b_\lambda^+)}$,
for $0\le j\le n-k-1$.  This completes the proof of the Lemma.
\end{proof}

This result has two useful Corollaries.

\begin{Corollary}\label{zeros}
Suppose that $\t\ne\t^\lambda$ is a standard $(k|n-k)$--tableau. Then
$$\<w_{\t^\lambda}',v_\t'\>=0.$$
\end{Corollary}

\begin{proof}
By Lemma~\ref{w_t}, if $x_{(\a|\b)}$ appears in $w_{\t^\lambda}'$ then
all but one of the entries in $\a$ are contained in
$\{1,n-k+1,\dots,n\}$.  On the other hand, by Lemma~\ref{+lot}, if
$x_{(\a|\b)}$ appears in $v_\t'$ then all of the entries in $\a$ are
contained in the first column of~$\t$. 

Suppose now that $\t\ne\t^\lambda$. Then, by the last paragraph,
$x_{(\a_\lambda^+|\b_\lambda^+)}$ cannot appear in~$v_\t'$ and the
only way that the inner product $\<w_{\t^\lambda}',v_\t'\>$ can be
non--zero is if the set of numbers in the first column of $\t$ is of
the form $T=\{1,j,n-k+1,\dots,n\}\setminus\{m\}$, for some integers
$j$ and $m$ with $1<j\le n-k$ and $n-k<m\le n$. Let $(\a|\b)$ be the
standard $(k|n-k)$--tableau whose first component contains exactly the
numbers in~$T\setminus\{j\}$ and let $(\s|\t)=(\a|\b)r_{1,j-1}$. Then
$(\a|\b)\prec\t^\lambda$, $I_\t(\a|\b)=2$ and $I_\t(\s|\t)=1$. Also
$\len(d(\s|\t))=\len(d(\a|\b))+j-1$, so
$x_{(\a|\b)}T_{1,j-1}=x_{(\s|\t)}$. Therefore, by Lemma~\ref{+lot} and
Lemma~\ref{w_t} and the remarks above,
\begin{align*}
v_\t'&=(-1)^kq^{\len(d(\t'))}
    \Big(q^{-\len(d(\s|\t))}x_{(\s|\t)}-q^{-\len(d(\a|\b))}x_{(\a|\b)}\Big)
           +\text{\ other standard terms}\\
\intertext{and}
w_{\t^\lambda}'&=q^{\len(w_{\lambda'})-\len(d(\a|\b))}
                     \Big(x_{(\s|\t)}+x_{(\a|\b)}\Big)
+\text{other standard terms,}
\end{align*}
where none of the ``other standard terms'' appear both in $v_\t'$ and
in $w_{\t^\lambda}'$. Consequently, $\<w_{\t^\lambda}',v_\t'\>=0$.
Hence, $\<w_{\t^\lambda}',v_\t'\>=0$ whenever $\t\ne\t^\lambda$ as
claimed.
\end{proof}

\begin{Corollary}\label{n-diagonals}
Suppose that $\t$ is a standard $(n-k,1^k)$--tableau and that
$n$ does not appear in the first row of $\t$. Then
$\<w_\t',v_\t'\>=q^{k(n-k-2)}[n]_q.$
\end{Corollary}

\begin{proof}
Recall that if $\t$ is a standard $\lambda$--tableau
then $d(\t')d(\t)^{-1}=w_{\lambda'}$, with the lengths adding; this is
well--known and is easily proved by induction on the dominance order
for tableaux. Therefore, 
\begin{align*}
\<w_\t',v_\t'\>&=\<w_{\t^{\lambda}}'T_{d(\t)},x_{(k|n{-}k)}y_{k+1}'T_{d(\t')}\>
          =\<w_{\t^{\lambda}}',x_{(k|n{-}k)}y_{k+1}'T_{d(\t')}T_{d(\t)}^*\>\\
         &=\<w_{\t^{\lambda}}',x_{(k|n{-}k)}y_{k+1}'T_{d({\t^{\lambda}}')}\>
          =\<w_{\t^\lambda}',v_{\t^\lambda}'\>.
\end{align*}
Hence, it is enough to consider the case where $\t=\t^\lambda$.

Suppose that $\t=\t^\lambda$. Then, by Lemma~\ref{+lot} and
Lemma~\ref{w_t},
\begin{align*}
\<w_{\t^\lambda}',v_{\t^\lambda}'\>
     &=q^{2\len(w_{\lambda'})}\Big\{
                        q^{-\len(d(\a_\lambda^+|\b_\lambda^+))}[n-k]_q
          +\sum_{\substack{(\a|\b)\prec\t^\lambda\\
                           (\a|\b)\ne(\a_\lambda^+|\b_\lambda^+)}}
                        q^{-\len(d(\a|\b))}\Big\}.
\intertext{Using the remarks before Lemma~\ref{signed} it is not hard
to see that $\len(d(\a_\lambda^+|\b_\lambda^+))=k(n-k)$ and that
$\len(d(\a|\b))=(k-1)(n-k)+2-I_\t(\a|\b)$, whenever
$(\a|\b)\prec\t^\lambda$ and $(\a|\b)\ne(\a_\lambda^+|\b_\lambda^+)$. 
Therefore,}
\<w_{\t^\lambda}',v_{\t^\lambda}'\>
     &=q^{2\len(w_{\lambda'})}\Big\{
         q^{-k(n-k)}[n-k]_q+\sum_{i=2}^{k+1}q^{-(k-1)(n-k)-2+i}\Big\}\\
     &=q^{2\len(w_{\lambda'})-k(n-k)}\Big\{
                       [n-k]_q+q^{n-k}\sum_{j=0}^{k-1}q^j\Big\}\\
     &=q^{2\len(w_{\lambda'})-k(n-k)}[n]_q.
\end{align*}
As $\len(w_{\lambda'})=k(n-k-1)$ the result follows.
\end{proof}

Finally, we can prove the main result of this section.

\begin{Proposition}\label{eds}
Suppose that $\lambda = (n-k,1^k)$, for some $k$ with $0\le k<n$.
Then the Gram matrix $G(\lambda)$ of $S(\lambda)$ is divisibly
diagonalizable over $\ZZ$ with $\binom{n-2}{k}$ elementary divisors
equal to $[k]_q^!$ and with the remaining $\binom{n-2}{k-1}$
elementary divisors being equal to $[k]_q^![n]_q$.
\end{Proposition}

\begin{proof}By Proposition~\ref{changing} the Gram matrix
$G(\lambda)$ of $S(\lambda)$ is equal to $[k]_q^!$ times the Gram
matrix of $S'(\lambda)$. Therefore, by Lemma~\ref{diag} it is enough
to show that there is an invertible diagonal matrix $D$ such that
$$G'(\lambda)=\Big(\<w_\s',v_\t'\>\Big)_{\s,\t\in\Std(k|n-k)}
     = D\cdot\left(\begin{array}{*4c} 
                     I & *\\ 
                     0 & [n]_qU
           \end{array}\right),$$ 
where $I$ is a $\binom{n-2}k\times\binom{n-2}k$ identity matrix and
$U$ is a $\binom{n-2}{k-1}\times\binom{n-2}{k-1}$ upper triangular matrix
with $1$'s down its diagonal. Here we order the rows and columns
lexicographically with respect to the entries in the first column of
$\s$ and $\t$. Because $D$ is invertible its non--zero entries are all
of the form $\pm q^m$, for some integer $m$.

By Corollary~\ref{top half}, the rows of $G'(\lambda)$ which are
indexed by those tableaux which have $n$ in their first row have the
required form. This accounts for the identity matrix in the top half
of the Gram matrix $G'(\lambda)$.

Next, suppose that $\s$ is a standard
$(k|n-k)$--tableau and that $n$ does not appear in the first row of
$\s$. If $\s =\t^\lambda$ then $\<w_\s',v_\t'\>=0$, for all $\t\ne\s$,
by Corollary~\ref{zeros}.
If $\s\ne\t^\lambda$ then there exists an integer $i$, $1\le i<n$, such
that $\len(d(\s)r_i)<\len(d(\s))$. Therefore,
$$
\<w_\s',v_\t'\>=\<w_{\s r_i}'T_i,v_\t'\>
                 =\<w_{\s r_i}',v_\t'T_i\>.
$$
It follows that $\<w_\s',v_\t'\>=0$ if $\t$ appears before $\s$ in our
chosen ordering of $\Std(\lambda)$. Finally, if $\t$ does not appear
before $\s$ then $[n]_q$ divides $\<w_\s',v_\t'\>$ by
Corollary~\ref{n-diagonals}.
\end{proof}

Notice, in particular, that the Gram matrix calculation in the proof of
the Proposition implies that $\set{w_\t'|\t\in\Std(\lambda)}$ is
indeed a basis of $S'(\lambda)$. 

Proposition~\ref{eds} also gives the decomposition numbers of
$S(\lambda)$ (by inducing the corresponding principal indecomposable
modules); however, as these are already known we leave these as an
exercise for the reader. We will, however, give one application of
this result.

Let $\pi\map{S(\lambda)}S'(\lambda)$ be the isomorphism of
Proposition~\ref{changing} and for each standard $\lambda$--tableau
$\t$ let $w_\t=\pi^{-1}(w_\t')$. Then $\set{w_\t|\t\in\Std(\lambda)}$
is a basis of $S(\lambda)$.  Then, in the case where $S(\lambda)$ is
not irreducible, the proof of Proposition~\ref{eds} also gives a basis
for the simple module $D(\lambda)$. More precisely, we have the
following.

\begin{Corollary}
Suppose that $R$ is a field, that $[k]_q^!\neq 0$ and that $[n]_q = 0$. Then
$S(\lambda)$ is not irreducible and a basis of
$D(\lambda) = S(\lambda)/\big(S(\lambda)^\perp\cap S(\lambda)\big)$ is given by 
$$
\set{w_\t + \big(S(\lambda)^\perp\cap S(\lambda)\big)|
               \t\in\Std(\lambda)\And\text{$n$ in first row of $\t$}}\;,
$$
and a basis of $S(\lambda)^\perp\cap S(\lambda)$ is given by
$
\set{w_\t |\t\in\Std(\lambda)\And\text{$n$ is in first row of $\t$}}.
$
\end{Corollary}
