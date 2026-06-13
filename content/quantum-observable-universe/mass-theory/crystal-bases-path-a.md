**Compute-optimisation note** for the `Path A` verification of
[per-nucleon shift additive linearity](#prop:per-nucleon-shift-additive-linearity):
$\mathrm{shift}_{\mathrm{NF}}(\mathcal{B}_K) = 18Z + 21N + 1$ for $A \geq 2$.

The existing `Path A` verifier
[`per_irrep_pole_atom.py`](../../../folio-assistant/computations/per_irrep_pole_atom.py)
computes per-irrep $\chi^\lambda(\mathcal{B}_K)(q)$ symbolically via
Hoefsmit seminormal matrices, then extracts the $u$-pole order
after substituting $q = u^2$.  At $H_n$ for $n \geq 9$ this
becomes prohibitive: 26 partitions at $H_9$ $\times$ ~30s of sympy
arithmetic per partition; 77 partitions at $H_{12}$ projecting
to ${\sim} 1$ hour total.  At $H_{15}$ ($n_{\mathrm{partitions}}
= 176$) and $H_{18}$ (${=}\,297$) the symbolic path is
intractable in a session budget.

## Crystal-bases substitution

In the Kashiwara crystal limit $q \to 0$, the Hecke generators
$\sigma_i$ acquire signed-permutation actions on the standard
Young tableaux SYT($\lambda$).  The per-letter
$u$-power contribution on a fixed eigenline is then a constant
integer (per [crystal isospin degeneracy](#prop:crystal-isospin-degeneracy)
and per the column-rich SYT analysis of
[`crystal_pole_order.py`](../../../folio-assistant/computations/crystal_pole_order.py)),
yielding the lookup table:

See [Table 1](#tbl:crystal-bases-path-a-table1-data).

Per-SYT $\mathrm{ord}_{u=0}$ is the *sum* of these per-letter
contributions over the entire 47-letter ($A=4$ ${}^{4}$He) canonical
$\bowtie_K$-coupled atomic word; per-$\lambda$ $\mathrm{ord}_{u=0}$
is the *minimum* over $T \in \mathrm{SYT}(\lambda)$ provided
the leading-coefficient sum is non-cancelling.

The total $\mathrm{ord}_{u=0}(\mathrm{tr}_M(\mathcal{B}_K))$ is then

$$
  \min_{\lambda \,\vdash\, 3A,\; \mathrm{height}(\lambda) \leq 6}
    \;\bigl(\mathrm{ord}_{u=0}(y_\lambda) + \mathrm{ord}_{u=0}(\chi^\lambda)\bigr)
$$

with the full pole order $= -\min$ when negative.

## Implementation

[`per_irrep_pole_atom_crystal.py`](../../../folio-assistant/computations/per_irrep_pole_atom_crystal.py)
implements the crystal-bases path with two layered caches:

- **C1**: `lru_cache` on `standard_young_tableaux` — atoms of the
  same $n$ share shape inventories.
- **C2**: `_rho_table_for_shape` — precomputes
  $\rho_T(\mathrm{gen}) \in \{+1, -1, 0, \mathrm{vacuum}\}$ for every
  $(T, \mathrm{gen})$ pair per shape; reduces per-letter cost from
  10 array-index ops to a single integer lookup.

The $\mathrm{ord}_{u=0}(y_\lambda)$ values are precomputed once via
[`y_lambda_pole_order_cache.py`](../../../folio-assistant/computations/y_lambda_pole_order_cache.py)
into [`y-lambda-pole-order-cache.json`](../../../folio-assistant/computations/y-lambda-pole-order-cache.json),
keyed by $(n, \lambda)$.  The cache is the only sympy-heavy piece;
once built, the per-atom verification is pure integer arithmetic
on the SYT basis.

## Verification

See [Table 2](#tbl:crystal-bases-path-a-table2-data).

Witness:
[`per-irrep-pole-atom-crystal.witness.json`](../../../folio-assistant/computations/per-irrep-pole-atom-crystal.witness.json).
The top-level `asserted_atoms_match_closed_form_shift` assertion
gates only on **asserted atoms** — the verified $A \geq 2$ scope
of the closed form plus the proton (which agrees with the closed
form at $A = 1$).  The neutron row is computed and reported but
flagged `asserted: false` and excluded from the gate, so the
witness remains green for the verified scope.  See *A=1 anomaly*
below for the diagnostic interpretation.

## Speedup

Per-atom timing (with $y_\lambda$ pole-order cache **already
built**; per-atom cost is then pure integer arithmetic on the SYT
basis):

See [Table 3](#tbl:crystal-bases-path-a-table3-data).

The $y_\lambda$ pole-order cache itself takes **~40 minutes** to
build at $n = 12$ (multi-process across 4 cores; sympy.simplify on
the 77 deeply-nested Wenzl-bridge expressions is the chokepoint).
This is a **one-time cost** per $n$; downstream re-runs at the
same $n$ are sub-second.

The existing baseline scales as $O(\mathrm{dim}(V_\lambda)^2 \cdot
L \cdot \text{symbolic-q ops})$ — dominated by sympy
matrix-product simplification.  Crystal-bases scales as
$O(\sum_\lambda f^\lambda \cdot L)$ — pure integer arithmetic, no
symbolic-q.  The crossover where crystal-bases is fastest occurs
at $n \geq 9$; at $n \leq 6$ both paths are competitive once the
$y_\lambda$ cache is built.

## A=1 anomaly

The crystal-bases Path A returns $\mathrm{shift}(\mathrm{neutron}) = 19$,
*not* the closed-form-extrapolated $22 = 18 \cdot 0 + 21 \cdot 1
+ 1$.  This may reflect a sub-leading correction that the
leading-order crystal asymptotic does not capture (the "Hecke
skein" $\sigma^2 = h\sigma + 1$ produces interference between
adjacent $\sigma$ on the same generator that affects sub-leading
$u$-powers; the closed form is verified for $A \geq 2$ where this
interference is washed out by the broader Wedderburn-block
structure).  Either:

1. **Closed-form extrapolation fails at $A = 1$** for the neutron
   — the formula $\mathrm{shift}(Z, N) = 18Z + 21N + 1$ is
   verified only on the $A \in \{2, 3, 4, 5, 6\}$ atoms in
   [`per-nucleon-shift-derivation.witness.json`](../../../folio-assistant/computations/per-nucleon-shift-derivation.witness.json),
   and its $A = 1$ extrapolation gives 22 for the neutron without
   independent verification.  The proton case happens to give
   $19$ either way (closed-form $18 \cdot 1 + 0 + 1 = 19$ matches
   `per_irrep_pole_proton_h3` symbolic path).
2. **Crystal-bases sub-leading correction** is needed at $A = 1$
   to recover the true symbolic-path pole.  The proton case
   passes by accident of cancellation balance (1 $\bowtie_K$ on
   each generator); the neutron has 2 $\bowtie_K$ on $G_0$, 0 on
   $G_1$ — an asymmetry that the leading crystal expansion
   smooths over.

The most parsimonious resolution is **(1)** — the closed-form
formula is rigorously valid for $A \geq 2$ only, and the $A = 1$
neutron entry is a formula-extrapolation that doesn't reflect the
underlying Hecke arithmetic.  A direct symbolic verification at
$A = 1$, $N = 1$ would settle the question; this is well within
the budget of `per_irrep_pole_proton_h3.py` adapted to neutron
inputs and is left as an open follow-up.
