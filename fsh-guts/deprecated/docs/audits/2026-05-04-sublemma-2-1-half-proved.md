> **DEPRECATED on 2026-05-24.** Point-in-time status, intermediate workplan iteration, dead-end exploration, or earlier sublemma version superseded by a later "refined" iteration. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T2 for the deprecation rationale.

# Sub-lemma 2.1 — half proved (no-interface case verified)

**Date:** 2026-05-04
**Branch:** `claude/categorical-mass-divergence-audit` (PR #534)
**Refs:**
- [`docs/audits/2026-05-04-confinement-nf-structure-forcing-proof.md`](2026-05-04-confinement-nf-structure-forcing-proof.md) — the proof skeleton
- [`computations/sublemma_2_1_deuteron_branching.py`](../../computations/sublemma_2_1_deuteron_branching.py)
- [`computations/sublemma-2-1-deuteron-branching.witness.json`](../../computations/sublemma-2-1-deuteron-branching.witness.json)

## Sub-lemma 2.1 (restatement)

For $\lambda \in A$,

$$
  \chi^\lambda(\beta_1 \cdot I \cdot \beta_2)
  \;=\; \sum_{(\mu, \nu) \,\vdash\, (n_1, n_2)}
        c^\lambda_{\mu, \nu}
        \cdot \chi^\mu(\beta_1)
        \cdot \alpha_{\mathrm{shift}}(I;\, \lambda, \mu, \nu)
        \cdot \chi^\nu(\beta_2),
$$

where $c^\lambda_{\mu, \nu}$ are LR coefficients and
$\alpha_{\mathrm{shift}}(I; \lambda, \mu, \nu)$ is the
$(\mu, \nu)$-block contribution of the interface $I$ in the
seminormal representation of $\lambda$.

The two parts:

| Part | Status |
|---|---|
| **Branching factorisation** $\chi^\lambda(\beta_1 \otimes \beta_2) = \sum c^\lambda_{\mu,\nu} \chi^\mu(\beta_1) \chi^\nu(\beta_2)$ when $I = \mathrm{id}$ | ✅ Standard ([Wenzl 1988]); now numerically verified for $H_6 \downarrow H_3 \times H_3$ |
| **Interface-block contribution** $\alpha_{\mathrm{shift}}(I; \lambda, \mu, \nu)$ explicit formula | 🔓 Open |

## What is now proved

### The no-interface branching theorem holds

For $\beta = \beta_1 \otimes \beta_2$ where $\beta_1 \in H_{n_1}(q)$
acts on the first $n_1$ strands and $\beta_2 \in H_{n_2}(q)$ on
the last $n_2$ (with no boundary crossing $\sigma_{n_1}$), the
[Wenzl 1988] Hecke-algebra branching theorem
$V_\lambda \downarrow_{H_{n_1}(q) \otimes H_{n_2}(q)}
   = \bigoplus_{(\mu,\nu)} c^\lambda_{\mu,\nu} \, V_\mu \otimes V_\nu$
gives the trace identity

$$
  \chi^\lambda(\beta_1 \otimes \beta_2)
  \;=\; \sum_{(\mu, \nu)}
        c^\lambda_{\mu, \nu} \cdot
        \chi^\mu(\beta_1) \cdot
        \chi^\nu(\beta_2).
$$

**Numerical verification** (`sublemma-2-1-deuteron-branching.witness.json`).
Take $\beta_1 = \beta_{\mathfrak{p}}$ and $\beta_2 = \beta_{\mathfrak{n}}$
in $H_3(q_0)$ (the per-nucleon braid words from
[`atom_braid_word_3A`](../../computations/mass_at_3A_proper.py)
with `include_inter=False`). Form the disjoint $H_6(q_0)$ word
$\beta_{\mathfrak{p}} \otimes \beta_{\mathfrak{n}}$ by re-indexing
$\beta_{\mathfrak{n}}$'s generators $\sigma_0, \sigma_1$ to
$\sigma_3, \sigma_4$ (acting on strands 3, 4, 5; never using
$\sigma_2$, the inter-block boundary generator). Then:

| $\lambda \vdash 6$ | $\chi^\lambda(\beta_{\mathfrak{p}} \otimes \beta_{\mathfrak{n}})$ | LR-prediction $\sum c^\lambda_{\mu,\nu} \chi^\mu \chi^\nu$ | rel. diff |
|---|---|---|---|
| $(6)$ | $+1.5513$ | $+1.5513$ | $1.4 \times 10^{-16}$ |
| $(5, 1)$ | $+5.9312$ | $+5.9312$ | $1.9 \times 10^{-15}$ |
| $(4, 2)$ | $+9.0059$ | $+9.0059$ | $2.6 \times 10^{-15}$ |
| $(4, 1, 1)$ | $+5.3660$ | $+5.3660$ | $6.0 \times 10^{-15}$ |
| $(3, 3)$ | $+4.6260$ | $+4.6260$ | $5.8 \times 10^{-16}$ |
| $(3, 2, 1)$ | $+7.6256$ | $+7.6256$ | $1.6 \times 10^{-14}$ |
| $(3, 1, 1, 1)$ | $-1.9176$ | $-1.9176$ | $8.5 \times 10^{-15}$ |
| $(2, 2, 2)$ | $+3.7480$ | $+3.7480$ | $4.7 \times 10^{-16}$ |
| $(2, 2, 1, 1)$ | $+0.8442$ | $+0.8442$ | $1.6 \times 10^{-14}$ |
| $(2, 1, 1, 1, 1)$ | $-2.2305$ | $-2.2305$ | $4.0 \times 10^{-15}$ |
| $(1^6)$ | $+0.6733$ | $+0.6733$ | $1.7 \times 10^{-16}$ |

**Max relative difference: $1.56 \times 10^{-14}$** (machine precision).

The $11$ partitions $\lambda \vdash 6$ all verify to ~$10^{-14}$
relative precision. The LR table used is hand-validated against
Pieri-rule Schur expansions and the dimension identity
$\sum_\lambda d_\lambda c^\lambda_{\mu,\nu} = \binom{n}{n_1} d_\mu d_\nu$
(yielding $80$ for $\mu = \nu = (2,1)$, etc.). A quick reference
implementation is included inline in the probe because the existing
`lr_coefficient` in [`sdp_multi_level.py`](../../computations/sdp_multi_level.py)
returns $0$ for several non-trivial cases (e.g.
$c^{(3,3)}_{(2,1),(2,1)} = 1$ but the function returns $0$ — a separate
bug to fix).

### Implication for the proof of Sub-lemma 2.1

The **easy half** of Sub-lemma 2.1 — that $\beta_1, \beta_2$ act
$(\mu,\nu)$-block-diagonally in the LR decomposition — is now
explicitly verified for the smallest non-trivial case
($H_6 \downarrow H_3 \times H_3$). This part of the proof is a
direct application of [Wenzl 1988] Theorem 3.4 (Hecke branching);
the verification merely confirms the theorem applies to our
specific $\beta_{\mathfrak{p}}$, $\beta_{\mathfrak{n}}$ words (which
contain Hecke-algebra elements $c \cdot \sigma_i + d \cdot 1$ with
$d \neq 0$, not just braid generators — so the additivity in
$d \cdot 1$ is also verified by the test).

## What remains open

The **hard half** is computing $\alpha_{\mathrm{shift}}(I; \lambda, \mu, \nu)$
explicitly for the atomic-braid interface $I$. Empirically the probe
gives the per-$\lambda$ deuteron-vs-disjoint ratios:

| $\lambda \vdash 6$ | $\chi^\lambda(\beta_D) / \chi^\lambda(\beta_{\mathfrak{p}} \otimes \beta_{\mathfrak{n}})$ |
|---|---|
| $(6)$ | $+1.0054$ |
| $(5, 1)$ | $+0.5422$ |
| $(4, 2)$ | $+0.1858$ |
| $(4, 1, 1)$ | $+0.0876$ |
| $(3, 3)$ | $+0.9185$ |
| $(3, 2, 1)$ | $+0.2587$ |
| $(3, 1, 1, 1)$ | $+0.2555$ |
| $(2, 2, 2)$ | $+0.9332$ |
| $(2, 2, 1, 1)$ | $+0.9710$ |
| $(2, 1, 1, 1, 1)$ | $+0.9664$ |
| $(1^6)$ | $+1.0054$ |

These ratios encode the interface contribution $I$ summed over
$(\mu, \nu)$ for each $\lambda$:

$$
  \frac{\chi^\lambda(\beta_{\mathfrak{p}} \cdot I \cdot \beta_{\mathfrak{n}})}
       {\chi^\lambda(\beta_{\mathfrak{p}} \otimes \beta_{\mathfrak{n}})}
  \;=\;
  \frac{\sum_{(\mu, \nu)} c^\lambda_{\mu, \nu} \cdot \chi^\mu(\beta_{\mathfrak{p}}) \cdot \alpha_{\mathrm{shift}}(I; \lambda, \mu, \nu) \cdot \chi^\nu(\beta_{\mathfrak{n}})}
       {\sum_{(\mu, \nu)} c^\lambda_{\mu, \nu} \cdot \chi^\mu(\beta_{\mathfrak{p}}) \cdot \chi^\nu(\beta_{\mathfrak{n}})}.
$$

When the maximizer $\lambda^*$ has a **single** $(\mu, \nu)$ in its
LR support (e.g. $\lambda = (6)$ with only $(\mu, \nu) = ((3),(3))$),
the ratio above directly equals
$\alpha_{\mathrm{shift}}(I; \lambda^*, (3), (3))$. From the table:
$\alpha_{\mathrm{shift}}(I; (6), (3), (3)) \approx 1.0054$.

For the interface $I$ being the **single inter-nucleon averaged
crossing** $\sigma_2 - \tfrac{1}{2}(q - q^{-1}) \cdot \mathbf{1}$ in
$H_6$, the $\alpha_{\mathrm{shift}}$ values cluster into bands:

- $\lambda \in \{(6), (1^6)\}$: ratio $\approx 1.005$ (one-row /
  one-column extremes; $I$ acts as a near-identity).
- $\lambda \in \{(2,2,2), (2,2,1,1), (2,1,1,1,1)\}$: ratio $\approx 0.93\text{-}0.97$.
- $\lambda \in \{(3,3)\}$: ratio $\approx 0.92$.
- Other $\lambda$ (especially $(4,2), (4,1,1)$, mixed-row): ratio
  $\approx 0.09\text{-}0.54$ (interface heavily reorders the
  $(\mu,\nu)$-block contributions).

These per-$\lambda$ ratios are the **categorical inputs** the
Hoefsmit-block computation must reproduce. The clean
torus-knot limit ([`prop:alpha-shift-torus-knot`](../../content/quantum-observable-universe/braids-and-knots/alpha-shift-torus-knot.md))
$\alpha_{\mathrm{shift}}(T_{p,k}) = k(p-1)$ on $V_{(1^p)}$ gives one
data point: $\alpha_{\mathrm{shift}}(T_{2,1}) = 1$ on
$V_{(1,1)}$ — and the table's $(1^6)$ value of $\approx 1.005$
(near-unity) is consistent in spirit (the $(1^6)$ lambda is the
"all anti-symmetric" extreme, where the torus-knot formula applies
directly).

## Concrete next steps

1. **Hoefsmit-block computation** of $\alpha_{\mathrm{shift}}(I; \lambda, \mu, \nu)$
   for single-crossing interfaces. The formula should reduce, on
   the column-partition extreme $\lambda = (1^n)$, to the proved
   $\alpha_{\mathrm{shift}}(T_{p,k}) = k(p-1)$.

2. **Atomic-shift coefficient closure**. With per-$\lambda$
   $\alpha_{\mathrm{shift}}$ values, the integer-LP profile
   $(1, 4, 0, 0, 1, 0)$ for atomic per-crossing shift contributions
   (`docs/audits/2026-05-03-w3-habiro-unblocked.md`) becomes a
   maximisation over $\lambda$ in the active set $A$.

3. **Lean formalisation**. Theorems 1, 3 of the proof skeleton
   are immediately Lean-formalisable via Mathlib's LP duality.
   Theorem 2 (and Sub-lemma 2.1) waits on the explicit
   $\alpha_{\mathrm{shift}}$ formula but the no-interface branching
   half is now numerically verified — sufficient for the
   conditional Lean statement.

## References

- [Wenzl 1988] *Hecke algebras of type $A_n$ and subfactors*,
  Inventiones Math. 92 (1988), 349–383. Theorem 3.4 (Hecke
  branching).
- [Hoefsmit 1974] *Representations of Hecke algebras of finite
  groups with $BN$-pairs of classical type*, PhD thesis,
  University of British Columbia.
- [`prop:alpha-shift-torus-knot`](../../content/quantum-observable-universe/braids-and-knots/alpha-shift-torus-knot.md)
  — the proved torus-knot limit.
- [`prop:atomic-mass-gb-nf`](../../content/quantum-observable-universe/braids-and-knots/atomic-mass-gb-nf.md)
  — the GB-NF mass identity needing $\rho_K$ closure (= Sub-lemma 2.1).
