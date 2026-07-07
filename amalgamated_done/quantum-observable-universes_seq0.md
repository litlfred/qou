<!-- FILE_START: qou-definition-intro.md -->
This chapter refines the quantum universe of Chapter 1 into a *quantum observable universe* by imposing four conditions: non-degenerate integration, observability, measurability, and a categorical volume constraint. We first establish the existence of this refined structure axiom by axiom. We then prove that the non-symmetric braiding provides a canonical well-ordering on the Hecke basis, identifying the categorical arrow of time. The section closes by demonstrating that the QOU on $\mathrm{SU}(2)$ exactly satisfies these constraints over an arbitrary commutative ring.
<!-- FILE_END: qou-definition-intro.md -->

<!-- FILE_START: quantum-observable-universe.md -->
A quantum universe $(\mathbf{C}, A, \tau)$ over $R$ is a **quantum observable universe** if the forgetful functor $\tau$ is faithful and four conditions hold:

1. *(Non-degenerate integration)* The Frobenius form $\int_A \colon A \to \mathbf{1}$ induces an isomorphism $A \xrightarrow{\sim} A^{\vee}$ via the pairing $(a, b) \mapsto \int_A ab$.
2. *(Observability)* There are no hidden global symmetries: $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$.
3. *(Measurability)* The categorical Chern classes of the adjoint object vanish: $c_1(\mathrm{Ad}(A)) = 0$ and $c_2(\mathrm{Ad}(A)) = 0$.
4. *(Categorical volume constraint)* There exists a non-degenerate epimorphism $\epsilon \colon \Lambda^2 V \to \mathbf{1}$ on the fundamental object $V$ preserved by all tensor automorphisms:

```tex
\begin{equation}\label{eq:categorical-volume-constraint}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \Lambda^2 V \ar[r, "\Lambda^2 g_V"]
              \ar[d, "\epsilon"', two heads]
  & \Lambda^2 V \ar[d, "\epsilon", two heads]
  \\
  \mathbf{1} \ar[r, "g_{\mathbf{1}} = \mathrm{id}"']
  & \mathbf{1}
\end{tikzcd}
\end{equation}
```
<!-- FILE_END: quantum-observable-universe.md -->

<!-- FILE_START: qou-axioms-physical-reading.md -->
These axioms carry direct physical meanings. The non-degenerate integration acts as a categorical Haar measure, ensuring the volume is a well-defined topological constant. Observability dictates that every internal degree of freedom is accessible to measurement, eliminating gauge transformations that act as the identity on all observables. Measurability acts as an anomaly-freedom condition. The vanishing of $c_1$ ensures the adjoint bundle is orientable, removing the primary topological obstruction to flatness. The vanishing of $c_2$ prevents the volume form from acquiring topological phases under non-contractible transport. Together, these conditions satisfy the nonabelian Stokes theorem, guaranteeing the integral is well-defined and anomaly-free.
<!-- FILE_END: qou-axioms-physical-reading.md -->

<!-- FILE_START: quantum-observable-universe-exists.md -->
Given a principal $\mathrm{SU}(2)$-bundle over a compact oriented manifold satisfying the measurability condition $c_1 = c_2 = 0$, there exists a quantum observable universe. Setting $\mathbf{C} = \mathbf{Rep}(U_q(\mathfrak{sl}_2))$, $A = \mathcal{O}_q(\mathrm{SU}(2))$, and $\tau$ to the forgetful functor realizes the axioms explicitly.
<!-- FILE_END: quantum-observable-universe-exists.md -->

<!-- FILE_START: qou-exists-axiom-1.md -->
The Haar state on $\mathcal{O}_q(\mathrm{SU}(2))$ provides the faithful integration.
<!-- FILE_END: qou-exists-axiom-1.md -->

<!-- FILE_START: qou-exists-axiom-2.md -->
The adjoint representation is the irreducible spin-1 representation, guaranteeing $\mathrm{Hom}(\mathbf{1}, V_1) = 0$.
<!-- FILE_END: qou-exists-axiom-2.md -->

<!-- FILE_START: qou-exists-axiom-3.md -->
The topological Chern-class constraints enforce measurability.
<!-- FILE_END: qou-exists-axiom-3.md -->

<!-- FILE_START: qou-exists-axiom-4.md -->
The standard determinant on $V \cong \mathbb{C}^2$ satisfies the volume constraint.
<!-- FILE_END: qou-exists-axiom-4.md -->

<!-- FILE_START: braiding-induced-ordering.md -->
If the braiding $c_{V,V}$ is non-symmetric ($c_{V,V}^2 \neq \mathrm{id}$), it supplies a canonical admissible well-ordering $\prec_c$ on the monomial basis of the Iwahori--Hecke algebra $H_n(q)$. The braiding $c_{V,V}$ strictly defines the positive crossing, thereby identifying the categorical arrow of time. The degree-lexicographic order on reduced positive braid monomials contains no infinite strictly descending chains.
<!-- FILE_END: braiding-induced-ordering.md -->

<!-- FILE_START: frobenius-integration.md -->
The Frobenius non-degeneracy directly provides the isomorphism $A \xrightarrow{ \sim } A^{\vee}$, formalizing the categorical Haar measure.
<!-- FILE_END: frobenius-integration.md -->

<!-- FILE_START: yekutieli-stokes-remark.md -->
The Yekutieli nonabelian Stokes theorem confirms that the $c_1 = c_2 = 0$ condition is necessary and sufficient to define the integral globally.
<!-- FILE_END: yekutieli-stokes-remark.md -->

<!-- FILE_START: fibre-functor-rigidity.md -->
The fibre functor $\tau$ plays a rigid, passive role precisely because of the observability axiom. The condition $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ is equivalent to the vanishing of the zeroth adjoint cohomology $H^0_G(\mathrm{Ad}(A)) = 0$. This kills all infinitesimal automorphisms of $\tau$. Tannaka--Krein reconstruction pins the functor uniquely up to natural isomorphism, stripping it of non-trivial first-order deformations.
<!-- FILE_END: fibre-functor-rigidity.md -->

<!-- FILE_START: qou-su2.md -->
The realization over $\mathrm{SU}(2)$ natively implements the QOU conditions.
<!-- FILE_END: qou-su2.md -->

<!-- FILE_START: base-field-independence.md -->
Because these axioms are formulated categorically, the existence result holds over any commutative ring $R$, independent of archimedean, $p$-adic, or finite-field realisations.
<!-- FILE_END: base-field-independence.md -->
