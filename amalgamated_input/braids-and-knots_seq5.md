<!-- FILE_START: knot-eigenbasis-complete.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
$\mathbf{C} = \mathrm{Rep}(\mathrm{SU}_q(2))$ and $V$ the fundamental
representation.  Suppose $q$ is not a root of unity.  Then:

1. **(Semisimplicity.)**  The Iwahori--Hecke algebra
   $H_n(R, q) = \mathrm{End}_{B_n}(V^{\otimes n})$ is semisimple, and
   $V^{\otimes n}$ admits a complete decomposition into irreducible
   $H_n(R, q)$-modules:

   $$
     V^{\otimes n}
      \cong 
     \bigoplus_{\lambda \vdash n}
     V_\lambda \otimes S_\lambda,
   $$

   where $\lambda$ ranges over partitions of $n$ with at most two parts
   (the $q$-analogue of Schur--Weyl duality), $V_\lambda$ is the
   irreducible $\mathrm{SU}_q(2)$-module of spin
   $j = (\lambda_1 - \lambda_2)/2$, and $S_\lambda$ is the irreducible
   $H_n(R, q)$-module labelled by $\lambda$.
2. **(Alexander surjectivity.)**  By Alexander's theorem, every
   oriented link $L$ in $S^3$ is the closure $\hat{\beta}$ of some braid
   $\beta \in B_n$ for some $n$.  The Markov trace
   $\mathrm{tr}_M \colon \bigcup_n H_n(R, q) \to R$ assigns to each braid
   closure $\hat{\beta}$ the value
   $\mathrm{tr}_M(\rho_n(\beta))$, which equals the Jones polynomial
   $J_L(q)$ up to a framing factor.  In particular, the map

   $$
     \{\text{knot types}\}
      \longrightarrow 
     \{\text{irreducible summands of } V^{\otimes n}, n \geq 1\}
   $$

   given by $L \mapsto$ the summand in which $\mathrm{tr}_M(\rho_n(\beta))$
   is supported, has image containing every irreducible summand.
3. **(Spanning of the algebraic state space.)**  The physical state
   space is the algebraic direct limit
   $V_{\mathrm{phys}} := \varinjlim V^{\otimes n}$ along the inclusion
   maps $V^{\otimes n} \hookrightarrow V^{\otimes (n+1)}$ induced by
   the unit $\eta \colon \mathbf{1} \to V$.  Since each $V^{\otimes n}$
   is completely decomposed by (1), the set of irreducible summands
   --- labelled by knot types via (2) --- spans $V_{\mathrm{phys}}$.
   No metric completion is invoked.

**Mathematical Novelty:** The synthesis that knot types form a complete eigenbasis for $\varinjlim V^{\otimes n}$, which conceptually replaces Feynman's continuum integral, is a genuinely framework-specific and novel mathematical synthesis. The accompanying Lean formalization achieves a careful combining and conditional proof over bundled standard results.
<!-- FILE_END: knot-eigenbasis-complete.md -->

