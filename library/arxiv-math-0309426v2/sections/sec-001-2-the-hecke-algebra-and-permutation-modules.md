---
doc_id: arxiv-math-0309426v2
doc_title: "ELEMENTARY DIVISORS OF SPECHT MODULES"
section_id: sec-001-2-the-hecke-algebra-and-permutation-modules
section_title: "The Hecke algebra and permutation modules"
section_number: 2
pages: 1-3
source_pdf: 0309426v2.pdf
source_sha256: f2aa01164d9f243c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.703
latex_coverage_ratio: 0.806
doc_brief: "ELEMENTARY DIVISORS OF SPECHT MODULES — 9 sections: Front matter; Introduction and statement of main; The Hecke algebra and permutation"
---
Fix a positive integer $n$ and let $\Sym_n$ be the symmetric group of
degree $n$. 

Let $R$ be a commutative domain and let $q$ be an
invertible element in $R$. 

The Iwahori--Hecke algebra of $\Sym_n$ with
parameter $q$ is the unital associative algebra $\H$ with generators
$T_1,T_2,\dots,T_{n-1}$ and relations
$$
\begin{array}{rcll}
  (T_i-q)(T_i+1)  & = & 0                   & \For 1\le i < n,\\
  T_i T_j         & = & T_j T_i             & \For 1\le i < j-1 < n-1,\\
  T_i T_{i+1} T_i & = & T_{i+1} T_i T_{i+1} & \For 1\le i < n-1 \; .
\end{array}
$$

Let $r_i=(i,i+1)$, for $i=1,2,\dots,n-1$. Then
$\{r_1,r_2,\dots,r_{n-1}\}$ generate $\Sym_n$ (as a Coxeter group).
If $w\in\Sym_n$ then $w = r_{i_1}\cdots r_{i_k}$ for some $i_j$ with $1\le i_j < n$.
The word $w = r_{i_1}\dots r_{i_k}$ is {\sf reduced} if $k$ is minimal;
in this case we say that $w$ has {\sf length} $k$ and we define $\len(w)=k$. 

If $r_{i_1}\dots r_{i_k}$ is reduced then we set $T_w = T_{i_1}\cdots T_{i_k}$. 
Then $T_w$ is independent of the choice of reduced
expression for $w$; see, for example, \cite[1.11]{M:IHA}. Furthermore, 
$\H$ is free as an $R$--module with basis $\set{T_w|w\in\Sym_n}$.

A {\sf composition} $\mu$ of $n$ is a sequence of non--negative
integers $(\mu_1,\mu_2,\dots)$ that sum to $n$. If, in addition,
$\mu_1\ge\mu_2\geq\dots$, then $\mu$ is a {\sf partition} of $n$.

Let $\mu$ be a composition of $n$ and let $\Sym_\mu$ be the associated
Young subgroup. Then $\H(\Sym_\mu)=\<\,T_w\mid w\in\Sym_\mu\,\>$ is a
subalgebra of $\H$. Given a (right) $\H(\Sym_\mu)$--module~$V$, we
define the induced $\H$--module
$$
\Ind_{\H(\Sym_\mu)}^\H(V) \; =\; V\otimes_{\H(\Sym_\mu)}\H\; .
$$
Let $\D_\mu=\set{d\in\Sym_n|\len(dr_i)>\len(d)\ForAll r_i\in\Sym_\mu}$ 
be the set of distinguished right coset
representatives of $\Sym_\mu$ in $\Sym_n$. Then, as an $R$-module, 
$$
\Ind_{\H(\Sym_\mu)}^\H(V)\cong\bigoplus_{d\in\D_\mu}V\otimes T_d
$$
by \cite[Theorem~2.7]{DJ:reps}.

Let $x_\mu = \sum_{w\in\Sym_\mu}T_w$. Then $T_w x_\mu = x_\mu T_w =
q^{\len(w)}x_\mu$ for all $w\in\Sym_\mu$.  The {\sf trivial
representation} of $\H(\Sym_\mu)$ is the free $R$--module 
$\mathbf 1_\mu = Rx_\mu$. 

Let $y_\mu = \sum_{w\in\Sym_\mu} (-q)^{-\len(w)} T_w$. Then 
$T_w y_\mu = y_\mu T_w = (-1)^{\len(w)} y_\mu$ for all $w\in\Sym_\mu$. 
The {\sf sign representation} of $\H(\Sym_\mu)$ is the free $R$--module 
$\mathcal E_\mu = Ry_\mu$.

For any composition $\mu$ we define the permutation module
$M(\mu)=\Ind_{\H(\Sym_\mu)}^\H(\mathbf 1_\mu)\cong x_\mu\H$. Then
$M(\mu)$ is free as an $R$--module of rank $[\Sym_n:\Sym_\mu]$ with
basis $\set{x_\mu T_d|d\in\D_\mu}$. The $\H$--action on $M(\mu)$ is
determined by 
$$x_\mu T_dT_i=\begin{cases}
          qx_\mu T_d,&\If \len(dr_i)>\len(d)\And dr_i\not\in\D_\mu,\\
 \phantom q x_\mu T_{dr_i},&\If\len(dr_i)>\len(d)\And dr_i\in\D_\mu,\\
          qx_\mu T_{dr_i}+(q-1)x_\mu T_d,&\Otherwise.
\end{cases}$$
Note that if $\len(dr_i)<\len(d)$ then $dr_i\in\D_\mu$. 

Let $*\map\H\H$ be the $R$--linear map on $\H$ determined by
$T_w^* = T_{w^{-1}}$, for all $w\in\Sym_n$. This defines
an $R$-algebra anti--automorphism on $\H$ of order $2$.

The module $M(\mu)$ carries a symmetric bilinear form 
$\<\ ,\ \>_\mu$ given by 
$$
\<x_\mu T_a,x_\mu T_b\>_\mu \; =\;
   \begin{cases}
                  q^{\len(a)}, & \If a=b,\\
                  0,           & \Otherwise,
   \end{cases}
$$
for $a,b\in\D_\mu$. It follows from the formulae above that the form
$\<\ ,\ \>_\mu$ is associative in the sense that
$$
\<xh,y\>_\mu\; =\;\<x,y h^*\>_\mu\;
$$
for all $x,y\in M(\mu)$ and all $h\in\H$. 

We will need two dualities on the category of right $\H$--modules.
Both of them come from involutions on $\H$. The first duality comes
from the involution $*$ defined above. The second is induced from the
automorphism $\#\map\H\H$ which is the $R$--linear map on $\H$
determined by $T_w^\# = (-q)^{l(w)}T_{w^{-1}}^{-1}$, for all
$w\in\Sym_n$. It is straightforward to check that $\#$ preserves the
relations in $\H$ and, hence, that it is an $R$-algebra automorphism of order $2$.
Note that the involutions $\#$ and $*$ commute.

If $V$ is an $\H$-module let $V^*$ be its $R$-linear dual. Then $V^*$
becomes an $\H$--module by letting $(\phi\cdot\xi)(v) :=
\phi(v\xi^*)$, where $\phi\in V^*$, $v\in V$ and $\xi\in\H$. With the
according operation on morphisms, this
defines a contravariant self--equivalence on the category of
$\H$-modules.

If $V$ is an $\H$-module let $V^\#$ the $\H$-module with underlying
$R$-module $V$ and operation $v\cdot_\# \xi := v\cdot \xi^\#$, where $v\in V$ and
$\xi\in\H$. With the identical operation on morphisms, this defines a covariant 
self--equivalence on the category of $\H$-modules.
