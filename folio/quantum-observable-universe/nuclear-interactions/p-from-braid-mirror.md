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

## Scope at the Hecke-letter level

**$P$ as written is a map on braid words, not on $H_n(q)$.** The conjecture defines $P$ by $\sigma_i \mapsto \sigma_i^{-1}$ with $q$ held fixed. On the braid group $B_n$ this is an involution. It does not descend to the Hecke algebra: an algebra map of $H_n(q)$ that is linear over the scalars and sends a generator to its inverse forces $2(q - q^{-1}) = 0$, so it exists only when $q^2 = 1$ in characteristic other than $2$. The reason is that $\sigma_i^{-1}$ satisfies the Hecke relation at the parameter $q^{-1}$, not at $q$.

**What does descend.** Let $P_+$ and $P_-$ be the idempotents of $\sigma_i$ for its eigenvalues $q$ and $-q^{-1}$, and let $e^- = \sigma_0\sigma_1\sigma_0$ with mirror $e^+ = \sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$, as in the [Breit–Wheeler vertex](#rem:breit-wheeler-vertex). Three involutions send a letter to a letter, and they form a Klein four-group.

- **The mirror $\sigma_i \mapsto \sigma_i^{-1}$ together with $q \mapsto q^{-1}$** is the bar involution on a letter. It keeps $P_+$ and $P_-$ and sends $e^-$ to $e^+$. Its profile is that of $C$, or of $CT$ if $q \mapsto q^{-1}$ is read as antilinear.
- **The map $\sigma_i \mapsto -\sigma_i^{-1}$** keeps $q$, exchanges $P_+$ and $P_-$, and sends $e^-$ to $-e^+$. Its profile is that of $CP$.
- **The map $\sigma_i \mapsto -\sigma_i$ together with $q \mapsto q^{-1}$** exchanges $P_+$ and $P_-$ and sends $e^-$ to $-e^-$. It is the only one of the three with the profile of $P$. It is not linear over the scalars unless $q^2 = 1$, and $q \mapsto q^{-1}$ has no counterpart at the real substrate value $q_0$.

**The bar involution as composite $CPT$.** At the letter level the bar involution keeps both eigenlines. A map with the profile of $CPT$ would exchange them, as $P$ does. So the factorisation bar $= P \cdot C \cdot T$ in the summary below is not supported at the letter level, where bar has the profile of $C$ (or $CT$).

**Item 1 below.** Multiplying $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$ by $\sigma_i^{-2}$ gives $(\sigma_i^{-1})^2 = (q^{-1} - q)\,\sigma_i^{-1} + 1$, which is the Hecke relation at $q^{-1}$. The quadratic at $q$ is therefore not preserved by $P$ with $q$ fixed.

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
