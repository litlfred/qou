$^{18}\mathrm{O}$ ($Z = 8$, $N = 10$, $A = 18$) is the canonical
**single-magic** test case: the proton count $Z = 8 \in \mathfrak{M}$
is saturated, but the neutron count $N = 10 \notin \mathfrak{M}$ is
not. This example illustrates the partition-level diagrammatic
content of the double-magic LR-fusion conjecture
([`conj:diagrammatic-double-magic-lr-fusion`](#conj:diagrammatic-double-magic-lr-fusion))
in the regime where exactly one block is saturated, and the
**$\kappa$-leakage** through the non-saturated $N$-block accounts
for the binding-energy tail beyond the saturated $Z = 8$
contribution.

## $Z$-block (saturated)

The proton count $Z = 8$ is magic, so by
[`conj:categorical-neutrality-saturated-shells`](../braids-and-knots/categorical-neutrality-saturated-shells.md)
the categorical mass at level $8$ is supported on a single
self-conjugate partition. The relevant partition is

$$
  \lambda_{Z=8} \;=\; (3, 2, 2, 1) \;=\; \lambda_{Z=8}'
$$

(self-conjugate, content sum $c(\lambda_{Z=8}) = 0$). The Young
diagram is symmetric under transposition:

```text
  ■ ■ ■
  ■ ■
  ■ ■
  ■
```

The full-twist $\Delta_8^2$ acts on $V_{\lambda_{Z=8}}$ by
$q^{c(\lambda_{Z=8})} = q^0 = 1$ — trivial, as the saturated-shell
conjecture demands.

## $N$-block (frayed)

The neutron count $N = 10$ is not magic. The categorical mass at
level $10$ is therefore *not* concentrated on a single
self-conjugate partition; instead, the Wedderburn support is spread
over multiple non-self-conjugate $\mu \vdash 10$, each contributing
a non-trivial full-twist eigenvalue $q^{c(\mu)} \neq 1$.
Phenomenologically the neutron block is **frayed** — its support
on Young's lattice forms a thicket of competing partitions rather
than a single self-conjugate diagram.

A representative non-self-conjugate partition is

$$
  \mu = (5, 3, 2) \quad\text{vs.}\quad \mu' = (3, 3, 2, 1, 1),
$$

these two partitions of $10$ differ in shape and contribute
independently to $\Phi_{10}$.

## LR fusion at $A = 18$

The LR fusion $V_{\lambda_{Z=8}} \otimes V_\mu(N=10)$ does **not**
collapse to a single $\nu$: the non-self-conjugacy of $\mu$ on the
$N$ side propagates through the LR rule
([`conj:diagrammatic-double-magic-lr-fusion`](#conj:diagrammatic-double-magic-lr-fusion))
to produce a sum

$$
  V_{\lambda_{Z=8}} \otimes V_{\mu(N=10)}
  \;\cong\;
  \bigoplus_{\nu \vdash 18}
    c^\nu_{\lambda_{Z=8}, \mu} \, V_\nu,
$$

with multiple non-zero $c^\nu$. The sum's spread over $\nu$ — the
non-zero off-diagonal LR coefficients — is the **$\kappa$-leakage**:
binding-energy capacity that the saturated $Z = 8$ side cannot
absorb, and that the frayed $N = 10$ side carries.

## What the diagram shows

The diagrammatic illustration in this example block is, schematically:

- **Left half**: the symmetric $\lambda_{Z=8} = (3,2,2,1)$ Young
  diagram, marked as "self-conjugate, full-twist trivial,
  saturated".
- **Right half**: a fragment of Young's lattice between
  $\mu = (5,3,2)$ and $\mu' = (3,3,2,1,1)$, with edges marking the
  Pieri / branching arrows; marked as "frayed, full-twist non-
  trivial, non-saturated".
- **Centre**: the LR-fusion arrow producing a *spread* over $\nu$
  rather than a single $\nu_{ZN}$. The width of the spread is the
  algebraic content of $\kappa$-leakage.

## Empirical match

The empirical $^{18}\mathrm{O}$ binding curve sits between $^{16}\mathrm{O}$
(double-magic, exceptionally bound) and $^{20}\mathrm{O}$ (binding
falls off as $N$ moves further from $8$). The single-magic spread
predicted here — saturated $Z$ contribution plus frayed $N$
contribution with $\kappa$-leakage — matches the observed binding
energy within the multi-term BW residual.
