**Remark (Option B at $H_3$ — naive stratum-prefactor approach does not yet close $2/(3\pi)$).**

[`rem:alpha-em-derivation-exploration-options`](#rem:alpha-em-derivation-exploration-options)
Option B proposes that $2/(3\pi)$ should arise as a depth-$\ell$
stratum prefactor of the GB filtration on the COUPLING side, by
analogy with the closed-form mass-formula $\alpha_k$. This remark
records a first-pass attempt in $H_3$ that did not close.

## Setup

In $H_3(R, q)$, the Markov-trace coefficients $y_\lambda$ are
determined by the cycle-type linear system
([`prop:alpha-k-derivation-procedure`](#prop:alpha-k-derivation-procedure)):

$$
  \sum_\lambda \chi_\lambda(w_\mu) y_\lambda = z^{n - \mathrm{len}(\mu)},
  \qquad z = 1/(\sqrt{q} + 1/\sqrt{q}).
$$

Solving symbolically for $H_3$:

$$
  y_{(3)} = \frac{q^4 z^2 + q^3 z + q^2 z^2 + 2qz + 1}{q^6 + 2q^4 + 2q^2 + 1},
  \qquad
  y_{(2,1)} = \frac{q^3 z - q^2 z^2 + q^2 - qz}{q^4 + q^2 + 1},
$$

$$
  y_{(1,1,1)} = \frac{q^6 - 2q^5 z + q^4 z^2 - q^3 z + q^2 z^2}{q^6 + 2q^4 + 2q^2 + 1}.
$$

At $q = q_0$ with $z \approx 0.4993$:

| $\lambda$ | $y_\lambda(q_0)$ |
|---|---|
| $(3)$ | $0.41540$ |
| $(2,1)$ | $0.28093$ |
| $(1,1,1)$ | $0.02274$ |

## Tested combinations vs target $2/(3\pi) \approx 0.21221$

| Combination | Value | Off |
|---|---|---|
| $y_{(3)} - y_{(1,1,1)}$ | $0.39265$ | $+85\%$ |
| $y_{(2,1)}/3$ | $0.09364$ | $-56\%$ |
| $(y_{(3)} + y_{(1,1,1)})/2$ | $0.21907$ | $+3.2\%$ |
| $z^2$ (depth-3 Markov trace) | $0.24932$ | $+17.5\%$ |
| Plancherel-Markov of $\sigma_0\sigma_1\sigma_0$ | $-0.55671$ | wrong sign |

**Closest naive combination** $(y_{(3)} + y_{(1,1,1)})/2 = 0.21907$ is
$3.2\%$ off — well outside the precision required for a structural
identity, but suggestive that $H_3$ contains the right scale of
contributions.

## Why no exact match in $H_3$

Two reasons the $H_3$ check is necessarily insufficient:

1. **The bare formula uses $H_n$ for $n \geq 5$.** The bare term
   $q\cdot[9]_q\cdot[10]_q$ pairs the force-carriers $T_{2,9} \in B_2$
   and $T_{3,5} \in B_3$, naturally embedded in $B_5 = B_2 \times B_3$
   (Markov stabilisation). The depth-$k$ stratum analysis must be done
   in $H_5$ (or the appropriate $H_n$ where both knots embed) for a
   proper match, not in $H_3$ alone. The $H_3$ analysis here verifies
   only the IDEA of stratum-decomposition, not the actual ambient.

2. **The "coupling-side analog" of the mass functional is not yet
   defined.** The mass-formula stratum prefactors come from
   Plancherel-weighted Frobenius integrals
   ([`prop:unified-curvature-rank-mass-formula`](#prop:unified-curvature-rank-mass-formula)):
   $\mathfrak{m}^{(k)} = \sum_{\lambda:\mathrm{depth}=k} w_\lambda \cdot \log|\!\int_{A_\lambda} \rho(\beta) \cdot \mathcal{T}|$.
   The COUPLING-side analog would be a *non-logged* Plancherel sum
   over the singlet idempotent's image in each Wedderburn block. This
   functional is not defined in the paper; defining it precisely is
   the open mathematical step.

## What's needed to advance Option B

1. **Define the coupling-side stratum functional** $\mathcal{K}^{(k)}$,
   analogous to $\mathfrak{m}^{(k)}$ but acting on the singlet
   idempotent rather than on log-Frobenius integrals. The natural
   candidate is

   $$
     \mathcal{K}^{(k)} = \sum_{\lambda: \mathrm{depth}(\lambda) = k}
       w_\lambda \cdot |\mathrm{tr}_\tau(e_-^\lambda)|^2
   $$

   where $e_-^\lambda$ is the antisymmetric (singlet) component of
   the Wedderburn block at $\lambda$.

2. **Compute $\mathcal{K}^{(k)}$ in the appropriate $H_n$** (likely
   $n \geq 5$) and verify the depth sum $\sum_k \mathcal{K}^{(k)}$
   recovers $1/\alpha = q[9]_q[10]_q + 2/(3\pi)$.

3. **Identify the depth $\ell$** at which the contribution equals
   $2/(3\pi)$. Conjecturally $\ell = 3$ (matching the GB-depth of
   the maximal-length basis element $\sigma_0\sigma_1\sigma_0$ in
   $H_3$ and the $/3$ chromaticity averaging).

This is real research mathematics — the infrastructure is in place
([`prop:spectral-sequence-collapse`](#prop:spectral-sequence-collapse),
[`prop:y-lambda-closed-form-wenzl-bridge`](#prop:y-lambda-closed-form-wenzl-bridge),
[`prop:unified-curvature-rank-mass-formula`](#prop:unified-curvature-rank-mass-formula))
but the precise specification of the coupling-side functional is the
open step.
