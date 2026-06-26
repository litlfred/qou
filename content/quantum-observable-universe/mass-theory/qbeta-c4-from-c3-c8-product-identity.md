**Proposition (c_4 derived from c_3 and c_8 via product identity).**

*The $\mathfrak{Q}_\beta$ precision-ladder coefficients $c_3$, $c_4$, $c_8$ satisfy the
structural product identity*

$$
  c_8 \;=\; c_3 \cdot c_4 \qquad (\text{symbolic in } b, \text{ exact } \forall b).
$$

*At the silver ratio $q = 1+\sqrt{2}$ where $c_3 = -2$, $c_4 = -49/32$,
and $c_8 = 49/16$, this becomes the $\mathbb{Q}$-rational identity*

$$
  (-2) \cdot (-49/32) \;=\; 49/16.
$$

*Consequently $c_4 = c_8 / c_3 = -2 \cdot b^4$ is **derived** from
$c_3$ (= $J_{\mathrm{Hopf}}$ at $q=1$) and $c_8$ (= $c_3^2 \cdot b^4$,
the second rung of the $\sigma$-action tower) — not stipulated.*

## Why this matters

The closed-form Pell-Lucas $\sigma$-action recursion $c_{k+2} = b^2
\cdot c_k$ holds for $k \geq 6$ but does not extend below $k = 6$:
no constant-kernel linear recursion of depth $\leq 3$ closes the gap
between $c_4$ and $c_5, c_6, c_7$. The $c_4$ closed form is therefore
not derivable from a Pell-Lucas-style additive recursion.

This proposition closes the gap by a **different route**: a
multiplicative product law instead of a linear recursion. Searching
all products $c_i \cdot c_j$ over the closed-form set discovers
exactly two non-trivial identities:

1. $c_3 \cdot c_4 = c_8$    (derives $c_4$ from $c_3, c_8$).
2. $c_3 \cdot c_6 = c_9$    (independent structural check).

The product structure of (1) categorically reads as: *applying the
$J_{\mathrm{Hopf}}$ Markov-trace twist (= $c_3 = -2$) to the $c_4$
object yields the $c_8$ object* — a Markov-trace product law in the
$\sigma$-action tower. If this product law follows from a
categorical theorem (e.g. a Hopf-link tensoring axiom in the
Markov-trace tower on $H_n(q)$), then $c_4$ is **forced** by $c_3$
and $c_8$ — derived rather than stipulated.

## Companion identity (independent check)

The second product identity $c_3 \cdot c_6 = c_9$ provides an
independent structural check: applying the same Hopf-trace twist
to $c_6$ (= $c_3^2 \cdot b^2$) yields $c_9$ (= $c_3^3 \cdot b^2$).
Symbolically $(-2) \cdot (4b^2) = -8b^2$; at silver $(-2) \cdot
(7/2) = -7$. Both check.

These two identities are the **only** product hits in the closed-
form set (verified by symbolic enumeration in
[`probes/qbeta_c4_structural_product_identities.py`](../../computations/probes/qbeta_c4_structural_product_identities.py)).
The c_5 averaging-resonance outlier and the c_2, c_7 seed values
do not participate in the product algebra.

## Lean proof structure

Two `norm_num`-closed $\mathbb{Q}$-rational identities at silver:

1. `c4_eq_c8_div_c3_at_silver`: $-2 \cdot (-49/32) = 49/16$ (i.e.
   $c_3 \cdot c_4 = c_8$ at silver).
2. `c3_times_c6_eq_c9_at_silver`: $-2 \cdot 7/2 = -7$ (i.e.
   $c_3 \cdot c_6 = c_9$ at silver).

Both close by `norm_num`. The Lean theorems are pure rational
arithmetic — no symbolic-q or transcendental machinery required.

## Honest caveats

1. The product identity $c_8 = c_3 \cdot c_4$ is observed
   symbolically (verified in $\mathbb{Z}[b]$); whether it follows
   from a categorical theorem (a Markov-trace product law in some
   tower) is **not yet derived**.
2. The c_5 averaging-resonance outlier is NOT covered by the
   product algebra ($c_3 \cdot c_5$ does not match any documented
   $c_k$).
3. The derivation $c_4 = c_8 / c_3$ presupposes $c_8 = c_3^2 \cdot
   b^4$ as the σ-action seed; the categorical reason $c_8$ takes
   this specific value at $q_0$ is the upstream open question.

Subject to that categorical proof, $c_4$ is **derived** from $c_3$
and $c_8$ via a structural product law. The $c_4$ closed form
$-2 \cdot b^4$ is no longer a stipulation — it is forced by the
two seed values $c_3 = -2$ ($J_{\mathrm{Hopf}}$ seed) and
$c_8 = 4 \cdot b^4$ ($\sigma$-action seed).

Per the authoritative
[c_k/d_k registry](../../../docs/coordination/ck-dk-canonical-registry.md),
$c_4$ holds **empirical** tier until that upstream $c_8$ categorical
proof lands: the product identity is a structural relation *among
empirical rungs*, not an unconditional derivation (only $c_2 = -1$ is
canonical). The conditional "derived" above is exactly the
"machinery-proved $\neq$ values-derived" distinction the registry codifies.

## q-usage discipline

The product identities are stated at the fibre level (Laurent
polynomial in $b$ over $\mathbb{Z}$, no $q$-archimedean evaluation
needed) and verified at the silver-ratio rational anchor $b^2 = 7/8$
in $\mathbb{Q}$.
