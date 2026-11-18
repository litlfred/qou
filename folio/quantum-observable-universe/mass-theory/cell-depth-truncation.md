*Let $A=H_n(K,q)$ be split semisimple over a field $K$, with central primitive idempotents $e_\lambda$, irreducible characters $\chi_\lambda$ and GB-depth $a(\lambda)$ as in [`prop:cellular-depth-filtration`](#prop:cellular-depth-filtration). For a trace $\tau$ on $A$ and $x\in A$ put*
$$
E_k:=\sum_{a(\lambda)=k}e_\lambda,\qquad \mathfrak{m}^{(k)}_\tau(x):=\tau(E_kx),\qquad k_\star(x):=\max\{a(\lambda):\chi_\lambda(x)\ne0\}
$$
*($k_\star(x):=0$ if no $\chi_\lambda(x)$ is nonzero). Then for every trace $\tau$, every $x\in A$ and all weights $(\alpha_k)\subset K$:*

1. *$\mathfrak{m}^{(k)}_\tau(x)=0$ for all $k>k_\star(x)$;*
2. *$\sum_{k=0}^{K'}\alpha_k\mathfrak{m}^{(k)}_\tau(x)=\sum_{k=0}^{k_\star(x)}\alpha_k\mathfrak{m}^{(k)}_\tau(x)$ for every $K'\ge k_\star(x)$;*
3. *$\sum_{k=0}^{k_\star(x)}\mathfrak{m}^{(k)}_\tau(x)=\tau(x)$.*
4. *(Vacuous on braids.) If $x=T_w$ for some $w\in S_n$, or $x$ is the image of a braid, then $k_\star(x)=\binom n2$, the largest value of $a$. So the truncation in items 1–3 removes nothing on these inputs. (This item uses the Kazhdan–Lusztig cell facts cited in the proof; they are not formalised.)*
5. *(The truncated $\Phi_q$ product does not stabilise.) Let $F$ be a field, $q,z\in F^\times$ with $1-q^{-j}z\ne0$ for all $j\ge1$, and $\Phi_q^{[\le K']}(z):=\prod_{j=1}^{K'}(1-q^{-j}z)^{-1}$. Then $\Phi_q^{[\le K'+1]}(z)\ne\Phi_q^{[\le K']}(z)$ for every $K'$. Hence no sequence $S_{K'}$ can satisfy both $S_{K'}=\Phi_q^{[\le K']}(z)$ for all $K'$ and $S_{K'}=S_{k_0}$ for all $K'\ge k_0$.*

Items 1–3 hold for any function on partitions in place of $a$; the content of the statement is the choice of $a$, which comes from the Kazhdan–Lusztig two-sided ideals of $A$ and not from any mass datum. Item 5 shows that the identification of the level-$K'$ partial sum with $\sum_i\Phi_q^{[\le K']}(z_i)$ in [`conj:phi-q-categorical-truncation`](#conj:phi-q-categorical-truncation) cannot hold together with items 1–2. Setting the level-$k$ term equal to $\Phi_q^{[\le k]}(z_i)-\Phi_q^{[\le k-1]}(z_i)$ defines a different object from $\tau(E_kx)$, and the two must not share the symbol $\mathfrak{m}^{(k)}$.
