*Let $K$ be a field and $q\in K^\times$ such that $H_n=H_n(K,q)$ is split semisimple, let $\{e_\lambda\}_{\lambda\vdash n}$ be its central primitive idempotents, and let $Z=Z(H_n)$. For a function $\delta$ from partitions of $n$ to $\mathbb N$, the cellular $\delta$-filtration of $Z$ is*
$$
F^\delta_k := \operatorname{span}_K\{e_\lambda : \delta(\lambda)\le k\},\qquad k\in\mathbb N.
$$
*The* GB-depth *of $\lambda$ is Lusztig's $a$-function of the two-sided Kazhdan–Lusztig cell of shape $\lambda$, which in the labelling where $(n)$ is the index representation is*
$$
a(\lambda)=\sum_i\binom{\lambda_i}{2}.
$$
*Write $n(\lambda)=\sum_i(i-1)\lambda_i$, so that $a(\lambda')=n(\lambda)$. Let $\#$ be the Goldman involution $\sigma_i\mapsto-\sigma_i^{-1}$, which satisfies $\#(e_\lambda)=e_{\lambda'}$ ([Schur-Weyl justification of shell-operator self-duality](#prop:shell-schur-weyl-self-duality)). Then:*

1. *(Filtration by ideals.) For every $\delta$: $F^\delta_j\subseteq F^\delta_k$ for $j\le k$; $F^\delta_j\cdot F^\delta_k\subseteq F^\delta_{\min(j,k)}$, so each $F^\delta_k$ is an ideal of $Z$; and $1\in F^\delta_k$ if and only if $k\ge\max_\lambda\delta(\lambda)$. So if $\delta>0$ somewhere, $F^\delta$ is not a unital algebra filtration.*
2. *(Transport by $\#$.) $\#(F^\delta_k)=F^{\delta\circ t}_k$, where $t(\lambda)=\lambda'$. For the GB-depth this reads $\#(F^a_k)=F^{n}_k$. For $n\ge2$ the GB-depth filtration is not $\#$-stable: $F^a_0=Ke_{(1^n)}$ and $\#(F^a_0)=Ke_{(n)}$. A depth $\delta$ gives a $\#$-stable filtration if and only if $\delta(\lambda')=\delta(\lambda)$ for all $\lambda$; examples are the symmetrised depth $a(\lambda)+a(\lambda')$ and the max-hook depth $\lambda_1+\lambda'_1-1$.*
3. *(Eigenvectors.) $e_\lambda$ is $\#$-fixed if and only if $\lambda=\lambda'$. For $\lambda\ne\lambda'$, $e_\lambda+e_{\lambda'}$ and $e_\lambda-e_{\lambda'}$ are $(+1)$- and $(-1)$-eigenvectors. If $\operatorname{char}K\ne2$, then $Z=Z^+\oplus Z^-$ with $\dim Z^\pm=\tfrac12\bigl(p(n)\pm sc(n)\bigr)$, where $sc(n)$ is the number of self-conjugate partitions of $n$.* (This dimension count follows by counting the eigenvectors above; it is not formalised.)
4. *(Conditional parity transfer.) Let $P$ be a $K$-vector space with a linear involution $\iota$ and projections $\pi_d$, let $\Phi:Z\to P$ be linear, and assume $\operatorname{char}K\ne2$ together with the hypotheses* (H-match) $\Phi\circ\#=\iota\circ\Phi$ *and* (H-parity) $\pi_d\circ\iota=(-1)^d\pi_d$. *Then $\pi_d\Phi(e_\lambda)=0$ for odd $d$ when $\lambda=\lambda'$; $\pi_d\Phi(e_{\lambda'})=(-1)^d\pi_d\Phi(e_\lambda)$ for all $\lambda$; and for odd $d$, $\pi_d\Phi(e_\lambda)\ne0$ if and only if $\pi_d\Phi(e_\lambda)\ne\pi_d\Phi(e_{\lambda'})$.*

Item 4 is the provable part of [Two-filtration bridge map in full generality](#conj:two-filtration-bridge-general). It does not depend on the depth filtration at all: it is a statement about the idempotents $e_\lambda$. Neither (H-match) nor (H-parity) is established in the corpus, and the values $2$ and $3$ of that conjecture need an additional non-vanishing that item 4 does not give. Item 2 shows that the GB-depth filtration and the transposition $\lambda\mapsto\lambda'$ are not compatible, so the parity picture cannot be phrased as "$\#$ preserves GB-depth".

The statistic $\lambda_1+\lambda'_1-1$ (maximal hook length), which earlier versions of the corpus called GB-depth, is called the max-hook depth here.
