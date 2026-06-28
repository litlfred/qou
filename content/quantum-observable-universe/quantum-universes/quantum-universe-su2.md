Continuing [rigid monoidal Vect](#ex:rigid-monoidal-vect), we verify each axiom
of [quantum universe](#def:quantum-universe) for $G = \mathrm{SU}(2)$.

**(i) Category.**
$\mathbf{C} = \mathrm{Rep}(\mathrm{SU}(2))$, the category of
finite-dimensional complex representations. Objects are vector spaces
$V$ with a continuous $G$-action $\rho_V \colon G \to \mathrm{GL}(V)$;
morphisms are $G$-equivariant linear maps. This is an
$\mathbb{C}$-linear rigid :refterm[monoidal category]{#monoidal-category}
([rigid monoidal Vect](#ex:rigid-monoidal-vect)). The $G$-action on tensor
products is diagonal: $g \cdot (v \otimes w) = (g \cdot v) \otimes (g \cdot w)$; on duals it is the contragredient:
$(g \cdot f)(v) = f(g^{-1} \cdot v)$.

**(ii) Frobenius--Hopf object.**
$A = \mathcal{O}(\mathrm{SU}(2))$, the coordinate ring of polynomial
functions on the group. Its Hopf structure encodes the group operations:

See [Table 1](#tbl:quantum-universe-su2-table1-data).

The [Frobenius pairing](#def:frobenius-pairing)
$\langle f, g \rangle = \int_A(\mu(f \otimes g)) = \int_G f(x) g(x) d\mu_{\mathrm{Haar}}(x)$
is positive definite (faithfulness of the Haar integral).

**(iii) Fibre functor.**
$\tau \colon \mathrm{Rep}(\mathrm{SU}(2)) \to \mathrm{Vect}_{\mathbb{C}}$ is the forgetful functor: $\tau(V, \rho) = V$ (forget the $G$-action, keep the vector space). It is exact
(short exact sequences of representations split), faithful (a non-zero
equivariant map is non-zero as a linear map), and monoidal
($\tau(V \otimes W) = \tau(V) \otimes \tau(W)$).
By Tannaka--Krein duality, $G$ can be recovered from $\tau$:
$G \cong \mathrm{Aut}^{\otimes}(\tau)$, the group of monoidal natural
automorphisms of the fibre functor.

**(iv) Differential calculus.**
The left-invariant calculus on $\mathrm{SU}(2)$ provides
$\Omega^1(A) = \mathrm{span}\{\omega_1, \omega_2, \omega_3\}$,
the left-invariant $1$-forms dual to the Lie algebra basis
$\{e_1, e_2, e_3\}$ of $\mathfrak{su}(2)$ (with
$[e_a, e_b] = \epsilon_{abc} e_c$;
[SU(2) basis](#def:su2-basis)).
The universal derivation $d \colon A \to \Omega^1(A)$
acts by $df = \sum_i (\partial_i f) \omega_i$, recovering the
Lie derivative along each generator.
