The [jet prolongation](#prop:jet-prolongation) of $A = \mathcal{O}(\mathrm{SU}(2))$ is constructed explicitly as follows.

**Kähler differentials.** The module of Kähler differentials is $\Omega^1(A) = \ker(m \colon A \otimes A \to A)$. For the left-invariant calculus on $\mathrm{SU}(2)$, this yields:
$$
  \Omega^1(A) = \mathrm{span}_A\{\omega_1, \omega_2, \omega_3\},
$$
where $\omega_a$ are the left-invariant $1$-forms dual to the Lie algebra basis $\{e_1, e_2, e_3\}$ of $\mathfrak{su}(2)$.

**The jet object.** By definition:
$$
  J^1(A) := A \otimes \Omega^1(A) \cong \mathcal{O}(\mathrm{SU}(2)) \otimes \mathrm{span}\{\omega_1, \omega_2, \omega_3\}.
$$
As a vector space, $J^1(A)$ consists of $\mathcal{O}(\mathrm{SU}(2))$-valued $1$-forms on $\mathrm{SU}(2)$. These exactly match the sections of the frame bundle $F(\mathrm{SU}(2))$.

**Inherited Frobenius–Hopf structure.** The comultiplication on $J^1(A)$ reads:
$$
  \Delta'(f \otimes \varTheta)(x, y) = f(xy) \otimes \varTheta_y,
$$
where $\varTheta_y$ denotes the left-translate of $\varTheta$ to $T_y G$. The counit $\varepsilon'(f \otimes \varTheta) = f(e)\varTheta_e$ and antipode $S'(f \otimes \varTheta)(x) = f(x^{-1}) \otimes (L_{x^{-1}})^*\varTheta$ extend similarly. The Frobenius form identically integrates the $1$-form component over $G$ via the Haar measure: $\int_{J^1 A}(f \otimes \varTheta) = \int_G f\varTheta$.

**QOU structure.** The induced fibre functor $\tau' = \tau \circ (\text{--} \otimes \Omega^1)$ retains the $1$-form structure while forgetting the $G$-action on sections. Because $\mathrm{SU}(2)$ is $3$-dimensional, $J^1(A)$ acts as a $3$-fold extension of $A$, forcing $\dim_{\tau'} J^1(A) = 3 \cdot \dim_\tau A$. The quadruple $(\mathrm{Rep}(\mathrm{SU}(2)), J^1(A), \tau', q)$ formally constitutes a quantum observable universe.
