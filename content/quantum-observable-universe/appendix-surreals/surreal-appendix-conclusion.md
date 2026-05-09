The surreal-number lift of QOU raises more questions than it
answers. A partial list:

1. **Mathlib gap.** There is no mature surreal-analysis library
   in mathlib. Formalising the birthday-grading definition and
   the Hoefsmit-as-$\{L\mid R\}$ proposition rigorously requires
   filling in the surreal-numbers development of mathlib (the
   `SetTheory.Game.Basic` hierarchy) up to a real-closed-field
   witness. This is independent of QOU and would benefit many
   other formalisation projects.

2. **Surreal measure?** The appendix concedes that $\mathbf{No}$
   carries no canonical Lebesgue measure. But Loeb-type
   constructions on hyperfinite subsets of $\mathbf{No}$ yield
   finitely additive measures that pull back to $\mathbb{R}$ under
   standard-part. Whether such a construction recovers the
   Frobenius integral $\int_A$ up to an infinitesimal is open.

3. **Surreal Hilbert-like object.** The scattering pipeline's
   Hilbert space $\mathcal{H}_{\mathrm{phys}}$ has no surreal
   analogue with a canonical inner product. Whether a suitable
   *birthday-bounded completion* gives a weaker surrogate — good
   enough to run the mass formula but lacking spectral theory —
   is worth investigating.

4. **Categorical size.** $\mathbf{No}$ is a proper class.
   Defining $\mathbf{Mod}_{\mathbf{No}}$ or
   $\mathbf{Rep}_{\mathbf{No}}(\mathrm{SU}_q(2))$ requires
   universe-polymorphic foundations (Grothendieck universes,
   or a restriction to a set-sized Hahn-series sub-field).
   The appendix sidesteps this by stating axioms over a
   fixed real-closed field $K$ extending $\mathbb{R}$.

5. **Are the infinitesimal relaxations genuine generalisations?**
   The strict QOU axioms ($\int \circ \eta = \mathrm{id}$,
   $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$) might force
   the $\varepsilon$-relaxed versions to coincide with the strict
   ones in any rigid :refterm[monoidal category]{#monoidal-category}. If so, the
   $\varepsilon$-flexibility is illusory and the main paper loses
   nothing by ignoring it. We conjecture the flexibility is
   *real* when the ground ring is not a field
   ([infinitesimal Frobenius](#conj\:infinitesimal-frobenius)),
   but a proof or counterexample is outstanding.

6. **Kashaev as a surreal statement.** The reformulation
   $\mathrm{st}\bigl(2 \pi \log |J_K(q_\omega, \omega)|/\omega\bigr) = \mathrm{Vol}(S^3 \setminus K)$
   ([Kashaev surreal](#conj\:kashaev-surreal)) is equivalent to the
   classical conjecture modulo the meaning of $q_\omega$. Its
   value, if any, is separating the algebraic (Hecke/Markov)
   content from the transcendental (dilogarithm, hyperbolic
   volume) content.

## What this appendix **does** accomplish

* It provides an explicit ambient for the $q \to 1$ limit and
  renormalisation blow-ups, avoiding informal $\infty$ notation.
* It exhibits a surprising isomorphism between the Hoefsmit
  seminormal form (already central to the paper's mass formula)
  and Conway's $\{L \mid R\}$ construction.
* It gives a disciplined framework for $\varepsilon$-relaxed
  axioms that may be useful even to readers uninterested in
  surreals per se.
* It catalogues which QOU constructions are purely algebraic
  (and therefore field-polymorphic) versus which are genuinely
  analytic.

The appendix is offered as raw material for future work rather
than as a completed extension of the theory.
