Let $R$ be a commutative ring. A *quantum universe over $R$* is a
triple $(\mathcal{C}, A, \omega)$ where:

1. $(\mathcal{C}, \otimes, \mathbf{1})$ is an $R$-linear rigid
   monoidal category
   ([rigid monoidal category](#def:rigid-monoidal-category));

2. $A$ is a *Frobenius--Hopf object* in $\mathcal{C}$: an
   object equipped with morphisms

   ```tex
   \[
   \begin{tikzcd}[row sep=1.5em, column sep=2.5em]
     A \otimes A \ar[r, "\mu"]
     & A \ar[r, "\lambda"]
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
   form $\lambda$ — satisfying:

   **(H)** $(A, \mu, \eta, \Delta, \varepsilon, S)$ is
   a Hopf algebra object in $\mathcal{C}$;

   **(F)** the [Frobenius pairing](#def:frobenius-pairing)
   $\lambda \circ \mu \colon A \otimes A \to \mathbf{1}$ is
   non-degenerate, inducing an isomorphism
   $A \xrightarrow{\;\sim\;} A^{\vee}$;

3. $\omega \colon \mathcal{C} \to R\text{-}\mathrm{Mod}$ is a
   *fibre functor*: an exact, faithful, $R$-linear monoidal
   functor;

4. $A$ admits a *differential calculus*: the module of
   K\"ahler differentials $\Omega^1(A)$ exists in $\mathcal{C}$.
