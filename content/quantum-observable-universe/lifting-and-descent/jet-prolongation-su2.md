We construct the [jet prolongation](#prop:jet-prolongation) of
$A = \mathcal{O}(\mathrm{SU}(2))$.

**Kahler differentials.** The module of Kahler differentials is
$\Omega^1(A) = \ker(m \colon A \otimes A \to A)$, which for the
left-invariant calculus on $\mathrm{SU}(2)$ gives

$$
  \Omega^1(A) =  \mathrm{span}_A\{\omega_1, \omega_2, \omega_3\},
$$

where $\omega_a$ are the left-invariant $1$-forms dual to the Lie
algebra basis $\{e_1, e_2, e_3\}$ of $\mathfrak{su}(2)$.

**The jet object.** By [jet prolongation](#prop:jet-prolongation),

$$
  J^1(A)  :=  A \otimes \Omega^1(A)
   \cong  \mathcal{O}(\mathrm{SU}(2)) \otimes
  \mathrm{span}\{\omega_1, \omega_2, \omega_3\}.
$$

As a vector space, $J^1(A)$ consists of $\mathcal{O}(\mathrm{SU}(2))$-valued
$1$-forms on $\mathrm{SU}(2)$, which are precisely the sections of the
frame bundle $F(\mathrm{SU}(2))$.

**Inherited Frobenius--Hopf structure.** The comultiplication on $J^1(A)$
is defined by

$$
  \Delta'(f \otimes \varTheta)(x, y)
  =  f(xy) \otimes \varTheta_y,
$$

where $\varTheta_y$ denotes the left-translate of $\varTheta$ to $T_y G$.
The counit and antipode extend similarly:
$\varepsilon'(f \otimes \varTheta) = f(e)\varTheta_e$ and
$S'(f \otimes \varTheta)(x) = f(x^{-1}) \otimes (L_{x^{-1}})^*\varTheta$.
The Frobenius form is
$\int_{J^1 A}(f \otimes \varTheta) = \int_G f\varTheta$, integrating the
$1$-form component over $G$ using the Haar measure.

**QOU structure.** The induced fibre functor is
$\tau' = \tau \circ (\text{--} \otimes \Omega^1)$, forgetting
the $G$-action on sections while retaining the $1$-form structure.
Since $\mathrm{SU}(2)$ is $3$-dimensional,
$J^1(A)$ is a $3$-fold extension of $A$, so
$\dim_{\tau'} J^1(A) = 3 \cdot \dim_\tau A$.
The quadruple $(\mathrm{Rep}(\mathrm{SU}(2)), J^1(A), \tau', q)$
is again a quantum observable universe.
