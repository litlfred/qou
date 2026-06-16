This remark reframes the pair blow-up set $\mathcal{P}_n$
([jet-brane reformulation](#rem\:mass-endomorphism-jet-tower))
using the Jucys--Murphy (JM) elements and standard Young tableaux
(SYT). The motivation: empirical probes show the optimal
$\mathcal{P}_n$ is *all pairs with no distance restriction*
([:refterm[descent]{#descent} rate empirical](#sim\:descent-rate-probe)), which
is most accordingly expressed in the JM / SYT cell basis.

## Jucys--Murphy elements

For $H_n(R, q)$ with generators $\sigma_1, \ldots, \sigma_{n-1}$, the
**Jucys--Murphy (JM) elements** are

$$
  L_k = \sigma_{k-1} \sigma_{k-2} \cdots \sigma_1 \sigma_1 \cdots \sigma_{k-1},
  \qquad k = 1, \ldots, n,
$$

with $L_1 = 1$. They commute pairwise ($[L_i, L_j] = 0$) and
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
[jet-brane form](#rem\:mass-endomorphism-jet-tower) is accordingly
**cell-indexed** via JM:

$$
  \mathcal{P}_n
  \;\longleftrightarrow\;
  \{\{k_1, k_2\} \subseteq \{1, 2, \ldots, n\}\},
$$

with each pair $\{k_1, k_2\}$ corresponding to a pair of cells
in any SYT shape $\lambda \vdash n$. Under this reindexing:

* **Generator distance $|i - j|$** is not preserved — JM indices
 $k$ range over cells, not over generator positions, so there is
 no "adjacent vs far-commuting" distinction.

* **Eigenvalue product** is diagonal: on $|T\rangle$,

 $$
    L_{k_1} L_{k_2} \, |T\rangle
    = q^{2(c_T(k_1) + c_T(k_2))} \, |T\rangle.
  $$

* **All pairs are on equal footing**: $[L_i, L_j] = 0$ by
 construction. This matches the empirical finding that
 $\beta(d) = 1$ uniformly across distances
 ([:refterm[descent]{#descent} rate probe](#sim\:descent-rate-probe)).

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

The pair weight $z^2$ in the cross sum matches the generator-indexed
form of [prop:mass-endomorphism-tower](#prop\:mass-endomorphism-tower)
and is justified universally (all $k_1 < k_2$, not just adjacent
pairs) by the
[Markov-trace factorization theorem](#thm\:markov-trace-factorization):
two successive Markov peels of commuting elements each contribute a
factor $z$, so $\mathrm{tr}_M(L_{k_1} L_{k_2}) = z^2$. In the JM /
SYT reindexing this is automatic — $[L_i, L_j] = 0$ makes every pair
structurally equivalent to the far-commuting case covered by the
factorization theorem.

## Advantages

1. **All pairs automatic.** $[L_i, L_j] = 0$ gives a symmetric
 pair sum with no adjacent/far distinction — consistent with the
 empirical $\beta(d) = 1$.
2. **:refterm[Descent]{#descent} structure visible.** The :refterm[descent]{#descent} involution acts on
 SYT shapes by box-removal: a jet-$(n+1)$ transient supported
 on a shape $\lambda \vdash n+1$ descends to jet-$n$ when the
 shape's removable corner is vacated. This is the formal
 :refterm[descent]{#descent} that the generator-indexed form struggles to express.
3. **Multi-level sum structural.** Summing over jet levels
 becomes summing over the SYT tree: each level adds one cell.
 The jet tower $\{A_n\}$ is built by box additions; the mass
 tower sums contributions at each addition.

## Implementation path

1. Compute $L_k$ seminormal eigenvalues $q^{2 c_T(k)}$ per SYT
 (already available via
 `hecke_characters.build_seminormal_matrices` in
 `computations/hecke/hecke_characters.py`).
2. Build $\hat V_k^{\mathrm{JM}}$ via Plancherel-weighted sum
 over SYTs.
3. Sum cell-pair Φ\_q contributions (all $\binom{n}{2}$ pairs,
 no distance filter).
4. Iterate over jet levels $n = 0, 1, \ldots, N$ and sum.

Implementation is stubbed in the
[multi-level jet sum simulator](#sim\:multi-level-jet-sum).

## Empirical validation

A first-pass implementation
(`computations/syt_cell_tower.py`) computes
$\hat V_k^{\mathrm{JM}}$ for $k = 1, \ldots, 3A$ on the atom braid
word and assembles the tower of
equation\~\ref{eq:syt-cell-tower}. Against the scalar all-pairs form
of [prop:mass-endomorphism-tower](#prop\:mass-endomorphism-tower),
with $E_0$ calibrated per path on the proton:

| Atom | scalar all-pairs | JM all-pairs |
| ---- | ---------------: | -----------: |
| D | 0.120% | 0.105% |
| T | 18.0% | **0.277%** |
| 3He | 60.1% | **0.219%** |

The scalar path suffers a pair-pathology on T and 3He even after
[mass-endomorphism-tower.md](#prop\:mass-endomorphism-tower)'s
all-pairs form is used; the JM path closes the residual by carrying
the per-SYT content structure missing from a scalar factorization.

## Open question

Does the SYT-cell form reproduce the generator-indexed form at
each $n$, or only up to a :refterm[descent]{#descent} involution? Naively the two
should agree at the per-irrep level (change of basis within each
$V_\lambda$), but the *pair-count* and *independence-claim*
structure may differ, since JM pairs are always commuting and
have no "adjacent vs far" ambiguity — a distinction now formally
absorbed into the
[Markov-trace factorization theorem](#thm\:markov-trace-factorization).
The T/3He residual closure in the table above suggests the JM
form is not only a basis change: it captures SYT-content
correlations that the scalar factorization drops.