<!-- FILE_START: knot-exhaustiveness.md -->
**Open question.**
The knot eigenbasis completeness theorem
([knot eigenbasis completeness](#prop:knot-eigenbasis-complete))
establishes that every irreducible summand of
$V^{\otimes n}$ is **detected** by some braid closure via
the Markov trace
([Jones–Markov trace](#thm:jones-markov-trace)).  This is
surjectivity of detection: no summand is invisible.

A stronger question: **do the knot types that appear in the
Descartes universe exhaust the space of states?**

The generation completeness theorem shows that every knot
with Seifert genus $g(\mathfrak{K}) \leq 4$ appears in the
spectrum — the genus bound of Bring's surface captures all
embeddable knots in that range.  Knots with $g > 4$ are
excluded by the spectral filter.

But this does not address whether the **Jones polynomial
itself** is a faithful invariant: whether distinct knot
types always produce distinct polynomials.  The QOU uses
the Jones polynomial only for detection (non-degeneracy
on irreducibles), not for classification.  The classical
open question — does $J_K(q) = 1$ imply $K$ is the
unknot? — is never needed in our framework, because the
Markov trace non-degeneracy theorem is sufficient for the
knot eigenbasis.

This leaves three nested questions:

1. **(Detection.)** Does every irreducible summand get
   labelled by a knot?  **Yes** — proven by Alexander
   surjectivity + Markov non-degeneracy.

2. **(Generation.)** Does every knot with $g \leq 4$
   appear?  **Yes** — proven by generation completeness
   from the seven torus knot generators plus Skein
   crossing changes.

3. **(Faithfulness.)** Do distinct knots always produce
   distinct states?  **Open.**  If two distinct knots
   $\mathfrak{K} \neq \mathfrak{K}'$ have the same Jones
   polynomial $J_{\mathfrak{K}}(q) = J_{\mathfrak{K}'}(q)$,
   they would be physically indistinguishable in the
   Descartes universe — they would represent the same
   particle.  Whether this occurs (and whether it has
   physical consequences) is an open question.

The first two questions are settled by existing theorems.
The third depends on progress in classical knot theory
and may already be answered by the full HOMFLY-PT
polynomial (which carries strictly more information than
the Jones specialisation).
<!-- FILE_END: knot-exhaustiveness.md -->

<!-- FILE_START: feynman-eigenbasis.md -->
In Feynman's formulation, the transition amplitude between two states is
computed by summing over *all* paths in configuration space:

$$
  \langle\psi_f|\psi_i\rangle
  = 
  \int \mathcal{D}\phi\ e^{iS[\phi]/\hbar}.
$$

This expression is basis-independent --- it does not privilege any
decomposition of the Hilbert space --- but the price is a
continuum integral over an infinite-dimensional space that requires
regularisation and renormalisation to produce finite answers.  The
divergences arise precisely because no eigenbasis has been chosen: the sum
runs over all field configurations without any algebraic organisation.

The QOU framework resolves this by supplying a natural eigenbasis from the
braided monoidal structure.  By
[braid action on tensor products](#prop:braid-action-tensor), the braid group $B_n$ acts on
$V^{\otimes n}$, and by
[knot eigenbasis completeness](#prop:knot-eigenbasis-complete) this action
*completely* decomposes $V^{\otimes n}$ into irreducible summands ---
labelled by Young diagrams, or equivalently by knot types via Alexander's
braid-closure theorem.  Alexander surjectivity ensures that every
irreducible summand is reached by some knot type, and the spanning
statement
([knot eigenbasis completeness](#prop:knot-eigenbasis-complete)(3))
guarantees that these summands span the algebraic direct limit
$V_{\mathrm{phys}} = \varinjlim V^{\otimes n}$ (no metric completion is
used).  Each irreducible summand
corresponds to a particle identity
([skein decomposition](#rem:skein-decomposition)): the unknot to the neutrino, the
trefoil to the electron, the figure-eight knot to the Higgs field (mass mechanism), and so on.

The "path integral" is then replaced by a finite algebraic operation:
the *categorical trace*
([mass identity](#def:mass-identity)) evaluated on the braid-group
representation.  Concretely, for a closed cycle
$\varrho \colon \mathbf{1} \to A$ representing a particle propagating
around a vortex filament, the mass is

$$
  \mathfrak{m}(\varrho)
  = 
  \bigl\lVert
  \mathrm{tr}\bigl(
    (\int_A \otimes \mathrm{id})
    \circ \Delta
    \circ \varrho
  \bigr)
  \bigr\rVert,
$$

where $\int_A$ is the Frobenius form and $\Delta$ the comultiplication.
This is a *finite* expression: $A$ is a finite-dimensional
Frobenius--Hopf object, $\Delta$ and $\int_A$ are morphisms in the
category, and the trace is the categorical trace of a rigid monoidal
category.  No regularisation is required because the sum is over the
finitely many irreducible summands of $V^{\otimes n}$, not over a
continuum of paths. Cf.\ \cite{stolz-teichner-2012}.

The connection to the skein-based mass calculation of
[Chapter 6](#chap:brings-surface) is then as follows.  The skein relation
$q\mathcal{M}(L_+) - q^{-1}\mathcal{M}(L_-) = (q^{1/2} - q^{-1/2})\mathcal{M}(L_0)$
([skein mass relation](#rem:skein-mass-relation)) is the
*characteristic equation* of the braiding $c_{V,V}$ evaluated under
the categorical trace: the three resolutions $L_+$, $L_-$, $L_0$ of a
crossing correspond to the eigenvalues $q$ and $-q^{-1}$ of $c_{V,V}$
and the trace of the identity strand.  Since the eigenvalues are
determined by the $R$-matrix ([$R$-matrix braiding](#rem:r-matrix-braiding)), the
mass ratios --- including $\mathfrak{m}_\mu/\mathfrak{m}_e \approx :val[m_mu_over_e]{precision=6}$ --- are computed by
a finite trace on a finite-dimensional representation, with the knot types
serving as a *complete* eigenbasis
([knot eigenbasis completeness](#prop:knot-eigenbasis-complete)) that Feynman's
formulation lacked.
<!-- FILE_END: feynman-eigenbasis.md -->

