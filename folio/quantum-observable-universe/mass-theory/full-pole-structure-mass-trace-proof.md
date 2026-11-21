## Proof

*Part 1.* Induct on $n$. On $H_1(q) = R$ the trace is $\mathrm{tr}_M(1) = 1$. For $w \in S_{n+1} \setminus S_n$ the coset decomposition gives $T_w = T_u\,\sigma_n\,T_v$ with $u, v \in S_n$, so the Markov property and cyclicity give
$\mathrm{tr}_M(T_w) = z\,\mathrm{tr}_M(T_v T_u)$.
The product $T_v T_u$ expands in the standard basis of $H_n(q)$ with coefficients in $\mathbb{Z}[h]$, because the only relation used is $\sigma_i^{2} = h\,\sigma_i + 1$. By induction each $\mathrm{tr}_M(T_x)$, $x \in S_n$, is a polynomial in $z$ of degree at most $n-1$ over $\mathbb{Z}[h]$, so $\mathrm{tr}_M(T_w)$ has degree at most $n$. For $w \in S_n$ the induction hypothesis applies directly. Since $h \in \mathbb{Z}[q^{\pm 1}]$ and $(q^{2}+1)z = q^{3}$, multiplying by $(q^{2}+1)^{n-1}$ clears every denominator.

*Part 2.* $\mathbb{Z}[q^{\pm1}] \subset \widehat{\mathbb{Z}[q]}$ because $q$ is a unit there. Sequential division by $(1 - q^{m+1})$ produces the coefficients $a_m$ ([atomic Habiro expansion](#cor:habiro-expansion-atomic), Step 2) \cite{habiro2004}.

*Part 3.* Evaluation at a root of unity is a ring homomorphism on $\widehat{\mathbb{Z}[q]}$. If $z$ lay in $\widehat{\mathbb{Z}[q]}$, applying evaluation at $q = i$ to $(1+q^{2})z = q^{3}$ would give $0 = -i$. $\square$

## Inadequacy of the previous wording

Two specific failures of the "meromorphic on $\mathbb{C}$" picture:

1. **Density on $S^1$.** The set
 $\{\zeta_n^{(j)} : \gcd(j,n)=1, n \geq 2\}$ is dense in $S^1$.
 A meromorphic function on a connected open set has only
 isolated poles; with poles dense in $S^1$ the only consistent
 picture is that $S^1$ is a natural boundary, and there is no
 single connected meromorphic continuation across it. The Habiro
 ring sidesteps this by working in the cyclotomic completion of
 $\mathbb{Z}[q]$, where evaluation at each root of unity is
 defined polynomially without any complex-analytic continuation.
2. **Convergence.** The Cauchy-kernel partial sum
 $\sum_{n \leq N} \sum_j r_n^{(j)}/(q - \zeta_n^{(j)})$ does not
 converge uniformly on any neighbourhood that crosses $S^1$.
 The Habiro expansion converges in the $q$-adic
 $((q;q)_\bullet)$-topology by construction, and reduces
 modulo $(q;q)_m$ at every truncation order.

This proposition replaces the earlier "meromorphic with poles at
all primitive roots of unity" wording with the algebraically
correct Habiro-ring statement; the residue spectral sum
([GB residue spectral sum](#prop:gb-residue-spectral-sum)) is
retained as the **symbolic feeding lemma** that produces the
cyclotomic coefficients $a_m$ from the Wedderburn-stratum residues
$r_n^{(j)}$, but is no longer claimed to define a global
$\mathbb{C}$-meromorphic function.
