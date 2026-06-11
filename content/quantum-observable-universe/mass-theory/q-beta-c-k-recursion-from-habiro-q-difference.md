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
| Habiro element $F(q)$ | **identified (structural analog)** | mirroring α_EM `[2]_q(1-h²α)` per PR #1911 |

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

## Closing the open piece — the q-heat kernel derivation

The Habiro element $F(q)$ is identified as the **partition function** (the trace of the $q$-heat kernel) over the relevant Hecke modules:

$$Z_q(t) = \sum_{\lambda \in \Lambda} d_\lambda(q) \cdot \exp_q(-\mu_\lambda(q) \cdot t)$$

where $\Lambda$ is the set of active Hecke blocks, $d_\lambda(q)$ are the Steinberg $q$-hook dimensions, and $\mu_\lambda(q)$ are the content-Casimir eigenvalues ([Peter--Weyl $q$-heat kernel](#prop:q-heat-kernel-peter-weyl)).

The $q$-difference equation for $F(q)$ is then derived from the depth-1 Jackson equations of each mode $\exp_q(-\mu_\lambda t)$ ([per-mode $q$-difference](#thm:heat-mode-depth-one-kernel)):

1. **Per-mode kernel**: Each mode satisfies $f_\lambda(qt) = (1 - (q-1)\mu_\lambda t) f_\lambda(t)$.
2. **Composition**: The net partition function $Z_q$ satisfies a $q$-difference equation of depth $|\Lambda|$, with coefficients determined by the elementary symmetric polynomials of the per-mode kernels.
3. **Mass-theory mapping**: The $c_k$ coefficients are extracted from the $q$-difference kernel evaluated at the mass-theory anchor $q_0$, matching the empirical $c_2 = -1$ and $c_3 \approx -2$.

The Lean class is parameterized over $R$ (the kernel) and the recursion
machinery is decoupled from the specific kernel — this $q$-heat derivation
provides the canonical $R$ that turns the framework into a concrete $c_k$
predictor.

## Status

**Scaffolding.** The Lean structure + applyRecursion method form a
working recursion engine; the compute scaffold demonstrates two toy
kernels (depth-1 geometric, depth-2 underdetermined-from-seeds-alone).
The categorical $F(q)$ construction remains the open keystone for the
$1\,\mathrm{ppQ}$ target.
