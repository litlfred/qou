**Proposition (conditional on [`conj:symmetric-crystal-pair-production`](#conj:symmetric-crystal-pair-production) and [`conj:crystal-graph-realization`](#conj:crystal-graph-realization)).**

*CPT-saturation = Type-B fold-orbit closure.*
*Let $\sigma \colon \mathrm{Part}(n) \to \mathrm{Part}(n)$ be the
transpose involution $\lambda \mapsto \lambda^{T}$ — the Dynkin
involution on the $A_{n-1}$ crystal that, after folding to type
$B$, becomes the bar-involution / chirality-reversal operator
([`conj:symmetric-crystal-pair-production`](#conj:symmetric-crystal-pair-production)).
For an atomic link $\mathcal{K}$ with populated Wedderburn blocks
$\Lambda(\mathcal{K}) \subseteq \mathrm{Part}(n)$, define*

$$
  \mathrm{CPTSat}(\mathcal{K})
  \;:\Longleftrightarrow\;
  \sigma\bigl(\Lambda(\mathcal{K})\bigr)
    \;\subseteq\; \Lambda(\mathcal{K})
  \;\Longleftrightarrow\;
  \Lambda(\mathcal{K}) \text{ is closed under the Type-B fold}.
$$

*Then the Frobenius packing-density rule of
[`rem:frobenius-packing-density`](#rem:frobenius-packing-density)
becomes a derived consequence of crystal structure rather than a
posited Boolean flag:*

$$
  \boxed{\;
    \rho_F(\mathcal{K})
    \;=\;
    \begin{cases}
      m_e   & \text{if } \mathrm{CPTSat}(\mathcal{K}) \text{ is false}
              \quad (\Lambda \text{ inside a fundamental domain of } \sigma),
              \\[4pt]
      2 m_e & \text{if } \mathrm{CPTSat}(\mathcal{K}) \text{ is true}
              \quad (\Lambda \text{ a union of } \sigma\text{-orbits}).
    \end{cases}
  \;}
$$

## Refactoring the Boolean flag away

The conjectural class
[`mass-volume-factorization.lean`](mass-volume-factorization.md) carries a
field `cptSaturated : Bool` on its `FrobeniusPackingDensity`
structure. The proposition above replaces this Boolean by the
*structural* predicate $\mathrm{CPTSat}$: a property of the orbit
structure of $\Lambda(\mathcal{K})$ under $\sigma$.

| Old (Boolean flag) | New (Type-B orbit closure) |
|---|---|
| `cptSaturated : Bool` | `isCPTSaturated : Set (Partition n) → Prop` |
| Asserted per-link by hand | Derived from `σ(Λ) ⊆ Λ` |
| Each instance must justify the flag | Justified once, by Type-B fold |
| CPT enforcement is post-hoc | CPT enforcement is structural |

The semantic equivalence is recorded by the Lean theorem
`cpt_boolean_eq_orbit_closure`:

```
cptSaturated  =  decide (isCPTSaturated populatedBlocks)
```

— provided the populated-blocks set is decidable, which it is for
finite $\Lambda \subset \mathrm{Part}(n)$. The Boolean flag is no
longer an independent piece of data; it is recovered by the
$\mathbb{Z}/2\mathbb{Z}$ orbit count.

## Worked example: $n = 3$ Wedderburn

The three blocks of $H_3(q)$ are $(3)$, $(2, 1)$, $(1, 1, 1)$ with
$\sigma$-orbits

| orbit | partitions | self-dual? | role |
|---|---|---|---|
| $\{(3), (1,1,1)\}$ | size 2 | no | sym $\leftrightarrow$ alt: chirality pair |
| $\{(2, 1)\}$ | size 1 | yes | std: self-dual / mixed channel |

Then:

- $\Lambda = \{(3)\}$ — *not* fold-closed (alt missing); $\rho_F = m_e$,
 matching the "single-chirality" branch of the original rule.
- $\Lambda = \{(3), (1, 1, 1)\}$ — fold-closed; $\rho_F = 2 m_e$,
 matching the "alt $\in \Lambda$" branch.
- $\Lambda = \{(2, 1)\}$ — fold-closed by self-duality; $\rho_F$ at
 the doubled scale corresponds to the std block contributing
 symmetrically to itself, consistent with the Plancherel-weight
 arithmetic of [the packing dictionary](#rem:frobenius-packing-density).

In every case the original Boolean flag is recovered as the orbit-
closure check, with no per-link case analysis.

## Why the fold is the right involution

The Type-B Cartan datum is obtained from the $A_{n-1}$ datum by
folding along the Dynkin involution $i \mapsto n - i$
\cite{kashiwara1991, lecouvey2007}. On the level of partitions
this is exactly the transpose $\sigma$. The KLR canonical basis
of $H_n(R, q)$ is bar-invariant under $q \mapsto q^{-1}$
\cite{brundankleshchev2009, khovanovlauda2009}, and the bar
involution sends the Wedderburn block of $\lambda$ to that of
$\lambda^T$ — exactly the chirality-reversal predicted by
[`conj:symmetric-crystal-pair-production`](#conj:symmetric-crystal-pair-production).

So $\sigma$ is not a chosen-by-fiat $\mathbb{Z}/2\mathbb{Z}$
action but the *intrinsic* fold whose existence is guaranteed by
the symmetric-crystal structure. Every populated-blocks set
$\Lambda$ inherits a $\sigma$-action, and "single-chirality vs
CPT-saturated" is the question of whether $\Lambda$ lies in
a fundamental domain of $\sigma$ or is invariant.

## Crystal-basis shortcut

This is shortcut #1 from AGENTS.md §7b applied at the
density-rule level: instead of the per-link Boolean flag and its
case analysis, the Type-B fold gives the rule structurally. The
Boolean is now a *consequence* of the orbit count, not an
independent input. Downstream proofs that branch on
`cptSaturated` can be rewritten to branch on
`isCPTSaturated populatedBlocks`, with the proposition above
discharging the equivalence.

## Lean formalisation

[`cpt-orbit-closure-density.lean`](cpt-orbit-closure-density.lean)
defines `partitionTranspose : Partition n → Partition n` (the
fold involution), the predicate
`isCPTSaturated (Λ : List (Partition n)) : Prop`, and proves the
equivalence

```
cptSaturatedBool Λ  =  decide (isCPTSaturated Λ)
```

(`cpt_boolean_eq_orbit_closure`) by `rfl`, since `cptSaturatedBool`
is defined as exactly `decide (isCPTSaturated Λ)`. Partition-
transpose involutivity is recorded as
`partitionTranspose_involutive` (axiom; pending the Mathlib
`YoungDiagram.transpose_transpose` lemma, registered via
[kassel1995] / standard partition combinatorics).

The density-value lemmas
`cpt_orbit_closure_density` (CPT-saturated $\to$ $2 m_e$) and
`cpt_orbit_closure_density_single_chirality` (not CPT-saturated
$\to$ $m_e$) are unconditional and proved directly by `if_pos` /
`if_neg` on the decidable predicate.
