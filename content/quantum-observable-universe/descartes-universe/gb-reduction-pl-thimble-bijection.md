**Conjecture (GB reduction ↔ PL thimble flow).**
*Under the archimedean realisation functor $\tau$, each inductive
Gröbner–Shirshov normal-form reduction step on $H_n(R, q)$
corresponds to one step of the gradient-flow ODE
$\dot z = -\overline{\nabla S(z)}$ on a Picard–Lefschetz thimble
$\mathcal{J}_{z_c}$ of the color-tube cubic, at constant imaginary
phase $\mathrm{Im}\,S$.*

| Algebraic step ($R$) | Archimedean shadow ($\mathbb{C}$) | Invariant |
|---|---|---|
| GB reduction (Hecke / Skein) | steepest-descent ODE | constant $\mathrm{Im}\,S$ |
| filtration depth $k_\star \to k_\star - 1$ | thimble parameter $t \to t + dt$ | matched |
| residue extraction at NF terms | residue at thimble base $z_c$ | matched |

## Why this matters

The bijection refines
([jet–GB–PL correspondence](#prop:jet-gb-pl-correspondence)) by giving
the **dynamics**, not just the **filtration data**: the inductive
reduction operator is the steepest-descent ODE under $\tau$. Two
consequences:

1. **Memoised substructures ↔ rigid descent endpoints.** Borromean
   nucleon caches sit at endpoints of completed thimble flows; by
   Mostow rigidity those endpoints have fixed shape parameters. The
   cached transfer matrices are the $\tau$-image of rigid thimble
   endpoints.
2. **Topological invariance ↔ constant phase.** Each GB reduction
   preserves Markov / Skein equivalence; steepest-descent flow
   preserves $\mathrm{Im}\,S$. The two invariants are identified.

## Proof sketch

*Assume
([jet–GB–PL correspondence](#prop:jet-gb-pl-correspondence)),
([sw-period thimble equivalence](#prop:sw-period-thimble-equivalence)),
([denominator zeros = SW critical points](#conj:denominator-zeros-as-sw-critical-points)).
The jet correspondence gives the static bijection on objects (depth
$\equiv$ thimble level). Each GB step strictly decreases the leading
deg-lex monomial; under the denominator-zeros conjecture the
extracted residue is the $\tau$-image of a thimble base point.
Constant-phase property of GB normal forms follows from the
$R$-side surface-integral representation
([rem:yekutieli-stokes](#rem:yekutieli-stokes)). Combining yields the
step-wise bijection. $\square$*

## Status

*Stated conditional on the three upstream blocks. After the
algebraic-residue swap of A2.4, this conjecture is **archimedean
exposition** — it gives a vivid picture of the algebraic reduction
but is no longer required for any rigorous derivation.*
