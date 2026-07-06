The fermion--boson decomposition ([fermions are knots, bosons are links](#prop:fermion-boson-knot-link)) extends the generator set ([knot-particle generation](#def:knot-particle-generation)) to the even-$n$ torus links, which represent bosons. These include $T(2,2)$ (gluon), $T(2,4)$ ($W$ boson), $T(2,6)$ ($Z$ boson), and $T(2,8)$ (Higgs boson). These are two-component links with $\gcd(2,n) = 2$, carrying integer spin.

All torus knots have zero hyperbolic volume. They are satellite/torus knots, not hyperbolic. Consequently, their bare mass under the topological mass formula ([topological mass formula](#prop:topological-mass-formula)) vanishes:

$$
  \mathcal{M}_{\mathrm{bare}}(T_{m,n}) = 
  \frac{\mathrm{Vol}(T_{m,n})}{\hbar_q^{2}} =  0.
$$

Mass arises entirely through the linking operations: Hopf linking on the exceptional divisor, color-tube threading, and Skein crossing changes.

**Presentation of the particle Skein module.**
The Skein module ([Skein generation](#prop:skein-generation)) admits the presentation

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
  \bigr),
$$

where $\mathcal{G}$ is the torus knot generator set and the quotient applies the HOMFLY-PT Skein relation at every crossing. Every particle in the knot--particle dictionary ([knot--particle dictionary](#rem:knot-particle-dictionary)) is a word in this presentation.
