**Remark (per-partition $k_\lambda$ — the open structural form of $n_\star$).**

The level-selection rule $n_\star$ of
[conj:brane-tower-z-habiro](#conj:brane-tower-z-habiro) was tested
empirically against the AME light-isotope sample $\{D, T, {}^3\mathrm{He}\}$
under three increasingly-refined ansatze, and is now sharpened to the
following structural form. The progression of refutations
(PR #638) and partial closures (PR #639) localises the open piece.

## Refutation chain (substrate-only scalar candidates)

| Form of $n_\star$ | Verdict | Witness |
|:---|:---:|:---|
| Scalar-eigenvalue family (uniform $k$, GB grade, additive $\ell n_0 + k$) | **refuted** | PR #638 §"Closure (2026-05-11): scalar-eigenvalue form…" |
| Per-eigenvalue operator-valued ($\Phi_q$ per $\mu_a^{(\lambda)}$, signed) | **refuted** at uniform $k$ | PR #638 §"Operator-valued probe" |
| Type-B-folded-crystal depth ($\#\{\lambda \vdash 3A : \lambda = \lambda^T\}$) | **partial** — fits $D$ and $T$, fails ${}^3\mathrm{He}$ | [probe-phiq-type-b-fold-depth.witness.json](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/probe-phiq-type-b-fold-depth.witness.json) (PR #639) |
| Type-B + scalar near-pole multiplicity $m$ (4 two-input rules) | **refuted** | [probe-phiq-multiplicity-refinement.witness.json](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/probe-phiq-multiplicity-refinement.witness.json) (PR #639) |

## Sharpened open form: per-partition $k_\lambda$

PR #639's analysis of #638's per-eigenvalue spectra showed that the
**failure at uniform $k = 2$ is dominated by ONE partition per atom**:

| Atom | dominant $\lambda$ | $\dim V_\lambda$ | $\text{contrib}_\lambda(k=2)$ | $\text{contrib}_\lambda(k=1)$ |
|:---|---:|---:|---:|---:|
| $D$ | $[2, 2, 1, 1]$ | $9$ | $-6.220$ | $\approx 0$ |
| $T$ | $[6, 3]$ | $48$ | $-3.001$ | $+0.050$ |
| ${}^3\mathrm{He}$ | $[5, 4]$ | $42$ | $-11.692$ | $-0.028$ |

Re-assigning $k_\lambda = 1$ for the dominant partition while keeping
$k_\lambda = 2$ for the other 29-or-so partitions collapses each
atom's total tower magnitude to $\lvert\mathrm{tower}\rvert < 2$
(vs uniform-$k$ towers in the range $5$–$11$).

This is the **sufficient relaxation** — non-uniform truncation
across Wedderburn blocks closes the gap that *no* scalar rule
(fold depth alone, $m_{\text{near-pole}}$ alone, or any 2-input
combination) could close at uniform $k$. The surviving open form
of the conjecture is:

> **Per-partition $k_\lambda$ form of $n_\star$.** *There exists a
> substrate-derivable map*
>
> $$
>   k_\lambda \;\colon\; \{\text{partitions of } 3A\}
>   \;\longrightarrow\; \mathbb{N}_{\geq 1},
> $$
>
> *such that*
>
> $$
>   \mathrm{tower}_{\mathrm{op}}^{(k_\lambda)}(\beta_\mathfrak{H})
>   \;:=\;
>   \Biggl\lvert
>   \sum_\lambda y_\lambda(q_0) \cdot
>     \sum_{a=1}^{\dim V_\lambda}
>       \Phi_q^{[\leq k_\lambda]}\bigl(\mu_a^{(\lambda)}\bigr)
>   \Biggr\rvert
> $$
>
> *closes the AME light-isotope binding* $B(\mathfrak{H})$ *to within
> $\sim 5\%$ across* $\{D, T, {}^3\mathrm{He}\}$ *without per-atom
> retuning of the rule itself.*

The empirical evidence
([probe-phiq-per-partition-klambda.witness.json](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/probe-phiq-per-partition-klambda.witness.json))
shows that the rule

$$
  k_\lambda = \begin{cases}
    1 & \text{if } \lambda \text{ is the maximum-} \lvert\mu\rvert \text{ partition of } \beta_\mathfrak{H}, \\
    2 & \text{otherwise}
  \end{cases}
$$

closes all three atoms simultaneously. The "max-$\lvert\mu\rvert$"
selector is a substrate property of the **braid word**'s action on
$V_\lambda$, not just of $\lambda$ in isolation — it distinguishes
${}^3\mathrm{He}$ (max $\lvert\mu\rvert \approx 10.69$ at $[5, 4]$)
from $T$ (max $\lvert\mu\rvert \approx 8.23$ at $[4, 3, 1, 1]$)
despite identical strand count $n = 9$.

## Why this is structurally meaningful

The eigenvalue magnitudes of $\rho_\lambda(\beta)$ in the Hoefsmit
seminormal form depend on **both** the partition $\lambda$ and the
braid word $\beta$. For a given $\lambda$, larger $\lvert\mu\rvert$
indicates the braid word's action has higher "winding" or
"twist" content in that Wedderburn block. The empirical pattern —
that *the* maximum-$\lvert\mu\rvert$ partition is the one requiring
shallower truncation — is consistent with the dilogarithm tail
intuition: deeper truncation $\Phi_q^{[\leq k]}$ amplifies
contributions of large-magnitude eigenvalues
(each factor $1/(1 - q^{-j} \mu)$ for fixed $j$ becomes more
sensitive to $\lvert\mu\rvert$ as $k$ grows).

## What this rules in / out

**Rules in:**

* The Wedderburn-decomposition of the brane-tower operator is the
  **correct level of structure** at which to formulate $n_\star$ —
  not a single scalar invariant per atom.
* The eigenvalue-magnitude profile of $\rho_\lambda(\beta_\mathfrak{H})$
  carries the multiplicity information that scalar substrate
  invariants miss.

**Rules out:**

* Any *uniform* $n_\star \in \mathbb{N}$ per atom (closed at uniform
  $k$ for at most $2/3$ of $\{D, T, {}^3\mathrm{He}\}$).
* Any rule constructed from scalar partitions of $(\ell, n_0, k, m)$
  alone (the four-tuple's $m$ is per-atom, not per-partition).

## Open structural question

The remaining identification problem:

> *Express the empirical selector "$\lambda$ has the maximum
> $\lvert\mu\rvert$ in the spectrum of $\rho_\lambda(\beta)$" as a
> **closed-form structural rule** in terms of substrate data
> (the braid word $\beta$, the partition $\lambda$, and substrate
> constants $q_0$, $\hbar_q$) — without empirical evaluation of
> the eigenvalue spectrum.*

Candidate routes:

* **Hoefsmit hook-content asymptotic.** The maximum eigenvalue of
  $\rho_\lambda(\sigma_i)$ in the Hoefsmit seminormal form is
  bounded by a hook-content product over the Young diagram of
  $\lambda$. Iterating along a braid word's reduced expression
  gives an a-priori upper bound on $\max \lvert\mu\rvert$ — possibly
  large enough to select the dominant partition combinatorially.
* **Type-B-folded-crystal weight asymptotic** (the natural next
  refinement of [audit-2026-05-11-type-b-fold-depth-n-star.md](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-11-type-b-fold-depth-n-star.md)).
* **Symbolic action of $\beta$ in the Kashiwara crystal.** The
  combinatorial action of the braid word on Young tableaux may
  identify the dominant partition without numerical eigenvalue
  evaluation.

Closure of this open form would constitute the structural lift
formula of [conj:brane-tower-z-habiro](#conj:brane-tower-z-habiro) — the missing piece flagged in
that conjecture's "Status of $n_\star$" section.
