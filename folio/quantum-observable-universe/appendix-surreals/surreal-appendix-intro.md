This appendix explores a speculative lift of the Quantum Observable
Universe from its native ground field $\mathbb{R}$ (or $\mathbb{C}$)
to Conway's surreal numbers $\mathbf{No}$ — the unique proper-class
real-closed field containing every ordered-field extension of
$\mathbb{R}$, including the hyperreals $^{*}\mathbb{R}$, the ordinals
$\mathrm{Ord}$, and all Hahn series $\mathbb{R}((t^{G}))$ \cite{conway1976,ehrlich2012}.

**Nothing in this appendix alters this paper.** The Quantum Observable Universe is developed and proved over $\mathbb{R}$ in the main text. This appendix offers an *ambient* field into which the archimedean content embeds and from which it is recovered via the standard-part map. The statements here are either **remarks** interpreting existing blocks, **conjectures** pending further development, or **definitions** of new auxiliary structures.

## Motivation for the surreal lift

Four distinct uses motivate the lift:

1. **An explicit ambient for $q \to 1$ limits.** Setting
   $q = 1 + \varepsilon$ for an infinitesimal $\varepsilon \in
   \mathbf{No}$ replaces the (classically broken) classical-limit
   functor ([classical limit functor](#def:classical-limit-functor))
   with the evaluation at a specific surreal, composed with
   Robinson's standard-part map \cite{robinson1966}. The classical
   regime becomes a quotient rather than a limit.

2. **A grading source aligned with braid combinatorics.** Gonshor's
   sign-sequence presentation of $\mathbf{No}$ \cite{gonshor1986} assigns
   every surreal a function $\alpha \to \{+,-\}$ for some ordinal
   $\alpha$. The Hecke generator $\sigma$ has two eigenvalues
   ($q$ and $-q^{-1}$), so a braid word decorated with eigenspace
   choices produces a sign sequence and therefore a surreal number.
   The Hoefsmit seminormal form ([Hoefsmit seminormal
   form](#prop:hoefsmit-seminormal-form)) turns out to *be* the
   surreal $\{L \mid R\}$ construction in disguise
   ([Hoefsmit is surreal construction](#prop:hoefsmit-is-surreal-construction)).

3. **Named values for blow-ups and singularities.** The Möbius
   energy integral, renormalisation scales, and hyperbolic-volume
   divergences become honest elements of $\mathbf{No}$
   (infinite surreals like $\omega$, $\omega^2$) rather than
   informal symbols $\infty$. Counterterms become named negative
   surreals.

4. **Infinitesimal axioms.** Strict equalities in the QOU axioms
   (Frobenius pairing $= \mathrm{id}$; observability cohomology
   $= 0$; vacuum $= 0$) can be relaxed to hold *up to an
   infinitesimal*. The archimedean theory is recovered by taking
   standard-parts; the surreal theory is strictly stronger
   (carries information about the infinitesimal deviation).

## Lossiness of the lift

A first-pass survey suggests that replacing $\mathbb{R}$ with
$\mathbf{No}$ must forfeit Lebesgue measure, Hilbert-space
completions, and hyperbolic geometry. But
an honest survey of the QOU development shows most of these
are *never actually used* in a load-bearing way (see
[analytic obstructions](#rem:analytic-obstructions)):

- **Lebesgue measure** enters only the Möbius energy integral
  (one block). Everywhere else, "integrals" are categorical
  (Frobenius counit) or reduce to rational/algebraic formulas.
- **Hilbert completion** appears in a single proof
  passage, where "dense" can be replaced by "spans the algebraic
  direct limit" without loss.
- **Hausdorff dimension** is given by the rational formula
  $d_H(q) = (2q-1)^2/q^3$, so it transfers to $\mathbf{No}$
  exactly.
- **Spectral theorems** are never used. Hoefsmit's seminormal
  form diagonalises Hecke generators algebraically over
  $\mathbb{Q}(q^{1/2})$.

The only obstructions that genuinely bite are the Möbius
energy integral and the hyperbolic-volume side of the Kashaev
comparison. This paper's mass-formula pipeline — Hoefsmit $\to$ Markov trace $\to$ Jones polynomial $\to$ categorical mass — transfers to $\mathbf{No}$ unchanged.

## Non-goals.

Four exclusions bound the scope of this appendix.

- Non-archimedean values carry no claimed physical interpretation (the
  treatment is purely mathematical).
- No main-text proof is replaced (all main-text results stand over $\mathbb{R}$).
- Kashaev's volume conjecture is not solved (though [Kashaev surreal
  reformulation](#conj:kashaev-surreal) separates its algebraic and
  transcendental parts).
- No canonical Lebesgue-like measure is constructed on $\mathbf{No}$.

## Structure of the appendix

Section 1 states the algebraic core that survives unchanged;
Section 2 lists the analytic obstructions; Section 3 shows what
survives of calculus up to infinitesimals. Sections 4--5 construct
the birthday and sign-sequence gradings and the standard-part
functor. Section 6 relaxes the strict QOU axioms. Section 7 gives
two speculative reformulations: the aether parameter as a Hahn series,
and Kashaev's conjecture as a standard-part identity.
