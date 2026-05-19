**Conjecture (Denominator zeros = SW critical points).**
*Let $\Phi_n(x; q_0)$ be the $q$-Pochhammer partial product
([q-Pochhammer partial product](#def:q-pochhammer-partial-product))
attached to a Hecke normal form word at GB-depth $n$, and let
$\Delta(z) = 0$ be the discriminant locus of the color-tube cubic
([color-tube cubic](#rem:color-tube-cubic)). Then the algebraic
denominator zeros of $\Phi_n$ map under the archimedean realisation
$\tau_{\mathrm{arch}}$ to the discriminant locus of the color-tube
cubic:*

$$
  \tau_{\mathrm{arch}}\!\bigl(
    \{x \in R : (x; q_0)_n = 0\}
  \bigr)
  \;=\;
  \{z_c \in \mathbb{C} : \Delta(z_c) = 0\}.
$$

| Side | Object | "Critical" event |
|---|---|---|
| Algebraic ($R$) | denominator $(x; q_0)_n$ | zero at $x = q_0^{-k}$ |
| Archimedean ($\mathbb{C}$) | discriminant $\Delta(z)$ of color-tube cubic | zero at $z = z_c$ |
| Geometric ($\mathbf{Hyp}_3$) | ideal-tetrahedron cusp | shape parameter at completeness locus |

*Each algebraic root $x = q_0^{-k}$ of $(x; q_0)_n$ is a discrete
address; under $\tau_{\mathrm{arch}}$ it lifts to a complex root
$z_c$ of $\Delta(z) = 0$, where $\partial F/\partial\mathbf{c} = 0$
forces a repeated root of the color-tube cubic and produces a pole
in $\lambda_{\mathrm{SW}}^{(1)}$.*

## Consequences

*Combined with
([sw-period thimble equivalence](#prop:sw-period-thimble-equivalence))
and its A2.4 algebraic-residue formula, the categorical Markov trace
is the sum of algebraic residues at the principal Galois orbit
$\mathcal{O}_{\mathrm{prin}} = \{z_c^\pm\}$, with the algebraic
denominator zeros prescribing the orbit's selection.*

*The conjecture also supplies the Newton–Raphson seeds for the
Thurston gluing equations: lift each denominator zero $q_0^{-k}$ to
its matched $z_c$ via $\tau_{\mathrm{arch}}$, then use $z_c$ as the
initial guess
([shared-denominator cusp holonomy](#conj:shared-denominator-cusp-holonomy)).*

*Consistent with the SW abelianisation results
([MI–SW abelianisation](#prop:mi-sw-abelianisation),
[MI–SW abelianisation Cartan](#lem:mi-sw-abelianisation-cartan)):
the conjecture specifies **where** the abelianisation occurs (at the
$\tau$-image of the algebraic denominator zeros), without altering
the abelianisation mechanism itself.*

## Status

*Stated conditional on
([algebraic-geometric dilog equivalence](#conj:algebraic-geometric-dilog-equivalence))
and
([shared-denominator cusp holonomy](#conj:shared-denominator-cusp-holonomy)).
The Lean formulation
`QOU.PicardLefschetz.denominator_zeros_eq_sw_critical_points` is a
class instance, parametrised by an `AlgebraicGeometricEquivalence`
instance.*
