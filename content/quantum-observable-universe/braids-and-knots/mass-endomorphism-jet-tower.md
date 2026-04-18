Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) with
substrate parameter $q$ and jet tower
$A_{n+1} = A_n \otimes \Omega^1(A_n)$
([recursive brane tower](#def:recursive-brane-tower)).  Let
$\hat{V}_i^{\mathrm{full},(n)}$ denote the additive Wedderburn
traced volume at generator $i$ evaluated at jet level $n$.

This remark reframes
([mass endomorphism tower](#prop:mass-endomorphism-tower))
in **jet-brane** language.

## Why quadratic per jet level is enough

The prop's formula keeps at most QUADRATIC $\hat{V}_i \hat{V}_j$
spectral coordinates (the $z^2 \Phi_q(|\hat V_i \hat V_j|)$ term)
and NO explicit triple or higher terms.  This is not a truncation
in the prop: it is the intended content.

$q$ calculations are not linear: the Hecke relation
$\sigma_i^2 = H_A \sigma_i + 1$ is quadratic, and the pentagon
identity of $\Phi_q$ ([quantum Bloch group](#def:quantum-bloch-group))
closes on pairs.  **Per jet level**, the mass formula therefore
contains:

- **$\hat V_i$ descended product** $\bigl\lvert\prod_i \hat V_i\bigr\rvert$
  (order-0: the saturated level-$n$ Markov trace).
- **$\Phi_q(|\hat V_i|)$ singletons** (order-1: single blow-up centres).
- **$z^2 \Phi_q(|\hat V_i \hat V_j|)$ pairs** (order-2: quadratic
  blow-up centres).

A triple / quadruple interaction at level $n$ is NOT an
independent order-3/4 term; it ASCENDS to jet level $n+1$ as a
new singleton/pair, and is already captured by the
level-$n+1$ contribution in the tower sum.  Conversely, some
level-$n+1$ quadratic interactions DESCEND to level-$n$ effective
pairs via the descent involution
([descent involution](#def:descent-involution)).

The full mass is therefore a tower sum of per-level quadratic
contributions:

```tex
\begin{equation}\label{eq:jet-tower-mass}
  \mathfrak{m}(\varrho)
  =
  \sum_{n=0}^{N}
    \Bigl(
    \underbrace{\bigl\lvert\textstyle\prod_i \hat V_i^{(n)}\bigr\rvert}_{\text{desc}}
    + \underbrace{\textstyle\sum_i \Phi_q(|\hat V_i^{(n)}|)}_{\text{singletons}}
    + \underbrace{z^2 \textstyle\sum_{\{i,j\} \in \mathcal{P}_n}
       \Phi_q(|\hat V_i^{(n)} \hat V_j^{(n)}|)}_{\text{quadratic pairs}}
    \Bigr)
\end{equation}
```

where $\mathcal{P}_n$ is the set of **independent pair blow-up
centres at jet level $n$** — the open question is exactly WHICH
pairs $(i, j)$ are in $\mathcal{P}_n$.

## Empirical correction to $\mathcal{P}_n$

The prop asserts $\mathcal{P}_n = \{(i, j) : |i - j| = 1\}$
(adjacent pairs only).  The justification via far-commutativity
gives no independent blow-up centre for $|i - j| \geq 2$ is
[audited as asserted-without-proof](#rem:mass-endomorphism-tower-adjacency-audit)
and empirically contradicted on stable atoms $A \geq 6$:

| Atom | adjacent $\mathcal{P}$ | all-pairs $\mathcal{P}$ |
|:-----|:-----------------------|:------------------------|
| 6Li  | 2.00%  | 0.57% |
| 9Be  | 1.91%  | 0.70% |
| 10B  | 2.35%  | 0.70% |
| 12C  | 2.34%  | 0.83% |
| 14N  | 2.44%  | 0.81% |
| 16O  | 2.45%  | 0.86% |

Including all pair centres closes the 2–3% heavy-atom bias to
under 1%, consistent with $\mathcal{P}_n = \{(i,j) : i < j\}$
(full quadratic pairs, no distance restriction).

Triple terms with $z^3 \Phi_q(|\hat V_i \hat V_j \hat V_k|)$
OVERSHOOT the target (0.6–1.3% at the same atoms), confirming
that higher-order terms should be handled by ascension to the
next jet level, NOT by adding explicit cubic terms at level $n$
([empirical witness](#sim:adjacent-vs-full-probe)).

## Open subconjectures

1. **Exact $\mathcal{P}_n$**: is it all pairs at every level, or
   do some pairs descend to singletons?  The empirical fit
   prefers all-pairs; proof/derivation from the descent involution
   is open.
2. **Jet-level sum convergence**: how many jet levels $N$ does
   the tower sum need before saturating?  The tower-binding-full
   simulator uses $n = 3A$ directly at one level; a genuinely
   multi-level jet sum is not yet implemented.
3. **Descent involution on pairs**: does $\hat\tau_n$ map some
   level-$(n+1)$ pairs back to level-$n$ singletons (or trivial)?
   If yes, partial descent explains why all-pairs works better
   than both adjacent-only and naive all-subsets.
