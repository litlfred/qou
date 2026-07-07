<!-- FILE_START: quantum-universe-intro.md -->
The rigid monoidal scaffold acquires its universe structure through one running example: the compact group $\mathrm{SU}(2)$, whose coordinate algebra $\mathcal{O}(\mathrm{SU}(2))$ carries an integration and a left-invariant calculus. Abstracting from it, a quantum universe is a triple $(\mathbf{C}, A, \tau)$ — an $R$-linear rigid braided monoidal category $\mathbf{C}$, a distinguished Frobenius--Hopf object $A$, and a fibre functor $\tau \colon \mathbf{C} \to R\text{-}\mathrm{Mod}$ — subject to four axioms. The triple is not empty: $\mathcal{O}(\mathrm{SU}(2))$ already furnishes one, and the conventions for the symbol $\tau$ are fixed here and used throughout.

The bulk of the section unpacks the Frobenius half of the data, whose organizing intuition is geometric. On $A$ the calculus $\Omega^1(A)$ is differentiation, the Frobenius form $\int_A$ is integration, and non-degeneracy of the resulting pairing is faithfulness of the measure. Concretely, the Frobenius pairing is the composite $\int_A \circ \mu \colon A \otimes A \to \mathbf{1}$ of the multiplication $\mu$ with the form $\int_A$, and non-degeneracy is the existence of a coevaluation satisfying the snake identities. The QU axioms force this composite to exist and — when $A$ is simple — pin it down uniquely up to a scalar in $\mathrm{Aut}_{\mathbf{C}}(\mathbf{1})$. On $A = \mathcal{O}(\mathrm{SU}(2))$ with the standard $\mathrm{SU}(2)$ integration the pairing is nothing exotic: it recovers the $L^2$ inner product and Peter--Weyl orthogonality.

The remaining blocks pin down the fundamental object and the higher-form complex. Verifying the four axioms on $\mathcal{O}(\mathrm{SU}(2))$ one at a time exhibits the left-invariant calculus $\Omega^1(A) = \mathrm{span}\{\omega_1, \omega_2, \omega_3\}$; the de Rham complex $\Omega^k(A) = \bigwedge_A^k \Omega^1(A)$ then follows, with differential satisfying $d^2 = 0$, and its Maurer--Cartan structure is computed on the running example. Finally, the rank-$2$ generator $V$ is isolated and its role under the fibre functor and Tannaka--Krein reconstruction characterised; the simplicity of the unit object $\mathbf{1}$, recorded here, is what forces the uniqueness of the volume form in the next section, *Consequences of the QU axioms*.
<!-- FILE_END: quantum-universe-intro.md -->

