One explicitly constructs the [jet prolongation](#prop:jet-prolongation) of $A = \mathcal{O}(\mathrm{SU}(2))$.

**Kähler differentials.** Let $I = \ker(m \colon A \otimes A \to A)$. The module of Kähler differentials is $\Omega^1_A = I/I^2$. Since $\mathrm{SU}(2)$ is a smooth group of dimension $3$, it is free with a left-invariant basis:
$$
  \Omega^1_A = \mathrm{span}_A\{\omega_1, \omega_2, \omega_3\},
$$
where $\omega_a$ are the left-invariant $1$-forms dual to the Lie algebra basis $\{e_1, e_2, e_3\}$ of $\mathfrak{su}(2)$.

**The tangent algebra.** By definition:
$$
  T(A) := \mathrm{Sym}_A(\Omega^1_A) = A[\omega_1, \omega_2, \omega_3],
$$
the polynomial algebra over $A$ in the three left-invariant forms. It is the coordinate algebra $\mathcal{O}(T\,\mathrm{SU}(2))$ of the tangent group $T\,\mathrm{SU}(2) \cong \mathrm{SU}(2) \ltimes \mathfrak{su}(2)$. The structure map $A \to T(A)$ and the augmentation $T(A) \to A$, $\omega_a \mapsto 0$, satisfy $r \circ \ell = \mathrm{id}_A$. The part of degree at most $1$ in the $\omega_a$ is the jet object $J^1(A) = A \oplus \Omega^1_A$ of [the categorical jet](#def:categorical-jet), a free $A$-module of rank $1 + 3 = 4$.

**Inherited Hopf structure.** In the left trivialisation $T\,\mathrm{SU}(2) \cong \mathrm{SU}(2) \times \mathfrak{su}(2)$ the group law is $(x, X)(y, Y) = (xy, \mathrm{Ad}_{y^{-1}} X + Y)$. The comultiplication of $T(A)$ is the pullback of this law: $\Delta'$ restricts to $\Delta$ on $A$, and on the coordinate functions $\omega_a$ it reads
$$
  \Delta'(\omega_a) = \sum_b (\mathrm{Ad}_{y^{-1}})_{ab}\, \omega_b \otimes 1 + 1 \otimes \omega_a .
$$
The counit is evaluation at $(e, 0)$ and the antipode is pullback along $(x, X) \mapsto (x^{-1}, -\mathrm{Ad}_x X)$. Because $\omega_a$ is not primitive in this coproduct, the obstruction recorded for $J^1(A)$ does not apply to $T(A)$.

**QOU structure.** The induced fibre functor $\tau'$ retains the $1$-form coordinates while forgetting the $G$-action on sections. $T(A)$ is a commutative Hopf algebra, and no Frobenius form on it is required. The group $T\,\mathrm{SU}(2)$ contains the vector group $\mathfrak{su}(2)$, so $T(A)$ carries no nonzero integral in characteristic zero.
