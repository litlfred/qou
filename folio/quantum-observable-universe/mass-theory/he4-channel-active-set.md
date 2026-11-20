## Setup

The $^4\mathrm{He}$ bound state admits three primary compositional channels summing to $A = 4$ nucleons:

| channel | constituents | $\sum \Delta_\mathrm{cat}$ (MeV) | residual $t_i$ (MeV) |
|---|---|---:|---:|
| $\mathrm{D} \oplus \mathrm{D}$    | $(1,1) + (1,1)$ | $4.05$ | $\mathbf{24.16}$ |
| $\mathrm{T} \oplus p$             | $(1,2) + (1,0)$ | $7.83$ | $\mathbf{20.38}$ |
| ${}^3\mathrm{He} \oplus n$        | $(2,1) + (0,1)$ | $7.04$ | $\mathbf{21.18}$ |

The **channel binding residual** is the excess binding beyond the free constituents:
$$
  t_i \;:=\; \Delta_\mathrm{cat}({}^4\mathrm{He}) \;-\; \sum_{j \in \mathrm{channel}\, i} \Delta_\mathrm{cat}(j).
$$
This measures the binding that the magic-shell coupling must explain beyond the free constituents. We load the empirical anchors from [`magic-shell-empirical-instantiation.witness.json`](computations/magic-shell-empirical-instantiation.witness.json).

## LP formulation

We apply the [Knot operator selection as linear program with LP duality](#prop:operator-selection-lp) canonical form. The vector $t \in \mathbb{R}^3$ holds the residuals. The matrix $G = I_3$ because the channels are orthogonal at leading order. Sub-braid corrections are sub-percent. The binding target is:
$$
  n_\mathrm{target} \;=\; \Delta_\mathrm{coupling}(2, 2)
  \;=\; \Delta_\mathrm{cat}({}^4\mathrm{He}) - 2\,\Delta_\mathrm{cat}({}^3\mathrm{He})
  \;=\; 13.197\,\mathrm{MeV}.
$$

## Solution

The LP solves uniquely with a duality gap of $0$. We have $\mathrm{primal\_obj} = \mathrm{dual\_obj} = 268.949$. The primal weights $x^\star$ and dual shadow prices $y^\star$ are:

| channel $i$ | $x^\star_i$ | $y^\star_i$ | status |
|---|---:|---:|---|
| $\mathrm{D} \oplus \mathrm{D}$    | $0$        | $\mathbf{3.778}$ | active |
| $\mathrm{T} \oplus p$             | $13.197$   | $0$              | primal-saturating |
| ${}^3\mathrm{He} \oplus n$        | $0$        | $0.796$          | active |

We have $y_0^\star = 20.380$. The **active set** contains the constraints with a positive dual variable:
$$
  \mathcal{A}({}^4\mathrm{He}) \;=\; \{\,\mathrm{D} \oplus \mathrm{D},\; {}^3\mathrm{He} \oplus n\,\}.
$$

## Proposition

**(Conditional on [`he4-sdp-compositional-canonical evaluation.witness.json`](computations/he4-sdp-compositional-canonical evaluation.witness.json).)**
For the $^4\mathrm{He}$ operator-selection LP:
1. **Unique primal optimum:** The system selects the $\mathrm{T} \oplus p$ channel with $x^\star_{\mathrm{T} \oplus p} > 0$ and $x^\star_i = 0$ for all $i \neq \mathrm{T} \oplus p$.
2. **Active set:** The dual-tight constraints are $\mathcal{A}({}^4\mathrm{He}) = \{\,\mathrm{D} \oplus \mathrm{D},\; {}^3\mathrm{He} \oplus n\,\}$.
3. **Dual ordering:** We have $y^\star_{\mathrm{D} \oplus \mathrm{D}} > y^\star_{{}^3\mathrm{He} \oplus n} > y^\star_{\mathrm{T} \oplus p} = 0$.

## Interpretation

The LP selects the $\mathrm{T} \oplus p$ decomposition to satisfy the binding constraint because it has the smallest residual. However, the shadow prices identify $\mathrm{D} \oplus \mathrm{D}$ as the most binding-receptive sub-braid. A unit perturbation of the deuteron-pairing channel changes the primal binding cost by $3.778$ MeV. This is five times the effect of the ${}^3\mathrm{He} \oplus n$ channel.

This two-tier fingerprint mirrors the Wedderburn-block fingerprint of [Two-row stratum carries $\ge 80\%$ of $\mathrm{tr}_M(\beta_{^4\mathrm{He}})$ at $q_0$ (exactly $1$ empirically)](#prop:he4-two-row-dominance). Both identify a $q$-symmetric deuteron-pairing structure as the load-bearing geometry of the magic-shell coupling. The $\mathrm{T} \oplus p$ channel provides the energetic accounting. We make this connection explicit in `rem:he4-magic-shell-fingerprint`.
