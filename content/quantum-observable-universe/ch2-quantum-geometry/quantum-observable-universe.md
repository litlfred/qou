A quantum universe $(\mathbf{C}, A, \tau)$ over $R$
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
   $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1},\,
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
   adjoint object vanish.  Precisely, define the *Chern classes of a
   categorical object* $X$ by pulling back through the fibre functor:

   $$c_i(X) \;:=\; c_i\!\bigl(\tau(X)\bigr)
     \;\in\; H^{2i}_{\mathrm{dR}}\!\bigl(\mathrm{Spec}\,R\bigr),$$

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

   The first condition ensures the adjoint bundle is
   orientable, precluding global anomalies; the second ensures
   the volume form acquires no topological phases (see
   [Remark](#rem:yekutieli-stokes-remark) for the connection to
   categorical flatness via Yekutieli's nonabelian Stokes theorem).
   For many applications, axioms (1), (2), and (4) suffice — axiom
   (3) is needed only when global topology of $M$ matters.

4. *(categorical volume constraint)*
   let $V$ denote the fundamental object of $\mathbf{C}$
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

5. *(temporal braiding)* the braiding
   $c_{V,V} \colon V \otimes V \to V \otimes V$ on
   $\mathbf{C}$ is **non-symmetric**: $c_{V,V}^2 \neq
   \mathrm{id}_{V \otimes V}$.  The braiding determines
   a canonical admissible ordering $\prec_c$ on the
   monomial basis $B$ of the Hecke algebra $H_n(q)$ of $A$
   ([admissible system](#def:admissible-system)) as follows:

   **(well-ordering on $B$.)** The monomial basis consists of
   positive braid monomials
   $\sigma_{i_1}\sigma_{i_2}\cdots\sigma_{i_k}$ in the image
   of $c_{V,V}$ under the braid representation
   $\rho_n(\sigma_i) = \mathrm{id}^{\otimes(i-1)} \otimes
   c_{V,V} \otimes \mathrm{id}^{\otimes(n-i-1)}$.  The
   braiding $c_{V,V}$ (as opposed to its inverse
   $c_{V,V}^{-1}$) defines "positive crossing" — forward
   time.  The ordering $\prec_c$ is degree-lexicographic:
   shorter words precede longer ones; at equal length,
   lexicographic order on the generator indices.  This is a
   well-ordering because: (a) total degree is bounded below
   by $0$; (b) at fixed degree, lexicographic order on a
   finite alphabet is well-founded.

   Forward time is the direction of Gröbner reduction under
   $\prec_c$: braiding (applying $c_{V,V}$, creating
   crossings $\sigma_i$).  Backward time is the opposite
   braiding $\bar{c}_{V,V} := c_{V,V}^{-1}$: unbraiding
   (resolving crossings $\sigma_i^{-1}$).  The ordering
   is not additional data — it is derived from the braiding,
   which is already part of the categorical structure.
