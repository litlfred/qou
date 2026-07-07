<!-- FILE_START: atomic-braid-mass-crossing-locality-cpt-intro.md -->
The preceding sub-section developed the foundations for the atomic-braid linear programming (LP) and mass formula. This included LP stability, the $q$-integer mass formula, the universal integer linear programming (ILP) algorithm, neutron-proton splitting, and color-pairing binding. We also covered the $Z = 1$-20 mass table, atomic normal form witnesses, step-LP verification, Gröbner reduction methods, tower binding energy, mass categorical descent, and Thurston-volume additivity. 

This sub-section establishes the consequences for crossing grading, locality, and CPT orbits. We treat mass-volume factorization, the crossing-graded mass expansion, and lifted-crossing locality. We derive $q$-holonomy locality, Frobenius-packing density, and CPT-orbit closure density. Finally, we establish bar-involution invariance and soft-confinement at $q_0$ to complete the atomic-braid mass-formula arc.
<!-- FILE_END: atomic-braid-mass-crossing-locality-cpt-intro.md -->

<!-- FILE_START: q-holonomy-locality-derivation.md -->
## Locality from flatness of the KZ connection

The [lifted-crossing locality](#conj:lifted-crossing-locality) hypothesis reduces to a statement about the holonomy of the Knizhnik-Zamolodchikov (KZ) connection at generic $q$. The physical meaning is direct: cross-talk between two lifted crossings measures the curvature of a flat connection on a punctured surface. Flatness implies factorization.

## Setup — the KZ connection

Let $X_n := \{(w_1, \ldots, w_n) \in \mathbb{C}^n : w_i \neq w_j\}$ be the configuration space of $n$ distinct complex points. The (quantum) KZ connection on $X_n$ with values in $V^{\otimes n}$ (for $V$ a $U_q(\mathfrak{sl}_2)$-module) is:

$$
  \nabla \;=\; d \;-\; \frac{\hbar_q}{2 \pi i}
  \sum_{i < j} \Omega_{ij}\,\frac{dw_i - dw_j}{w_i - w_j},
$$

where $\Omega_{ij}$ is the Casimir element acting on factors $i, j$ of $V^{\otimes n}$.

**Theorem** (Kohno-Drinfeld \cite{kohno1987}).
*The KZ connection is flat:*
$$
  [\nabla_i, \nabla_j] \;=\; 0
  \quad\Longleftrightarrow\quad
  [\Omega_{ij}, \Omega_{kl}] = 0 \text{ for disjoint pairs,}
  \text{ and infinitesimal braid relations.}
$$
*The monodromy representation of $\pi_1(X_n / S_n) = B_n$ on $V^{\otimes n}$ coincides with the quantum-group R-matrix representation of $U_q(\mathfrak{sl}_2)$.*

## Applying to the mass endomorphism

We model each crossing $c$ of an atomic braid as a puncture in the configuration space $X_n$. A lifted crossing inserts a quantum-dilogarithm operator $\Phi_q(z_c)$ at that puncture; an unlifted crossing inserts the identity.

The mass contribution of a configuration with lifted subset $S \subseteq \mathrm{Cr}(\mathcal{K})$ is the trace of the resulting braid-word operator. Parallel transport along the closure of the braid word in $X_n / S_n$ computes this trace.

**Claim.**
*At generic $q$, the parallel transport factorizes over disjoint punctures:*
$$
  \mathrm{Tr}\!\left[
    \prod_{c \in S} \Phi_q(z_c) \cdot \rho(\beta)
  \right]
  \;=\;
  \mathrm{Tr}[\rho(\beta)] \cdot \prod_{c \in S}
  \eta(c),
$$
*where $\eta(c)$ is the single-crossing expectation value.*

**Proof sketch.**
1. By flatness (Kohno-Drinfeld), any two closed loops $\gamma_i, \gamma_j$ encircling separated subsets $S_i, S_j \subseteq S$ have commuting holonomies: $[\mathrm{Mon}(\gamma_i), \mathrm{Mon}(\gamma_j)] = 0$.
2. Simultaneous diagonalization of the commuting monodromies decomposes the trace into a sum over eigenvalue-labelings.
3. The $\Phi_q$ insertions act by scalar on each eigenstrand (they are diagonal in the R-matrix eigenbasis).
4. Therefore, the multi-crossing expectation is a product of single-crossing expectations.

The scalar obstruction — the only failure mode — requires non-abelian monodromy, which flatness rules out. $\square$

## Failure of flatness

Flatness is equivalent to the semisimplicity of the braided tensor category of $U_q(\mathfrak{sl}_2)$-representations:

- **Generic $q$ (not a root of unity)**: $U_q$-representations are semisimple, the KZ connection is flat, and locality holds.
- **$q = e^{2 \pi i / \ell}$ (root of unity)**: Non-semisimple subquotients appear (the Jones-Wenzl truncation at level $\ell - 2$). The category remains modular via Lyubashenko's construction, but the KZ connection acquires monodromy along paths encircling truncated weight spaces. Locality fails at level $\ell$.
- **$q = 1/\varphi^2$ (golden degeneration)**: The connection is still flat on $X_n$, but the Descartes curve $\mathcal{E}_q$ itself becomes singular, making $z_q$ undefined. Locality becomes vacuous.

## The substrate as the locality window

At the pinned substrate parameter $q_0 \approx 1.11$, which is real and generic:

$$
  q_0 \in \mathbb{R}_{>1} \setminus \{\text{roots of unity}\}
  \;\Longrightarrow\;
  \text{KZ flat}
  \;\Longrightarrow\;
  \text{locality.}
$$

Moreover, the [soft confinement level $\ell_*(q_0) \approx 10$](#rem:soft-confinement-at-q0) is far enough from the first non-trivial root of unity $q = e^{i \pi / 3}$ (level $\ell = 3$) that Plancherel weights for higher representations are exponentially suppressed. Locality holds to extremely high order in $1/\ell_*$.

## Corollary — exponential mass scaling

Combining locality with the [crossing-graded expansion](#conj:crossing-graded-mass-expansion):

$$
  \mathfrak{m}(\mathcal{K}; q_0)
  \;=\;
  \mathfrak{m}_{\mathrm{GB}}(\mathcal{K}) \cdot
  \prod_{c \in \mathrm{Cr}(\mathcal{K})} (1 + \xi(q_0)\,\eta(c)).
$$

At the homogeneous fixed point $\eta(c) \equiv 1$:

$$
  \mathfrak{m}(\mathcal{K}; q_0)
  \;=\;
  \mathfrak{m}_{\mathrm{GB}}(\mathcal{K}) \cdot (1 + \xi(q_0))^{c(\mathcal{K})}.
$$

At $q_0$, $\xi(q_0) = D(\lambda(\mathcal{E}_{q_0}))/\hbar_q^2 \approx 0.9170/0.00982 \approx 93.4$. Each crossing multiplies mass by $\approx 94$. Exponential scaling in crossing count is the empirical signature of KZ flatness at the substrate.
<!-- FILE_END: q-holonomy-locality-derivation.md -->

<!-- FILE_START: cpt-orbit-closure-density.md -->
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
<!-- FILE_END: cpt-orbit-closure-density.md -->

<!-- FILE_START: bar-involution-invariance.md -->
**Proposition (conditional on [`conj:symmetric-crystal-pair-production`](#conj:symmetric-crystal-pair-production) and [`conj:crystal-graph-realization`](#conj:crystal-graph-realization)).**
Let $\bar\cdot \colon \mathbb{Z}[q, q^{-1}] \to \mathbb{Z}[q, q^{-1}]$ be the bar-involution sending $q \mapsto q^{-1}$. This is the Dynkin-fold involution on the $A_{n-1}$ Hecke algebra after Type-B folding (\cite{kashiwara1991, khovanovlauda2009, brundankleshchev2009}). Then:

1. (**Plancherel-weight invariance**) For every partition $\lambda \vdash n$ and every $q > 0$, the Plancherel weight satisfies $\overline{w_\lambda(q)} = w_\lambda(q)$, i.e. $w_\lambda(q^{-1}) = w_\lambda(q)$.
2. (**Transpose-pair equality**) $w_\lambda(q) = w_{\lambda^T}(q)$ for every $\lambda \vdash n$, where $\lambda^T$ is the transpose partition (the Dynkin involution / chirality-reversal from [`conj:cpt-orbit-closure-density`](#conj:cpt-orbit-closure-density)).
3. (**Type-B-folded normal forms**) Any Hecke normal form $T_w$ produced by the symmetric-crystal pair-production engine of [`conj:symmetric-crystal-pair-production`](#conj:symmetric-crystal-pair-production) is bar-invariant: $\overline{T_w} = T_w$. Equivalently, the image of the folded crystal-step operator $(\tilde f_i, \tilde f_{\bar i})$ is fixed by the bar-involution.

## Significance: a witness against hand-rolled CPT violations

The conditions $\overline{T_w} = T_w$ and $w_\lambda(q^{-1}) = w_\lambda(q)$ are necessary consequences of Type-B folding. Any normal form, mass formula, or LP cost vector computed via the QOU pipeline must satisfy them. Failure of either condition signals that the computation has introduced a chirality bias incompatible with the symmetric-crystal substrate.

This block packages the invariance lemmas as a regression-test witness. It provides a structural cross-check that downstream Lean files in `particle-interactions/` can call to certify that no manual $\mathbb{Z}/2\mathbb{Z}$ CPT rule has been introduced.

## Proofs

**(1) Plancherel-weight invariance.** The Plancherel weight is $w_\lambda(q) = \dim_q(V_\lambda)^2 / [n]_q!$ where the $q$-integer is $[k]_q = (q^k - q^{-k})/(q - q^{-1})$. Direct calculation gives:

$$
  [k]_{q^{-1}}
  \;=\; \frac{q^{-k} - q^k}{q^{-1} - q}
  \;=\; \frac{-(q^k - q^{-k})}{-(q - q^{-1})}
  \;=\; [k]_q.
$$

Thus $[k]_q$ is bar-invariant. Since $\dim_q V_\lambda$ is a ratio of products of $q$-integers (hook formula), and $[n]_q!$ is a product of $q$-integers, the entire Plancherel weight is a quotient of bar-invariants, hence bar-invariant. $\square$

**(2) Transpose-pair equality.** Hook lengths are unchanged by transpose. If $\lambda^T$ is obtained from $\lambda$ by swapping rows and columns, then for every cell $x = (i, j) \in \lambda$ there is a corresponding cell $x^T = (j, i) \in \lambda^T$ with $h_{\lambda^T}(x^T) = h_\lambda(x)$. Hence $\prod_x [h(x)]_q$ is unchanged, and $\dim_q V_\lambda = \dim_q V_{\lambda^T}$. Squaring and dividing by $[n]_q!$ gives $w_\lambda(q) = w_{\lambda^T}(q)$. $\square$

**(3) Type-B-folded normal forms.** This follows from the symmetric-crystal pair-production conjecture ([`conj:symmetric-crystal-pair-production`](#conj:symmetric-crystal-pair-production)). The folded operator pair $(\tilde f_i, \tilde f_{\bar i})$ produces two descendants whose Hecke normal forms are bar-conjugates. Their sum is the only object the engine emits, and is therefore bar-invariant. Single-chirality outputs are unreachable.

Steps (1) and (2) are unconditional; step (3) is conditional on [`conj:symmetric-crystal-pair-production`](#conj:symmetric-crystal-pair-production) and is registered as such in the Lean file (class-conditional, per AGENTS.md §3b-cond).

## Worked example: $n = 3$

The three Wedderburn blocks $(3)$, $(2, 1)$, $(1, 1, 1)$ have hook lengths:

| $\lambda$ | hooks | $[\,h\,]_q$ products |
|---|---|---|
| $(3)$ | $3, 2, 1$ | $[3]_q [2]_q [1]_q$ |
| $(2, 1)$ | $3, 1, 1$ | $[3]_q [1]_q [1]_q$ |
| $(1, 1, 1)$ | $3, 2, 1$ | $[3]_q [2]_q [1]_q$ |

Transpose pairing $(3) \leftrightarrow (1, 1, 1)$ has identical hook products. This yields identical $\dim_q$ and identical $w_\lambda$, matching (2). The self-dual $(2, 1)$ has $\lambda = \lambda^T$ by definition.

Bar-invariance under $q \mapsto q^{-1}$ follows from $[k]_{q^{-1}} = [k]_q$ on every factor.

## Lean formalisation

[`bar-involution-invariance.lean`](bar-involution-invariance.lean)

- Defines `barInvolution : ℝ → ℝ → ℝ` as the substitution $q \mapsto q^{-1}$ on the multiplicative group $\mathbb{R}_{>0}$.
- Defines `qInteger` (the $q$-integer $[k]_q$) and proves `q_integer_bar_invariant`: $[k]_{q^{-1}} = [k]_q$ for $q > 0$.
- Defines the abstract Plancherel weight as a quotient of $q$-integer products and proves `plancherel_weight_bar_invariant` and `plancherel_weight_transpose_eq` (parts 1 and 2 above).
- Records part 3 as a conditional theorem under the class `SymmetricCrystalPairProduction n` (per AGENTS.md §3b-cond), citing the upstream conjecture.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs (real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$). Any generic categorical or $q$-deformation identities it uses remain valid over an abstract coefficient ring; we only specialise their archimedean realisation here.
<!-- FILE_END: bar-involution-invariance.md -->

<!-- FILE_START: soft-confinement-at-q0.md -->
**1. Soft confinement at the substrate parameter.**
The Wedderburn block labels of $H_n(q)$ (partitions $\lambda \vdash n$) are combinatorial and $q$-independent. The measure on this grading (the Plancherel weights $w_\lambda(q) = d_q(\lambda)^2 / [n]_q!$) depends sensitively on $q$.

At roots of unity $q = e^{2 \pi i / \ell}$, quantum dimensions $d_q(\lambda)$ vanish or turn negative. Representations with more than $\ell - 1$ rows become strictly confined (zero-weight). This is the Jones-Wenzl truncation underlying fusion-category constructions: a sharp cutoff at level $\ell$.

At the substrate parameter $q_0 = 1.109978595554181\ldots$ (generic real, not a root of unity), no representation is strictly confined. But Plancherel weights decay rapidly with partition size, producing a soft confinement level:
$$
  \ell_*(q_0)
  \;\sim\;
  \frac{1}{\log q_0}
  \;\approx\;
  \frac{1}{\log 1.10998}
  \;\approx\;
  9.6.
$$
Partitions of depth or width exceeding $\ell_*$ contribute negligibly to the Frobenius packing and can be truncated.

**2. Implication for atomic braids.**
An atomic braid with $A$ nucleons has $3A$ strands and lives in $H_{3A}(q_0)$, whose Wedderburn sum ranges over partitions $\lambda \vdash 3A$. Soft confinement implies:

- **Light atoms** ($A \leq 3$, $3A \leq 9 \lesssim \ell_*$): The full Plancherel sum is active. No truncation occurs.
- **Medium atoms** ($A \sim 4$ to $6$, $3A \sim 12$ to $18$): Partitions with more than $\sim 10$ rows or columns have exponentially small weight and drop out.
- **Heavy atoms** ($A \gtrsim 10$): The sum effectively truncates at shape $\approx \ell_*$, the natural ceiling of the Plancherel-concentrated regime (the Vershik-Kerov limit shape, $\lambda_1 \sim 2\sqrt{n}$).

The transition from $H_3$-per-nucleon to the full $H_{3A}$ sum dictates why [$\alpha$-cluster unfolding](#prop:tower-binding-energy) is numerically necessary beyond $A \sim 4$. The block structure of $H_{3A}$ for larger $A$ exceeds $\ell_*$, and cross-Wedderburn couplings that collapse under truncation must be re-summed via cluster decomposition.

**3. Numerical estimate.**
At $q_0 = 1.109978595554181\ldots$:
See [Table](#tbl:soft-confinement-at-q0-table-data).

The rapid saturation of cumulative weight by the first few partitions quantitatively demonstrates soft confinement. The [cutoff $\ell_*(q_0) \approx 10$](#prop:local-substrate-q) represents the horizon where the substrate's grading effectively terminates.
<!-- FILE_END: soft-confinement-at-q0.md -->

