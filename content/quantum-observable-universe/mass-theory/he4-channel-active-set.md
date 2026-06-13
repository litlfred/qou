*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

## Setup

The $^4\mathrm{He}$ bound state admits three primary compositional
channels (each summing to $A = 4$ nucleons):

| channel | constituents | $\sum \Delta_\mathrm{cat}$ (MeV) | residual $t_i$ (MeV) |
|---|---|---:|---:|
| $\mathrm{D} \oplus \mathrm{D}$    | $(1,1) + (1,1)$ | $4.05$ | $\mathbf{24.16}$ |
| $\mathrm{T} \oplus p$             | $(1,2) + (1,0)$ | $7.83$ | $\mathbf{20.38}$ |
| ${}^3\mathrm{He} \oplus n$        | $(2,1) + (0,1)$ | $7.04$ | $\mathbf{21.18}$ |

The **channel binding residual** is
$$
  t_i \;:=\; \Delta_\mathrm{cat}({}^4\mathrm{He}) \;-\; \sum_{j \in \mathrm{channel}\, i} \Delta_\mathrm{cat}(j)
$$
— the binding that the magic-shell coupling
must explain *beyond* the free-constituent sum. Empirical anchors
loaded from
[`magic-shell-empirical-instantiation.witness.json`](folio-assistant/computations/magic-shell-empirical-instantiation.witness.json).

## LP formulation

Apply the
[`prop:operator-selection-lp`](#prop:operator-selection-lp)
canonical form with $t \in \mathbb{R}^3$ the residual vector above,
$G = I_3$ (channels orthogonal at leading order — corrections from
shared sub-braids are sub-percent), and
$$
  n_\mathrm{target} \;=\; \Delta_\mathrm{coupling}(2, 2)
  \;=\; \Delta_\mathrm{cat}({}^4\mathrm{He}) - 2\,\Delta_\mathrm{cat}({}^3\mathrm{He})
  \;=\; 13.197\,\mathrm{MeV}
$$
(the doubly-magic anchor from ).

## Solution

The LP solves uniquely (strong duality holds, duality gap $= 0$;
$\mathrm{primal\_obj} = \mathrm{dual\_obj} = 268.949$). The primal
weights $x^\star$ and dual shadow prices $y^\star$ are:

| channel $i$ | $x^\star_i$ | $y^\star_i$ | status |
|---|---:|---:|---|
| $\mathrm{D} \oplus \mathrm{D}$    | $0$        | $\mathbf{3.778}$ | active |
| $\mathrm{T} \oplus p$             | $13.197$   | $0$              | primal-saturating |
| ${}^3\mathrm{He} \oplus n$        | $0$        | $0.796$          | active |

with $y_0^\star = 20.380$. The **active set** —
constraints whose dual variable is positive — is therefore
$$
  \mathcal{A}({}^4\mathrm{He}) \;=\; \{\,\mathrm{D} \oplus \mathrm{D},\; {}^3\mathrm{He} \oplus n\,\}.
$$

## Proposition

**(Conditional on
[`he4-sdp-compositional-probe.witness.json`](folio-assistant/computations/he4-sdp-compositional-probe.witness.json).)**
For the $^4\mathrm{He}$ operator-selection LP defined above:

1. **Unique primal optimum** at the $\mathrm{T} \oplus p$ channel:
   $x^\star_{\mathrm{T} \oplus p} > 0$ and $x^\star_i = 0$ for all
   $i \neq \mathrm{T} \oplus p$.
2. **Active set** $\mathcal{A}({}^4\mathrm{He}) =
   \{\,\mathrm{D} \oplus \mathrm{D},\; {}^3\mathrm{He} \oplus n\,\}$
   (dual-tight constraints).
3. **Dual ordering**
   $y^\star_{\mathrm{D} \oplus \mathrm{D}} >
    y^\star_{{}^3\mathrm{He} \oplus n} >
    y^\star_{\mathrm{T} \oplus p} = 0$.

## Interpretation

The LP "uses" the $\mathrm{T} \oplus p$ decomposition to satisfy
the binding constraint (it has the smallest per-unit cost — the
smallest residual after subtracting free constituents). But the
**shadow prices identify $\mathrm{D} \oplus \mathrm{D}$ as the
most binding-receptive sub-braid**: a unit perturbation of the
deuteron-pairing channel would change the primal binding cost by
$3.778$ MeV per MeV — five times more than the
${}^3\mathrm{He} \oplus n$ channel and infinitely more than the
$\mathrm{T} \oplus p$ channel (whose shadow price is zero, since
it is the primal-saturating decomposition).

This **two-tier structural fingerprint** is the channel-level
analogue of the Wedderburn-block fingerprint
[`prop:he4-two-row-dominance`](#prop:he4-two-row-dominance): both
identify a $q$-symmetric deuteron-pairing structure as the
load-bearing geometry of the doubly-magic
magic-shell coupling, while
$\mathrm{T} \oplus p$ provides the energetic accounting. The
remark
`rem:he4-magic-shell-fingerprint`
makes this connection explicit.
