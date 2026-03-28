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

   **(well-ordering on $B$: definition and proof.)**
   The monomial basis $B$ of $H_n(q)$ consists of reduced
   positive braid monomials
   $w = \sigma_{i_1}\sigma_{i_2}\cdots\sigma_{i_k}$ —
   the images of the braiding $c_{V,V}$ under
   $\rho_n(\sigma_i) = \mathrm{id}^{\otimes(i-1)} \otimes
   c_{V,V} \otimes \mathrm{id}^{\otimes(n-i-1)}$
   ([braid action on tensor powers](#prop:braid-action-tensor)).
   The braiding $c_{V,V}$ (as opposed to its inverse
   $c_{V,V}^{-1}$) defines "positive crossing" — forward
   time.

   *Definition.* A **well-ordering** on a set $S$ is a total
   order $\prec$ such that every non-empty subset of $S$ has
   a least element.  Equivalently: there are no infinite
   strictly descending chains
   $s_1 \succ s_2 \succ s_3 \succ \cdots$.

   *Definition.* The **degree-lexicographic ordering**
   $\prec_c$ on $B$ is:
   $w \prec_c w'$ if and only if

   $$
     \ell(w) < \ell(w'),
     \quad\text{or}\quad
     \ell(w) = \ell(w') \;\text{and}\;
     (i_1, \ldots, i_k) <_{\mathrm{lex}} (i_1', \ldots, i_k')
   $$

   where $\ell(w) = k$ is the word length (number of
   crossings) and $<_{\mathrm{lex}}$ is lexicographic order
   on the generator indices
   $i_j \in \{1, \ldots, n-1\}$.

   *Proof that $\prec_c$ is a well-ordering on $B$.*
   Let $S \subseteq B$ be non-empty.

   (a) **Degree is bounded below.**  Every $w \in B$ has
   $\ell(w) \geq 0$.  Let $d = \min\{\ell(w) : w \in S\}$.
   The set $S_d = \{w \in S : \ell(w) = d\}$ is non-empty.

   (b) **Finite alphabet at each degree.**  Each $w \in S_d$
   is a word of length $d$ over the finite alphabet
   $\{1, \ldots, n-1\}$.  There are at most $(n-1)^d$ such
   words — a finite set.  Every finite totally ordered set
   has a minimum.  Let $w_0$ be the lex-minimum of $S_d$.

   (c) **$w_0$ is the minimum of $S$.**  For any $w \in S$:
   if $\ell(w) > d$ then $w_0 \prec_c w$ (shorter words
   first); if $\ell(w) = d$ then $w_0 \leq_{\mathrm{lex}} w$
   by construction.  $\square$

   *Admissibility.*  The ordering $\prec_c$ is
   **admissible** in the sense of
   ([admissible system](#def:admissible-system)):
   left and right multiplication by basis elements preserves
   the ordering ($w \prec_c w'$ implies
   $u \cdot w \cdot v \prec_c u \cdot w' \cdot v$ whenever
   both products are non-zero), because degree-lex is
   compatible with any associative multiplication whose
   defining relations (Hecke, Yang–Baxter) have leading terms
   of bounded degree — the Hecke relation is quadratic.

   **Two faces of the arrow of time.**  The braiding
   $c_{V,V}$ and the Reeb vector field $\xi$
   ([categorical Reeb](#def:categorical-reeb)) express the
   same arrow of time from two complementary viewpoints:

   - **Categorical arrow** ($c_{V,V}$): which strand crosses
     *over*.  A positive crossing $\sigma_i$ applies
     $c_{V,V}$; a negative crossing $\sigma_i^{-1}$ applies
     $\bar{c}_{V,V} := c_{V,V}^{-1}$.  The ordering
     $\prec_c$ is the algebraic encoding: forward time =
     Gröbner reduction under $\prec_c$.

   - **Geometric arrow** ($\xi$): which direction the Reeb
     flow runs.  The one-parameter subgroup $\phi_t^q$
     generated by $\xi$ is the flow of forward time on the
     state bundle $\mathcal{S}$.  At each Planck step, one
     application of $c_{V,V}$ advances $\phi_t^q$ by one
     tick.

   **Crossing reversal = time reversal.**  The crossing
   reversal involution $\sigma \colon K \mapsto \bar{K}$
   (mirror all crossings) corresponds to switching the
   braiding: $c_{V,V} \leftrightarrow \bar{c}_{V,V}$.
   This flips the ordering $\prec_c$ and reverses the Reeb
   flow $\xi \mapsto -\xi$.  In the Feynman–Stueckelberg
   interpretation, an antiparticle ($\bar{K}$) is its
   particle ($K$) with time reversed — precisely the
   opposite braiding.  CPT symmetry is the statement that
   the QOU axioms are invariant under simultaneous
   $c_{V,V} \leftrightarrow \bar{c}_{V,V}$ (T),
   $K \mapsto \bar{K}$ (C), and $\sigma_i \mapsto
   \sigma_{n-i}$ (P, strand reflection).

   The ordering is not additional data — it is derived from
   the braiding, which is already part of the categorical
   structure.
