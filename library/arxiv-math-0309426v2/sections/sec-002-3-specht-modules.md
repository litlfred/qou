---
doc_id: arxiv-math-0309426v2
doc_title: "ELEMENTARY DIVISORS OF SPECHT MODULES"
section_id: sec-002-3-specht-modules
section_title: "Specht modules"
section_number: 3
pages: 3-4
source_pdf: 0309426v2.pdf
source_sha256: f2aa01164d9f243c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.758
doc_brief: "ELEMENTARY DIVISORS OF SPECHT MODULES — 9 sections: Front matter; Introduction and statement of main; The Hecke algebra and permutation"
---
We recall some well-known facts due to Dipper and
James~\cite{DJ:reps}.

Let $\lambda = (\lambda_1,\lambda_2,\dots)$ be a composition of $n$.
The {\sf diagram} of $\lambda$ is the set $[\lambda] = \set{(i,j)\in\N^2|1\le
j\le\lambda_i}$. We identify the diagram of $\lambda$ with an array of
boxes in the plane. For example, if $\lambda = (4,3,2)$ then
$$
[\lambda] \; =\; \yng(4,3,2) \; .
$$
The {\sf conjugate} of $\lambda$ is the partition
$\lambda' = (\lambda_1',\lambda_2',\dots)$, where
$\lambda_j' = \#\set{i\ge 1|\lambda_i\ge j}$ for all $j$; that is,
$\lambda'$ is the partition of $n$ whose diagram is obtained by
interchanging the rows and columns of the diagram of $\lambda$.

Formally, a {\sf $\lambda$--tableau} is a bijection
$\t\map{[\lambda]}\{1,2,\dots,n\}$; however, we will think of a
$\lambda$--tableau as a labelling of the diagram of $\lambda$ by the
numbers $1,2,\dots,n$. Accordingly, we will speak of the rows and
columns of a tableau. For example, 
$$\young(123,45)\;,\qquad\young(135,24)\;,\qquad\young(145,23)\qquad\And\qquad
  \young(234,15)$$ 
are all $(3,2)$--tableaux. 

A tableau is {\sf row standard} if in each row its entries increase
from left to right. A tableau is {\sf standard} if it is row standard
and in each column its entries increase from top to bottom. Let
$\Std(\lambda)$ be the set of standard $\lambda$-tableaux.

All of the tableaux above are row standard; however, only the first
two tableaux are standard.

The {\sf initial $\lambda$--tableau} $\t^\lambda$ is the standard
$\lambda$--tableau which has the numbers $1,2,\dots,n$
entered in order from left to right, and then top to bottom, along its
rows. The {\sf terminal $\lambda$--tableau} $\t_\lambda$ is the standard
$\lambda$--tableau which has the numbers $1,2,\dots,n$
entered in order from top to bottom, and then left to right, along its
columns. Of the $(3,2)$--tableaux above, the first is $\t^{(3,2)}$ and
the second is $\t_{(3,2)}$.

The symmetric group $\Sym_n$ acts from the right on the set of
$\lambda$--tableaux by permuting their entries. If $\t$ is a
$\lambda$--tableau let $d(\t)$ be the unique permutation such that
$\t=\t^\lambda d(\t)$. In particular, we set
$w_\lambda=d(\t_\lambda)$.

We remark that $\D_\mu = \set{d(\t)|\t\text{\ is a row standard $\mu$--tableau}}.$

Suppose that $\lambda$ is a partition of $n$ and let 
$z_\lambda= x_\lambda T_{w_\lambda} y_{\lambda'}$. The {\sf Specht
module} is the submodule $S(\lambda) = z_\lambda\H$ of $M(\lambda)$.

Let $S(\lambda)^\perp = \set{x\in M(\lambda)|\< x,y\>=0\ForAll y\in S(\lambda)}$.
As $\<\ ,\ \>_\lambda$ is associative,
$S(\lambda)^\perp$ is an $\H$-submodule of $M(\lambda)$. More
precisely, $S(\lambda)^\perp$ is the kernel of the $\H$-linear map
$$
M(\lambda)\;\lraa{\delta_\lambda}\;S(\lambda)^\ast \; ;\;\;\; x_\lambda h \;\lramaps\;\< x_\lambda h, - \>_\lambda \; ,
$$
where $h\in\H$. 

By restricting the bilinear form $\<\ ,\ \>_\lambda$ on $M(\lambda)$
we obtain a bilinear form on $S(\lambda)$.  If $R$ is a field then
$D(\lambda) = S(\lambda)/S(\lambda)\cap S(\lambda)^\perp$ is either
zero or absolutely irreducible. Moreover, all of the irreducible
$\H$--modules arise uniquely in this way \cite[Theorem~5.2]{DJ:reps}.

Before we can give a basis of $S(\lambda)$ we need some more notation.
If $\t$ is a $\lambda$--tableau let $\t'$ be the $\lambda'$--tableau
obtained by interchanging the rows and columns of~$\t$. For example,
$(\t^\lambda)'=\t_{\lambda'}$ and $(\t_\lambda)'=\t^{\lambda'}$.
Finally, if $\t$ is a standard $\lambda$--tableau let 
$v_\t = z_\lambda T_{d(\t')}$.

\begin{Point}\it{(Dipper--James~\cite[Theorem~5.6]{DJ:reps})}
The Specht module $S(\lambda)$ is free as an $R$--module with basis 
$\set{v_\t|\t\in\Std(\lambda)}$.
\label{DJ_basis}\end{Point}

We call $\set{v_\t|\t\in\Std(\lambda)}$ the {\sf Dipper--James basis} of $S(\lambda)$.
Let $n_\lambda = \#\Std(\lambda)$ be the number of standard
$\lambda$--tableaux. Then, as an $R$-module, $S(\lambda)$ is free of
rank~$n_\lambda$.

Fix an ordering of $\Std(\lambda)$ and let
$$G(\lambda)=\Big(\<v_\s,v_\t\>_\lambda\Big)_{\s,\t\in\Std(\lambda)}$$ 
be the Gram matrix of the bilinear form $\<\ ,\ \>_\lambda$, with
respect to the Dipper--James basis. The matrix $G(\lambda)$ depends on
the choice of ordering on $\Std(\lambda)$; however, all of the quantities
that we are interested in will be independent of this choice. We remark
that $\det G(\lambda)$ has been explicitly computed by Dipper and
James~\cite[Theorem~4.11]{DJ:blocks}.
