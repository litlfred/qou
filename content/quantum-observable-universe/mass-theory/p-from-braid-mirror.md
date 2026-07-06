**Conjecture (D7 parity closure).**
*Within the QOU framework, parity $P$ acts as the **mirror reflection
of the braid diagram** — each positive crossing $\sigma_i \mapsto
\sigma_i^{-1}$ and vice versa, with the q-parameter held fixed
($q \mapsto q$, not $q \mapsto q^{-1}$).  Equivalently, $P$ negates
the signed writhe $w(K) \mapsto -w(K)$ of every braid word.  $P$ is
an involution ($P^2 = \mathrm{id}$) and is **distinct from**:*

- *the bar-involution [`def:bar-involution`](#def:bar-involution),
  which acts as $q \mapsto q^{-1}$ AND $\sigma_i \mapsto \sigma_i^{-1}$
  simultaneously (= composite CPT);*
- *charge conjugation [`conj:c-from-color-flavor-swap`](#conj:c-from-color-flavor-swap)
  (D6), which acts on color-sheet flavor labels with no Hecke-
  generator action;*
- *time-reversal [`conj:t-from-trace-cyclicity`](#conj:t-from-trace-cyclicity)
  (D8), which reverses the braid word at the Markov-trace level.*

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
[`bar-involution-table3-data`](bar-involution.md#tbl:bar-involution-table3-data).

## Disentanglement of D7 from CPT

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
| Color sheets only | flavor $u \leftrightarrow \bar u$ (= **C** alone, D6) |
| Markov trace cyclicity only | braid word reversal (= **T** alone, D8) |

P alone (this conjecture) corresponds to the **first row only** — it
fixes $q$, fixes color-sheet flavors, and fixes trace cyclicity; it
only mirrors the diagram.  Composed with C and T, it recovers the
bar-involution.

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration level**: ℓ-dependent per-atom (P preserves Coxeter
  length but flips signs of generators).
- **Jet order**: $h^0$ (P fixes $q$; no q-deformation parameter
  enters the P action).
- **Bar-symmetry status**: bar-trivial (P does not act on $q$;
  bar-involution acts on $q$ AND $\sigma_i$, so P alone is a strict
  sub-action).

Writhe $w(K)$ (the observable that P negates) is classified in
[`bar-involution-table3-data`](bar-involution.md#tbl:bar-involution-table3-data)
as bar-anti-symmetric, consistent: bar reverses writhe via the
composite $P \cdot C \cdot T$, of which P is the writhe-acting
factor.

## Lean axiomatisation (sketch)

```lean
class PFromBraidMirror (M : Type*) [BrCategory M] [Hecke M] where
  /-- The braid-mirror involution on braid-group elements. -/
  p_action : Braid n → Braid n
  /-- P^2 = id. -/
  p_involution : ∀ β, p_action (p_action β) = β
  /-- P flips the sign of every Hecke generator. -/
  p_on_generator : ∀ i, p_action (Hecke.sigma i) = Hecke.sigma_inv i
  /-- P fixes q (no bar-action). -/
  p_preserves_q : ∀ q, p_q_action q = q
  /-- Bar-involution factorisation: bar = P · C · T. -/
  bar_eq_p_c_t : bar_involution = p_action ∘ c_action ∘ t_action
```

## Consumers / downstream

- [`conj:cpt-orbit-closure-density`](#conj:cpt-orbit-closure-density)
  becomes a corollary of $\mathrm{CPT} = C \cdot P \cdot T$ once D6,
  D7, D8 are all closed.
- The writhe-based chirality classification
  [`prop:chirality-writhe-ribbon-derivation`](#prop:chirality-writhe-ribbon-derivation)
  gets a categorical home: chirality measures the P-anti-symmetric
  part of a knot, separately from C and T.

## Open R&D

1. **Verify canonical** that the Hecke quadratic preserves under P
   (since both $\sigma_i$ and $\sigma_i^{-1}$ satisfy the same
   relation): the quadratic
   $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$ is invariant under P
   because $(\sigma_i^{-1} - q)(\sigma_i^{-1} + q^{-1}) = 0$ also
   holds (multiply the original by $\sigma_i^{-2}$). Concrete canonical evaluation
   in a follow-up.
2. **D7 to closed** requires the Lean class instance + a `prop:` block
   stating bar = P $\cdot$ C $\cdot$ T as a derivable identity.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) §1 D7
  + §2 Cluster A (CPT decomposition D5 $\to$ D6 + D7 + D8)
- Sibling Z/2 decompositions of CPT:
  [`conj:c-from-color-flavor-swap`](c-from-color-flavor-swap.md) (D6),
  [`conj:t-from-trace-cyclicity`](t-from-trace-cyclicity.md) (D8)
- Composite CPT: [`conj:cpt-orbit-closure-density`](#conj:cpt-orbit-closure-density)
- Bar-involution: [`bar-involution.md`](bar-involution.md) Tables 1-4
