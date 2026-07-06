**Conjecture (D8 time-reversal closure).**
*Within the QOU framework, time-reversal $T$ acts as **word reversal on braid words at the Markov-trace level**:*

$$
  T \;:\;
  \sigma_{i_1}^{\epsilon_1} \cdots \sigma_{i_\ell}^{\epsilon_\ell}
  \;\longmapsto\;
  \sigma_{i_\ell}^{\epsilon_\ell} \cdots \sigma_{i_1}^{\epsilon_1}.
$$

*By the Markov trace cyclicity axiom $\mathrm{tr}_M(ab) = \mathrm{tr}_M(ba)$ ([`thm:jones-markov-trace`](#thm:jones-markov-trace), [jones1987]), word reversal is trace-invariant for the Markov closure. The Jones polynomial of $K$ and of its time-reversed counterpart $K^T$ coincide. The operator $T$ is an involution ($T^2 = \mathrm{id}$). It preserves $q$, color-sheet flavors, and Hecke generator signs. It acts purely on the **ordering** of crossings.*

## The action

For a braid word $\beta = \sigma_{i_1}^{\epsilon_1} \cdots \sigma_{i_\ell}^{\epsilon_\ell}$, define $\beta^T$ as the reversed word. At the Markov-trace level (where braids close to knots or links), trace cyclicity gives:

$$
  \mathrm{tr}_M(\beta)
  \;=\;
  \mathrm{tr}_M(\beta^T).
$$

The reversed word produces the **mirror-orientation** link, which has the same Jones polynomial as the original by trace cyclicity.

## Disentanglement of D8 from CPT

The composite bar-involution acts on $q$, $\sigma_i$, and the trace orientation (when followed by Markov closure). We separate the three categorical sources:

| Acts on | Symbol map |
|---------|------------|
| Hecke generator chirality only | $\sigma_i \mapsto \sigma_i^{-1}$ (= **P** alone, D7) |
| Color sheets only | flavor $u \leftrightarrow \bar u$ (= **C** alone, D6) |
| Braid word ordering only | $\beta \mapsto \beta^T$ (= **T** alone, this conjecture) |

$T$ alone is the **trace-cyclicity dual**. It acts only on the combinatorial ordering of generators in a braid word. It leaves generator signs, $q$, and color sheets fixed. Composed with $C$ and $P$, it recovers the bar-involution = $CPT$ composite.

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration level**: $T$ preserves Coxeter length $\ell(\beta)$ (word reversal does not change generator count).
- **Jet order**: $h^0$ ($T$ fixes $q$ entirely).
- **Bar-symmetry status**: bar-trivial. Markov-trace values are invariant under $T$ by trace cyclicity. Thus, $T$-anti-symmetric observables are bar-trivial at the Markov-trace level.

## Lean axiomatisation (sketch)

```lean
class TFromTraceCyclicity (M : Type*) [BrCategory M] [Hecke M] where
  /-- Word-reversal involution on braid-group elements. -/
  t_action : Braid n → Braid n
  /-- T^2 = id. -/
  t_involution : ∀ β, t_action (t_action β) = β
  /-- T fixes Hecke generator signs and q. -/
  t_preserves_generators :
    ∀ (β : Braid n) (i : Fin n),
      sigma_count_in (t_action β) i = sigma_count_in β i
  /-- T preserves Markov trace (cyclicity). -/
  t_preserves_tr_M : ∀ β, tr_M (t_action β) = tr_M β
  /-- Bar-involution factorisation: bar = P · C · T. -/
  bar_eq_p_c_t : bar_involution = p_action ∘ c_action ∘ t_action
```

## Consumers / downstream

- [`conj:cpt-orbit-closure-density`](#conj:cpt-orbit-closure-density) becomes a corollary of $CPT = C \cdot P \cdot T$ once D6, D7, and D8 close.
- The Markov-trace cyclicity axiom [`thm:jones-markov-trace`](#thm:jones-markov-trace) supplies the $T$-invariance directly. This conjecture is the smallest possible closure (an axiomatic statement that $T$ = word-reversal and $CPT$ = bar via composition).

## Open R&D

1. **Verify numerically** that for canonical atomic braids, the word reversal $\beta_K^T$ has identical $|\mathrm{tr}_M|$ via trace cyclicity. This is immediate from [`thm:jones-markov-trace`](#thm:jones-markov-trace), but worth a witness for the canonical atom catalogue.
2. **D8 to closed** requires a Lean instance proving the trace-cyclicity compatibility and the $\text{bar} = P \cdot C \cdot T$ factorisation.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) §1 D8
  + §2 Cluster A (CPT decomposition D5 $\to$ D6 + D7 + D8)
- Sibling Z/2 decompositions of CPT:
  [`conj:c-from-color-flavor-swap`](c-from-color-flavor-swap.md) (D6),
  [`conj:p-from-braid-mirror`](p-from-braid-mirror.md) (D7)
- Markov-trace cyclicity:
  [`thm:jones-markov-trace`](jones-markov-trace.md)
- Composite CPT: [`conj:cpt-orbit-closure-density`](#conj:cpt-orbit-closure-density)
- Bar-involution: [`bar-involution.md`](bar-involution.md)
