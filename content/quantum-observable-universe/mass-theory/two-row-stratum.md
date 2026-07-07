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

The :defterm[two-row projection]{#two-row-projection} is the orthogonal projection onto the two-row Wedderburn subalgebra:
$$
  \pi_{\mathrm{2-row}} \;\colon\; H_n(q) \;\to\;
    \bigoplus_{\lambda \in \Lambda^2(n)} \mathrm{End}(V_\lambda).
$$
The map is an idempotent ($\pi_{\mathrm{2-row}}^2 = \pi_{\mathrm{2-row}}$). The canonical Markov trace splits as:
$$
  \mathrm{tr}_M(\beta)
  \;=\; \underbrace{\sum_{\lambda \in \Lambda^2(n)} y_\lambda(q) \cdot \chi^\lambda_q(\beta)}_{\mathrm{tr}_M(\pi_{\mathrm{2-row}}\,\beta)}
  \;+\; \underbrace{\sum_{\ell(\lambda) > 2} y_\lambda(q) \cdot \chi^\lambda_q(\beta)}_{\mathrm{tr}_M((1-\pi_{\mathrm{2-row}})\,\beta)}
$$
where $y_\lambda$ is the Wenzl weight from [`prop:wedderburn-weight-canonical`](#prop:wedderburn-weight-canonical).

## Structural significance

The two-row stratum carries the $\mathrm{SU}(2)$ Schur–Weyl image. We restrict to the $\mathrm{SU}(2)$ action:
$$
  H_n(q) \;\twoheadrightarrow\; \mathrm{End}_{\mathrm{SU}(2)}\!\bigl(V^{\otimes n}\bigr),
\quad V = \mathbb{C}^2.
$$
Partitions with $\ell(\lambda) > 2$ map to zero. They correspond to higher-rank symmetry components absent from the $\mathrm{SU}(2)$ spin-pairing observable. The $q$-deformed spin observables, including the magic-shell coupling of `conj:magic-shell-stabilization`, live strictly in the two-row sector.

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

We compute the per-partition decomposition $c_\lambda := y_\lambda(q_0) \cdot \chi^\lambda_q(\beta_{^4\mathrm{He}})$ across all 77 partitions of 12. The two-row stratum $\Lambda^2(12)$ carries $86.6\,\%$ of the total trace $\mathrm{tr}_M(\beta_{^4\mathrm{He}})$. We formalize this in [`prop:he4-two-row-dominance`](#prop:he4-two-row-dominance).

We establish the identical pattern across the $\{D, T, {}^3\mathrm{He}, {}^4\mathrm{He}\}$ series. The dominant block for each atom always lies in $\Lambda^2(3A)$.
