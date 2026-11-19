For the Descartes universe with $\chi(A) = -6$, the bound on the [torus knot generators](#def:knot-particle-generation) is $N(-6) = 9$, admitting the generators listed in [the table](#tbl:knot-particle-generation-table-data).

The fermion--boson decomposition extends the generator set to the even-$n$ torus links, which represent bosons. These include the $T(2,2)$ gluon, the $T(2,4)$ $W$ boson, the $T(2,6)$ $Z$ boson, and the $T(2,8)$ Higgs boson. These are two-component links with $\gcd(2,n) = 2$, carrying integer spin.

All torus knots have zero hyperbolic volume. Thurston's trichotomy sorts every knot into torus, satellite, or hyperbolic; torus knots are their own class, and only the hyperbolic class carries a volume. Consequently, their bare mass under the topological mass formula vanishes:

$$
  \mathfrak{m}_{\mathrm{bare}}(T_{m,n}) = 
  \frac{\mathrm{Vol}(T_{m,n})}{\hbar_q^{2}} =  0.
$$

Mass arises entirely through the linking operations: Hopf linking on the exceptional divisor, color-tube threading, and Skein crossing changes.

**Presentation of the particle Skein module.**
The Skein module admits the presentation

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

where $\mathcal{G}$ is the torus knot generator set. The quotient applies the HOMFLY-PT Skein relation at every crossing. Every particle in the knot--particle dictionary is a word in this presentation.
