One explicitly constructs the [jet prolongation](#prop:jet-prolongation) of $A = \mathcal{O}(\mathrm{SU}(2))$.

**Kähler differentials.** Let $I = \ker(m \colon A \otimes A \to A)$. The module of Kähler differentials is $\Omega^1_A = I/I^2$. Since $\mathrm{SU}(2)$ is a smooth group of dimension $3$, it is free with a left-invariant basis:
$$
  \Omega^1_A = \mathrm{span}_A\{\omega_1, \omega_2, \omega_3\},
$$
where $\omega_a$ are the left-invariant $1$-forms dual to the Lie algebra basis $\{e_1, e_2, e_3\}$ of $\mathfrak{su}(2)$.

**The jet object.** By definition:
$$
  J^1(A) := (A \otimes A)/I^2 \cong A \oplus \Omega^1_A = A \oplus \mathrm{span}_A\{\omega_1, \omega_2, \omega_3\},
$$
the splitting being $a \mapsto [a \otimes 1]$ with retraction induced by $m$ ([direct-summand lemma](#lem:jet-prolongation-categorical-jet)). An element of $J^1(A)$ is a function together with a $1$-form, the algebraic first jet of a function on $\mathrm{SU}(2)$. The $1$-form component matches the sections of the frame bundle $F(\mathrm{SU}(2))$.

**Inherited Frobenius–Hopf structure.** The comultiplication on the $1$-form component of $J^1(A)$ reads:
$$
  \Delta'(f \otimes \varTheta)(x, y) = f(xy) \otimes \varTheta_y,
$$
where $\varTheta_y$ denotes the left-translate of $\varTheta$ to $T_y G$. The counit $\varepsilon'(f \otimes \varTheta) = f(e)\varTheta_e$ and antipode $S'(f \otimes \varTheta)(x) = f(x^{-1}) \otimes (L_{x^{-1}})^*\varTheta$ extend similarly. The Frobenius form identically integrates the $1$-form component over $G$ via the Haar measure: $\int_{J^1 A}(f \otimes \varTheta) = \int_G f\varTheta$.

**QOU structure.** The induced fibre functor $\tau'$ retains the $1$-form structure while forgetting the $G$-action on sections. Because $\mathrm{SU}(2)$ is $3$-dimensional, $J^1(A)$ is a free $A$-module of rank $1 + 3 = 4$. The quadruple $(\mathrm{Rep}(\mathrm{SU}(2)), J^1(A), \tau', q)$ formally constitutes a quantum observable universe.
