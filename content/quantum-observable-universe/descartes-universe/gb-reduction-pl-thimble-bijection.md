**Conjecture (GB reduction ↔ PL thimble flow).**
*Under the Archimedean realization functor $\tau_{\mathrm{arch}}$, the
discrete degree-lexicographic Gröbner–Shirshov normal-form reduction
maps bijectively to the continuous Picard–Lefschetz steepest-:refterm[descent]{#descent}
flow on the thimbles $\mathcal{J}_{z_c}$ of the color-tube cubic.*

Concretely: every inductive GB reduction step
$N_{\leq k} \mapsto N_{\leq k+1} = \mathrm{NF}\bigl(N_{\leq k} \cdot
C(N_k, N_{k+1}) \cdot N_{k+1}\bigr)$
on the algebraic side corresponds, under $\tau_{\mathrm{arch}}$, to a
strictly monotone :refterm[descent]{#descent} step along the gradient flow
$\dot z = -\overline{\nabla S(z)}$ on the geometric side, at constant
imaginary phase $\mathrm{Im}\,S$.

| Algebraic step ($R$)                       | Archimedean step ($\mathbb{C}$)                                           | Invariant                         |
| ------------------------------------------ | ------------------------------------------------------------------------- | --------------------------------- |
| GB reduction (Hecke / Skein normalisation) | steepest-:refterm[descent]{#descent} flow $\dot z = -\overline{\nabla S}$ | constant $\mathrm{Im}\,S$ (phase) |
| filtration depth $k_\star \to k_\star - 1$ | thimble parameter $t \to t + dt$                                          | matched                           |
| residue extraction at NF terms             | residue at thimble base point $z_c$                                       | matched                           |

## Why this matters

The bijection refines the existing
[jet–GB–PL correspondence](#prop\:jet-gb-pl-correspondence) by giving
the **dynamics**, not just the **filtration data**. Where the jet
correspondence asserts a static identification "level $k$ on the
filtration $\equiv$ level $k$ on the thimble," the present conjecture
asserts that the **inductive reduction operator** (the algebraic
clock) is the **steepest-:refterm[descent]{#descent} ODE** (the geometric clock) under
$\tau_{\mathrm{arch}}$.

This matters for two reasons:

1. **Topological invariance ↔ constant phase.** Each GB reduction step
   preserves Markov / Skein equivalence — a topological invariant.
   On the geometric side, steepest-:refterm[descent]{#descent} flow preserves $\mathrm{Im}\,
   S(z)$ (the imaginary part of the action). The bijection identifies
   the two invariants: topological invariance of GB reductions is the
   constant-imaginary-phase property of the thimble.

2. **Memoisation ↔ rigid :refterm[descent]{#descent} endpoint.** Memoised descended
   substructures (Borromean nucleons) sit at the **endpoints of
   completed thimble flows**. By Mostow rigidity, those endpoints have
   fixed shape parameters. The conjecture says the cached transfer
   matrices on the algebraic side are precisely the
   $\tau_{\mathrm{arch}}$-image of those rigid thimble endpoints.

## Proof sketch (modulo the upstream conjectures)

Assume
([jet–GB–PL correspondence](#prop\:jet-gb-pl-correspondence)),
([SW-period $\equiv$ thimble integral](#prop\:sw-period-thimble-equivalence)),
and
([denominator zeros = SW critical points](#conj\:denominator-zeros-as-sw-critical-points)).

1. **Filtration ↔ thimble level**
   ([jet–GB–PL correspondence](#prop\:jet-gb-pl-correspondence))
   identifies the GB-depth $k_\star(T_w)$ of an algebraic state with
   the thimble level on the geometric side. This gives the static
   bijection on objects.

2. **Reduction step is monotone :refterm[descent]{#descent}** (algebraic side). Each GB
   reduction step strictly decreases the leading monomial in the
   degree-lexicographic order. Under
   ([denominator zeros = SW critical points](#conj\:denominator-zeros-as-sw-critical-points)),
   the extracted residue at each step is a $\tau_{\mathrm{arch}}$-
   image of a denominator zero, i.e. a thimble base point.

3. **Constant phase ↔ topological invariance** (archimedean side).
   The Yekutieli non-abelian Stokes license
   ([Yekutieli–Stokes remark](#rem\:yekutieli-stokes))
   represents the categorical pairing as a surface integral. The
   surface integrand has constant $\mathrm{Im}\,S$ along thimbles
   (the defining property of steepest :refterm[descent]{#descent}). Topological
   invariance of GB normal forms (Hecke / Skein relations) is the
   $\tau$-image of this constant-phase property.

4. **Bijection on dynamics.** Combining 1–3, each inductive GB
   reduction step is the discrete shadow of one step of the
   gradient-flow ODE on a thimble; the chain of GB reductions to
   normal form is the full thimble flow. $\square$

## Status

Stated conditional on the three upstream blocks above. The Lean
formulation `QOU.PicardLefschetz.gb_reduction_pl_thimble_bijection`
is a class instance.
