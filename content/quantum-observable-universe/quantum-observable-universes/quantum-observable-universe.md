A quantum universe $(\mathbf{C}, A, \tau)$ over $R$
([quantum universe](#def:quantum-universe)) is a
**quantum observable universe** — is *observable* — if the
forgetful functor $\tau$
([Example](#ex:rigid-monoidal-vect)) is faithful and the following
conditions hold:

1. *(non-degenerate integration)* the Frobenius form
 $\int_A \colon A \to \mathbf{1}$ induces a
 non-degenerate pairing
 $(a, b) \mapsto \int_A ab$
 ([Frobenius pairing](#def:frobenius-pairing)), giving an
 isomorphism $A \xrightarrow{ \sim } A^{\vee}$;

2. *(observability)* there are no hidden global symmetries:
 $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$, where $\mathrm{Ad}(A)$ is the adjoint object
 ($A$ acted on by conjugation). The
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
 adjoint object vanish. Precisely, define the *Chern classes of a
 categorical object* $X$ by pulling back through the fibre functor:

 $$
   c_i(X)  :=  c_i\!\bigl(\tau(X)\bigr)
      \in  H^{2i}_{\mathrm{dR}}\!\bigl(\mathrm{Spec}R\bigr),
   $$

 where the right-hand side is the classical Chern class of the
 realised $R$-module (or, in the archimedean setting, of the
 associated vector bundle $\tau(X) \times_G M$). This definition is
 intrinsic to the pair $(\mathbf{C}, \tau)$ — the fibre functor
 $\tau$ is part of the QOU datum — and reduces to the standard
 topological Chern classes in every geometric realisation. The
 measurability axiom requires:

 $$
     c_1(\mathrm{Ad}(A)) = 0
     \qquad\text{and}\qquad
     c_2(\mathrm{Ad}(A)) = 0.
   $$


4. *(categorical volume constraint)*
 let $V$ denote the fundamental object of $\mathbf{C}$
 ([Remark](#sec:fundamental-object-explication)); there exists a
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

The braiding $c_{V,V}$ on $\mathbf{C}$ (which is non-symmetric:
$c_{V,V}^2 \neq \mathrm{id}$, since $\mathbf{C}$ is braided
monoidal but not symmetric monoidal) induces a canonical
admissible well-ordering on the Hecke basis. See
[braiding-induced ordering](#prop:braiding-induced-ordering).
