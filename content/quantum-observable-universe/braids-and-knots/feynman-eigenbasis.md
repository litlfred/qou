In Feynman's formulation, the transition amplitude between two states is computed by summing over all paths in configuration space:

$$
  \langle\psi_f|\psi_i\rangle
  = 
  \int \mathcal{D}\phi\ e^{iS[\phi]/\hbar}.
$$

This expression is basis-independent. It does not privilege any decomposition of the Hilbert space. However, it requires a continuum integral over an infinite-dimensional space that demands regularisation and renormalisation to produce finite answers. The divergences arise because no eigenbasis has been chosen: the sum runs over all field configurations without algebraic organisation.

The QOU framework resolves this by supplying a natural eigenbasis from the braided monoidal structure. By [braid action on tensor products](#prop:braid-action-tensor), the braid group $B_n$ acts on $V^{\otimes n}$. By [knot eigenbasis completeness](#prop:knot-eigenbasis-complete), this action completely decomposes $V^{\otimes n}$ into irreducible summands. These summands are labelled by Young diagrams, or equivalently by knot types via Alexander's braid-closure theorem. Alexander surjectivity ensures that every irreducible summand is reached by some knot type. The spanning statement ([knot eigenbasis completeness](#prop:knot-eigenbasis-complete)(3)) guarantees that these summands span the algebraic direct limit $V_{\mathrm{phys}} = \varinjlim V^{\otimes n}$. No metric completion is used. Each irreducible summand corresponds to a particle identity ([skein decomposition](#rem:skein-decomposition)). For example, the unknot corresponds to the neutrino, the trefoil to the electron, and the figure-eight knot to the Higgs field (mass mechanism).

The path integral is then replaced by a finite algebraic operation: the categorical trace ([mass identity](#def:mass-identity)) evaluated on the braid-group representation. Concretely, for a closed cycle $\varrho \colon \mathbf{1} \to A$ representing a particle propagating around a vortex filament, the mass is

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

where $\int_A$ is the Frobenius form and $\Delta$ the comultiplication. This expression is finite. $A$ is a finite-dimensional Frobenius–Hopf object, $\Delta$ and $\int_A$ are morphisms in the category, and the trace is the categorical trace of a rigid monoidal category. No regularisation is required because the sum is over the finitely many irreducible summands of $V^{\otimes n}$, rather than over a continuum of paths (cf. \cite{stolz-teichner-2012}).

The connection to the skein-based mass calculation of [Chapter 6](#chap:brings-surface) follows directly. The skein relation $q\mathcal{M}(L_+) - q^{-1}\mathcal{M}(L_-) = (q^{1/2} - q^{-1/2})\mathcal{M}(L_0)$ ([skein mass relation](#rem:skein-mass-relation)) is the characteristic equation of the braiding $c_{V,V}$ evaluated under the categorical trace. The three resolutions $L_+$, $L_-$, $L_0$ of a crossing correspond to the eigenvalues $q$ and $-q^{-1}$ of $c_{V,V}$ and the trace of the identity strand. The eigenvalues are determined by the $R$-matrix ([$R$-matrix braiding](#rem:r-matrix-braiding)). Therefore, the mass ratios—including $\mathfrak{m}_\mu/\mathfrak{m}_e \approx :val[m_mu_over_e]{precision=6}$—are computed by a finite trace on a finite-dimensional representation. The knot types serve as a complete eigenbasis ([knot eigenbasis completeness](#prop:knot-eigenbasis-complete)) that Feynman's formulation lacked.
