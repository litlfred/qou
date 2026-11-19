In Feynman's formulation, the transition amplitude is a continuum integral over all paths:

$$
  \langle\psi_f|\psi_i\rangle
  = 
  \int \mathcal{D}\phi\ e^{iS[\phi]/\hbar}.
$$

Because this formulation does not privilege any eigenbasis, it requires regularisation and renormalisation to handle divergences.

The present framework supplies a natural eigenbasis from the braided monoidal structure. The braid group acts on $V^{\otimes n}$, and this action completely decomposes the space into irreducible summands. By Alexander's theorem, these summands are labelled by knot types, which span the algebraic direct limit $V_{\mathrm{phys}} = \varinjlim V^{\otimes n}$. Each irreducible summand represents a specific particle identity: the unknot is the neutrino, the trefoil is the electron, and the figure-eight knot corresponds to the Higgs field.

This replaces the continuum path integral with a finite algebraic operation: the categorical trace. For a closed cycle $\varrho \colon \mathbf{1} \to A$ representing a particle propagating around a vortex filament, the mass is:

$$
  \mathfrak{m}(\varrho)
  = 
  \bigl\lVert
  \mathrm{tr}\bigl(
    (\textstyle\int_A \otimes \mathrm{id})
    \circ \Delta
    \circ \varrho
  \bigr)
  \bigr\rVert.
$$

Since $A$ is a finite-dimensional Frobenius--Hopf object, this categorical trace is intrinsically finite. No regularisation is required because the sum runs over the finitely many irreducible summands of $V^{\otimes n}$.

The skein relation $q\mathfrak{m}(L_+) - q^{-1}\mathfrak{m}(L_-) = (q^{1/2} - q^{-1/2})\mathfrak{m}(L_0)$ is the characteristic equation of the braiding $c_{V,V}$ evaluated under the categorical trace, *after* the writhe normalisation that makes the invariant framing-independent. The traced characteristic equation alone gives $\mathfrak{m}(L_+) - \mathfrak{m}(L_-) = (q - q^{-1})\,\mathfrak{m}(L_0)$; the weights $q^{\pm 1}$ on the two crossing terms are the framing correction, since $L_+$ and $L_-$ differ in writhe by two. The two relations are not rescalings of one another. Because the $R$-matrix determines the eigenvalues, mass ratios such as $\mathfrak{m}_\mu/\mathfrak{m}_e$ emerge exactly from a finite trace over this complete knot eigenbasis.
