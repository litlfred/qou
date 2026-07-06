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
