**Proposition (scaffolding).** *Let* $F(q) \in \mathbb{Z}[q, q^{-1}]^\wedge$
*be a fibre-level Habiro element associated to the operator-valued $T_\beta$
selection
([`prop:t-beta-markov-frobenius-collapse`](t-beta-markov-frobenius-collapse.md))
satisfying a $q$-difference equation of depth $d$:*

$$
F(q\xi) \;=\; R(q,\xi)\cdot F(\xi),
\qquad R(q,\xi) \in \mathbb{Q}(q)[\xi, \xi^{-1}] \text{ of degree} \le d.
$$

*Then the precision-ladder coefficients $c_k$ of
[`prop:q-beta-over-e0-classical-vanishing`](q-beta-over-e0-classical-vanishing.md)
satisfy a depth-$d$ linear recursion*

$$
c_{k+1} \;=\; \sum_{j=1}^{d} a_j(q_0)\cdot c_{k+1-j},
\qquad a_j(q_0) \in \mathbb{Q}(q_0),
$$

*with kernel coefficients $\{a_j\}$ extracted from $R(q_0, \xi)$ via the
$(u;u)_m \to u^k$ change-of-basis of the Habiro ring (Habiro 2004).*

## Why this is the right structure

The shape-collapse audit (PR [#1750](https://github.com/litlfred/qou/pull/1750))
established the operator content: $T_\beta = S \cdot \mathbf{1}$, with
$S$ pinned by the SDP constraint. The SDP strict-complementarity audit
(PR [#1752](https://github.com/litlfred/qou/pull/1752)) showed the
*direction* of the selector is $S$-independent and $q$-rational. The
diagnostic
[`prop:q-beta-over-e0-classical-vanishing`](q-beta-over-e0-classical-vanishing.md)
showed the SDP-constraint scalar $S = Q_\beta/E_0$ is *not* the ladder
normalization. Together these pin $F(q) = Q_\beta(q)/[Q_A(q) \cdot \cos(\alpha_{\mathrm{eff}}(q))]$
as a single fibre-level Habiro object whose $q$-difference structure
determines the $c_k$.

## What the recursion buys

Once a *single* $F$ is identified, the seven scalar coefficients
$c_2, \ldots, c_8$ (required for the $1\,\mathrm{ppQ}$ truncation
target, per [`docs/precision-goals.md`](https://github.com/litlfred/qou/blob/main/docs/precision-goals.md))
collapse to:

- One **seed** $c_2 = -1$, proved categorically (bar-even constraint, PR [#1602](https://github.com/litlfred/qou/pull/1602)).
- One **kernel** $R(q_0, \xi)$ of bounded degree $d$, determined by the
  categorical structure of $T_\beta$ and the Habiro embedding.
- The recursion produces $c_3, c_4, \ldots, c_8$ automatically.

Compare to the brute force: each $c_k$ ($k \ge 3$) currently requires
its own derivation (see the four-session $c_3$ flip-flop in
[`docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md))
or is extracted from the CODATA residual (the caveat of
[`qbeta-1ppq-achieved.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/qbeta/qbeta-1ppq-achieved.witness.json)
where $c_4 = -0.97157$ was a fit).

## The kernel — what's known, what's open

| Slot | Status | Source |
|---|---|---|
| Seed $c_2 = -1$ | **proved** | PR [#1602](https://github.com/litlfred/qou/pull/1602), bar-even constraint |
| $c_3 \approx -2$ | near-match (3 % cross-anchor swing) | empirical, four sessions of analysis |
| $c_4$ at $1\,\mathrm{ppQ}$ | fit (CODATA residual), value $-0.97157$ | [`qbeta_1ppq_achieved.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/qbeta/qbeta_1ppq_achieved.py) |
| $c_5, \ldots, c_8$ | not derived | open |
| Kernel $R(q,\xi)$ | structurally constrained (bar-even, $\zeta_4$ residue, $\sqrt{u}$-to-$u^2$ lift) | [`habiro_ladder_bridge.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/habiro/habiro_ladder_bridge.py) |
| Habiro element $F(q)$ | not derived (needs symbolic $\alpha(q)$) | open |

## What this content block provides

- A formal Lean structure
  `CKRecursion R` capturing the depth $d$ + kernel $\{a_j\}$ data
  ([`q-beta-c-k-recursion-from-habiro-q-difference.lean`](q-beta-c-k-recursion-from-habiro-q-difference.lean)).
- A method `applyRecursion : (Fin depth → R) → R` that performs one
  step of the recursion given the last $d$ values of the $c_k$
  sequence.
- A companion compute scaffold
  ([`qbeta_c_k_recursion_scaffold.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/qbeta/qbeta_c_k_recursion_scaffold.py))
  demonstrating the recursion machinery on toy depth-1 and depth-2
  kernels, with the seed $c_2 = -1$.

## Closing the open piece — the categorical f-construction

The remaining work is constructing one specific $F(q)$:

1. **Symbolic $\alpha(q)$** — extract from the operator-valued $N{=}3$
   witness or derive from the Hoefsmit seminormal blocks of $H_3(q)$.
2. **Kernel $R(q,\xi)$** — read off the $q$-difference equation of
   $F(q\xi) = R(q,\xi) F(\xi)$ from $\alpha(q)$.
3. **Verify** $c_3 \approx -2$ falls out of the recursion at the
   correct anchor $q_0$ — this discharges the empirical near-match.

The Lean class is parameterized over $R$ (the kernel) and the recursion
machinery is decoupled from the specific kernel — once a particular
$F(q)$ is identified, instantiating `CKRecursion ℝ` with the extracted
kernel turns the framework into a concrete $c_k$ predictor.

## Status

**Scaffolding.** The Lean structure + applyRecursion method form a
working recursion engine; the compute scaffold demonstrates two toy
kernels (depth-1 geometric, depth-2 underdetermined-from-seeds-alone).
The categorical $F(q)$ construction remains the open keystone for the
$1\,\mathrm{ppQ}$ target.
