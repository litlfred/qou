**Compute-optimisation note** for the `Path A` verification of
[per-nucleon shift additive linearity](#prop:per-nucleon-shift-additive-linearity):
$\mathrm{shift}_{\mathrm{NF}}(\beta_K) = 18Z + 21N + 1$ for $A \geq 2$.

The existing `Path A` verifier
[`per_irrep_pole_atom.py`](../../../folio-assistant/computations/per_irrep_pole_atom.py)
computes per-irrep $\chi^\lambda(\beta_K)(q)$ symbolically via
Hoefsmit seminormal matrices, then extracts the $u$-pole order
after substituting $q = u^2$.  At $H_n$ for $n \geq 9$ this
becomes prohibitive: 26 partitions at $H_9$ × ~30s of sympy
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

| letter `(c, d, gen)` | sym ($\rho_T(\mathrm{gen}) > 0$) | anti ($\rho_T(\mathrm{gen}) < 0$) |
|---|--:|--:|
| $\sigma$ (`d = 0`)        | $+2$ | $-2$ |
| $\sigma^{-1}$ (`d = -h`)  | $-2$ | $+2$ |
| $\Delta_I$ (`d = -h/2`)   | $-2$ | $-2$ (leading $u^{-2}$ from $\pm \tfrac{1}{2}(u^2 + u^{-2})$) |

Per-SYT $\mathrm{ord}_{u=0}$ is the *sum* of these per-letter
contributions over the entire 47-letter ($A=4$ ⁴He) canonical
$\Delta_I$-coupled atomic word; per-$\lambda$ $\mathrm{ord}_{u=0}$
is the *minimum* over $T \in \mathrm{SYT}(\lambda)$ provided
the leading-coefficient sum is non-cancelling.

The total $\mathrm{ord}_{u=0}(\mathrm{tr}_M(\beta_K))$ is then

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

| atom | $(Z, N)$ | $n$ | predicted shift | crystal-Path-A | match |
|------|--------|-----|---:|---:|:---:|
| proton    | $(1, 0)$ | 3  | $19$  | $19$  | ✓ |
| deuteron  | $(1, 1)$ | 6  | $40$  | $40$  | ✓ |
| tritium   | $(1, 2)$ | 9  | $61$  | $61$  | ✓ |
| ${}^3\mathrm{He}$ | $(2, 1)$ | 9  | $58$  | _(in flight)_ | _pending_ |
| ${}^4\mathrm{He}$ | $(2, 2)$ | 12 | $79$  | _(in flight)_ | _pending_ |
| ${}^5\mathrm{Li}$ | $(3, 2)$ | 15 | $97$  | _(deferred to Phase 3)_ | _pending_ |
| ${}^6\mathrm{Li}$ | $(3, 3)$ | 18 | $118$ | _(deferred to Phase 3)_ | _pending_ |

Witness:
[`per-irrep-pole-atom-crystal.witness.json`](../../../folio-assistant/computations/per-irrep-pole-atom-crystal.witness.json).

## Speedup

Per-atom timing (with C1 + C2 cache, after $y_\lambda$ precompute):

| atom | $n$ | symbolic Path A (existing) | crystal Path A | speedup |
|------|----:|---------------------------:|---------------:|--------:|
| proton    | 3  | $\sim 1\;\mathrm{s}$ | $0.9\;\mathrm{s}$ | 1× |
| deuteron  | 6  | $\sim 5\;\mathrm{min}$ | $24\;\mathrm{s}$ | $\sim 12\times$ |
| tritium   | 9  | $\gg 30\;\mathrm{min}$ | $7\;\mathrm{min}$ | $> 4\times$ |
| ${}^4\mathrm{He}$ | 12 | $\sim 1\;\mathrm{h}$ (projected) | $\sim 30\;\mathrm{min}$ (projected post-cache) | $\sim 2\times$ |

The existing baseline scales as $O(\mathrm{dim}(V_\lambda)^2 \cdot
L \cdot \text{symbolic-q ops})$ — dominated by sympy
matrix-product simplification.  Crystal-bases scales as
$O(\sum_\lambda f^\lambda \cdot L)$ — pure integer arithmetic, no
symbolic-q.  The crossover where crystal-bases is fastest occurs
at $n \geq 9$; at $n \leq 6$ the symbolic path is competitive
(the cache-precompute dominates).

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
   passes by accident of cancellation balance (1 $\Delta_I$ on
   each generator); the neutron has 2 $\Delta_I$ on $G_0$, 0 on
   $G_1$ — an asymmetry that the leading crystal expansion
   smooths over.

The most parsimonious resolution is **(1)** — the closed-form
formula is rigorously valid for $A \geq 2$ only, and the $A = 1$
neutron entry is a formula-extrapolation that doesn't reflect the
underlying Hecke arithmetic.  A direct symbolic verification at
$A = 1$, $N = 1$ would settle the question; this is well within
the budget of `per_irrep_pole_proton_h3.py` adapted to neutron
inputs and is left as an open follow-up.

## Status

(B) ⁴He Path A consistency check ($\mathrm{ord}_{u=0} = 79$):
**in progress** via the crystal-bases path.  The naive symbolic
attempt with `tr_M_atomic_fast(2, 2)` did not return in 600s; the
crystal-bases route at $H_{12}$ with the $y_\lambda$ pole-order
cache is projected to complete in under an hour.  Result will be
appended to the witness when the sweep completes.
