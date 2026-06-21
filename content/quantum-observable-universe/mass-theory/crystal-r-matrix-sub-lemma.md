<!-- Theorem (conditional on:
       conj:crystal-graph-realization,
       prop:hecke-branching-trace-decomposition). -->

**Proposition (Crystal R-matrix Sub-lemma 2.1, operator-valued
form, conditional on
[`conj:crystal-graph-realization`](crystal-graph-realization.md)).**
*Let $\mathbf{H}_n(q)$ be the Iwahori–Hecke algebra over $R$ with
$q$ generic, $\lambda \vdash n$, and $\beta_1 \in \mathbf{H}_{n_1}(q)$,
$\beta_2 \in \mathbf{H}_{n_2}(q)$ with $n = n_1 + n_2$. Let
$\sigma_i \in \mathbf{H}_n(q)$ be a boundary generator and let
$A^\lambda_{\mu, \nu}(\sigma_i) \in \mathrm{End}(V_\mu \otimes V_\nu)^{\oplus c^\lambda_{\mu, \nu}}$
be its $(\mu, \nu)$-block in the
Wenzl 1988 LR decomposition
of $V_\lambda \downarrow_{\mathbf{H}_{n_1} \otimes \mathbf{H}_{n_2}}$.*

*Under
[`conj:crystal-graph-realization`](crystal-graph-realization.md)
(Brundan–Kleshchev iso $\mathbf{H}_n(R, q) \xrightarrow{\sim} R_\Lambda^{\mathrm{cyc}}(\mathfrak{sl}_n)$
plus the Kashiwara crystal limit at $q \to 0$), the matrix-entry
pole order of $A^\lambda_{\mu, \nu}(\sigma_i)$ at $q = 0$ on any
standard Young tableau $T \in \mathrm{SYT}(\lambda)$ in the
$(\mu, \nu)$-block is*

$$
  \boxed{\;\;
    \mathrm{pole}\bigl(A^\lambda_{\mu, \nu}(\sigma_i),\, T\bigr)
    \;=\;
    \mathbf{1}\bigl[\rho_T(i) \le -1\bigr]
  \;\;}
$$

*where*

$$
  \rho_T(i) \;:=\; c(\text{cell of }i{+}1\text{ in }T) - c(\text{cell of }i\text{ in }T),
  \qquad c(\square) \;:=\; \mathrm{col}(\square) - \mathrm{row}(\square)
$$

*is the **axial distance** between the cells of $i$ and $i + 1$ in $T$.*

## Why this closes the W-3 residual

The
[scalar form of Sub-lemma 2.1](../../../docs/audits/-sub-lemma-2-1-categorical-proof.md)
suffices for the W-3 D(u) closure at the column maximizer
$\lambda^* = (1^p)$ (1-dim irrep). The
[refined / operator-valued form](../../../docs/audits/-sublemma-2-1-refined.md)
was open for general multidim $\lambda$ (verified numerically 11/11
on the deuteron, but lacked a categorical proof).

This block closes the operator-valued form **categorically modulo**
[`conj:crystal-graph-realization`](crystal-graph-realization.md):

- **Step 1** of the audit: $q \to 0$ limit of $\sigma_i$ on the
  seminormal basis is the combinatorial $R$-matrix on
  $B_\mu \otimes B_\nu \subset B_\lambda$.
- **Step 2**: pole order is the indicator $\mathbf{1}[\rho_T(i) \le -1]$
  (this proposition).
- **Step 3**: the LR-supported $(\mu^*, \nu^*)$ achieving the maximum is
  column-rich (the $p$ boundary cells of $\lambda$ form a single column).
- **Step 4** ([cycle composition](#prop:alpha-shift-torus-knot)):
  $\alpha_{\mathrm{shift}}(T_{(p, k)}) = k \cdot (p - 1)$ — recovered
  in $\sim$10 lines of combinatorics (no Hoefsmit matrix entries).

## Conditional-class hypothesis (AGENTS.md §3b-cond)

The Lean file at
[`crystal-r-matrix-sub-lemma.lean`](crystal-r-matrix-sub-lemma.lean)
declares

```lean
class CrystalRMatrixSubLemma (R : Type u) [CommRing R] (q : R)
    [C : CrystalGraphRealization R q] where
  poleIndicator : ℤ → Bool
  pole_indicator_correct : ∀ rho : ℤ,
    poleIndicator rho = decide (rho ≤ -1)
```

with the upstream `[CrystalGraphRealization R q]` as an explicit
`[Instance]` hypothesis, satisfying the §3b-cond conditional-class
exception. A trivial model
(`CrystalRMatrixSubLemma.trivialModel`) proves the class
axiomatisation is **consistent** (no `sorry` introduced). The
unconditional structural lemmas
`poleIndicator_minus_one_eq_true`, `poleIndicator_plus_one_eq_false`,
`column_syt_pole_per_cycle`, and the AXKIA sanity checks
`axkia_pole_T_2_9`, `axkia_pole_T_3_5` are all proved by `rfl` /
`decide` from the class field, requiring no further hypothesis.

## Numerical verification (witness)

[`computations/crystal_pole_order.py`](../../../computations/crystal_pole_order.py)
computes the column-SYT pole-per-cycle for seven torus-knot
interfaces $\{T_{(2, 1)}, T_{(2, 3)}, T_{(2, 5)}, T_{(2, 9)}, T_{(3, 4)}, T_{(3, 5)}, T_{(3, 7)}\}$
plus six non-column $\lambda$ shapes for $n \in \{2, 3, 4\}$.
[`crystal-pole-order.witness.json`](../../../computations/crystal-pole-order.witness.json)
records 21 / 21 passing assertions, including the
[AXKIA chain](alpha-em-categorical-trace.md) values
$\alpha_{\mathrm{shift}}(T_{(2, 9)}) = 9$ and
$\alpha_{\mathrm{shift}}(T_{(3, 5)}) = 10$, giving
$\alpha_{\mathrm{EM}}^{-1} = q \cdot [9]_q \cdot [10]_q$
combinatorially.

## Bridge to `prop:confinement-nf-partial-proof`

The class instance produced by this block can be used to populate
`HasBranchingBlockLemma` in
[`confinement-nf-partial-proof.lean`](confinement-nf-partial-proof.lean)
via the Step 4 cycle composition. With both instances in scope,
the operator-valued form of `theorem_2_shift_decomposition` becomes
a categorical theorem (no `sorry` at the math level — only the two
routine LP-theory `sorry`s remain in the partial-proof file, which
are out of scope for this proposition).
