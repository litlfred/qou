Continuing [rigid monoidal Vect](#ex:rigid-monoidal-vect), we verify the [quantum universe](#def:quantum-universe) axioms for $G = \mathrm{SU}(2)$.

**(i) Category.** $\mathbf{C} = \mathrm{Rep}(\mathrm{SU}(2))$ is the category of finite-dimensional complex representations. This is a $\mathbb{C}$-linear rigid :refterm[monoidal category]{#monoidal-category}. The $G$-action on tensor products is diagonal; on duals it is the contragredient.

**(ii) Frobenius--Hopf object.** $A = \mathcal{O}(\mathrm{SU}(2))$ is the coordinate ring. Its Hopf structure encodes the group operations (see [Table 1](#tbl:quantum-universe-su2-table1-data)). The [Frobenius pairing](#def:frobenius-pairing) is positive definite.

**(iii) Fibre functor.** $\tau \colon \mathrm{Rep}(\mathrm{SU}(2)) \to \mathrm{Vect}_{\mathbb{C}}$ is the forgetful functor. It is exact, faithful, and monoidal. By Tannaka--Krein duality, $G \cong \mathrm{Aut}^{\otimes}(\tau)$.

**(iv) Differential calculus.** The left-invariant calculus on $\mathrm{SU}(2)$ provides $\Omega^1(A) = \mathrm{span}\{\omega_1, \omega_2, \omega_3\}$. The universal derivation $d \colon A \to \Omega^1(A)$ acts by $df = \sum_i (\partial_i f) \omega_i$.
