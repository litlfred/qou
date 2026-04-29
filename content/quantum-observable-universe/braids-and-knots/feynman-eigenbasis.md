In Feynman's formulation, the transition amplitude between two states is
computed by summing over *all* paths in configuration space:

$$
  \langle\psi_f|\psi_i\rangle
  = 
  \int \mathcal{D}\phi\ e^{iS[\phi]/\hbar}.
$$

This expression is basis-independent --- it does not privilege any
decomposition of the Hilbert space --- but the price is a
continuum integral over an infinite-dimensional space that requires
regularisation and renormalisation to produce finite answers.  The
divergences arise precisely because no eigenbasis has been chosen: the sum
runs over all field configurations without any algebraic organisation.

The QOU framework resolves this by supplying a natural eigenbasis from the
braided monoidal structure.  By
[braid action on tensor products](#prop:braid-action-tensor), the braid group $B_n$ acts on
$V^{\otimes n}$, and by
[knot eigenbasis completeness](#prop:knot-eigenbasis-complete) this action
*completely* decomposes $V^{\otimes n}$ into irreducible summands ---
labelled by Young diagrams, or equivalently by knot types via Alexander's
braid-closure theorem.  Alexander surjectivity ensures that every
irreducible summand is reached by some knot type, and the spanning
statement
([knot eigenbasis completeness](#prop:knot-eigenbasis-complete)(3))
guarantees that these summands span the algebraic direct limit
$V_{\mathrm{phys}} = \varinjlim V^{\otimes n}$ (no metric completion is
used).  Each irreducible summand
corresponds to a particle identity
([skein decomposition](#rem:skein-decomposition)): the unknot to the neutrino, the
trefoil to the electron, the figure-eight knot to the Higgs field (mass mechanism), and so on.

The "path integral" is then replaced by a finite algebraic operation:
the *categorical trace*
([mass identity](#def:mass-identity)) evaluated on the braid-group
representation.  Concretely, for a closed cycle
$\varrho \colon \mathbf{1} \to A$ representing a particle propagating
around a vortex filament, the mass is

$$
  \mathfrak{m}(\varrho)
  = 
  \bigl\lVert
  \mathrm{tr}\bigl(
    (\int_A \otimes \mathrm{id})
    \circ \Delta
    \circ \varrho
  \bigr)
  \bigr\rVert,
$$

where $\int_A$ is the Frobenius form and $\Delta$ the comultiplication.
This is a *finite* expression: $A$ is a finite-dimensional
Frobenius--Hopf object, $\Delta$ and $\int_A$ are morphisms in the
category, and the trace is the categorical trace of a rigid monoidal
category.  No regularisation is required because the sum is over the
finitely many irreducible summands of $V^{\otimes n}$, not over a
continuum of paths.

The connection to the skein-based mass calculation of
[Chapter 6](#chap:descartes-universe) is then as follows.  The skein relation
$q\mathcal{M}(L_+) - q^{-1}\mathcal{M}(L_-) = (q^{1/2} - q^{-1/2})\mathcal{M}(L_0)$
([skein mass relation](#rem:skein-mass-relation)) is the
*characteristic equation* of the braiding $c_{V,V}$ evaluated under
the categorical trace: the three resolutions $L_+$, $L_-$, $L_0$ of a
crossing correspond to the eigenvalues $q$ and $-q^{-1}$ of $c_{V,V}$
and the trace of the identity strand.  Since the eigenvalues are
determined by the $R$-matrix ([$R$-matrix braiding](#rem:r-matrix-braiding)), the
mass ratios --- including $\mathfrak{m}_\mu/\mathfrak{m}_e \approx :val[m_mu_over_e]{precision=6}$ --- are computed by
a finite trace on a finite-dimensional representation, with the knot types
serving as a *complete* eigenbasis
([knot eigenbasis completeness](#prop:knot-eigenbasis-complete)) that Feynman's
formulation lacked.
