<!-- FILE_START: quantum-universe-intro.md -->
The rigid monoidal scaffold acquires its universe structure through the compact group $\mathrm{SU}(2)$. Its coordinate algebra $\mathcal{O}(\mathrm{SU}(2))$ carries an integration and a left-invariant calculus. Abstracting from this, a quantum universe is a triple $(\mathbf{C}, A, \tau)$: an $R$-linear rigid braided monoidal category $\mathbf{C}$, a Frobenius--Hopf object $A$, and a fibre functor $\tau \colon \mathbf{C} \to R\text{-}\mathrm{Mod}$. The triple is non-empty, as $\mathcal{O}(\mathrm{SU}(2))$ provides an instance.

The Frobenius data is geometric. On $A$, the calculus $\Omega^1(A)$ is differentiation, and the Frobenius form $\int_A$ is integration. Non-degeneracy of the pairing indicates a faithful measure. The Frobenius pairing is the composite $\int_A \circ \mu \colon A \otimes A \to \mathbf{1}$. Non-degeneracy ensures a coevaluation satisfying the snake identities. When $A$ is simple, the axioms pin this composite down uniquely up to a scalar. On $\mathcal{O}(\mathrm{SU}(2))$, the pairing recovers the $L^2$ inner product and Peter--Weyl orthogonality.

The fundamental object and higher-form complex follow. On $\mathcal{O}(\mathrm{SU}(2))$, the left-invariant calculus is $\Omega^1(A) = \mathrm{span}\{\omega_1, \omega_2, \omega_3\}$. The de Rham complex $\Omega^k(A) = \bigwedge_A^k \Omega^1(A)$ follows, with $d^2 = 0$. The rank-$2$ generator $V$ plays a central role under the fibre functor and Tannaka--Krein reconstruction. The simplicity of the unit object $\mathbf{1}$ forces the uniqueness of the volume form.
<!-- FILE_END: quantum-universe-intro.md -->

