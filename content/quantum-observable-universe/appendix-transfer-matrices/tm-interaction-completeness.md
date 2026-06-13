The introduction states that the embeddability bound on $\Sigma_4$
yields **exactly seven** transfer-matrix interactions: six non-trivial
force operators plus the identity.  This block enumerates them,
referencing the explicit matrices in
[tm-interactions](#tm-interactions) and the per-pair transfer
matrices in [tm-knot-pairs](#tm-knot-pairs).

## Roster

See [Table](#tbl:tm-interaction-completeness-table-data).

Double beta decay ($2\beta$) is **not** a fresh operator: it is the
quadratic composite $\Delta_\beta \cdot C \cdot \Delta_\beta$ at two
positions, with $C$ a product of unchanged transfer matrices between
them ([tm-interactions §5](#tm-interactions)).  Higher $n$-fold
processes decompose similarly.  The Toffoli transfer matrix
([tm-interactions §6](#tm-interactions)) is a *gate construction* on
three strands, not a fresh interaction at a single crossing.

## Why exactly seven

The count follows from three constraints:

1. **Crossing-type alphabet on $\Sigma_4$.**  Each crossing on the
   four-strand braid space carries a quark-flavour pair from
   $\{\mathfrak{u}, \mathfrak{d}\}^2$, giving four crossing types
   ($\mathfrak{uu}, \mathfrak{ud}, \mathfrak{du}, \mathfrak{dd}$).
2. **Reidemeister-I local completeness.**  Single-crossing changes
   that respect the Hecke quadratic $\sigma_i^2 = (q-q^{-1})\sigma_i + 1$
   factor through $\{T_{pp}, T_{pp}^{-1}\}$ for emission/absorption
   plus $\{\Delta_\beta, -\Delta_\beta\}$ for flavour-flip — four
   non-trivial operators.  Pair creation/annihilation reuse
   $\pm\Delta_\beta$ but at a different crossing-pair structure
   (unknot/unknot vs trefoil/mirror-trefoil), giving two further
   distinct operators.
3. **Identity.**  The trivial process is included to make the
   operator algebra closed under composition.

Total: $1 + 4 + 2 = 7$.  The catalogue table above is
exhaustive: any $\Sigma_4$-admissible single-crossing change
reduces to one of these seven, possibly composed with itself or
with $\Delta_\beta$ at multiple positions for $n$-fold processes.
