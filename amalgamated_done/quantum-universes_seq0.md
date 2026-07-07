<!-- FILE_START: qu-intro.md -->
We establish the **quantum universe (QU)** as the root categorical substrate of the framework.

A quantum universe is a rigid monoidal category $\mathbf{C}$ acting on a distinguished Frobenius–Hopf object. This encapsulates the algebraic structure of the physical state space prior to geometry. We isolate the five necessary axioms in **Definition: Quantum universe**: monoidal rigidity, a Frobenius–Hopf object, a compatible braiding, spherical trace, and a categorical mass identity. These axioms are sufficient to construct the brane tower.

We state the abstract axioms and anchor them in the primary example (**Example: SU(2) as a QU**). We define the structural operators: **temporal braiding**, **fibre adjoint involution**, and **projective line object**. These serve as the base of the brane tower. We identify the **substrate parameter** $q$ and the **quantum gauge group** $G_q$. We define the **adelic substrate** to provide the global arithmetic context for place-by-place analysis.

The output is the abstract QU $\mathbf{C}$. The next section introduces the *observability* condition. This promotes a QU to a quantum observable universe (QOU).
<!-- FILE_END: qu-intro.md -->

<!-- FILE_START: quantum-universe.md -->
**Definition.**
A **quantum universe** is a tuple $(\mathbf{C}, A, \tau)$ consisting of:
1. an $R$-linear rigid [monoidal category](#monoidal-category) $\mathbf{C}$,
2. a distinguished object $A \in \mathrm{Ob}(\mathbf{C})$ equipped with a [Frobenius–Hopf algebra](#frobenius-hopf-algebra) structure,
3. an $R$-linear faithful fibre functor $\tau \colon \mathbf{C} \to \mathbf{Vect}_R$,

satisfying the following five axioms:
1. **(Rigidity)** Every object $V \in \mathbf{C}$ possesses left and right duals.
2. **(Frobenius--Hopf)** $A$ carries compatible associative multiplication $\mu$, co-multiplication $\Delta$, unit $\eta$, co-unit $\varepsilon$, and antipode $S$. The space $A$ acts on every $V \in \mathbf{C}$ via a categorical representation $\rho_V \colon A \otimes V \to V$.
3. **(Temporal braiding)** $\mathbf{C}$ admits a braiding isomorphism $c_{V,W} \colon V \otimes W \xrightarrow{\sim} W \otimes V$. The induced ordering $\prec_c$ on the Hecke basis of $A$ is well-founded.
4. **(Spherical)** The left and right categorical traces coincide for every endomorphism.
5. **(Mass identity)** The Frobenius codimensional trace identity ([Frobenius co-Casimir universal](#thm:frobenius-codim-universal)) holds in $A$:
$$
  \tau_M(C_{\dim_q}) \;=\; \sum_\lambda \frac{1}{\dim_q(\lambda)}.
$$
<!-- FILE_END: quantum-universe.md -->

<!-- FILE_START: qu-su2.md -->
We establish the primary motivating example of a [quantum universe](#def:quantum-universe).

**Example (SU(2) as a QU).**
Let $R = \mathbb{C}$.
1. **Category:** Let $\mathbf{C} = \mathrm{Rep}(\mathrm{SU}(2))$ be the category of finite-dimensional representations of $\mathrm{SU}(2)$. It is a $\mathbb{C}$-linear rigid symmetric monoidal category.
2. **Object:** Let $A = \mathcal{O}(\mathrm{SU}(2))$ be the algebra of representative functions on $\mathrm{SU}(2)$. It is a Frobenius–Hopf algebra under point-wise multiplication, co-multiplication $\Delta(f)(g,h) = f(gh)$, and the Haar integral as the Frobenius trace. The space $A$ acts on representations via the regular action.
3. **Functor:** Let $\tau \colon \mathrm{Rep}(\mathrm{SU}(2)) \to \mathbf{Vect}_{\mathbb{C}}$ be the standard forgetful fibre functor.

This triple satisfies the axioms:
1. **Rigidity:** Finite-dimensional $\mathrm{SU}(2)$ representations have duals.
2. **Frobenius--Hopf:** Peter–Weyl theory provides the compatible structures on $\mathcal{O}(\mathrm{SU}(2))$.
3. **Temporal braiding:** The symmetric braiding $v \otimes w \mapsto w \otimes v$ induces the trivial well-founded ordering.
4. **Spherical:** $\mathrm{Rep}(\mathrm{SU}(2))$ is spherical because $\mathrm{SU}(2)$ is compact.
5. **Mass identity:** The Frobenius trace evaluates to the Peter–Weyl sum over irreducible dimensions.

The quantum group deformation $\mathrm{Rep}(\mathrm{SU}_q(2))$ provides the non-symmetric braiding essential for the $q$-difference structure.
<!-- FILE_END: qu-su2.md -->

<!-- FILE_START: temporal-braiding.md -->
Let $(\mathbf{C}, A, \tau)$ be a [quantum universe](#def:quantum-universe). The temporal braiding is the specific generator of the braid group action on tensor powers $V^{\otimes n}$ of an object $V \in \mathbf{C}$.

**Proposition.**
*The braiding isomorphism $c_{V,V} \colon V \otimes V \to V \otimes V$ induces a representation of the braid group $B_n$ on $V^{\otimes n}$ via the temporal braiding operators:*
$$
  \sigma_i \;=\; \mathrm{id}_{V^{\otimes (i-1)}} \otimes c_{V,V} \otimes \mathrm{id}_{V^{\otimes (n-i-1)}}.
$$
*These satisfy the Yang–Baxter relation:*
$$
  \sigma_i \sigma_{i+1} \sigma_i \;=\; \sigma_{i+1} \sigma_i \sigma_{i+1}.
$$
*The action of $\sigma_i$ rigorously factorises through the Iwahori–Hecke algebra $H_n(q)$ for a distinguished parameter $q \in R^{\times}$.*

We will formalize the [substrate parameter](#def:substrate-parameter) $q$ arising from this factorisation.
<!-- FILE_END: temporal-braiding.md -->

<!-- FILE_START: fiber-adjoint-involution.md -->
**Proposition.**
*Let $(\mathbf{C}, A, \tau)$ be a [quantum universe](#def:quantum-universe). Let $\mathrm{Ad}(A)$ denote the adjoint representation of $A$ on itself, given by $a \mapsto \sum a_{(1)} x S(a_{(2)})$. There exists a distinguished involution:*
$$
  \sigma \;\colon\; \mathbf{1} \;\hookrightarrow\; \mathrm{End}_{\mathbf{C}}(A)
$$
*that maps the monoidal unit to the identity endomorphism. Under the fibre functor $\tau$, this evaluates to the identity matrix $\mathrm{id}_{\tau(A)}$.*

This involution embeds the trivial representation into the endomorphism algebra. The observability condition will demand the trivial representation vanishes in the *adjoint* action: $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$.
<!-- FILE_END: fiber-adjoint-involution.md -->

<!-- FILE_START: projective-line-object.md -->
**Definition.**
Let $(\mathbf{C}, A, \tau)$ be a [quantum universe](#def:quantum-universe). A **projective line object** is an object $L \in \mathbf{C}$ such that:
1. $L$ has categorical dimension $\dim_{\mathbf{C}}(L) = 2$.
2. The symmetric algebra $\mathrm{Sym}(L)$ admits a unique non-degenerate spherical trace.

In the [SU(2) example](#ex:qu-su2), $L = V_1 \cong \mathbb{C}^2$ is the standard representation. The projective space $\mathbb{P}(\tau(L))$ is the Riemann sphere $\mathbb{CP}^1$. This object defines the base site $\mathcal{S}$ for the gerbe theory of the brane tower.
<!-- FILE_END: projective-line-object.md -->

<!-- FILE_START: substrate-parameter.md -->
**Definition.**
Let $(\mathbf{C}, A, \tau)$ be a [quantum universe](#def:quantum-universe). The **substrate parameter** $q \in R^{\times}$ is the scalar controlling the quadratic relation of the temporal braiding operators $\sigma_i$ ([temporal braiding](#prop:temporal-braiding)) on the projective line object $L$:
$$
  (\sigma_i - q)(\sigma_i + q^{-1}) \;=\; 0
  \quad\text{in}\quad
  \mathrm{End}_{\mathbf{C}}(L^{\otimes n}).
$$

This relation forces the braid group action to factor through the Iwahori–Hecke algebra $H_n(q)$. The substrate parameter is the fundamental deformation parameter of the universe. When $q=1$, the braiding is symmetric. The physical mass evaluations fix $q_0 \approx 0.999812$.
<!-- FILE_END: substrate-parameter.md -->

<!-- FILE_START: quantum-gauge-group.md -->
**Definition.**
Let $(\mathbf{C}, A, \tau)$ be a [quantum universe](#def:quantum-universe). The **quantum gauge group** $G_q$ is the Tannakian reconstruction group of the category:
$$
  G_q \;:=\; \mathrm{Aut}^{\otimes}(\tau).
$$
The elements of $G_q$ are the natural monoidal automorphisms of the fibre functor.

By Tannakian reconstruction, $\mathbf{C} \cong \mathrm{Rep}(G_q)$. The Frobenius–Hopf object $A$ is isomorphic to the coordinate algebra $\mathcal{O}(G_q)$. The substrate parameter $q$ determines the explicit deformation structure of $G_q$.
<!-- FILE_END: quantum-gauge-group.md -->

<!-- FILE_START: adelic-substrate.md -->
The quantum universe parameters live in a ring $R$. For global arithmetic evaluations, we set $R = \mathbb{Q}$ and study the completions.

**Definition.**
The **adelic substrate** is the ring of adeles:
$$
  \mathbb{A} \;=\; \mathbb{R} \times \prod_{p}^{\prime} \mathbb{Q}_p.
$$
The evaluations of the quantum universe invariants (e.g., categorical mass) take values in $\mathbb{A}$. The restricted product ensures evaluations are $p$-adic integers $\mathbb{Z}_p$ for almost all primes $p$.

The adelic formulation unifies the archimedean (geometric) and non-archimedean (arithmetic) characteristics of the QOU. The global constraints (e.g., rational mass values) enforce compatibility conditions across the entire adelic product.
<!-- FILE_END: adelic-substrate.md -->