<!-- FILE_START: quantum-universe.md -->
A quantum universe is the categorical substrate of the physical observables. Its fibre functor $\tau$ and Frobenius object $A$ carry the observable and mass data. The archetypal instance is the category $\mathbf{Rep}(\mathrm{SU}_q(2))$. Its classical limit $\mathrm{SU}(2)$ is the concrete picture worked in [Example](#ex:quantum-universe-su2).

Let $R$ be a commutative ring. A **quantum universe over $R$** is a triple $(\mathbf{C}, A, \tau)$ where:

1. $(\mathbf{C}, \otimes, \mathbf{1})$ is an $R$-linear rigid :refterm[braided monoidal category]{#braided-monoidal-category} ([rigid :refterm[monoidal category]{#monoidal-category}](#def:rigid-monoidal-category)) with braiding $c_{X,Y} \colon X \otimes Y \xrightarrow{\sim} Y \otimes X$.

2. $A$ is a *Frobenius--Hopf object* in $\mathbf{C}$, equipped with morphisms:

   ```tex
   \[
   \begin{tikzcd}[row sep=1.5em, column sep=2.5em]
     A \otimes A \ar[r, "\mu"]
     & A \ar[r, "\int_A"]
     & \mathbf{1}
     & {\scriptstyle\text{(multiplication, Frobenius form)}}
     \\
     \mathbf{1} \ar[r, "\eta"]
     & A \ar[r, "\varepsilon"]
     & \mathbf{1}
     & {\scriptstyle\text{(unit, counit)}}
     \\
     A \ar[r, "\Delta"]
     & A \otimes A
     & A \ar[l, "S"']
     & {\scriptstyle\text{(comultiplication, antipode)}}
   \end{tikzcd}
   \]
   ```

   satisfying:
   **(H)** $(A, \mu, \eta, \Delta, \varepsilon, S)$ is a Hopf algebra object in $\mathbf{C}$;
   **(F)** the [Frobenius pairing](#def:frobenius-pairing) $\int_A \circ \mu \colon A \otimes A \to \mathbf{1}$ is non-degenerate, inducing an isomorphism $A \xrightarrow{ \sim } A^{\vee}$.

3. $\tau \colon \mathbf{C} \to R\text{-}\mathrm{Mod}$ is a *fibre functor*: an exact, faithful, $R$-linear monoidal functor.

4. $A$ admits a *differential calculus*: the module of Kähler differentials $\Omega^1(A)$ exists in $\mathbf{C}$.
<!-- FILE_END: quantum-universe.md -->

<!-- FILE_START: quantum-universe-exists.md -->
The four [quantum universe](#def:quantum-universe) axioms are jointly satisfiable. There exists a triple $(\mathbf{C}, A, \tau)$ satisfying them.
<!-- FILE_END: quantum-universe-exists.md -->

<!-- FILE_START: tau-notation.md -->
We denote the forgetful functor by $\tau$ to avoid conflict with differential-form notation ($\omega_i$, $\omega_V$). The choice of $\tau$ carries physical and mathematical resonances:

- **Tannakian reconstruction.** The letter $\tau$ recalls the Tannaka--Krein theorem reconstructing the gauge group $G = \mathrm{Aut}^{\otimes}(\tau)$.
- **Trace / integration.** In von Neumann algebras, a faithful normal state is denoted $\tau$. The forgetful functor underlies the Frobenius integration $\int_A$ ([integral notation](#sec:frobenius-integration)).
- **Proper time.** In the archimedean realisation, $\tau$ represents the observer's proper time. It parameterises the emergence of $R$-modules from the abstract category.
<!-- FILE_END: tau-notation.md -->

<!-- FILE_START: frobenius-pairing.md -->
The Frobenius pairing makes $A$ self-dual. The motivating instance is the quantum-dimension pairing of $\mathbf{Rep}(\mathrm{SU}_q(2))$ (see [example](#ex:frobenius-pairing-su2)). 

Let $(\mathbf{C}, A, \tau)$ be a [quantum universe](#def:quantum-universe) with multiplication $\mu \colon A \otimes A \to A$ and Frobenius form $\int_A \colon A \to \mathbf{1}$. The **Frobenius pairing** is the composite:

```tex
\begin{equation}\label{eq:frobenius-pairing}
\begin{tikzcd}[column sep=2.5em]
  A \otimes A \ar[r, "\mu"]
  & A \ar[r, "\int_A"]
  & \mathbf{1}
\end{tikzcd}
\end{equation}
```

The Frobenius pairing is *non-degenerate* when it induces an isomorphism $A \xrightarrow{ \sim } A^{\vee}$. Equivalently, the snake identities hold: there exists a coevaluation $\tilde{\eta} \colon \mathbf{1} \to A \otimes A$ such that the composites

$$
A \xrightarrow{\rho^{-1}} A \otimes \mathbf{1}
  \xrightarrow{\mathrm{id} \otimes \tilde{\eta}} A \otimes A \otimes A
  \xrightarrow{\alpha^{-1}} (A \otimes A) \otimes A
  \xrightarrow{(\int_A \circ \mu) \otimes \mathrm{id}} \mathbf{1} \otimes A
  \xrightarrow{\lambda_A} A
$$

and its mirror equal $\mathrm{id}_A$. For $\mathbf{C} = \mathbf{Rep}(\mathrm{SU}_q(2))$, this recovers the quantum-dimension pairing.
<!-- FILE_END: frobenius-pairing.md -->

<!-- FILE_START: frobenius-pairing-exists.md -->
The Frobenius form makes the multiplication a non-degenerate pairing, yielding the self-duality $A \cong A^\vee$. It sends a pair $(a, b)$ to the scalar $\int_A(\mu(a, b))$. 

Let $(\mathbf{C}, A, \tau)$ be a [quantum universe](#def:quantum-universe) with multiplication $\mu$ and Frobenius form $\int_A$. The non-degenerate [Frobenius pairing](#def:frobenius-pairing) $\langle \cdot, \cdot \rangle = \int_A \circ \mu$ exists as a morphism in $\mathbf{C}$. Its adjoint $A \to A^\vee$ is an isomorphism. Uniqueness up to scalar is established in [uniqueness of Frobenius pairing](#prop:frobenius-pairing-unique).
<!-- FILE_END: frobenius-pairing-exists.md -->
