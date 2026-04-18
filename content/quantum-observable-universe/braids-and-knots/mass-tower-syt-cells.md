This remark reframes the pair blow-up set $\mathcal{P}_n$
([jet-brane reformulation](#rem:mass-endomorphism-jet-tower))
using the Jucys--Murphy (JM) elements and standard Young tableaux
(SYT).  The motivation: empirical probes show the optimal
$\mathcal{P}_n$ is *all pairs with no distance restriction*
([descent rate empirical](#sim:descent-rate-probe)), which
is most naturally expressed in the JM / SYT cell basis.

## Jucys--Murphy elements

For $H_n(q)$ with generators $T_1, \ldots, T_{n-1}$, the
**Jucys--Murphy (JM) elements** are

$$
  L_k = T_{k-1} T_{k-2} \cdots T_1 T_1 \cdots T_{k-1},
  \qquad k = 1, \ldots, n,
$$

with $L_1 = 1$.  They commute pairwise ($[L_i, L_j] = 0$) and
act diagonally on the Young basis: for a SYT $T$ of shape
$\lambda$ and basis vector $|T\rangle$,

$$
  L_k \, |T\rangle
  = q^{2 c_T(k)} \, |T\rangle,
$$

where $c_T(k) = j - i$ is the content of the cell of $T$
containing the integer $k$ (cell at row $i$, column $j$).

## SYT cell reindexing

The pair set $\mathcal{P}_n$ in
[jet-brane form](#rem:mass-endomorphism-jet-tower) is naturally
**cell-indexed** via JM:

$$
  \mathcal{P}_n
  \;\longleftrightarrow\;
  \{\{k_1, k_2\} \subseteq \{1, 2, \ldots, n\}\},
$$

with each pair $\{k_1, k_2\}$ corresponding to a pair of cells
in any SYT shape $\lambda \vdash n$.  Under this reindexing:

- **Generator distance $|i - j|$** is not preserved — JM indices
  $k$ range over cells, not over generator positions, so there is
  no "adjacent vs far-commuting" distinction.
- **Eigenvalue product** is diagonal: on $|T\rangle$,

  $$
    L_{k_1} L_{k_2} \, |T\rangle
    = q^{2(c_T(k_1) + c_T(k_2))} \, |T\rangle.
  $$

- **All pairs are on equal footing**: $[L_i, L_j] = 0$ by
  construction.  This matches the empirical finding that
  $\beta(d) = 1$ uniformly across distances
  ([descent rate probe](#sim:descent-rate-probe)).

## Reformulated mass tower

Using JM / SYT cells, the per-jet-level contribution becomes:

```tex
\begin{equation}\label{eq:syt-cell-tower}
  \mathfrak{m}^{(n)}(\varrho)
  =
  \bigl\lvert\textstyle\prod_{k=1}^{n} \hat V_k^{\mathrm{JM}}\bigr\rvert
  + \textstyle\sum_{k=1}^n \Phi_q(|\hat V_k^{\mathrm{JM}}|)
  + z^2 \textstyle\sum_{1 \leq k_1 < k_2 \leq n}
      \Phi_q(|\hat V_{k_1}^{\mathrm{JM}} \hat V_{k_2}^{\mathrm{JM}}|),
\end{equation}
```

where $\hat V_k^{\mathrm{JM}}$ is the Markov-trace-weighted
eigenvalue of $L_k$ in the braid word's irrep, weighted by the
Plancherel measure on $\lambda \vdash n$:

$$
  \hat V_k^{\mathrm{JM}}
  =
  \sum_{\lambda \vdash n} w_\lambda
    \sum_{T \in \mathrm{SYT}(\lambda)}
      \mu_T \cdot q^{2 c_T(k)},
$$

with $\mu_T$ = normalised SYT Plancherel weight.

## Advantages

1. **All pairs automatic.** $[L_i, L_j] = 0$ gives a symmetric
   pair sum with no adjacent/far distinction — consistent with the
   empirical $\beta(d) = 1$.
2. **Descent structure visible.** The descent involution acts on
   SYT shapes by box-removal: a jet-$(n+1)$ transient supported
   on a shape $\lambda \vdash n+1$ descends to jet-$n$ when the
   shape's removable corner is vacated.  This is the formal
   descent that the generator-indexed form struggles to express.
3. **Multi-level sum structural.** Summing over jet levels
   becomes summing over the SYT tree: each level adds one cell.
   The jet tower $\{A_n\}$ is built by box additions; the mass
   tower sums contributions at each addition.

## Implementation path

1. Compute $L_k$ seminormal eigenvalues $q^{2 c_T(k)}$ per SYT
   (already available via
   ``hecke_characters.build_seminormal_matrices`` in
   ``folio-assistant/computations/hecke_characters.py``).
2. Build $\hat V_k^{\mathrm{JM}}$ via Plancherel-weighted sum
   over SYTs.
3. Sum cell-pair Φ_q contributions (all $\binom{n}{2}$ pairs,
   no distance filter).
4. Iterate over jet levels $n = 0, 1, \ldots, N$ and sum.

Implementation is stubbed in the
[multi-level jet sum simulator](#sim:multi-level-jet-sum).

## Open question

Does the SYT-cell form reproduce the generator-indexed form at
each $n$, or only up to a descent involution?  Naively the two
should agree at the per-irrep level (change of basis within each
$V_\lambda$), but the *pair-count* and *independence-claim*
structure may differ, since JM pairs are always commuting and
have no "adjacent vs far" ambiguity.
