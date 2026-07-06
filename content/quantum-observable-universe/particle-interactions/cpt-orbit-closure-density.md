**Proposition (conditional on [`conj:symmetric-crystal-pair-production`](#conj:symmetric-crystal-pair-production) and [`conj:crystal-graph-realization`](#conj:crystal-graph-realization)).**

Let $\sigma \colon \mathrm{Part}(n) \to \mathrm{Part}(n)$ be the transpose involution $\lambda \mapsto \lambda^{T}$—the Dynkin involution on the $A_{n-1}$ crystal that becomes the bar-involution (chirality-reversal) operator after folding to type $B$ ([`conj:symmetric-crystal-pair-production`](#conj:symmetric-crystal-pair-production)). For an atomic link $\mathcal{K}$ with populated Wedderburn blocks $\Lambda(\mathcal{K}) \subseteq \mathrm{Part}(n)$, define

$$
  \mathrm{CPTSat}(\mathcal{K})
  \;:\Longleftrightarrow\;
  \sigma\bigl(\Lambda(\mathcal{K})\bigr)
    \;\subseteq\; \Lambda(\mathcal{K})
$$

which means $\Lambda(\mathcal{K})$ is closed under the Type-B fold.

Then the Frobenius packing-density rule of [`rem:frobenius-packing-density`](#rem:frobenius-packing-density) is a derived consequence of crystal structure:

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

## Elimination of the Boolean flag

The conjectural class [`mass-volume-factorization.lean`](mass-volume-factorization.md) carries a field `cptSaturated : Bool` on its `FrobeniusPackingDensity` structure. The proposition replaces this Boolean with the structural predicate $\mathrm{CPTSat}$, a property of the orbit structure of $\Lambda(\mathcal{K})$ under $\sigma$.

| Old (Boolean flag) | New (Type-B orbit closure) |
|---|---|
| `cptSaturated : Bool` | `isCPTSaturated : Set (Partition n) → Prop` |
| Asserted per-link by hand | Derived from `σ(Λ) ⊆ Λ` |
| Each instance must justify the flag | Justified once, by Type-B fold |
| CPT enforcement is post-hoc | CPT enforcement is structural |

The semantic equivalence is recorded by the Lean theorem `cpt_boolean_eq_orbit_closure`:

```
cptSaturated  =  decide (isCPTSaturated populatedBlocks)
```

This holds provided the populated-blocks set is decidable, which it is for finite $\Lambda \subset \mathrm{Part}(n)$. The Boolean flag is recovered by the $\mathbb{Z}/2\mathbb{Z}$ orbit count.

## Example: $n = 3$ Wedderburn

The blocks of $H_3(q)$ are $(3)$, $(2, 1)$, $(1, 1, 1)$ with $\sigma$-orbits:

| orbit | partitions | self-dual? | role |
|---|---|---|---|
| $\{(3), (1,1,1)\}$ | size 2 | no | sym $\leftrightarrow$ alt: chirality pair |
| $\{(2, 1)\}$ | size 1 | yes | std: self-dual / mixed channel |

Then:

- $\Lambda = \{(3)\}$ is not fold-closed; $\rho_F = m_e$. This matches the single-chirality branch.
- $\Lambda = \{(3), (1, 1, 1)\}$ is fold-closed; $\rho_F = 2 m_e$. This matches the alt-included branch.
- $\Lambda = \{(2, 1)\}$ is fold-closed by self-duality; $\rho_F = 2 m_e$. The doubled scale corresponds to the std block contributing symmetrically to itself, consistent with the Plancherel-weight arithmetic of [the packing dictionary](#rem:frobenius-packing-density).

In every case, the Boolean flag is recovered as the orbit-closure check.

## Correctness of the fold involution

The Type-B Cartan datum is obtained from the $A_{n-1}$ datum by folding along the Dynkin involution $i \mapsto n - i$ \cite{kashiwara1991, lecouvey2007}. On partitions, this is exactly the transpose $\sigma$. The KLR canonical basis of $H_n(R, q)$ is bar-invariant under $q \mapsto q^{-1}$ \cite{brundankleshchev2009, khovanovlauda2009}. The bar involution sends the Wedderburn block of $\lambda$ to that of $\lambda^T$, matching the chirality-reversal predicted by [`conj:symmetric-crystal-pair-production`](#conj:symmetric-crystal-pair-production).

Thus, $\sigma$ is the intrinsic fold whose existence is guaranteed by the symmetric-crystal structure. Every populated-blocks set $\Lambda$ inherits a $\sigma$-action. The question of CPT-saturation is whether $\Lambda$ lies in a fundamental domain of $\sigma$ or is invariant.

## Lean formalisation

The file [`cpt-orbit-closure-density.lean`](cpt-orbit-closure-density.lean) defines `partitionTranspose : Partition n → Partition n` and `isCPTSaturated (Λ : List (Partition n)) : Prop`. It proves the equivalence `cptSaturatedBool Λ = decide (isCPTSaturated Λ)` (`cpt_boolean_eq_orbit_closure`) by `rfl`. Partition-transpose involutivity is recorded as `partitionTranspose_involutive` (an axiom, pending the Mathlib `YoungDiagram.transpose_transpose` lemma).

The density-value lemmas `cpt_orbit_closure_density` (CPT-saturated $\to$ $2 m_e$) and `cpt_orbit_closure_density_single_chirality` (not CPT-saturated $\to$ $m_e$) are proved directly by `if_pos` and `if_neg`.

**Archimedean specialisation (§7c).** This block invokes real- or complex-analytic constructs (observables, bounds, numerical evaluation). Categorical identities remain valid over an abstract coefficient ring; their archimedean realisation is specialised here.
