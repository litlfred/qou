## Definition

Let $H_n(q)$ be the Iwahori–Hecke algebra on $n$ strands. It admits the canonical Wedderburn decomposition
$$
  H_n(q) \;\cong\; \bigoplus_{\lambda \vdash n} \mathrm{End}(V_\lambda)
$$
indexed by partitions $\lambda \vdash n$. The :defterm[two-row stratum]{#two-row-stratum} contains the partitions with at most two parts:
$$
  \Lambda^2(n) \;:=\; \{\, \lambda \vdash n : \ell(\lambda) \le 2 \,\}
  \;=\; \{\, (n-k, k) : 0 \le k \le \lfloor n/2 \rfloor \,\}.
$$

The orthogonal projection onto this two-row Wedderburn subalgebra — the two-row projection $\pi_{\mathrm{2-row}}$ — and the induced splitting of the canonical Markov trace are given in [Two-row projection $\pi_{\mathrm{2-row}}$ onto the two-row Wedderburn subalgebra](#def:two-row-projection).

## Structural significance

The two-row stratum carries the $\mathrm{SU}(2)$ Schur–Weyl image. We restrict to the $\mathrm{SU}(2)$ action:
$$
  H_n(q) \;\twoheadrightarrow\; \mathrm{End}_{\mathrm{SU}(2)}\!\bigl(V^{\otimes n}\bigr),
\quad V = \mathbb{C}^2.
$$
Partitions with $\ell(\lambda) > 2$ map to zero. They correspond to higher-rank symmetry components absent from the $\mathrm{SU}(2)$ spin-pairing observable. The $q$-deformed spin observables, including the magic-shell coupling of `conj:magic-shell-stabilization`, live strictly in the two-row sector.

**Scope of the two-row stratum: it is the whole support, in the trace and in the binding sum alike.** Under the production convention D the restriction is not a dominance but an identity. The Wenzl weight satisfies $y_\lambda = 0$ exactly when $\ell(\lambda) \geq 3$, because the Schur–Weyl fibre is the two-dimensional fundamental of $\mathrm{SU}_q(2)$; so every $\ell(\lambda) > 2$ term of $\mathrm{tr}_M = \sum_\lambda y_\lambda \chi^\lambda$ vanishes, and so does every $\ell(\lambda) > 2$ term of the binding sum $\sum_\lambda y_\lambda \chi^\lambda \Delta_\lambda$ — the factor $\Delta_\lambda = (-1)^{n(\lambda)} f^\lambda$ multiplies a weight that is already zero. The binding sum therefore **does** inherit the restriction, at every $A$, exactly.

**Two-row concentration under Convention D.** While $\Delta_\lambda$ in isolation grows largest on balanced many-row diagrams, under Convention D all weights with $\ell(\lambda) > 2$ vanish identically ($y_\lambda = 0$), so only the two-row stratum $\Lambda^2(n)$ contributes to the ordinary Markov trace.

## Indexing the stratum

We have $|\Lambda^2(n)| = \lfloor n/2 \rfloor + 1$. For the $^4\mathrm{He}$ strand count ($n = 12$), we obtain **7** partitions:
$$
\Lambda^2(12) = \{(12), (11,1), (10,2), (9,3), (8,4), (7,5), (6,6)\}.
$$

Distinguished partitions include:
- $\lambda = (n)$: the trivial representation. It is one-dimensional, $V_{(n)} = \mathbb{C}$.
- $\lambda = (n-1, 1)$: the standard representation. It has dimension $n - 1$.
- Self-conjugate $\lambda \in \Lambda^2(n)$: this is only $(n/2, n/2)$ for even $n$, the **balanced two-row** partition. For $n = 12$, this is $(6, 6)$.

The non-self-conjugate partitions $(n-k, k)$ with $k < n/2$ form mirror pairs under the bar involution $q \mapsto q^{-1}$. The conjugate partition $(n-k, k)'$ exits $\Lambda^2(n)$, so each $(n-k, k)$ pairs with itself under the involution.

## Empirical use

We compute the per-partition decomposition $c_\lambda := y_\lambda(q_0) \cdot \chi^\lambda_q(\beta_{^4\mathrm{He}})$ across all 77 partitions of 12. The two-row stratum $\Lambda^2(12)$ carries the total trace $\mathrm{tr}_M(\beta_{^4\mathrm{He}})$ **exactly** — $100\,\%$, not as a measurement but as an identity, since $y_\lambda = 0$ for the $70$ partitions of $12$ with $\ell(\lambda) > 2$. The figure $86.6\,\%$ previously quoted here is the convention-C value and is withdrawn (2026-08-09); with it goes the reading of the result as a *dominance* rather than a support statement. We formalize this in [Two-row stratum carries $\ge 80\%$ of $\mathrm{tr}_M(\beta_{^4\mathrm{He}})$ at $q_0$ (exactly $1$ empirically)](#prop:he4-two-row-dominance).

We establish the identical pattern across the $\{D, T, {}^3\mathrm{He}, {}^4\mathrm{He}\}$ series. The dominant block for each atom always lies in $\Lambda^2(3A)$.
