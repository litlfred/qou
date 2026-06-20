*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

The particle spectrum is generated from a finite set of torus knot
*generators* $T_{m,n}$ (with $\gcd(m,n) = 1$) embedded in the
standard torus $\mathbb{T}^2 \subset S^3$, together with two
*linking operations* that act on the exceptional divisor and the
color-tube fibration.

**Notation.** A torus knot $T_{m,n}$ winds $m$ times around the
meridian and $n$ times around the longitude of $\mathbb{T}^2$.
We reserve $q$ for the substrate parameter
([substrate parameter](#def:substrate-parameter)) and $p$ for base
points, so the winding indices are always $(m,n)$.

**Generator set.** The *torus knot generators* are the family

$$
  \mathcal{G} =  \bigl\{ T_{m,n}  \big| 
  \gcd(m,n) = 1, m < n,
  m + n \leq N(\chi) \bigr\}
$$

where $N(\chi)$ is a cutoff determined by the Euler characteristic
of the Frobenius--Hopf object.  For the Descartes universe with
$\chi(A) = -6$, the bound is $N(-6) = 9$, admitting:

See [Table](#tbl:knot-particle-generation-table-data).

The fermion--boson decomposition
([fermions are knots, bosons are links](#prop:fermion-boson-knot-link))
extends the generator set to the even-$n$ torus *links*, which
represent bosons: $T(2,2)$ (gluon), $T(2,4)$ ($W$ boson),
$T(2,6)$ ($Z$ boson), $T(2,8)$ (Higgs boson).  These are
2-component links with $\gcd(2,n) = 2$, carrying integer spin.

All torus knots have *zero hyperbolic volume*: they are not
hyperbolic but satellite/torus type.  Consequently their bare mass
under the topological mass formula
([topological mass formula](#prop:topological-mass-formula)) vanishes:

$$
  \mathcal{M}_{\mathrm{bare}}(T_{m,n}) = 
  \frac{\mathrm{Vol}(T_{m,n})}{\hbar_q^{2}} =  0.
$$

Mass arises *entirely* through the linking operations: Hopf linking
on the exceptional divisor, color-tube threading, and Skein crossing
change.

**Presentation of the particle Skein module.** The Skein module
([Skein generation](#prop:skein-generation)) admits a presentation

$$
  \mathrm{Sk}_q(\mathbf{C}) = 
  \mathbb{Z}[q^{\pm 1}]\bigl\langle
    \mathcal{G},
    \mathcal{L}_{\mathrm{Hopf}},
    \ell_c
  \bigr\rangle
  \Big/
  \bigl(
    qL_+ - q^{-1}L_- - (q^{1/2} - q^{-1/2})L_0
  \bigr)
$$

where $\mathcal{G}$ is the torus knot generator set and the
relation is the HOMFLY-PT Skein relation applied at every crossing.
Every particle in the knot--particle dictionary
([knot--particle dictionary](#rem:knot-particle-dictionary)) is
a word in this presentation.
