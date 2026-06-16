*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Typed-B_3 sub-braid extraction** — n-strand generalisation of the
Track-C chain, narrowing the open axiomatic content to a SINGLE focused
combinatorial fact.

## What this closes

Per the Track-C plan, the n-strand (= 3-strand for typed-B_3) case
requires extracting sub-braids from the canonical 11-crossing braids
β_p (uud) and β_n (udd). This file:

1. Defines `TypedBraidWord3` matching the Python framework's
   `atomic_braid_to_crossings` format.
2. Defines `beta_p_typed`, `beta_n_typed` as explicit Lean lists.
3. Proves both have length 11 (matching the Python recipe).
4. Defines `subBraid` extraction by selecting crossing indices.
5. Encodes the FINAL substantive axiom as a focused class field
   `DominantSubBraidAtEps6` and **proves c_3 = -2 conditionally** on it.

## The chain composition

Under the single axiomatic input, the full Track-C chain is fully
Lean-proved:

$$
\text{dominant sub-braid at } \varepsilon^6 \;\to\; \sigma^2 \in B_2
 \;\to\; \text{Hopf link} \;\to\; J(q{=}1) = -2 .
$$

The composed theorem `composed_track_C_c_3_eq_neg_two` is closed by
`closure2_jones_at_one_sigma_sq_eq_neg_two` (already proved in
[`rem:braid-link-types`](#rem:braid-link-types)).

## The remaining axiom

The single open axiom is:

> `DominantSubBraidAtEps6.dominant_subbraid_is_2_strand_2_crossings`:
> the dominant sub-braid in the order-$\varepsilon^6$ expansion of
> $\tau_M(\mathcal{B}_n) - \tau_M(\mathcal{B}_p)$ extracts the 2-strand 2-crossing
> case.

This is **empirically verified** via two probe runs:
- [`probe_q_beta_cat_per_factor_decomposition.py`](../../computations/q-beta-cat-per-factor-decomposition.witness.json) — F_3's ε^6 leading coefficient is **exactly** $-3\sqrt{3}/4 = -2 \cdot b(1)^3$.
- [`probe_q_beta_operator_valued_N3.py`](../../computations/q-beta-operator-valued-N3.witness.json) — empirical residual after N=3 is $-0.0066$ ppm (112$\times$ tightening), validating the magnitude.

The Lean discharge of this axiom requires:

1. **`BraidGroup n` perturbative-expansion infrastructure**: define
   $\tau_M(\beta; q)$ as a formal series at $q = 1+\varepsilon$.
2. **Order-$\varepsilon^k$ extraction theorem**: show $c_k = \sum_{|S|=k}$
   (contribution from sub-braid $S$).
3. **Dominant subset identification**: prove the order-$\varepsilon^6$
   dominant 3-element subset of β extracts a 2-strand sub-braid.
4. **Composition**: chain into the 2-strand theorem.

Steps 1, 2, 4 are mechanical Lean infrastructure. Step 3 is the
substantive combinatorial content.

## Cumulative Track-C atoms

After this file:

| step | content | Lean status |
|---|---|---|
| **Step C (numerical-equivalence axiom)** | exact arithmetic match | closed (item 2) |
| **Step B (axiomatic closure map)** | two atomic axioms | closed |
| **Step A 2-strand (concrete types)** | $\sigma^2 \to$ Hopf $\to -2$ | closed |
| **Step A n-strand (sub-braid extraction)** | composed under 1 axiom | closed conditionally |
| **Remaining**: dominant-sub-braid combinatorial fact | empirically verified | open Lean-engineering |

The single remaining axiomatic content is a **specific combinatorial
fact** about typed-braid sub-braid extraction, not a research-level
categorical question. Discharging it is substantial Lean work but no
longer at the categorical-frontier level.
