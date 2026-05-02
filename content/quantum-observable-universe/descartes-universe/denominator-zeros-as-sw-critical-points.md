**Conjecture (Denominator zeros = SW critical points).**
*Let $\Phi_n(x; q_0)$ be the $q$-Pochhammer partial product
([definition](#def:q-pochhammer-partial-product))
attached to a Hecke normal-form word at GB-depth $n$, and let
$\Delta(z) = 0$ be the discriminant locus of the color-tube cubic*

$$
  F(z, \mathbf{c})
  \;=\;
  \mathbf{c}^3 + (4z + 1)\mathbf{c}^2
    + (6z^2 + 3z + 1)\mathbf{c}
    + (4z^3 + 3z^2 + 2z + 1)
$$

*([color-tube cubic](#rem:color-tube-cubic)).
The Picard–Lefschetz critical points $\{z_c\}$ of the SW action
$S(z) = \int^z \lambda_{\mathrm{SW}}^{(1)}\, dz'$
([Picard–Lefschetz thimble](#def:picard-lefschetz-thimble))
are identically the **algebraic image** of the denominator zeros of
$\Phi_n$ under the Archimedean realization
([archimedean realization functor](#def:archimedean-realization-functor)):*

$$
  \tau_{\mathrm{arch}}\!\bigl(
    \{x \in R : (x; q_0)_n = 0\}
  \bigr)
  \;=\;
  \{z_c \in \mathbb{C} : \Delta(z_c) = 0\}.
$$

## Why this matters

The conjecture says the **algebraic poles of the categorical state
sum and the geometric critical points of the SW action are the same
data**, viewed from opposite sides of the fibre functor $\tau$.
Each algebraic root $x = q_0^{-k}$ of $(x; q_0)_n$ is a discrete
address; under $\tau_{\mathrm{arch}}$ it lifts to a complex root
$z_c$ of $\Delta(z) = 0$, where $\partial F/\partial \mathbf{c} = 0$
forces a repeated root of the color-tube cubic and produces a pole
in $\lambda_{\mathrm{SW}}^{(1)}$.

| Side | Object | "Critical" event |
|---|---|---|
| Algebraic ($R$) | denominator $(x; q_0)_n$ | zero at $x = q_0^{-k}$ |
| Archimedean ($\mathbb{C}$) | discriminant $\Delta(z)$ of color-tube cubic | zero at $z = z_c$ |
| Geometric ($\mathbf{Hyp}_3$) | ideal-tetrahedron cusp | shape parameter $z_k$ at completeness locus |

The first row is the algebraic computation; the second row is the
PL setup ([picard-lefschetz-thimble](#def:picard-lefschetz-thimble));
the third row is the geometric interpretation
([shared-denominator cusp holonomy](#conj:shared-denominator-cusp-holonomy)).
The conjecture asserts the rows are isomorphic under $\tau$.

## Bridge to the existing PL infrastructure

The PL framework on Bring's surface
([sw-period $\equiv$ thimble integral](#prop:sw-period-thimble-equivalence))
already identifies critical points of the SW action with the
discriminant locus of the color-tube cubic (hypothesis A2.1, derived
on the $R$-side). The present conjecture promotes that identification
one step further: the discriminant locus is the **archimedean image**
of the algebraic $q$-Pochhammer denominator zeros. Equivalently, the
GB-depth filtration on the algebraic side and the PL critical-point
filtration on the archimedean side are matched by $\tau$
([jet-GB-PL correspondence](#prop:jet-gb-pl-correspondence)).

Combined with
([sw-period $\equiv$ thimble integral](#prop:sw-period-thimble-equivalence)),
the conjecture allows the categorical Markov trace to be written as a
sum of Seiberg–Witten thimble integrals, with **the algebraic
denominator zeros prescribing the thimble base points**:

$$
  \tau\bigl(\mathfrak{m}^{(k)}_{\text{alg}}(T_w)\bigr)
  \;=\;
  \sum_\sigma n_\sigma^{(k)} \oint_{\mathcal{J}_{z_{c,\sigma}}}
    \lambda_{\mathrm{SW}}^{(k)}\, dz,
  \qquad
  z_{c,\sigma} \in \tau_{\mathrm{arch}}\bigl(
    (x; q_0)_n^{-1}(0)
  \bigr).
$$

This is the QOU-native form of the duality between algebraic state
sums and Picard–Lefschetz contour integrals: the algebraic poles do
not vanish on either side, they are the **same poles** under $\tau$.

## Computational consequence (Newton–Raphson seeding)

The conjecture supplies the algebraic seeds for the Newton–Raphson
solver of the Thurston gluing equations: lift each denominator zero
$q_0^{-k}$ to its matched $z_c$ via $\tau_{\mathrm{arch}}$, then use
$z_c$ as the initial guess. The full seeding pipeline and witness
are recorded under
([shared-denominator cusp holonomy §implication](#conj:shared-denominator-cusp-holonomy)).

## Relation to existing abelianisation

The conjecture is consistent with the SW abelianisation results
([MI–SW abelianisation](#prop:mi-sw-abelianisation),
[MI–SW abelianisation Cartan](#lem:mi-sw-abelianisation-cartan)):
at each algebraic pole, the nonabelian multiplicative integral
trivialises by $\pi_1(\mathrm{SU}(2)) = 0$ over the exceptional
divisor $\mathcal{S}_c \cong \mathbb{P}^1(\mathbb{C})$, and the
gauge connection reduces to its Cartan component. The present
conjecture does not alter that picture; it specifies **where** the
abelianisation occurs (at the $\tau$-image of the algebraic
denominator zeros) and ties those locations to the algebraic side.

## Status

Stated conditional on
([algebraic-geometric dilog equivalence](#conj:algebraic-geometric-dilog-equivalence))
and
([shared-denominator cusp holonomy](#conj:shared-denominator-cusp-holonomy)).
The Lean formulation
`QOU.PicardLefschetz.denominator_zeros_eq_sw_critical_points` is a
class instance, parametrised by an `AlgebraicGeometricEquivalence`
instance.
