**Conjecture (parity closure).**
*Within the QOU framework, parity $P$ acts as the **mirror reflection
of the braid diagram** — each positive crossing $\sigma_i \mapsto
\sigma_i^{-1}$ and vice versa, with the q-parameter held fixed
($q \mapsto q$, not $q \mapsto q^{-1}$).  Equivalently, $P$ negates
the signed writhe $w(K) \mapsto -w(K)$ of every braid word.  $P$ is
an involution ($P^2 = \mathrm{id}$) and is **distinct from**:*

- *the bar-involution [Bar-involution and its $P_{\mathrm{avg}}$ / $P_{\mathrm{skew}}$ projections](#def:bar-involution),
  which acts as $q \mapsto q^{-1}$ AND $\sigma_i \mapsto \sigma_i^{-1}$
  simultaneously (= composite CPT);*
- *charge conjugation [Charge conjugation $C$ as the color-sheet flavor-swap $u \leftrightarrow \bar u$, $d \leftrightarrow \bar d$](#conj:c-from-color-flavor-swap),
  which acts on color-sheet flavor labels with no Hecke-
  generator action;*
- *time-reversal [Time-reversal $T$ as Markov-trace word reversal (trace cyclicity dual)](#conj:t-from-trace-cyclicity),
  which reverses the braid word at the Markov-trace level.*

## The action

For a braid word $\beta = \sigma_{i_1}^{\epsilon_1} \cdots
\sigma_{i_\ell}^{\epsilon_\ell}$ in $B_n$ (or its image in $H_n(q)$):

$$
  P \;:\;
  \sigma_{i_k}^{\epsilon_k}
  \;\longmapsto\;
  \sigma_{i_k}^{-\epsilon_k}
  \qquad (q\text{ held fixed}).
$$

On the writhe, this gives $w(P\beta) = -w(\beta)$ — a sign flip on
the bar-anti-symmetric writhe quantity classified in
[`bar-involution-table3-data`](../braids-and-knots/bar-involution.md#tbl:bar-involution-table3-data).

## Disentangling parity from CPT

The composite bar-involution acts as both:

$$
  (\text{bar}) \;:\;
  \sigma_i \mapsto \sigma_i^{-1},
  \qquad
  q \mapsto q^{-1}.
$$

This is **CPT composed**: bar = $P \cdot C \cdot T$ in the natural
order, where:

| Acts on | Symbol map |
|---------|------------|
| Hecke generator chirality only | $\sigma_i \mapsto \sigma_i^{-1}$, $q$ fixed (= **P** alone) |
| Color sheets only | flavor $u \leftrightarrow \bar u$ (= **C** alone) |
| Markov trace cyclicity only | braid word reversal (= **T** alone) |

P alone (this conjecture) corresponds to the **first row only** — it
fixes $q$, fixes color-sheet flavors, and fixes trace cyclicity; it
only mirrors the diagram.  Composed with C and T, it recovers the
bar-involution.

## Structural invariants


- **GB filtration level**: ℓ-dependent per-atom (P preserves Coxeter
  length but flips signs of generators).
- **Jet order**: $h^0$ (P fixes $q$; no q-deformation parameter
  enters the P action).
- **Bar-symmetry status**: bar-trivial (P does not act on $q$;
  bar-involution acts on $q$ AND $\sigma_i$, so P alone is a strict
  sub-action).

Writhe $w(K)$ (the observable that P negates) is classified in
[`bar-involution-table3-data`](../braids-and-knots/bar-involution.md#tbl:bar-involution-table3-data)
as bar-anti-symmetric, consistent: bar reverses writhe via the
composite $P \cdot C \cdot T$, of which P is the writhe-acting
factor.

## The hypothesis in summary

The conjecture asserts an involution $P$ on braid-group elements ($P^2 = \mathrm{id}$) sending each Hecke generator $\sigma_i$ to $\sigma_i^{-1}$, fixing $q$, and such that the bar-involution factors as $P \circ C \circ T$.

## Consumers / downstream

- The writhe-based chirality classification
  [Chirality factor $1 + w \cdot h$ from ribbon-twist framing (writhe $w$)](#prop:chirality-writhe-ribbon-derivation)
  gets a categorical home: chirality measures the P-anti-symmetric
  part of a knot, separately from C and T.

## What remains open

1. **Invariance of the Hecke quadratic under $P$.** The quadratic is preserved
   (since both $\sigma_i$ and $\sigma_i^{-1}$ satisfy the same
   relation): the quadratic
   $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$ is invariant under P
   because $(\sigma_i^{-1} - q)(\sigma_i^{-1} + q^{-1}) = 0$ also
   holds (multiply the original by $\sigma_i^{-2}$).
2. Closing the conjecture needs the existence of such a map $P$, and a
   derivation of bar $= P \cdot C \cdot T$ as an identity rather than an assumption.

## Cross-references

- The sibling $\mathbb{Z}/2$ factors of CPT — charge conjugation and time
  reversal, this conjecture supplying parity:
  [Charge conjugation $C$ as the color-sheet flavor-swap $u \leftrightarrow \bar u$, $d \leftrightarrow \bar d$](../brings-surface/c-from-color-flavor-swap.md),
  [Time-reversal $T$ as Markov-trace word reversal (trace cyclicity dual)](../nuclear-interactions/t-from-trace-cyclicity.md)
- Bar-involution: [Bar-involution and its $P_{\mathrm{avg}}$ / $P_{\mathrm{skew}}$ projections](../braids-and-knots/bar-involution.md) Tables 1-4
