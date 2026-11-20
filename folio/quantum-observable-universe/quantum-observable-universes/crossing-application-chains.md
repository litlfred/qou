Fix $n \geq 2$ strands. A *tick* is one application of a crossing. On words in the generators $\sigma_1, \ldots, \sigma_{n-1}$, a tick appends one letter, $w \mapsto w\,\sigma_i$. On a monoid $G$ of states with crossing elements $s_1, \ldots, s_{n-1}$, a tick is $g \mapsto g\,s_i$. A *closed chain* through $x$ is a finite chain of ticks from $x$ back to $x$.

(a) Every tick on words is a strict $\prec_c$-step, so no word lies on a closed chain. This holds for every braiding.

(b) Suppose there is a homomorphism $\chi \colon G \to \mathbb{Z}$ with $\chi(s_i) = 1$ for all $i$. Then no state lies on a closed chain. The braid group $B_n$ with its writhe (total exponent sum) is an example.

(c) Suppose some crossing has finite order, $s_i^{k+1} = 1$. Then every state lies on a closed chain. In particular, this holds when $s_i^{2} = 1$, as for the adjacent transpositions in $S_n$, the image of $B_n$ under a symmetric braiding.

Neither (b) nor (c) covers every state monoid. For example, for $H_n(q)$ at generic $q$ neither condition is established here.