<!-- FILE_START: quantum-universe.md -->
A quantum universe is the categorical substrate from which the
framework's physical observables are later read off: its fibre functor
$\tau$ and Frobenius object $A$ are what subsequently carry the
observable and mass data. The archetypal instance is the category
$\mathbf{Rep}(\mathrm{SU}_q(2))$ of representations of the quantum
group; its classical symmetric ($q \to 1$) limit $\mathrm{SU}(2)$ is the
concrete picture worked in [Example](#ex:quantum-universe-su2). Keep
that example in mind behind the abstract triple.

Let $R$ be a commutative ring. A **quantum universe over $R$** is a
triple $(\mathbf{C}, A, \tau)$ where:

1. $(\mathbf{C}, \otimes, \mathbf{1})$ is an $R$-linear rigid
   :refterm[braided monoidal category]{#braided-monoidal-category}
   ([rigid :refterm[monoidal category]{#monoidal-category}](#def:rigid-monoidal-category)) with
   braiding $c_{X,Y} \colon X \otimes Y \xrightarrow{\sim} Y \otimes X$ — the braiding is required for
   exterior powers $\Lambda^k V$ and need not be symmetric
   ($c^2 \neq \mathrm{id}$ in general);

2. $A$ is a *Frobenius--Hopf object* in $\mathbf{C}$: an
   object equipped with morphisms

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

   — multiplication $\mu$, unit $\eta$, comultiplication $\Delta$,
   counit $\varepsilon$, antipode $S$, and Frobenius
   form $\int_A$ — satisfying:

   **(H)** $(A, \mu, \eta, \Delta, \varepsilon, S)$ is
   a Hopf algebra object in $\mathbf{C}$;

   **(F)** the [Frobenius pairing](#def:frobenius-pairing)
   $\int_A \circ \mu \colon A \otimes A \to \mathbf{1}$ is
   non-degenerate, inducing an isomorphism
   $A \xrightarrow{ \sim } A^{\vee}$;

3. $\tau \colon \mathbf{C} \to R\text{-}\mathrm{Mod}$ is a
   *fibre functor*: an exact, faithful, $R$-linear monoidal
   functor;

4. $A$ admits a *differential calculus*: the module of
   Kähler differentials $\Omega^1(A)$ exists in $\mathbf{C}$.
<!-- FILE_END: quantum-universe.md -->

<!-- FILE_START: quantum-universe-exists.md -->
The four [quantum universe](#def:quantum-universe) axioms are jointly
satisfiable, so the notion is non-vacuous: there exists a triple
$(\mathbf{C}, A, \tau)$ satisfying them — rigid braided
:refterm[monoidal category]{#monoidal-category}, Frobenius--Hopf object, fibre functor, and
differential calculus.
<!-- FILE_END: quantum-universe-exists.md -->

<!-- FILE_START: tau-notation.md -->
We denote the forgetful (fibre) functor by $\tau$ rather than the
more common $\omega$ to avoid conflict with differential-form
notation ($\omega_i$ for left-invariant $1$-forms, $\omega_V$ for the
vertical curvature form) that appears throughout the paper. The
choice of $\tau$ carries several resonances:

- **Tannakian reconstruction.** The letter $\tau$ recalls the
  Tannaka--Krein theorem that reconstructs the gauge group
  $G = \mathrm{Aut}^{\otimes}(\tau)$ from the functor alone.

- **Trace / integration.** In von Neumann algebra theory, a faithful
  normal state is traditionally denoted $\tau$ (the trace). Since the
  forgetful functor underlies the Frobenius integration $\int_A$
  ([integral notation](#sec:frobenius-integration)), this
  identification is more than notational.

- **Proper time.** In the archimedean realisation, $\tau$ can be read
  as the observer's proper time: the functor parameterises the
  "emergence" of $R$-modules from the abstract category, turning
  the static quantum universe into a temporal observable one.
<!-- FILE_END: tau-notation.md -->

<!-- FILE_START: frobenius-pairing.md -->
The structure that makes $A$ self-dual and equips it with a
categorical trace is a pairing $A \otimes A \to \mathbf{1}$ built from
its multiplication and Frobenius form; we record it here before using
it. The motivating instance is the quantum-dimension pairing of
$\mathbf{Rep}(\mathrm{SU}_q(2))$ (see
[example](#ex:frobenius-pairing-su2)); the general definition abstracts
it as follows. Let $(\mathbf{C}, A, \tau)$ be a
[quantum universe](#def:quantum-universe) with multiplication
$\mu \colon A \otimes A \to A$ and Frobenius form
$\int_A \colon A \to \mathbf{1}$. The **Frobenius pairing** is the
composite

```tex
\begin{equation}\label{eq:frobenius-pairing}
\begin{tikzcd}[column sep=2.5em]
  A \otimes A \ar[r, "\mu"]
  & A \ar[r, "\int_A"]
  & \mathbf{1}
\end{tikzcd}
\end{equation}
```

We say the Frobenius pairing is *non-degenerate* when this composite
induces an isomorphism $A \xrightarrow{ \sim } A^{\vee}$ to the
dual object. Equivalently, the standard snake identities hold: there exists a
coevaluation $\tilde{\eta} \colon \mathbf{1} \to A \otimes A$ such
that the two composites (where $\alpha$ is the associator and
$\rho$, $\lambda_A$ are the right and left unitors of $\mathbf{C}$)

$$
A \xrightarrow{\rho^{-1}} A \otimes \mathbf{1}
  \xrightarrow{\mathrm{id} \otimes \tilde{\eta}} A \otimes A \otimes A
  \xrightarrow{\alpha^{-1}} (A \otimes A) \otimes A
  \xrightarrow{(\int_A \circ \mu) \otimes \mathrm{id}} \mathbf{1} \otimes A
  \xrightarrow{\lambda_A} A
$$

and its mirror are both equal to $\mathrm{id}_A$. For
$\mathbf{C} = \mathbf{Rep}(\mathrm{SU}_q(2))$ this recovers the
quantum-dimension pairing (see [example](#ex:frobenius-pairing-su2)).
<!-- FILE_END: frobenius-pairing.md -->

<!-- FILE_START: frobenius-pairing-exists.md -->
The Frobenius form promotes the multiplication into a non-degenerate
pairing, yielding the self-duality $A \cong A^\vee$ used throughout.
Concretely, it sends a pair $(a, b)$ to the scalar
$\int_A(\mu(a, b))$ — the Frobenius form evaluated on their product.
Let $(\mathbf{C}, A, \tau)$ be a
[quantum universe](#def:quantum-universe) with multiplication
$\mu \colon A \otimes A \to A$ and Frobenius form
$\int_A \colon A \to \mathbf{1}$.  Then the non-degenerate
[Frobenius pairing](#def:frobenius-pairing)
$\langle \cdot, \cdot \rangle = \int_A \circ \mu
  \colon A \otimes A \to \mathbf{1}$
exists as a morphism in $\mathbf{C}$, and its adjoint
$A \to A^\vee$ is an isomorphism.

Uniqueness (up to scalar) is
([uniqueness of Frobenius pairing](#prop:frobenius-pairing-unique)).
<!-- FILE_END: frobenius-pairing-exists.md -->

