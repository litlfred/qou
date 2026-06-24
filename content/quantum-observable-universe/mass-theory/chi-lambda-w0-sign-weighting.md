*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

The empirical $c_k$ chain at $H_3$ (extracted from the
$\varepsilon^{2k}$ coefficients of $\chi_\lambda(\mathcal{B}_n; q) - \chi_\lambda(\mathcal{B}_p; q)$
at $q = 1 + \varepsilon$ per
[`rem:chi-per-irrep-cyclotomic-closed-forms`](#rem:chi-per-irrep-cyclotomic-closed-forms))
does **not** match a uniform Plancherel-weighted sum
$\sum_\lambda w_\lambda \cdot c_k^{(\lambda)}$ with the canonical
$w_\lambda = (\dim V_\lambda)^2 / n!$: the Plancherel-weighted
sum has the **wrong sign** at both $k = 5$ and $k = 6$ (see the
`per-wedderburn-block-ck` probe witness's `c5_match_status` and
`c6_match_status` fields).

This proposition identifies the **correct weighting**: the
**character values at the long element** $w_0 \in S_3$, i.e.
$\chi_\lambda(w_0) = (1, 0, -1)$ for $\lambda \in \{(3), (2,1), (1,1,1)\}$.

## Statement

**Proposition.**
*Let $\mathcal{B}_p, \mathcal{B}_n \in \mathbf{B}_3$ be the canonical typed-braid
representatives of the proton and neutron, and define*

$$
  c_k^{(\lambda)} \;:=\; [\varepsilon^{2k}]\,
  \bigl(\chi_\lambda(\mathcal{B}_n;\,q) - \chi_\lambda(\mathcal{B}_p;\,q)\bigr)\Big|_{q = 1 + \varepsilon}
  \qquad (\lambda \vdash 3,\ k \geq 0).
$$

*Let $w_0 \in S_3$ denote the longest element (the unique element
of length $3$ in the Coxeter realisation; equivalently the
order-reversing involution $(1\,3)$ in cycle form). Then the
character-weighted sum*

$$
  S_k^{(w_0)} \;:=\; \sum_{\lambda \vdash 3}
    \chi_\lambda(w_0) \cdot c_k^{(\lambda)}
  \;=\; c_k^{(3)} \;-\; c_k^{(1,1,1)},
$$

*has the same sign as the empirical $c_k$ measured by the
Wenzl-bridge Markov trace at $H_3$
([`prop:alpha-k-derivation-procedure`](#prop:alpha-k-derivation-procedure))
for $k = 5$ and $k = 6$. The character values used are the
standard $S_3$ irreducible-character evaluations at the long
element:*

| $\lambda \vdash 3$ | irrep | $\dim V_\lambda$ | $\chi_\lambda(w_0)$ |
|--------------------|-------|------------------|---------------------|
| $(3)$              | trivial | $1$ | $+1$ |
| $(2,1)$            | standard (Hoefsmit) | $2$ | $0$ |
| $(1,1,1)$          | sign | $1$ | $-1$ |

## Numerical verification

From [`per-wedderburn-block-ck.witness.json`](https://github.com/litlfred/qou/blob/main/computations/per-wedderburn-block-ck.witness.json)
( merge, per-Wedderburn-block probe at $q = 1 + \varepsilon$
to order $\varepsilon^{12}$):

| $k$ | $c_k^{(3)}$ | $c_k^{(2,1)}$ | $c_k^{(1,1,1)}$ | $S_k^{(w_0)}$ | empirical $c_k$ | sign agreement |
|----:|------------:|--------------:|----------------:|--------------:|----------------:|:--------------:|
| $5$ ($\varepsilon^{10}$) | $0.25$ | $16.25$ | $266.5$ | $-266.25$ | $-395.41$ | ✓ |
| $6$ ($\varepsilon^{12}$) | $0.25$ | $22.5$ | $477.5$ | $-477.25$ | $-45485$ | ✓ |

Both signs agree. The magnitude ratios are
$|\text{empirical}/S_k^{(w_0)}| \approx 1.49$ at $k = 5$ and
$\approx 95.3$ at $k = 6$; the $S_3$ character weights are **necessary
but not sufficient** for full magnitude closure. The residual
factor must come from cross-block coupling (e.g. via the
$\sigma_1$ matrix elements that mix the 2-dimensional $V_{(2,1)}$
into the per-block-diagonal sum).

## Why $w_0$ and not $-I$

The probe agent that surfaced this finding informally referred to
the weighting as "character $\chi_\lambda(-I)$." In the symmetric
group $S_n$ realised as a Coxeter group, "$-I$" has no canonical
meaning (the group is not realised as matrices acting on a real
vector space with a $-I$ element); the closest analog is the
**longest element** $w_0 \in S_n$, which is the unique involution
of maximal length and plays the role of "central reversal." For
$S_3$ specifically, $w_0 = (1\,3)$ is the order-reversing
transposition, and its character values agree with the
informal "$-I$" reading because $w_0 \cdot w_0 = 1$ (involution)
and the irreducible $S_3$-characters on involutions are
$\chi_{(3)} = 1, \chi_{(2,1)} = 0, \chi_{(1,1,1)} = \mathrm{sgn}(w_0) = -1$.

The substantive content of the proposition is therefore: **the
$c_k$ Markov-trace decomposition is governed by the long-element
character, not the identity character**. This is consistent with
the Coxeter-theoretic role of $w_0$ as the maximal mixing element.

## Open: magnitude closure

The proposition closes the **sign** at $k = 5, 6$. The **magnitude**
ratios ($1.49\times$ at $c_5$, $95.3\times$ at $c_6$) remain open.
Candidate refinements:

1. **Cross-block coupling via $\sigma_1$ matrix elements.** The
   $V_{(2,1)}$ Hoefsmit matrix mixes the std rep into the
   diagonal sum at the $b$-element (off-diagonal Hoefsmit entry).
   The empirical c_k may carry a $b^{2k}$-multiplicative factor
   not captured by the diagonal $\chi_\lambda$ values.
2. **q-deformed long-element character** $\chi_\lambda^q(w_0)$ at
   $q = q_0$ rather than $q = 1$. The character ring of $H_3(q)$
   differs from that of $S_3$ at $q \neq 1$; the appropriate
   weighting may use the q-deformed evaluation.
3. **Higher partitions** (k $\ge$ 7) where additional $\lambda \vdash 3$
   cancellations or new $\lambda \vdash 6$ contributions enter via
   the Wenzl-bridge inductive ascent.

These extensions are flagged for follow-up under the
`conj:alpha-k-categorical-closure` proposal.
