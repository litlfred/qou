**Proposition (confinement = spectral-sequence collapse).**
*The collapse of the GB-filtration spectral sequence
([spectral sequence collapse](#prop:spectral-sequence-collapse))
is the categorical statement of color confinement: only central
elements of $A = H_n(R, q)$ survive as physical observables, and
"colored" non-central elements are cohomologically trivial.*

**Statement.**
*Let $A = H_n(R, q)$ be semisimple at generic $q$, with Frobenius
integral $\int_A : A \to R$ (the Markov trace).  Then:*

1. *(Survival.)
   The only $E_\infty$-page contributions are
   $E_\infty^{0, 0} = Z(A) = \bigoplus_\lambda R \cdot e_\lambda$.
   Non-central elements vanish on the $E_\infty$-page.*

2. *(Trace factorization.)
   The Frobenius integral factors through the centre:*

   $$
     \int_A \;=\; \mu \,\circ\, \pi_Z, \qquad
     \pi_Z : A \twoheadrightarrow Z(A), \quad
     \mu : Z(A) \to R,
   $$

   *with $\pi_Z(a) = \sum_\lambda e_\lambda \cdot a \cdot e_\lambda$
   the Wedderburn projection and $\mu(e_\lambda) = w_\lambda$ the
   Plancherel weight.*

3. *(Observables are Wedderburn residues.)
   Every physical observable
   $\mathfrak{W}(\mathcal{K}, \mathcal{T}) = \int_A \rho(\beta_\mathcal{K}) \cdot \mathcal{T}$
   factors as a sum of Wedderburn residues
   ([universal residue](#prop:plancherel-term-7-formulation)):*

   $$
     \mathfrak{W}(\mathcal{K}, \mathcal{T})
     \;=\; \sum_\lambda \int_{A_\lambda}\!\!\rho(\beta_\mathcal{K}) \cdot \mathcal{T}.
   $$
