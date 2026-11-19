*Proof.*
The proof exhibits the triple $(\mathbf{C}, A, \tau)$ and verifies the four
axioms of
[quantum observable universe](#def:quantum-observable-universe).

### Construction

For $q \in \mathbb{C}^{\times}$ not a non-trivial root of unity, take
$\mathbf{C} := \mathbf{Rep}(U_{q}(\mathfrak{g}))$ — the rigid ribbon
:refterm[braided monoidal category]{#braided-monoidal-category} of finite-dimensional type-I representations
of the Drinfeld--Jimbo quantum group \cite{chari1994guide, kassel1995};
$A := \mathcal{O}_{q}(G)$ — the restricted dual Hopf algebra of matrix
coefficients \cite{woronowicz1988, chari1994guide}, with
$\int_{A} := h$ the unique faithful invariant Haar state
\cite{woronowicz1987}; and $\tau \colon \mathbf{C} \to
\mathrm{Vect}_{\mathbb{C}}$ the (faithful) forgetful functor.

### Verification of axioms

The four axioms hold by
([axiom 1: Frobenius pairing](#lem:qou-exists-axiom-1)),
([axiom 2: observability](#lem:qou-exists-axiom-2)),
([axiom 3: Chern classes](#lem:qou-exists-axiom-3)), and
([axiom 4: volume constraint](#lem:qou-exists-axiom-4)) respectively.

### Conclusion

All four axioms hold for
$(\mathbf{Rep}(U_{q}(\mathfrak{g})), \mathcal{O}_{q}(G), \mathrm{forget})$
under the Chern-class hypothesis, establishing existence.  The triple
specialises to the archimedean realisation
($\mathbb{C}$-QOU) upon choosing a
fibre functor landing in a module category over a contact CR manifold.

**Non-uniqueness.**  Any $(\mathbf{C}', A', \tau')$ with $\mathbf{C}'$
Morita-equivalent to $\mathbf{Rep}(U_{q}(\mathfrak{g}))$ and $A'$
Hopf-equivalent to $\mathcal{O}_{q}(G)$ gives another QOU.  Uniqueness
up to such equivalences is Tannaka--Krein reconstruction
\cite{woronowicz1988}, taken here as background and not re-proved.
$\square$
