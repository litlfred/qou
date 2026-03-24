A quantum universe $(\mathcal{C}, A, \tau)$ over $R$
([quantum universe](#def:quantum-universe)) is *observable* if the
forgetful functor $\tau$
([Example](#ex:rigid-monoidal-vect)) is faithful and the following
conditions hold:

1. *(non-degenerate integration)* the Frobenius form
   $\int_A \colon A \to \mathbf{1}$ induces a
   non-degenerate pairing
   $(a, b) \mapsto \int_A ab$
   ([Frobenius pairing](#def:frobenius-pairing)), giving an
   isomorphism $A \xrightarrow{\;\sim\;} A^{\vee}$;

2. *(observability)* there are no hidden global symmetries:
   $\mathrm{Hom}_{\mathcal{C}}(\mathbf{1},\,
   \mathrm{Ad}(A)) = 0$, where $\mathrm{Ad}(A)$ is the adjoint object
   ($A$ acted on by conjugation). Physically, this means every
   internal degree of freedom is accessible to measurement — no
   gauge transformation acts trivially on all observables. The
   formal statement is that every morphism
   $\mathbf{1} \to \mathrm{Ad}(A)$ is zero:

   ```tex
   \[
   \begin{tikzcd}[column sep=2.5em]
     \mathbf{1} \ar[r, "0"] & \mathrm{Ad}(A)
   \end{tikzcd}
   \qquad\text{(observability)}
   \]
   ```

3. *(measurability / anomaly-free)* the primary Chern classes of the
   adjoint object vanish in the cohomology induced by the forgetful
   projection $\tau$:

   $$
     c_1(\mathrm{Ad}(A)) = 0
     \qquad\text{and}\qquad
     c_2(\mathrm{Ad}(A)) = 0.
   $$

   Here the Chern classes $c_i$ are defined via the fibre functor:
   $c_i(\mathrm{Ad}(A)) := c_i(\tau(\mathrm{Ad}(A)))$ in the
   de Rham cohomology of the realised bundle.
   The first condition ($c_1 = 0$) ensures the adjoint bundle is
   orientable, precluding global anomalies; the second ($c_2 = 0$)
   ensures the volume form acquires no topological phases.
   For many applications, axioms (1), (2), and (4) suffice — axiom
   (3) is needed only when global topology of $M$ matters.

4. *(categorical volume constraint)*
   let $V$ denote the fundamental object of $\mathcal{C}$
   ([Remark](#rem:fundamental-object-explication)); there exists a
   non-degenerate epimorphism $\epsilon$ preserved by the rigid
   dualities, making the following diagram commute for every
   $g \in \mathrm{Aut}^{\otimes}(\tau)$:

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
   \qquad\text{(volume constraint)}
   \end{equation}
   ```
