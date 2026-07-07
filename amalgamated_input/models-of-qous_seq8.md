<!-- FILE_START: finite-fields-intro.md -->
Finite fields provide an independent check on the axioms. They reproduce the knot-theoretic and Frobenius structure of the archimedean models in characteristic $\pp$.

Let $q$ range over $\mathbb{F}_\pp^{\times}$, or a primitive $\ell$-th root of unity in $\overline{\mathbb{F}}_\pp$ with $\ell$ coprime to $\pp$. The categorical data forms a fusion category with finitely many simple objects. The $\mathbb{F}_\pp$ realisation constructs $\mathrm{Rep}_{\mathbb{F}_\pp}(\mathrm{SU}_q(2))$ as a QOU. The regular representation satisfies the Frobenius and observability axioms. This supplies the finite-field counterpart to the Calabi--Yau and Bring's-surface witnesses. 

Comparison with characteristic zero proceeds through reduction from $\mathbb{Q}_\pp$ to $\mathbb{F}_\pp$, finite-group representation theory, and Betti-number matching. The universal $R$-matrix of $U_q(\mathfrak{sl}_2)$ at a root of unity yields the Jones polynomial $J_K(q)$ via the Markov trace. This recovers the knot-theoretic output of the archimedean models. 

This compatibility sets up the rigidity-pairing narrative of the next section, which examines Mostow confinement and the Archimedean wall.
<!-- FILE_END: finite-fields-intro.md -->

<!-- FILE_START: finite-field-realisation.md -->
The finite field setting demonstrates that the Frobenius non-degeneracy and observability conditions do not depend on characteristic zero or archimedean structure.

Fix a prime $\pp$ and set $k = \mathbb{F}_\pp$. Let $\mathbf{C} = \mathrm{Rep}_{\mathbb{F}_\pp}(\mathrm{SU}_q(2))$ be the category of finite-dimensional representations of the quantum group $\mathrm{SU}_q(2)$ over $\mathbb{F}_\pp$. Here $q \in \mathbb{F}_\pp^{\times}$. More generally, let $q \in \overline{\mathbb{F}}_\pp$ be a primitive $\ell$-th root of unity, with $\ell$ coprime to $\pp$. Then $\mathbf{C}$ extends to a fusion category over $\mathbb{F}_\pp(q)$ with finitely many simple objects.

The regular representation provides the Frobenius--Hopf object $A$. The forgetful functor to $\mathrm{Vect}_{\mathbb{F}_\pp}$ provides the fibre functor $\tau$. Semisimplicity of the fusion category guarantees the non-degeneracy of the Frobenius form $\int_A$. The observability condition $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ holds for $q \neq 1$, as the trivial representation does not appear as a summand of the adjoint representation.
<!-- FILE_END: finite-field-realisation.md -->

<!-- FILE_START: jones-polynomials.md -->
Jones polynomials bridge the finite-field models of this section and the categorical machinery of [Chapter](#chap:path-integrals-braiding). We outline the correspondence here.

The fusion category $\mathrm{Rep}_{\mathbb{F}_\pp}(\mathrm{SU}_q(2))$ carries a canonical $R$-matrix. This arises from the universal $R$-matrix of $U_q(\mathfrak{sl}_2)$ specialised at a primitive $\ell$-th root of unity in $\overline{\mathbb{F}}_\pp$. This $R$-matrix promotes the fundamental representation $V$ to a braided object. The braid group $B_n$ acts on $V^{\otimes n}$. The Markov trace then produces a knot invariant. Following standard Reshetikhin–Turaev normalisation, this yields the Jones polynomial $J_K(q) \in \mathbb{Z}[q^{\pm 1/2}]$ modulo $\pp$.

The knot crossing number counts the $R$-matrix applications. Thus $J_K(q)$ is a polynomial of degree bounded by the crossing number. The Hecke algebra structure constants control its coefficients ([Chapter](#chap:path-integrals-braiding)). At a root of unity $q = \zeta_\ell$, divisibility patterns of $J_K(q)$ encode the modular-Hecke combinatorics of [the modular Markov-trace conventions](#tm-notation).

The $\pp$-adic (Witt-vector) lift of the substrate parameter ([Witt-vector lift](#rem:witt-lift-qou)) recovers the Jones polynomial by reducing the lifted $R$-matrix modulo $\pp$. The modular Jones invariant agrees with the characteristic-zero invariant where both are defined. The finite-field and archimedean models thus produce identical knot-theoretic output. We construct the Markov trace and link the Jones polynomial to the mass formula in [the topological mass formula](#prop:topological-mass-formula).
<!-- FILE_END: jones-polynomials.md -->

